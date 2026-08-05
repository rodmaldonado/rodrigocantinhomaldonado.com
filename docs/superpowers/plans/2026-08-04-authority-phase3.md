# Authority Phase 3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the personal site with nine substantial, distinct pages that strengthen Rodrigo Cantinho Maldonado's authority in real estate, hospitality, and business decision-making.

**Architecture:** Add one idempotent Python generator following the existing phase pattern. It renders SEO-complete static pages, updates the sitemap, and adds a compact topic hub to the homepage; the build script invokes it after phases 1 and 2.

**Tech Stack:** Python 3 standard library, static HTML, JSON-LD, shell build pipeline.

## Global Constraints

- Do not invent awards, certifications, companies, clients, wealth, or performance claims.
- Use Rodrigo Cantinho Maldonado's full name consistently.
- Every page must have one H1, a canonical URL, metadata, JSON-LD, breadcrumbs, and relevant internal links.
- The generator must be safe to run repeatedly without duplicate sitemap or homepage entries.

---

### Task 1: Phase 3 generator

**Files:**
- Create: `scripts/expand_authority_phase3.py`
- Create: `tests/test_expand_authority_phase3.py`
- Modify: `scripts/build.sh`

**Interfaces:**
- Consumes: the generated `public/` directory from phases 1 and 2.
- Produces: `PAGES`, `render(page)`, `sitemap_entry(page)`, and nine page directories under `public/`.

- [ ] Write tests asserting nine unique pages, substantial copy, SEO metadata, structured data, and internal links.
- [ ] Run `python -m unittest tests/test_expand_authority_phase3.py -v` and confirm failure because the generator does not exist.
- [ ] Implement the generator with the minimum functionality required by the tests.
- [ ] Run the unit test and confirm it passes.
- [ ] Add `python3 scripts/expand_authority_phase3.py` to `scripts/build.sh`.
- [ ] Run the complete build and SEO validator.
- [ ] Commit only the Phase 3 files on an isolated branch and open a pull request.
