# Repository guidance

- Use Python 3.14 (`.python-version`; `requires-python` in `pyproject.toml`) and `uv` for the environment and dependencies; pytest is the sole declared dev dependency.
- Run the full test suite from the project root with `uv run pytest`; run a focused test with `uv run pytest src/tests/ostoskori_test.py -q` (or pass a pytest `-k` expression).
- Tests live in `src/tests/` and import modules such as `ostoskori` directly; run pytest from the repository root so `src` is on the import path.
- Core shopping-cart classes are in `src/`: `Ostoskori` (`ostoskori.py`), `Ostos` (`ostos.py`), and `Tuote` (`tuote.py`). Keep changes and tests aligned with their Finnish names and method APIs.

## TDD rules

- Tests must be executed with `uv run pytest`.
- Do not modify `src/ostos.py` or `src/tuote.py`.
- Do not modify any test files unless explicitly asked.
- Always implement the absolutely minimal code required to make the current failing test pass.
- Do not implement functionality for future TDD steps in advance.
- Follow the TDD cycle: failing test, minimal implementation, passing test, then commit.
