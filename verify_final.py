"""Verify the standardized CDOT dossier and published branch surface."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_BRANCHES = {
    "audit/claim1-convex-qp",
    "audit/claim2-pseudometric-dispersion",
    "audit/claim3-synthetic-table2",
    "audit/claim4-oasis-cohort",
    "audit/claim5-tudataset",
    "audit/claim6-risk-consistency",
    "audit/judge-repair-oasis",
    "audit/lean-kernel-claims1-2-6",
    "main",
    "release/cumulative-evidence",
    "release/judge-visible-20260729",
    "release/lean-kernel-evaluator-20260730",
    "release/raw-oasis-evidence",
}
EXPECTED_COMMITS = 45
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
EXPECTED_STATUSES = {
    "C1": "VERIFIED_SCOPED",
    "C2": "VERIFIED_SCOPED",
    "C3": "VERIFIED_SCOPED",
    "C4": "FALSIFIED_SCOPED",
    "C5": "FALSIFIED_SCOPED",
    "C6": "VERIFIED_SCOPED",
}
EXPECTED_OVERALL = "VERIFIED_C1_C2_C3_C6_FALSIFIED_C4_C5_LIVE_SCORE_12_OF_12"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"verification failed: {message}")


def read_json(path: str) -> dict[str, object]:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def published_branches() -> set[str]:
    try:
        lines = git("ls-remote", "--heads", "origin").splitlines()
    except subprocess.CalledProcessError:
        lines = []
    if lines:
        return {line.split("\t", 1)[1].removeprefix("refs/heads/") for line in lines}
    return set(git("for-each-ref", "--format=%(refname:short)", "refs/heads").splitlines())


def main() -> None:
    claims = read_json("claims.json")
    verdicts = read_json("reproduction_verdicts.json")
    manifest = read_json("EVIDENCE_MANIFEST.json")
    state = read_json("AUTONOMOUS_STATE.json")

    branches = published_branches()
    require(branches == EXPECTED_BRANCHES, "published branches")
    require(not any(branch.startswith("orx/") for branch in branches), "legacy orx branch")
    require(int(git("rev-list", "--all", "--count")) == EXPECTED_COMMITS, "reachable commit count")
    identities = git("log", "--all", "--format=%an <%ae>%n%cn <%ce>").splitlines()
    require(identities and all(identity == CANONICAL_IDENTITY for identity in identities), "canonical identity")

    require(claims["overall_status"] == EXPECTED_OVERALL, "claims overall status")
    require(verdicts["overall_verdict"] == EXPECTED_OVERALL, "verdict overall status")
    require(verdicts["claim_statuses"] == EXPECTED_STATUSES, "verdict statuses")
    require(state["repository"]["expected_reachable_commits"] == EXPECTED_COMMITS, "state commit count")
    require(state["repository"]["canonical_email"] == "MachineLearning-Nerd@users.noreply.github.com", "state identity")
    require(all((ROOT / path).exists() for path in manifest["required_paths"]), "manifest paths")

    c1 = read_json(".openresearch/artifacts/claim_1/raw/claim_1_result.json")
    c2 = read_json(".openresearch/artifacts/claim_2/raw/claim_2_result.json")
    c2_independent = read_json(".openresearch/artifacts/claim_2/raw/claim_2_independent_checker.json")
    c3 = read_json(".openresearch/artifacts/claim_3/raw/claim_3_result.json")
    c3_independent = read_json(".openresearch/artifacts/claim_3/raw/claim_3_independent_checker.json")
    c4 = read_json(".openresearch/artifacts/claim_4/raw/claim_4_result.json")
    c4_independent = read_json(".openresearch/artifacts/claim_4/raw/claim_4_independent_checker.json")
    c5 = read_json(".openresearch/artifacts/claim_5/raw/claim_5_result.json")
    c5_independent = read_json(".openresearch/artifacts/claim_5/raw/claim_5_independent_checker.json")
    c6 = read_json(".openresearch/artifacts/claim_6/raw/claim_6_result.json")
    formal = read_json(".openresearch/artifacts/formal_theorems/raw/formal_gate_summary.json")
    formal_independent = read_json(".openresearch/artifacts/formal_theorems/raw/formal_independent_checker.json")
    formal_negative = read_json(".openresearch/artifacts/formal_theorems/raw/formal_negative_control.json")
    judge = read_json(".openresearch/artifacts/judge_12_of_12/judge_result.json")
    release = read_json(".openresearch/artifacts/release/postpublication_audit.json")

    require(c1["status"] == "VERIFIED" and c1["independent_all_gates_pass"] is True, "C1 evidence")
    require(c2["status"] == "VERIFIED" and c2["all_gates_pass"] is True, "C2 evidence")
    require(c2_independent["all_gates_pass"] is True, "C2 independent evidence")
    require(c3["status"] == "VERIFIED" and c3["all_gates_pass"] is True, "C3 evidence")
    require(c3_independent["all_gates_pass"] is True, "C3 independent evidence")
    require(c4["status"] == "FALSIFIED" and c4["all_gates_pass"] is True, "C4 evidence")
    require(c4_independent["all_gates_pass"] is True, "C4 independent evidence")
    require(c5["status"] == "FALSIFIED", "C5 evidence")
    require(c5["results"]["ENZYMES"]["CDOT_minus_FGW_accuracy"] < 0, "C5 ENZYMES reversal")
    require(c5["results"]["ENZYMES"]["gates"]["three_repeated_nested_10fold_runs"] is True, "C5 repeated runs")
    require(c5_independent["all_gates_pass"] is True, "C5 independent evidence")
    require(c6["status"] == "VERIFIED" and c6["all_gates_pass"] is True, "C6 evidence")
    require(formal["verdict"] == "VERIFIED" and all(formal["gates"].values()), "formal gates")
    require(formal_independent["all_gates_pass"] is True, "formal independent replay")
    require(formal_negative["rejected_as_intended"] is True, "formal negative control")

    require(judge["selection"]["space_id"] == "DineshAI/nPC7M7XLEv", "judge Space")
    require(judge["selection"]["sha"] == "819b602292066602b465aa8ac59babce4f673b95", "judge revision")
    require(judge["points"] == 12 and judge["maximum_points"] == 12, "judge score")
    require(release["result"] == "PASS", "release audit")
    require(release["uploaded_hash_errors"] == [], "release hashes")
    require(release["historical_safety"]["protected_pages_byte_identical"] is True, "historical safety")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require("arXiv:2606.02047" in readme, "paper citation")
    require("Thank you" in readme, "thank-you note")
    require("12/12" in readme, "live score")
    require("STATUS.md" in readme and "CLAIM_EVIDENCE.md" in readme, "dossier links")
    require("AUTHOR_THANK_YOU.md" in readme, "author note link")
    branch_audit = (ROOT / "branch-audit.md").read_text(encoding="utf-8")
    require(CANONICAL_IDENTITY in branch_audit, "branch identity documentation")

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(EXPECTED_BRANCHES)} commits={EXPECTED_COMMITS} "
        "claims=C1:C2:C3:C6_verified_scoped,C4:C5_falsified_scoped "
        "live_score=12/12 current_score_claim=true publication_allowed=false"
    )


if __name__ == "__main__":
    main()
