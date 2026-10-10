---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
# Technology Stack

**Analysis Date:** 2026-10-10

## Languages

**Primary:**
- Liquid templating (Jekyll) - Layouts and includes in `_layouts/` and `_includes/`, plus `assets/js/categories.js` (generated via Liquid front matter)
- HTML5 - Page shells in `_layouts/blog.html`, `_layouts/post.html`, `_includes/head.html`, `_includes/header.html`, `_includes/footer.html`, `index.html`, `blog.html`
- Markdown (kramdown) - Post and page content in `all_collections/_posts/*.md` (31 posts), `all_collections/_archive/`, `all_collections/_drafts/`, `about.md`, `contact.md`, `404.md`, `index.md`
- CSS - `assets/css/common.css`, `assets/css/blog.css`, `assets/css/post.css`, `assets/css/syntax.css`

**Secondary:**
- Vanilla JavaScript (ES2015+, no transpilation) - `assets/js/mode.js` (dark/light toggle), `assets/js/lbox.js` (image lightbox), `assets/js/categories.js` (category modal)
- YAML - `_config.yml`, `_data/author.yml`, `.github/workflows/jekyll.yml`, `.github/FUNDING.yml`
- Ruby - Only as the Jekyll build runtime and Gemfile; no custom Ruby source in the repo

## Runtime

**Environment:**
- Ruby 3.1 (pinned in CI via `ruby-version: '3.1'` in `.github/workflows/jekyll.yml`; no `.ruby-version` file present)
- Browser runtime for client-side JS (no Node.js runtime, no `package.json`)

**Package Manager:**
- Bundler (`BUNDLED WITH 2.3.5` in `Gemfile.lock`)
- Lockfile: present (`Gemfile.lock`)
- No npm/yarn/pnpm usage. No `package.json` or `node_modules`.

## Frameworks

**Core:**
- Jekyll 4.2.2 - Static site generator (pinned in `Gemfile.lock`); builds to `_site/` (gitignored)
- kramdown 2.3.2 (with kramdown-parser-gfm 1.1.0) - Markdown engine, set by `markdown: kramdown` in `_config.yml`
- Liquid 4.0.3 - Template engine used by Jekyll
- Rouge 3.28.0 - Syntax highlighting for fenced code blocks (styles in `assets/css/syntax.css`)
- github-pages (declared in `Gemfile`, but NOT present in `Gemfile.lock`; see Configuration notes)

**Testing:**
- Not detected. No test framework, test config, or test directory.

