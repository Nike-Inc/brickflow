# AGENTS.md

## Executable commands
- Install dev env: `make dev`
- Install deps only: `make poetry-install`
- Lint: `make check`
- Typecheck: `make mypy`
- Test: `make test`
- Lint + test + coverage: `make cov`
- Build wheel: `make build`
- Format: `make fmt`

## Project structure
- `brickflow/` — core library; primary code changes go here
- `brickflow_plugins/` — Databricks/Airflow plugins
- `tests/` — pytest suite; add tests for new behavior
- `examples/` — sample workflows; reference unless task requires changes
- `docs/` — MkDocs documentation site
- `tools/` — internal scripts; avoid unless requested

## Code style
- Python >=3.9, <3.13
- Format with Black (`make fmt` / `make black-check`)
- Type-check with mypy on core modules (`make mypy`)
- Lint with prospector/pylint (`make check`)
- Match existing naming, imports, and module patterns
- Do not add comments that restate obvious code

## Testing requirements
- Run `make cov` before reporting work complete
- Add pytest tests under `tests/` for new behavior
- Do not lower coverage or skip tests to pass checks

## Git workflow
- Branch from `main` (e.g. `feature/...`, `fix/...`)
- One logical change per PR
- Meaningful commit messages
- PR must pass CI (`.github/workflows/onpush.yml`)

## Three-tier boundaries

### NEVER
- Commit secrets, tokens, or credentials
- Force-push to shared branches
- Add dependencies without clear need
- Modify unrelated files outside the task scope

### ASK FIRST
- Public API or CLI behavior changes
- Version/release strategy changes
- Large refactors spanning multiple packages

### ALWAYS
- Run `make check` and `make cov` before finishing
- Follow patterns in surrounding code
- Update docs when user-visible behavior changes
