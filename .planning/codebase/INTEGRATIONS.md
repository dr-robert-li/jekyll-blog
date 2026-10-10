---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
# External Integrations

**Analysis Date:** 2026-10-10

This repository is a static Jekyll site with no backend. Integrations are limited to build-time services (GitHub Actions, GitHub Pages, RubyGems) and client-side resources loaded by the browser (CDN fonts and MathJax). No APIs, databases, auth providers, analytics, or webhooks are wired in.

## APIs & External Services

**Client-side CDNs (loaded by visitor browsers):**
- MathJax 3 - Renders LaTeX math on post pages
  - Loaded from: `https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js`
  - Declared in: `_includes/head.html` (only when `page.layout == "post"`)
  - Configuration: inline `MathJax = { tex: { inlineMath: [['$','$'],['\\(','\\)']], displayMath: [['$$','$$'],['\\[','\\]']] ... } }` in `_includes/head.html`
  - SDK/Client: none (script tag)
  - Auth: none
- Google Fonts - JetBrains Mono web font
  - Loaded from: `https://fonts.googleapis.com/css2?family=JetBrains+Mono:...`
  - Declared in: `assets/css/blog.css` and `assets/css/post.css` (`@import url(...)`)
  - SDK/Client: none
  - Auth: none

**Build-time / publishing services:**
- GitHub Pages - Hosts the built `_site/` output
  - Deploy action: `actions/deploy-pages@v4` in `.github/workflows/jekyll.yml`
  - Page setup: `actions/configure-pages@v5` (provides `base_path` for `--baseurl`)
  - Artifact upload: `actions/upload-pages-artifact@v3`
  - Auth: `GITHUB_TOKEN` with `pages: write` and `id-token: write` permissions (declared in the workflow)
- GitHub Actions - Runs the build and deploy on push to `main` (and manual `workflow_dispatch`)
  - Ruby setup: `ruby/setup-ruby` (pinned to commit SHA) with `bundler-cache: true`
  - Checkout: `actions/checkout@v4`
- RubyGems (`https://rubygems.org`) - Gem source declared in `Gemfile`; resolved during `bundle install`

**Content / profile links (outbound hyperlinks, not API calls):**
- GitHub profile `https://github.com/dr-robert-li` - in `_data/author.yml` (contact list and bio)
- LinkedIn `https://www.linkedin.com/in/robert-li` - in `_data/author.yml`
- Email `mailto:dr.robert.li.au@gmail.com` and `mailto:robert.li@australiagtm.com` - in `_data/author.yml`
- GitHub avatar `https://avatars.githubusercontent.com/u/155333421?v=4` - `dp:` field in `_data/author.yml`
- GitHub Sponsors `github: dr-robert-li` - `.github/FUNDING.yml`

## Data Storage

**Databases:**
- Not applicable. No database client, ORM, or connection string in the repo.

**File Storage:**
- Local filesystem only. Static assets live in `assets/` and `images/`. Research papers and worksheets (PDF, DOCX) live in `all_collections/_papers/` and `all_collections/_worksheets/`.
- Posts are Markdown files under `all_collections/_posts/`.

**Caching:**
- None at the application level. Jekyll writes `.jekyll-cache/` and `.sass-cache/` locally (both gitignored).

## Authentication & Identity

**Auth Provider:**
- Not applicable. The site has no login, sessions, or user accounts.
- The only identity surface is the GitHub token used by GitHub Actions for Pages deployment (`GITHUB_TOKEN`, no custom secret).

## Analytics, Tracking & Comments

**Analytics:** Not detected. No Google Analytics, GTM, Plausible, Umami, Fathom, or similar script found in `_includes/`, `_layouts/`, or `assets/js/`.

**Comments:** Not detected. No Disqus, Giscus, Utterances, or similar integration.

**Search:** Not detected. No Algolia or client-side search index. Categories are handled in-page by `assets/js/categories.js` using Liquid-generated data from `site.categories`.

**Social embeds:** Not detected. No tweet, YouTube, or gist embed tags.

## Monitoring & Observability

**Error Tracking:** None detected (no Sentry, Bugsnag, or similar).

**Logs:**
- Jekyll console output only during build and `jekyll serve`.
- `assets/js/categories.js` contains a `console.log(categories)` debug statement that runs in the browser.

## CI/CD & Deployment

**Hosting:**
- GitHub Pages, custom domain `drli.blog` (from `CNAME`)
- Environment name `github-pages` in the deploy job

**CI Pipeline:**
- GitHub Actions, single workflow: `.github/workflows/jekyll.yml`
  - Job `build`: checkout, Ruby 3.1 with bundler cache, `configure-pages`, `bundle exec jekyll build --baseurl ...` with `JEKYLL_ENV=production`, upload Pages artifact
  - Job `deploy`: `actions/deploy-pages@v4`, depends on `build`
  - Concurrency group `pages`, `cancel-in-progress: false`

## Environment Configuration

**Required env vars:**
- None for the site itself.
- CI uses only the built-in `GITHUB_TOKEN` (no repository secrets referenced in the workflow).

**Secrets location:**
- No secrets are stored in the repo. `.gitignore` excludes `.env*`, `*.pem`, `*.key`, `secrets/`, `credentials/`, and similar patterns as a precaution.
- The author's email and profile links in `_data/author.yml` and `_config.yml` are public contact details, not secrets.

## Webhooks & Callbacks

**Incoming:**
- None. Static site, no server endpoints.

**Outgoing:**
- None. No HTTP calls from the site code. The only outbound browser requests are the CDN resources listed above.

## Operational Notes

- Changing the MathJax CDN URL or version in `_includes/head.html` affects every post page with math. Pin the version explicitly when editing (currently `mathjax@3`, unpinned minor).
- Google Fonts `@import` is duplicated in `blog.css` and `post.css`. Either file alone is enough to load the font.

---

*Integration audit: 2026-10-10*
