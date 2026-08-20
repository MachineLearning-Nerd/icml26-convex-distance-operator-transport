# Audit report

## Final result

The live evaluator awarded **12/12** at the exact Space revision
819b602292066602b465aa8ac59babce4f673b95. The six verdicts were:

| Claim | Result | Evidence |
| --- | --- | --- |
| C1 | VERIFIED | Lean kernel and independent quadratic-form gates |
| C2 | VERIFIED | Lean kernel, 320 finite cells, and 32 diffuse witnesses |
| C3 | VERIFIED | N=2000, 100 trials, paired confidence intervals |
| C4 | FALSIFIED | Primary OASIS archive counterexample and full raw pair inventory |
| C5 | FALSIFIED | Full MUTAG/ENZYMES nested-CV reversal |
| C6 | VERIFIED | Lean bound, consistency squeeze, and invalid schedule control |

The result is a recorded live judge outcome, not a forecast. No author
endorsement is claimed.

## How the claims are produced

Claims 1, 2, and 6 combine kernel-checked theorem obligations with
independent finite diagnostics. Claim 3 reproduces the declared synthetic
scale and tests method ordering with paired intervals. Claim 4 uses both
the full primary archive and the registered all-pairs rerun, with the
168-node session serving as an assumption-matched contradiction. Claim 5
executes every graph pair and the nested CV contract, with ENZYMES reversing
the claimed direction under all three outer seeds.

Every claim has a source audit, contract, raw output, and control in the
repository. The full production paths are in [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md).

## Release integrity

The published Space release contains 249 allowlisted text paths. Its
postpublication audit verifies all uploaded hashes, 248 release-manifest
entries, all six evaluator claim pages, zero traversal gaps, and byte-identical
protected judged pages. Two evaluator-blind red-team passes are recorded as
passing.

The Lean release separately records the pinned toolchain, source hash,
independent replay, negative-control rejection, and absence of forbidden
source tokens. These records are provenance for the 12/12 result and are not
replaced by this GitHub documentation commit.

## Limitations

The paper leaves several empirical choices unpublished, including random
seeds and some optimization or preprocessing details. Those choices are
predeclared and disclosed in the claim pages. The formal source proves the
general mathematical steps under explicit premises; it does not silently
reprove the paper's full measure-theoretic and empirical-process interfaces.
