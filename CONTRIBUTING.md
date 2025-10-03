# Contributing to Pyro-Ops

Thanks for your interest in contributing! This project aims to provide reliable, modular ground-segment tooling for SmallSat missions.

## Getting started

1. Fork and clone the repository.
2. Create a virtual environment:
   - Windows PowerShell: `python -m venv .venv; .venv\Scripts\Activate.ps1`
   - Unix/macOS: `python -m venv .venv && source .venv/bin/activate`
3. Install dev deps: `pip install -e .[dev]`
4. Run tests: `pytest -q`

## Code style and quality
- Lint: `ruff check .`
- Type-check: `mypy src/pyro_ops`
- Tests: `pytest -q`
- Keep functions small and readable; prefer explicit names and type hints.
- Avoid adding heavy runtime dependencies to the core; use optional extras.

## Commit messages
- Use concise, descriptive messages.
- Reference issues like: `Fix #123: handle variable-length PUS packets`.

## Branching and PRs
- Create a feature branch from `main`.
- Ensure CI is green (lint, type, tests, build).
- Fill in the PR template, describing changes and risks.

## Security and safety
- Do not include secrets in code or tests.
- Ground ops safety: never auto-uplink in examples or tests. Networking actions must support a `dry_run`.
- See SECURITY.md for reporting vulnerabilities.

## Releases
- Version bump in `pyproject.toml` and `src/pyro_ops/__init__.py`.
- Build: `python -m build`
- Preferred: publish via GitHub Actions Trusted Publisher. Fallback: `twine upload dist/*`.

## Documentation
- Docs are generated with Sphinx. Install: `pip install .[docs]`, build: `sphinx-build -b html docs _build/html`.

Thanks again for contributing!
