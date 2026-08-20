# Branch audit

This repository was migrated from generated OpenResearch and date-stamped release branch names to descriptive branches. The clean branches preserve the claim, repair, and release lineage.

## Mapping

| Former branch | Clean branch | Purpose |
| --- | --- | --- |
| orx/baseline-source-pin-and-claim-1-certificate | audit/claim1-convex-qp | Source pin and Theorem 3.4 convex-QP certificate. |
| orx/claim-2-pseudometric-and-dispersion-certificate | audit/claim2-pseudometric-dispersion | Theorems 3.5/3.7 certificate and finite witness domain. |
| orx/claim-6-risk-bound-and-consistency-certificate | audit/claim6-risk-consistency | Theorem 5.6/Corollary 5.7 risk-bound certificate. |
| orx/claim-4-exhaustive-oasis-3-cohort-falsification | audit/claim4-oasis-cohort | Exhaustive OASIS-3 archive audit and cohort contradiction. |
| orx/claim-5-full-tudataset-nested-cv-reproduction | audit/claim5-tudataset | Full MUTAG/ENZYMES nested-CV reproduction. |
| orx/claim-3-full-scale-synthetic-table-2-cpu-reprodu | audit/claim3-synthetic-table2 | Exact-scale synthetic Table 2 reconstruction. |
| orx/judge-repair-canonical-trackio-pages-plus-oasis | audit/judge-repair-oasis | Canonical judge pages and faithful all-pairs OASIS rerun. |
| orx/lean-kernel-certificates-for-claims-1-2-and-6 | audit/lean-kernel-claims1-2-6 | Pinned Lean kernel checks and independent replay. |
| orx/release-candidate-complete-raw-oasis-evidence | release/raw-oasis-evidence | Evaluator-downloadable 19,800-row OASIS evidence. |
| orx/release-evaluator-visible-cumulative-claim-packa | release/cumulative-evidence | Cumulative evaluator-visible claim package. |
| release/judge-visible-cumulative-20260729 | release/judge-visible-20260729 | Preserve the pre-Lean judge-visible release. |
| release/lean-kernel-evaluator-visible-20260730 | release/lean-kernel-evaluator-20260730 | Preserve the published revision that received 12/12. |
| main | main | Cumulative publication surface. |

## Migration guarantees

- Every live branch contains the current README and this branch audit.
- All reachable commits are attributed to MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>.
- Former generated branches are deleted after their clean replacements are published.
- Active notebook, report, and README links use the renamed repository and clean branch names.
- The DineshAI Space identifier, judged revision, dataset hashes, and immutable result records are retained as provenance, not as GitHub ownership or branch names.

## Verification checklist

~~~
git show-ref --verify refs/heads/<branch>
git show <branch>:README.md >/dev/null
git show <branch>:branch-audit.md >/dev/null
git log <branch> --format='%an <%ae>' | sort -u
~~~
