# Security Policy

## Supported versions

We support the latest minor version. Please update to the newest release for fixes.

## Reporting a vulnerability

If you discover a security issue:
- Do NOT open a public issue with sensitive details.
- Email: `yadikrish@gmail.com` with subject "Pyro-Ops Security".
- Provide steps to reproduce and affected versions. We aim to acknowledge within 72 hours.

## Scope and safety
- No automatic uplinks: examples and APIs must support `dry_run` for network actions.
- Secrets (tokens, keys) must never be committed; use environment variables or CI secrets.
- Dependencies: we pin and scan dependencies; report known CVEs that affect runtime components.
