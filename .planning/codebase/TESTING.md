---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
<!-- refreshed: 2026-10-10 -->

# Testing Patterns

**Analysis Date:** 2026-10-10

## Test Framework

**Runner:**
- None. No test framework is installed or configured.
- No `package.json`, `jest.config.*`, `vitest.config.*`, `karma.conf.*`, `.rspec`, `spec/` directory, or `test/` directory exists in the repository.
- Gemfile (`Gemfile`) contains only the Jekyll stack (`github-pages`, `jemoji`, `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed`). No test gems (rspec, minitest, html-proofer) are declared.

**Assertion Library:**
- Not applicable.

**Run Commands:**

```bash
bundle exec jekyll build                 # Only automated verification: full site build
bundle exec jekyll serve                 # Manual check at http://localhost:4000
JEKYLL_ENV=production bundle exec jekyll build --baseurl ""   # Matches CI build (.github/workflows/jekyll.yml)
```

- No test, watch, or coverage command exists.

## Automated Verification in CI

**Workflow:** `.github/workflows/jekyll.yml`
- Triggers: push to `main`, and `workflow_dispatch`.
- Job `build`: checks out code, sets up Ruby `3.1` with bundler cache, runs `bundle exec jekyll build --baseurl "<pages base_path>"` with `JEKYLL_ENV=production`, then uploads `_site/`.
- Job `deploy`: publishes to GitHub Pages (`actions/deploy-pages@v4`).
- The build is the only gate. A Liquid or front-matter error fails the deploy. Nothing checks link validity, HTML validity, or rendered output.

**What CI does not check:**
- No link checker, no HTML validator, no spell or style check, no image existence check, no front-matter schema check.

## Test File Organization

**Location:**
- Not applicable. No test files exist. Do not create a `test/` or `spec/` directory without first agreeing on a runner.

**Naming:**
- Not applicable.

**Structure:**

```
(none)
```

## Test Structure

**Suite Organization:**
- Not applicable.

**Patterns:**
- Not applicable.

## Mocking

**Framework:** None.

**Patterns:**
- No mocks exist. Browser globals used by the front-end scripts (`document`, `localStorage`, `window.onload`) are not isolated anywhere.

**What to Mock (if tests are added later):**
- `localStorage` for `assets/js/mode.js` (key `theme`).
- The Liquid-generated `categories` object in `assets/js/categories.js`. It is produced at build time, so tests should read the built output in `_site/assets/js/categories.js` rather than the source template.

**What NOT to Mock:**
- The Jekyll build itself. Build a real site with `bundle exec jekyll build` and inspect `_site/` instead of mocking Liquid.

## Fixtures and Factories

**Test Data:**
- Real content is the only fixture. Posts in `all_collections/_posts/` serve as examples for every front-matter variant (31 posts).
- No factories, seed data, or fixture files exist.

**Location:**
- Not applicable.

## Coverage

**Requirements:** None enforced.

**View Coverage:**
- Not available. No instrumentation is configured.

## Test Types

**Unit Tests:**
- None.

**Integration Tests:**
- None. The closest equivalent is the production build in CI (see above).

**E2E Tests:**
- Not used.

**Manual verification (current practice):**
- Preview with `bundle exec jekyll serve` and check the following by hand:
  - Dark/light toggle in the header persists across reloads (`assets/js/mode.js`, `localStorage` key `theme`).
  - Category pills open the modal and list posts (`assets/js/categories.js`). Check multi-word categories specifically; see the lookup bug in `CONVENTIONS.md` Gotchas.
  - Images in a post open in the lightbox (`assets/js/lbox.js`).
  - MathJax renders `$...$` and `$$...$$` on post pages (`_includes/head.html`).
  - Chart.js charts render on posts that load it (e.g. `all_collections/_posts/2025-09-24-citation-attention.md`).
  - Listing excerpts on `blog.html` and `_layouts/blog.html` show the TL;DR text (posts without a TL;DR show the full body; see Gotchas in `CONVENTIONS.md`).

## Common Patterns

**Build-time check (copy this for quick local verification):**

```bash
bundle exec jekyll build 2>&1 | tail -20
grep -c "<article" _site/blog.html        # Should equal the number of posts (31 at analysis time)
grep -o 'category-modal' _site/posts/*/index.html | wc -l
```

**Post front-matter sanity check (no test runner needed):**

```bash
for f in all_collections/_posts/*.md; do
  head -1 "$f" | grep -q '^---$' || echo "bad front matter open: $f"
  grep -q '^layout: post$' "$f"    || echo "missing layout: $f"
  grep -q '^date: ' "$f"           || echo "missing date: $f"
  grep -q '^categories: \[' "$f"   || echo "categories not inline array: $f"
done
```

**Filename vs date check:**

```bash
for f in all_collections/_posts/*.md; do
  fn=$(basename "$f" | cut -c1-10)
  fm=$(grep -m1 '^date:' "$f" | awk '{print $2}')
  [ "$fn" = "$fm" ] || echo "date mismatch: $f (front matter $fm)"
done
```

- Currently reports three mismatches: `2024-04-29-ai-training-data-model-collapse.md`, `2024-07-03-gen-ai-business.md`, `2024-09-22-reference-architecture.md`.

**Async Testing:**
- Not applicable. No async code is tested.

**Error Testing:**
- Not applicable. The only error page is `404.md`, which can be checked by building and opening `_site/404.html`.

## Adding Tests (Guidance)

If a test runner is introduced, keep it proportional to a static blog:
- Prefer a single shell or Ruby script that runs the front-matter and filename checks above over a full JS test framework.
- For browser behaviour (theme toggle, modal, lightbox), a single Playwright smoke test against `_site/` is the smallest useful addition. Put it in `test/` and document the command here.
- Do not add a test framework to `Gemfile` without also adding a CI step to `.github/workflows/jekyll.yml`.

---

*Testing analysis: 2026-10-10*
