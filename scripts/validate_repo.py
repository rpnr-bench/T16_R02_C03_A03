#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'SECURITY.md', 'mkdocs.yml', 'requirements.txt', 'docs/index.md']
errors = []
for rel in required:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')


mkdocs = (root / 'mkdocs.yml').read_text()
if 'site_name:' not in mkdocs or 'nav:' not in mkdocs:
    errors.append('mkdocs.yml must define site_name and nav')

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    sys.exit(1)
print('OK: T16_R02')
