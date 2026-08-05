#!/bin/sh
set -eu

rm -rf public site.tar.gz
mkdir -p public

cat site.part.00 site.part.01 site.part.02 site.part.03 site.part.04 > site.tar.gz
tar -xzf site.tar.gz -C public

python3 -m unittest tests/test_expand_authority_phase3.py -v
python3 scripts/expand_seo_hospitality.py
python3 scripts/expand_authority_phase2.py
python3 scripts/expand_authority_phase3.py

if python3 -c "import bs4, lxml" >/dev/null 2>&1; then
  python3 scripts/validate_site.py public
else
  echo "SEO pages generated. Install beautifulsoup4 and lxml to run validation locally."
fi
