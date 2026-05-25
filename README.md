# MkDocs API Reference

A MkDocs-powered API reference site covering overview, authentication, configuration, and error response documentation.

## Project layout

- `docs/api/` — API reference pages.
- `mkdocs.yml` — Navigation and site configuration.
- `requirements.txt` — Documentation build dependencies.
- `scripts/` — Repository validation helpers.

## Quick start

```bash
make validate
```
```bash
pip install -r requirements.txt
```
```bash
mkdocs build --strict
```

## Documentation workflow

1. Add or update Markdown pages under `docs/`.
2. Keep `mkdocs.yml` navigation synchronized with new pages.
3. Run repository validation for quick checks.
4. Run `mkdocs build --strict` before release.

## Maintenance notes

Keep API overview links aligned with the navigation tree.

## Contributing

Keep changes focused, update documentation when behavior changes, and run the validation commands before submitting a pull request.