**Build/Dev:**
- `bundle exec jekyll build` / `bundle exec jekyll serve` - Build and local dev server (commands from `README.md`)
- Prettier (config in `.prettierrc`: tabWidth 2, printWidth 80, singleQuote false; editor wiring in `.vscode/settings.json` with `editor.formatOnSave: true`). Prettier is an editor-side tool; no `package.json` pins it.
- GitHub Actions (`actions/checkout@v4`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`, `ruby/setup-ruby` pinned by SHA) - CI build and deploy

## Key Dependencies

**Critical (from `Gemfile`, versions from `Gemfile.lock`):**
- `jekyll` 4.2.2 - Core site generator (transitive; declared through `github-pages` in `Gemfile`)
- `jekyll-feed` 0.16.0 - Generates Atom feed (`feed.xml`); configured under `plugins:` in `_config.yml`, author info from `_config.yml` `author:` block
- `jekyll-seo-tag` 2.8.0 - SEO meta tags; plugin listed in `_config.yml`
- `jekyll-sitemap` 1.4.0 - Generates `sitemap.xml` (excluded from source output by `exclude:` in `_config.yml`)
- `jemoji` 0.12.0 (with `gemoji` 3.0.1) - Converts `:emoji:` shortcodes in content; listed in `_config.yml` plugins

**Infrastructure (transitive, from `Gemfile.lock`):**
- `nokogiri` 1.13.6 (x86_64-linux platform gem) - HTML parsing for jemoji/html-pipeline
- `sassc` 2.4.0 via `jekyll-sass-converter` 2.2.0 - Sass compilation hook (no `.scss` files currently in repo; CSS is plain `.css`)
- `kramdown` 2.3.2 - Markdown
- `rouge` 3.28.0 - Code highlighting
- `listen` 3.7.1 / `jekyll-watch` 2.2.1 - File watching for `jekyll serve`
- `activesupport` 7.0.2.3, `i18n` 1.10.0, `tzinfo` 2.0.4, `concurrent-ruby` 1.1.10 - Utility libraries pulled in by Jekyll/html-pipeline
- `addressable` 2.8.0, `pathutil` 0.16.2, `safe_yaml` 1.0.5, `liquid` 4.0.3, `mercenary` 0.4.0, `terminal-table` 2.0.0, `colorator` 1.1.0 - Jekyll internals
- `em-websocket` 0.5.3 / `eventmachine` 1.2.7 - LiveReload support during `jekyll serve`

**Front-end (loaded at runtime in the browser, not managed by a package manager):**
- MathJax 3 (`https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js`) - Math rendering; loaded only on `post` layout pages via `_includes/head.html`
- JetBrains Mono web font (Google Fonts CSS2 import) - imported by `assets/css/blog.css` and `assets/css/post.css`

## Configuration

**Site configuration:**
- `_config.yml` - Site title (`Dr. Robert Li`), `markdown: kramdown`, `timezone: Australia/Brisbane`, `author` block (used by jekyll-feed), `plugins` list, `collections_dir: all_collections`, `collections.posts.output: true`, front-matter defaults for `_posts` (`layout: post`, `permalink: /posts/:title/`), and `exclude:` list (`sitemap.xml`, `feed.xml`, `LICENSE`, `README.md`)
- `_data/author.yml` - Author bio HTML, contact links (LinkedIn, GitHub, email); consumed by `_includes/bio.html`
- `CNAME` - Custom domain `drli.blog` for GitHub Pages

**Environment:**
- No environment variables are read by the site code. No `.env` file in the repo (`.gitignore` excludes `.env*` patterns).
- Build-time env: `JEKYLL_ENV=production` set in CI (`.github/workflows/jekyll.yml`).
- Build-time arg: `--baseurl` supplied from `actions/configure-pages` output in CI.

**Build:**
- `Gemfile` / `Gemfile.lock` - Ruby dependencies
- `_config.yml` - Jekyll configuration
- `.github/workflows/jekyll.yml` - CI build and GitHub Pages deploy (triggered on push to `main`, plus `workflow_dispatch`)
- `.prettierrc`, `.vscode/settings.json` - Formatting for the editor

**Dependency notes (for planner/executor):**
- `Gemfile` declares `gem "github-pages"` but `Gemfile.lock` does not contain the `github-pages` gem and lists `jekyll` 4.2.2 directly. The lock appears out of sync with the Gemfile; running `bundle install` may rewrite it. Verify before upgrading.
- The lock only includes the `x86_64-linux` platform for nokogiri. macOS development needs a platform add (`bundle lock --add-platform`) if the lock is regenerated there.
- Jekyll 4.2.2 is an older release. Newer Jekyll/github-pages versions are not reflected in the lock.

## Platform Requirements

**Development:**
- Ruby with Bundler (CI uses Ruby 3.1)
- Native build tools for nokogiri/sassc/eventmachine if compiling from source (not needed when the prebuilt linux gem is used)
- A modern browser for previewing the site (MathJax and Google Fonts load from CDN)

**Production:**
- GitHub Pages (static hosting), deployed by `.github/workflows/jekyll.yml` via `actions/deploy-pages@v4`
- Custom domain `drli.blog` (via `CNAME`)
- No server-side runtime, database, or container. Output is pure static files in `_site/`.

---

*Stack analysis: 2026-10-10*
