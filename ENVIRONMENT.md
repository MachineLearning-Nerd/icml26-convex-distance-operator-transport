# Environment and reproduction contract

## Fixed command

~~~bash
uv sync --frozen --python 3.12
uv run --frozen --python 3.12 python -m cdot_repro.run
~~~

The formal Lean release uses the same cumulative Python command and then
compiles the pinned Lean project, runs IndependentReplay.lean, and requires
NegativeControl.lean to be rejected.

## Pinned numerical environment

- Python: >=3.12,<3.13
- NumPy: 2.2.4
- PyTorch: 2.6.0 CPU build
- POT: 0.9.6.post1
- SciPy: 1.16.1
- scikit-learn: 1.7.1
- NetworkX: 3.4.2
- SymPy: 1.13.1
- Backend: CPU; no GPU used
- Recorded numerical workers: 64 logical CPUs visible, effective thread
  limit one where declared

## Pinned formal environment

- Lean: 4.19.0
- mathlib: c44e0c8ee63ca166450922a373c7409c5d26b00b
- Formal release runtime: approximately 5h37m on Hugging Face cpu-upgrade
- Numerical cumulative run: approximately 38,009.7 seconds on
  Hugging Face cpu-upgrade

No full rerun is required for documentation normalization. The committed raw
outputs, exact data hashes, kernel reports, release manifests, and blind
red-team records are the reproducibility inputs.

## Evidence locations

- Primary source and contracts: .openresearch/artifacts/
- Lean proof source: formal/
- Numerical source: src/cdot_repro/
- Evaluator candidate pages: candidate/
- Published release mirror and manifests: space_release/
- Live judge record: .openresearch/artifacts/judge_12_of_12/
