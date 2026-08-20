# Reproduction status

## Overall verdict

**VERIFIED_C1_C2_C3_C6_FALSIFIED_C4_C5_LIVE_SCORE_12_OF_12**

This repository is an independent, claim-by-claim audit of
[*Convex Distance Operator Transport: A Convex and Geometry-Preserving
Formulation*](https://arxiv.org/abs/2606.02047). It is not the authors'
official implementation.

- The exact live evaluator record awards **12/12** at Space revision
  819b602292066602b465aa8ac59babce4f673b95.
- Claims 1, 2, 3, and 6 received VERIFIED; Claims 4 and 5 received
  FALSIFIED, each for full credit.
- The judged Space revision is preserved as immutable external provenance;
  later GitHub documentation does not claim to alter that judged artifact.
- No author endorsement is claimed.

| Claim | Status | How the result is produced | Boundary |
| --- | --- | --- | --- |
| C1 convex program and attainment | VERIFIED_SCOPED | Lean kernel checks compact attainment and Jensen convexity; 48 independent quadratic forms and a destructive control are recorded | Paper-specific continuity and lower-semicontinuity interfaces remain explicit premises |
| C2 pseudometric and dispersion gap | VERIFIED_SCOPED | Lean checks weighted Minkowski and conditional-variance identities; 320 finite cells and 32 diffuse witnesses pass | Finite checks do not replace the population theorem |
| C3 synthetic Table 2 | VERIFIED_SCOPED | Exact N=2000, 100-trial reconstruction with paired confidence intervals below zero | Independent seeds, initialization, and step-size policy are disclosed deviations |
| C4 OASIS-3 cohort and Table 3 | FALSIFIED_SCOPED | Full archive audit finds subject OAS30938 with a 168-node session; all 4,950 pair rows are retained | Falsifies the literal 696-by-170 cohort premise; numeric recovery is reported separately |
| C5 TUDataset graph classification | FALSIFIED_SCOPED | Full all-pairs nested CV reverses ENZYMES under all three outer seeds | Unpublished split, feature-scaling, and stopping choices remain protocol risks |
| C6 risk bound and consistency | VERIFIED_SCOPED | Lean checks the E1+E2+E3 bound, O(1/T) term, consistency squeeze, and invalid-schedule control | Measure/operator assumptions are explicit and not silently reproved |

See [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) for the production path of each
claim, [SOURCE_AUDIT.md](SOURCE_AUDIT.md) for source and judge provenance, and
[ENVIRONMENT.md](ENVIRONMENT.md) for the locked numerical and Lean toolchains.
