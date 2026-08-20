# Claim evidence ledger

Each result below is tied to a paper anchor, a committed claim contract, a
primary verifier, an independent checker or kernel replay, and a deliberate
control. VERIFIED_SCOPED records the scope supported by the theorem
certificate and finite audit. FALSIFIED_SCOPED records an explicit
assumption-matched contradiction to the stated conjunction.

| Claim | Verdict | Primary evidence | Production path |
| --- | --- | --- | --- |
| C1 | VERIFIED_SCOPED | .openresearch/artifacts/claim_1/raw/claim_1_result.json and formal_theorems/raw/formal_gate_summary.json | src/cdot_repro/claim1.py and formal/CDOTProofs.lean |
| C2 | VERIFIED_SCOPED | .openresearch/artifacts/claim_2/raw/claim_2_result.json and claim_2_independent_checker.json | src/cdot_repro/claim2.py and formal/CDOTProofs.lean |
| C3 | VERIFIED_SCOPED | .openresearch/artifacts/claim_3/raw/claim_3_result.json and claim_3_independent_checker.json | src/cdot_repro/claim3.py |
| C4 | FALSIFIED_SCOPED | .openresearch/artifacts/claim_4/raw/claim_4_result.json and claim_4_independent_checker.json | src/cdot_repro/claim4.py |
| C5 | FALSIFIED_SCOPED | .openresearch/artifacts/claim_5/raw/claim_5_result.json and claim_5_independent_checker.json | src/cdot_repro/claim5.py |
| C6 | VERIFIED_SCOPED | .openresearch/artifacts/claim_6/raw/claim_6_result.json and formal_theorems/raw/formal_gate_summary.json | src/cdot_repro/claim6.py and formal/CDOTProofs.lean |

## C1 — Theorem 3.4, convex quadratic program and attainment

The paper states that the CDOT objective over fixed-marginal couplings
attains an optimum and is convex in the coupling. The production path has
two layers. The Lean kernel certificate checks compact attainment, the
squared-residual identity, and Jensen convexity. The independent numerical
route checks 48 quadratic forms across the declared finite panels, with
minimum Jensen gap approximately negative 8.88e-16 and zero monotonicity
failures. A negated-squared-norm mutation produces positive Jensen excess
0.017777777777777774 and is rejected.

The universal theorem is carried by the reconstructed obligations, not by
the finite panels alone. Continuity and lower-semicontinuity of the
paper-specific population objective remain explicit interfaces.

## C2 — Theorems 3.5 and 3.7, pseudometric and dispersion gap

The audit reconstructs the weighted two-component Minkowski step and the
conditional-variance decomposition. Lean checks both declarations in the
pinned formal source. The finite route exhaustively enumerates 320 declared
two-point cells and 32 diffuse dispersion witnesses; all identities,
symmetry checks, and triangle checks pass. The maximum independent
dispersion error is 1.942890293094024e-16. Squaring the valid discrepancy
creates a triangle excess of 0.0812 and is rejected as the negative control.

The production path keeps the population proof obligations separate from
finite witness diagnostics.

## C3 — Synthetic Table 2

The exact contract uses 500 points in each of four regions, N=2000,
alpha=0.5, T=200, and 100 PCG64-seeded trials. CDOT mean MSE is
0.001693640051, compared with 0.003514014474 for FGW and 0.003377851629
for IsoRank. The paired 95 percent interval upper endpoints for CDOT minus
FGW and CDOT minus IsoRank are -0.001786151398 and -0.001649891199,
respectively, so the ordering gate passes.

All 300 method rows are present, marginals and optimization traces pass,
and independent raw inventory agrees. The paper does not publish code,
random seeds, an initial coupling, or an empirical step-size rule; the
registered independent choices are disclosed rather than presented as
author-exact recovery.

## C4 — OASIS-3 cohort and Table 3

The stated cohort premise says that all 696 subjects are represented by
170-node networks. The primary archive contains 975 sessions and all 696
subject IDs, but subject OAS30938 has a session whose atlas IDs are exactly
1 through 168. The direct XML reparse independently confirms 168 nodes.
There are 695 subjects with a valid 170-node session, so the universal
696-by-170 premise is false.

The production path hashes the 654,450,976-byte archive, parses every
session, preserves the 19,800 raw rows for all 4,950 pairs, and rejects a
fabricated padding control. The full conjunction is therefore
FALSIFIED_SCOPED. The directional numerical rerun and the literal cohort
contradiction are reported separately; no numeric table value is inferred
from the counterexample.

## C5 — TUDataset graph classification

The exact route hashes and parses all MUTAG and ENZYMES graphs, evaluates
all unordered pairs at the published alpha grid, and performs three seeded
stratified outer 10-fold runs with inner five-fold joint alpha, C, and gamma
selection. On MUTAG, CDOT is 0.8408382066 versus FGW 0.8335282651. On
ENZYMES, CDOT is 0.3922222222 versus FGW 0.4477777778, a stable
CDOT-minus-FGW difference of -0.0555555556. All integrity and permuted-label
controls pass.

Because the paper's statement is a conjunction over both named datasets,
the stable ENZYMES reversal FALSIFIES that conjunction within the registered
protocol. Unpublished split seeds, ENZYMES standardization, feature-cost
scaling, and optimizer tolerance remain disclosed interpretation risks.

## C6 — Theorem 5.6 and Corollary 5.7

The Lean source checks the exact E1+E2+E3 bound, the fixed-sample O(1/T)
optimization term, the consistency squeeze, and the invalid schedule
control. The numerical support runs two predeclared panels: the maximum final
Frank–Wolfe gap is 9.900242946852059e-06 and the minimum theorem bound is
0.04680643588493418. The valid T_n=n^2 schedule has n_min/T_n tending to
zero, while the invalid T_n=n mutation leaves the limit indicator at
15.953261927945473 and is rejected.

The result is VERIFIED_SCOPED under the paper's stated measure, operator,
and empirical-process assumptions. Those assumptions are documented rather
than silently promoted to newly proved facts.
