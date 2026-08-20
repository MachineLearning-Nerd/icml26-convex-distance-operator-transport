# Source and provenance audit

## Paper

- Title: *Convex Distance Operator Transport: A Convex and
  Geometry-Preserving Formulation*
- Authors: Junhyoung Chung, Euijong Song, Won Hwa Kim, and Gunwoong Park
- Source: [arXiv:2606.02047](https://arxiv.org/abs/2606.02047)
- Audited version: arXiv:2606.02047v1
- HTML: https://ar5iv.labs.arxiv.org/html/2606.02047
- Retrieved UTC: 2026-07-28T12:12:31Z
- HTML SHA-256:
  602040fe82ec6bd4c0422ee488315d8e09f86bef50c6f06d4be61f942094d43f
- PDF SHA-256:
  fe1dda5d0e3f2aea86b9b3b5ebf79b79cbc7d06e3fcbe4b20b6f097cc556375d

This GitHub repository is an independent reproduction and evidence audit. It
does not claim to be maintained by, endorsed by, or identical to the authors'
implementation. The paper did not publish the code, random seeds, or every
experimental choice used by the numerical tables; each registered deviation
is preserved in the claim source audits.

## Paper anchors used

- Theorem 3.4 and Appendix G.3: convex objective and attainment
- Theorems 3.5 and 3.7 and Appendices G.4-G.5: pseudometric and dispersion
- Section 6.1, Table 2, and Appendix H.2: synthetic experiment
- Section 6, Table 3, and Appendix H.3: OASIS-3 cohort and matching
- Section 6, Table 4, and Appendix H.4: MUTAG and ENZYMES classification
- Theorems 5.6-5.7 and Appendix G.6: risk bound and consistency

## Formal provenance

- Lean toolchain: leanprover/lean4:v4.19.0
- mathlib resolved commit:
  c44e0c8ee63ca166450922a373c7409c5d26b00b
- Lean source SHA-256:
  5f56b005ebf859199d653e09fe114731abb1f75f577819180cdd85f223aabd0d
- Primary kernel compile, Lake build, independent replay: passed
- Deliberately false theorem: rejected by the kernel as intended
- Forbidden source tokens checked: no sorry, admit, custom axiom, or unsafe

The formalization deliberately keeps paper-specific continuity,
measure/operator, and empirical-process obligations visible as premises.

## Historical and live evaluation provenance

- Space: DineshAI/nPC7M7XLEv
- Judged revision:
  819b602292066602b465aa8ac59babce4f673b95
- Judged UTC: 2026-07-30T06:11:11+00:00
- Judge quality: high
- Live result: **12/12**
- Machine-readable record:
  .openresearch/artifacts/judge_12_of_12/judge_result.json

The Space head was verified after judgment. The judged Space is treated as
immutable provenance; GitHub documentation changes do not rewrite or claim
to republish that evaluator artifact.
