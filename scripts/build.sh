#!/bin/sh
set -eu
rm -rf public site.tar.gz
mkdir -p public
cat site.part.00 site.part.01 site.part.02 site.part.03 > site.tar.gz
tar -xzf site.tar.gz -C public
