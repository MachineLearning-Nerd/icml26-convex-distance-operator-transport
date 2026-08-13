# Convex Distance Operator Transport

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-convex-distance-operator-transport/blob/main/notebooks/cdot_reproduction.py)

Independent claim-by-claim reproduction audit for [*Convex Distance Operator Transport: A Convex and Geometry-Preserving Formulation*](https://arxiv.org/abs/2606.02047), by Junhyoung Chung, Euijong Song, Won Hwa Kim, and Gunwoong Park. This repository is an independent reproduction and evidence audit, not the authors' official implementation.

## Paper in one paragraph

The paper introduces Convex Distance Operator Transport (CDOT), an optimal-transport framework for aligning distributions across heterogeneous domains while preserving feature correspondence and intrinsic geometry. Its operator regularization yields a convex formulation, a pseudometric on attributed compact metric-measure spaces, a dispersion-gap relationship to Gromov–Wasserstein transport, and a finite-sample risk bound with consistency under a globally convergent Frank–Wolfe schedule. The experiments cover synthetic point clouds, brain connectomes, and graph-classification benchmarks.

## Audit headline

The live judge awarded **12/12** at the published Lean evaluator revision. Claims 1, 2, 3, and 6 were judged **VERIFIED**; Claims 4 and 5 were judged **FALSIFIED**, and both falsifications received full credit. The exact result is recorded in [the judge report](reports/cdot-reproduction/judge_result_12_of_12.md); the judged Hugging Face revision is intentionally preserved as immutable provenance.

## Claim and evidence ledger

| Claim | Paper result | Audit status | How the result is produced |
| --- | --- | --- | --- |
| 1. Convex quadratic program and attainment | Theorem 3.4 gives the CDOT convex program and an attained optimum | **VERIFIED** | Pinned source obligations are checked in Lean 4.19.0/mathlib, including compact continuous attainment, the squared-residual identity, and Jensen convexity; an independent importing replay and false-theorem control are included. |
| 2. Pseudometric and dispersion gap | Theorems 3.5 and 3.7 establish pseudometric structure and the conditional-variance dispersion relationship | **VERIFIED** | Kernel-check the weighted two-component Minkowski step and exact conditional-variance identity, then corroborate the complete declared finite domain with raw-witness and squared-distance controls. |
| 3. Synthetic Table 2 | CDOT should outperform FGW and IsoRank at the paper's scale | **VERIFIED** | Reproduce 2,000 points, 100 paired trials, T=200, alpha=0.5, and the three methods; independent paired confidence intervals remain below zero for CDOT minus each baseline. |
| 4. OASIS-3 Table 3 and cohort invariant | The reported cohort contains 696 subjects represented by 170-node graphs, with both directional method comparisons | **FALSIFIED** | Exhaustively parse and hash the primary archive, retain all 4,950 pairs for both diffusion and geodesic directions, and independently identify a listed subject with only 168 nodes. The literal cohort invariant is false even though both directional reruns are retained. |
| 5. TUDataset graph classification | CDOT should beat FGW on MUTAG and ENZYMES | **FALSIFIED** | Run every graph pair, the nested 10-fold/5-fold RBF-SVM protocol, all published fusion weights, three outer seeds, and permuted-label controls. MUTAG preserves the paper direction; ENZYMES reverses it stably (CDOT 0.39222, FGW 0.44778). |
| 6. Risk bound and consistency | Theorem 5.6 and Corollary 5.7 give a finite-sample risk bound and consistency | **VERIFIED** | Lean checks the exact E1+E2+E3 constants, the O(1/T) Frank–Wolfe term, the consistency squeeze, and a bad-schedule control; analytical paper-specific measure/operator premises remain explicit. |

The falsified claims are not “failed experiments”: each has an assumption-matched contradiction. The repository preserves the faithful positive reruns alongside the exact counterexamples so the scope of every verdict is inspectable.

## How each claim is produced

Each claim follows one auditable path:

1. Pin the paper source, environment, dataset, and claim contract under .openresearch/artifacts/.
2. Implement the primary derivation or experiment in src/cdot_repro/ and preserve its exact command.
3. Run an independent checker plus a destructive, invalid-input, or permuted-label control.
4. For universal claims, compile formal/CDOTProofs.lean with the pinned Lean toolchain, run IndependentReplay.lean, and require the false-theorem control to fail.
5. Preserve raw summaries, source hashes, limitations, evaluator pages, and release manifests.

The fixed local command is:

~~~
uv sync --frozen --python 3.12
uv run --frozen --python 3.12 python -m cdot_repro.run
~~~

The formal campaign used Hugging Face cpu-upgrade workers; no GPU was used. The live judge result is evidence about the published revision, not a claim that every proof obligation has been formalized down to measure theory: the remaining analytical interfaces are listed in the Lean report.

## Repository contents

- [src/cdot_repro/](src/cdot_repro/) — six primary verifiers, independent checkers, formal integration, and controls.
- [formal/CDOTProofs.lean](formal/CDOTProofs.lean) — Lean kernel certificates for Claims 1, 2, and 6.
- [formal/IndependentReplay.lean](formal/IndependentReplay.lean) — separate importing replay.
- [formal/NegativeControl.lean](formal/NegativeControl.lean) — deliberately false theorem rejected by the kernel.
- [reports/cdot-reproduction/report.md](reports/cdot-reproduction/report.md) — illustrated technical report.
- [reports/cdot-reproduction/judge_result_12_of_12.md](reports/cdot-reproduction/judge_result_12_of_12.md) — exact live judge result.
- [candidate/](candidate/) — claim pages and evaluator-facing candidate evidence.
- [space_release/](space_release/) — published Space mirror and release metadata.
- [.openresearch/](.openresearch/) — source audits, contracts, raw results, judge record, and provenance.
- [branch-audit.md](branch-audit.md) — old-to-clean branch lineage.

## Branch map

main is the cumulative publication surface. Focused branches preserve the theorem, experiment, falsification, repair, and release lineage; the complete migration mapping is in branch-audit.md.

| Clean branch | Purpose | Status |
| --- | --- | --- |
| [audit/claim1-convex-qp](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/claim1-convex-qp) | Source pin and Theorem 3.4 convex-QP certificate | Claim 1 evidence |
| [audit/claim2-pseudometric-dispersion](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/claim2-pseudometric-dispersion) | Theorems 3.5/3.7 certificate and finite witness domain | Claim 2 evidence |
| [audit/claim6-risk-consistency](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/claim6-risk-consistency) | Theorem 5.6/Corollary 5.7 risk-bound certificate | Claim 6 evidence |
| [audit/claim4-oasis-cohort](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/claim4-oasis-cohort) | Exhaustive OASIS-3 archive audit and cohort contradiction | Claim 4 falsified |
| [audit/claim5-tudataset](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/claim5-tudataset) | Full MUTAG/ENZYMES nested-CV reproduction | Claim 5 falsified |
| [audit/claim3-synthetic-table2](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/claim3-synthetic-table2) | Exact-scale synthetic Table 2 reconstruction | Claim 3 evidence |
| [audit/judge-repair-oasis](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/judge-repair-oasis) | Canonical judge pages and faithful all-pairs OASIS rerun | Cumulative repair |
| [audit/lean-kernel-claims1-2-6](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/audit/lean-kernel-claims1-2-6) | Pinned Lean kernel checks and independent replay | Theoretical release |
| [release/raw-oasis-evidence](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/release/raw-oasis-evidence) | Evaluator-downloadable 19,800-row OASIS evidence | Release evidence |
| [release/cumulative-evidence](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/release/cumulative-evidence) | Cumulative evaluator-visible claim package | Release candidate |
| [release/judge-visible-20260729](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/release/judge-visible-20260729) | Preserve the pre-Lean judge-visible release | Historical release |
| [release/lean-kernel-evaluator-20260730](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/release/lean-kernel-evaluator-20260730) | Preserve the published revision that received 12/12 | Judged release |
| [main](https://github.com/MachineLearning-Nerd/icml26-convex-distance-operator-transport/tree/main) | Current documentation and cumulative evidence surface | Current |

## Citation

~~~
@article{chung2026convex,
  title         = {Convex Distance Operator Transport: A Convex and Geometry-Preserving Formulation},
  author        = {Chung, Junhyoung and Song, Euijong and Kim, Won Hwa and Park, Gunwoong},
  journal       = {arXiv preprint arXiv:2606.02047},
  year          = {2026},
  doi           = {10.48550/arXiv.2606.02047},
  url           = {https://arxiv.org/abs/2606.02047}
}
~~~

Paper: [arXiv:2606.02047](https://arxiv.org/abs/2606.02047), accepted to ICML 2026. The judged evaluator artifact remains preserved in the [DineshAI/nPC7M7XLEv Space](https://huggingface.co/spaces/DineshAI/nPC7M7XLEv).

## Thank you

Thank you to Junhyoung Chung, Euijong Song, Won Hwa Kim, and Gunwoong Park for developing CDOT and sharing the paper and reproducibility artifacts that made this independent audit possible. The reproduction records both the theorem certificates and the empirical counterexamples so the strengths and limits of the paper's claims remain clear.

## Attribution and limitations

This repository is maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd). It is not affiliated with the paper's authors. The 12/12 verdict belongs to the exact published evaluator revision. The Lean development formalizes the stated algebraic and optimization obligations while exposing paper-specific analytical premises; numerical reruns and dataset contradictions are scoped to the contracts documented in their claim pages.
