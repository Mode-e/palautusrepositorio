# Copilot Instructions

## Build and test

- Use Python 3.14 as declared in `.python-version`; dependencies are managed with `uv`.
- Install dependencies from the project root with `uv sync`.
- Run the complete test suite with `uv run pytest`.
- Run one test file with `uv run pytest src/tests/ostoskori_test.py`.
- Run one unittest method with `uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`.
- There is no configured lint or formatting command in `pyproject.toml`.

## Architecture

- `src/tuote.py` defines `Tuote`, the product model. It exposes `nimi()` and `hinta()` and currently keeps its `_saldo` field only as product state.
- `src/ostos.py` defines `Ostos`, a product-and-quantity entry. It starts at quantity 1, can change quantity through `muuta_lukumaaraa()`, clamps quantity at zero, and reports the line's total via `hinta()`.
- `src/ostoskori.py` defines `Ostoskori`, the incomplete cart API. It should aggregate `Ostos` entries and implement `tavaroita_korissa()`, `hinta()`, `lisaa_tuote()`, `poista_tuote()`, `tyhjenna()`, and `ostokset()`.
- `src/index.py` is a placeholder for test code and is not an application entry point.
- Tests live in `src/tests/` and use `unittest.TestCase`; pytest discovers and runs them.

## Conventions

- Preserve the existing Finnish domain naming (`Tuote`, `Ostos`, `Ostoskori` and method names such as `lisaa_tuote` and `poista_tuote`) for public APIs.
- Import modules as top-level names within `src`; for example, `ostoskori.py` and `ostos.py` import `Tuote` from `tuote`.
- Keep the cart implementation in `src/ostoskori.py` and product/line behavior in their respective `Tuote` and `Ostos` classes; avoid adding cart logic directly to tests or `index.py`.
- This repository is a TDD exercise: `src/ostoskori.py` contains method stubs. Implement behavior incrementally and keep `Ostos` quantity changes consistent with its zero-clamping behavior.
- Execute tests only with `uv run pytest`.
- Do not change `src/ostos.py` or `src/tuote.py`.
- Do not edit tests unless the user explicitly asks.
- Implement only the minimal code needed to make the tests pass.
