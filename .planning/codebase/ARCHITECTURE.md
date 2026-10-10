---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
<!-- refreshed: 2026-10-10 -->

# Architecture

**Analysis Date:** 2026-10-10

## System Overview

```text
┌─────────────────────────────────────────────────────────────────────┐
│                 Content (Markdown + front matter)                    │
│  `all_collections/_posts/`   `about.md`  `contact.md`  `404.md`      │
│  `index.md`  `blog.html`  `index.html`                               │
└───────────────┬─────────────────────────────┬───────────────────────┘
                │ Jekyll build (kramdown, Liquid)  `_config.yml`
                ▼                              ▼
┌──────────────────────────────┐   ┌────────────────────────────────┐
│ Layouts  `_layouts/`         │   │ Data  `_data/author.yml`       │
│ post.html, blog.html         │   │ (site.data.author)             │
└───────────────┬──────────────┘   └───────────────┬────────────────┘
                │ {% include %}                     │
                ▼                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Partials  `_includes/`                                              │
│ head.html, header.html, bio.html, footer.html, category-modal.html  │
└───────────────┬─────────────────────────────────────────────────────┘
                │ emits static HTML into `_site/` (gitignored)
                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Browser runtime                                                      │
│ `assets/js/mode.js`  `assets/js/categories.js`  `assets/js/lbox.js`  │
│ Styles: `assets/css/common.css` + `blog.css` | `post.css` + syntax  │
│ MathJax (CDN, post pages only)                                       │
└─────────────────────────────────────────────────────────────────────┘
```

Build and deploy sit beside this pipeline: `.github/workflows/jekyll.yml` runs `bundle exec jekyll build` with `JEKYLL_ENV=production` on pushes to `main` and deploys `_site/` to GitHub Pages. Dependencies come from `Gemfile` (`github-pages` plus four plugins).

## Pattern Overview

**Overall:** Static site generation with a Jekyll "collections" content model, Liquid-templated layouts and partials, and progressive-enhancement client JavaScript. No application server, no database, no API.

**Key Characteristics:**
- All dynamic behaviour happens at build time. Liquid loops over `site.posts` and `site.categories` and writes HTML and one JS file.
- Content is non-standard for Jekyll: `_config.yml` sets `collections_dir: all_collections`, so the `_posts`, `_archive`, `_drafts`, `_papers`, `_worksheets` folders live under `all_collections/` rather than the repo root.
- Only the `posts` collection is declared in `_config.yml` (`collections: posts: output: true`), so only `all_collections/_posts/` is rendered. The other underscore folders are source or archive material and are not emitted.
- Theme state is a `data-theme` attribute on `<html>`, set from `localStorage` before first paint and toggled by `mode.js`. CSS falls back to `prefers-color-scheme` when no choice is stored.
- Single-theme-package layout: the repo is a fork of a Jekyll theme (see `README.md`) that has been customised for one author. There is no `_plugins/`, no `_sass/`, and no test suite.

## Layers

**Content layer:**
- Purpose: Authored articles, research notes, and reference material.
- Location: `all_collections/_posts/` (31 posts, all `layout: post`), `all_collections/_archive/` (49 drafts and iterations, not rendered), `all_collections/_papers/` (PDFs, DOCX, and dated markdown notes, not rendered), `all_collections/_worksheets/`, `all_collections/_drafts/` (editorial guides, not rendered).
- Contains: Markdown with YAML front matter (`layout`, `title`, `date`, `categories`), inline HTML, and image references.
- Depends on: `_layouts/post.html` (via the `defaults` block in `_config.yml`, which applies `layout: post` and `permalink: /posts/:title/` to anything in `_posts`).
- Used by: `_layouts/blog.html` (listing loop over `site.posts`) and `assets/js/categories.js` (category index built from `site.categories`).

**Page layer (root content files):**
- Purpose: Top-level site pages.
- Location: `index.md`, `index.html`, `blog.html`, `about.md`, `contact.md`, `404.md` at repo root.
- Contains: Front matter and short bodies. `about.md` and `contact.md` are placeholder text.
- Depends on: `_layouts/blog.html` (`index.md`), `_layouts/post.html` (`404.md`), or the missing `default` layout (see Anti-Patterns).
- Used by: Jekyll output paths `/`, `/blog.html`, `/about/`, `/contact/`, `/404.html`.

**Layout layer:**
- Purpose: Page shells.
- Location: `_layouts/post.html`, `_layouts/blog.html`.
- Contains: Full HTML documents. Each includes `head.html`, `header.html`, content, `footer.html`, and `category-modal.html`. `blog.html` also contains the article-list loop.
- Depends on: `_includes/*`.
- Used by: Pages and posts via the `layout:` key.

**Partial layer:**
- Purpose: Reusable HTML fragments and the single shared `<head>`.
- Location: `_includes/head.html`, `_includes/header.html`, `_includes/bio.html`, `_includes/footer.html`, `_includes/category-modal.html`.
- Contains: `head.html` chooses CSS by `page.layout == "post"` and loads MathJax and `lbox.js` only for posts. `bio.html` reads `site.data.author`.
- Depends on: `site.baseurl`, `site.title`, `site.data.author`, `page.layout`.
- Used by: Both layouts.

**Data layer:**
- Purpose: Author profile used by the bio block and social icons.
- Location: `_data/author.yml`.
- Contains: `name`, `dp` (avatar URL), `description` (HTML string), `email`, and a `contact` list whose `title` values map to icon filenames under `assets/icons/`.
- Depends on: Nothing.
- Used by: `_includes/bio.html`.

**Presentation layer:**
- Purpose: Styling and theme switching.
- Location: `assets/css/common.css` (shared variables, modal, `hr`), `assets/css/blog.css` (listing page), `assets/css/post.css` (article page), `assets/css/syntax.css` (Pygments-style code colours for post pages).
- Contains: CSS custom properties per `[data-theme="light"]` and `[data-theme="dark"]`, with `@media (prefers-color-scheme ...)` fallbacks.
- Depends on: The `data-theme` attribute.
- Used by: `_includes/head.html`, which selects the stylesheet set based on layout.

**Behaviour layer (client JS):**
- Purpose: Three small, independent scripts.
- Location: `assets/js/mode.js`, `assets/js/categories.js`, `assets/js/lbox.js`.
- Contains: See Key Abstractions.
- Depends on: DOM IDs and classes from `_includes/header.html` (`#dark-mode-toggle`), `_includes/category-modal.html` (`#category-modal*`, `#category-modal-bg`), and `_layouts/post.html` (`.article .content img`).
- Used by: `categories.js` is loaded from `_includes/head.html` on every page. `mode.js` is loaded from `_includes/footer.html`. `lbox.js` is loaded from `_includes/head.html` on post pages only.

**Build and delivery layer:**
- Purpose: Reproducible build and GitHub Pages deployment.
- Location: `Gemfile`, `Gemfile.lock`, `.github/workflows/jekyll.yml`, `CNAME`.
- Contains: Ruby 3.1 CI job, `actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages`.
- Depends on: `github-pages` gem, `jemoji`, `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed`.
- Used by: GitHub Actions on push to `main`.

## Data Flow

### Primary Request Path (static build of a post)

1. Jekyll reads `_config.yml`, which points `collections_dir` at `all_collections` and declares the `posts` collection (`_config.yml`).
2. For each file in `all_collections/_posts/`, the `defaults` block injects `layout: post` and `permalink: /posts/:title/` (`_config.yml`).
3. Kramdown converts the Markdown body to HTML. Front matter `categories` populates `site.categories`.
4. `_layouts/post.html` renders: `_includes/head.html` (post CSS, `syntax.css`, `common.css`, `categories.js`, `lbox.js`, MathJax), `_includes/header.html`, the article header (title, date, categories), `{{content}}`, `_includes/footer.html`, `_includes/category-modal.html`.
5. `categories.js` is emitted with a generated object literal built from `site.categories`, keyed by category name with spaces replaced by underscores (see `assets/js/categories.js`).
6. Output is written to `_site/posts/<slug>/index.html`.

### Primary Request Path (home page)

1. `index.md` (`layout: blog`, `title: Blog`) is the file that produces `/`. Its body is empty; the listing comes from the layout.
2. `_layouts/blog.html` loops over `site.posts`, printing title, date, categories and a 40-word excerpt. The excerpt is `post.content | strip_html | split: 'TL;DR' | last`, so it uses text after a `TL;DR` marker when present, otherwise the start of the post (`_layouts/blog.html`).
3. `_layouts/blog.html` includes `head.html`, `header.html`, `bio.html`, `footer.html`, and `category-modal.html`, so `/` gets the full shell. Only the root `blog.html` page lacks it (see Anti-Patterns).

### Client-side theme flow

1. Inline script in `_includes/head.html` reads `localStorage.theme` and sets `data-theme` on `<html>` before body render (prevents flash).
2. `_includes/header.html` renders `#dark-mode-toggle`. `assets/js/mode.js` binds a click that flips `data-theme` between `light` and `dark` and writes `localStorage.theme`.
3. CSS selectors `[data-theme="light"]` and `[data-theme="dark"]` in `assets/css/common.css`, `blog.css`, and `post.css` supply colours. With no stored value, `@media (prefers-color-scheme: light)` applies.

### Category modal flow

1. `categories.js` binds `window.onload` and attaches a click handler to every `.category` element (rendered in `_layouts/post.html` and `_layouts/blog.html`).
2. On click it looks up `categories[innerText.replace(" ", "_")]`, builds a list of article links, and fills `#category-modal-content`. `#category-modal` and `#category-modal-bg` receive class `open`.

### Image lightbox flow (posts only)

1. `assets/js/lbox.js` (deferred, loaded only when `page.layout == "post"`) creates `#lightbox` and binds clicks on `.article .content img`.

**State Management:**
- No server state. Client state is limited to `localStorage.theme`.
- Build-time state lives in Jekyll's `site` object (`site.posts`, `site.categories`, `site.data.author`).

## Key Abstractions

**Collection `posts`:**
- Purpose: The publishable article set.
- Examples: `all_collections/_posts/2026-06-01-frontier-gtm-engineering.md`, `all_collections/_posts/2021-11-04-jekyll-markdown.md`
- Pattern: Date-prefixed filenames `YYYY-MM-DD-slug.md`. The date in the filename is ignored by the permalink, which uses `:title` (slug without date) under `/posts/`.

**Front-matter taxonomy (categories):**
- Purpose: Drives the category pills, the category modal, and the `categories.js` index.
- Examples: `categories: [GTM Engineering, Revenue Operations, ...]` in `all_collections/_posts/2026-06-01-frontier-gtm-engineering.md`.
- Pattern: Array of display strings. There is no separate tags system and no category pages on disk; the modal is the only category view.

**Author data object:**
- Purpose: Single source for name, avatar, bio HTML, and social links.
- Examples: `_data/author.yml`, consumed by `_includes/bio.html`.
- Pattern: Icons are resolved by convention: `assets/icons/{{ contact.title }}.png`. Two entries share the title `email`, so they share one icon.

**Theme attribute:**
- Purpose: Single switch for light and dark styling.
- Examples: `assets/js/mode.js`, inline script in `_includes/head.html`, `assets/css/common.css`.
- Pattern: `data-theme` attribute on `<html>`, persisted under `localStorage` key `theme`.

**Category index object (`categories`):**
- Purpose: Client-side map from category name to post list for the modal.
- Examples: Generated inline at the top of `assets/js/categories.js`. Liquid writes the literal at build time.
- Pattern: Build-time code generation in a `.js` asset. Keys are only valid JS identifiers when the category has no hyphens and only one space (see Anti-Patterns).

## Entry Points

**Home (`/`):**
- Location: `index.md` (listing, `layout: blog`). Also `index.html` at repo root with the same output path; see Anti-Patterns.
- Triggers: GitHub Pages request for the site root.
- Responsibilities: Lists every post from `site.posts`.

**Post pages (`/posts/<slug>/`):**
- Location: `all_collections/_posts/*.md`, rendered by `_layouts/post.html`.
- Triggers: Link from the home list, the category modal, or the sitemap/feed.
- Responsibilities: Render article, MathJax, lightbox, category pills.

**Blog listing (`/blog.html`):**
- Location: `blog.html` (`layout: default`, inline listing loop).
- Triggers: Direct URL.
- Responsibilities: Duplicate of the home listing, without the shared header and theme styling.

**Static pages (`/about/`, `/contact/`, `/404.html`):**
- Location: `about.md`, `contact.md`, `404.md`.
- Triggers: Direct URL, or unknown route (404).
- Responsibilities: Placeholder text (`about.md`, `contact.md`) and a homepage link (`404.md`).

**Build entry point:**
- Location: `.github/workflows/jekyll.yml` (job `build`, step `bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"`).
- Triggers: Push to `main`, or `workflow_dispatch`.
- Responsibilities: Build to `_site/`, upload Pages artifact, deploy.

**Local preview:**
- Location: `bundle exec jekyll serve` (documented in `README.md`).
- Triggers: Manual.

## Architectural Constraints

- **Threading:** Not applicable. Build is single-process Jekyll. Browser JS is single-threaded and runs on the main thread.
- **Global state:** Build-time `site` object only. Browser globals: `categories` (`assets/js/categories.js`), `currentTheme` (top-level `const` in the inline script in `_includes/head.html`, read by `assets/js/mode.js`), `MathJax` (set in `_includes/head.html`), `window.onload` (`assets/js/categories.js`).
- **Circular imports:** Not applicable. There is no module graph. Liquid includes are acyclic (`_layouts/*` include `_includes/*`; no partial includes a layout).
- **Script load order:** `categories.js` is synchronous in `<head>` and runs before the body exists, but it only attaches handlers inside `window.onload`, so the ordering is safe. `mode.js` is `defer` in the footer and depends on `currentTheme` from the inline head script; removing that inline `const` would break `mode.js`.
- **Content path coupling:** Liquid `permalink` depends on the filename slug. Renaming a post file changes its URL.
- **External dependencies at runtime:** MathJax from `cdn.jsdelivr.net` (posts only). Avatars from `avatars.githubusercontent.com`. Post images reference `raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/...` in many posts, so those images only resolve once pushed to `main`.

## Anti-Patterns

### Two root files both render `/`

**What happens:** `index.html` (`layout: default`, placeholder text "Welcome to My Blog") and `index.md` (`layout: blog`, listing) both compile to `_site/index.html`.
**Why it's wrong:** Jekyll writes both to the same output path. Which one survives depends on processing order, so the live home page is not deterministic from the source.
**Do this instead:** Keep one of them. The intended home is the listing, so keep `index.md` and delete `index.html`, or move the listing into `index.html` with `layout: blog`.

### Missing `default` layout

**What happens:** `index.html`, `about.md`, `contact.md`, and `blog.html` use `layout: default`. There is no `_layouts/default.html`. Only `_layouts/post.html` and `_layouts/blog.html` exist.
**Why it's wrong:** Those pages either render without the shared `head.html`/`header.html`/`footer.html` shell or fail to build, depending on Jekyll's handling of a missing layout. The theme cannot be relied on for those pages.
**Do this instead:** Add `_layouts/default.html` that includes `head.html`, `header.html`, `{{ content }}`, `footer.html`, and `category-modal.html`, or change those pages to an existing layout.

### Duplicated listing logic

**What happens:** The article loop lives in both `_layouts/blog.html` (used by `index.md`) and the body of `blog.html`.
**Why it's wrong:** Two copies drift. `blog.html` has no header, no theme toggle, and no `categories.js` binding, so `/blog.html` and `/` already behave differently.
**Do this instead:** Keep the loop in `_layouts/blog.html`. Make `blog.html` a three-line stub with `layout: blog`.

### Build-time JS object with unquoted keys

**What happens:** `assets/js/categories.js` emits `{{ category_name | replace " ", "_" }}: [...]` without quoting. Category names containing hyphens (for example `Go-to-Market`, `Post-Browser Era`, `Human-Computer Interaction`, `Digital-First Commerce`) produce invalid JS object keys.
**Why it's wrong:** A syntax error in `categories.js` aborts that script, so no category click handler is bound on any page. Also, the click handler uses `innerText.replace(" ", "_")` with a string pattern, which replaces only the first space. Multi-space names such as `Top of Funnel` or `Go-to-Market Strategy` then fail the lookup and throw in `posts.forEach`.
**Do this instead:** Emit quoted keys with `{{ category_name | replace: " ", "_" | jsonify }}` (or `json`-encode the whole map), and in the click handler use `innerText.replace(/ /g, "_")`. Better still, key the map by the raw name with `JSON.stringify`, and drop the replacement entirely.

### Excerpt depends on a `TL;DR` marker

**What happens:** `_layouts/blog.html` and `index.html` take the text after `TL;DR` as the excerpt, falling back to the start of the body.
**Why it's wrong:** The fallback is silent. Posts without the marker get an excerpt from the first paragraph, which may be a title or image line.
**Do this instead:** Document the marker convention in `README.md` or add an explicit `excerpt:` front-matter key and use `post.excerpt` when present.

### Cross-file implicit global

**What happens:** `assets/js/mode.js` reads `currentTheme`, which is defined as a top-level `const` in an inline script in `_includes/head.html`, not in `mode.js`.
**Why it's wrong:** The dependency is invisible from `mode.js`. `mode.js` also contains a duplicate `if (currentTheme)` block that re-sets the attribute the head script already set.
**Do this instead:** Remove the duplicate block in `mode.js` and read `localStorage.getItem("theme")` directly where needed.

### Debug output in production JS

**What happens:** `assets/js/categories.js` calls `console.log(categories)` on every page load.
**Why it's wrong:** Ships the entire post index to the browser console on each visit.
**Do this instead:** Delete the line.

## Error Handling

**Strategy:** Build-time failures stop the GitHub Actions job. Runtime JavaScript has no error handling; the code assumes DOM elements and category entries exist.

**Patterns:**
- Liquid nil-safety is implicit (missing front matter yields empty output rather than errors).
- `categories.js` has no guards on `posts` (undefined for unmatched category keys) or on missing DOM nodes.
- `lbox.js` and `mode.js` assume their elements exist and do not check for `null`.

## Cross-Cutting Concerns

**Logging:** `console.log` in `assets/js/categories.js` only. No build-time logging beyond Jekyll defaults.
**Validation:** None on content or data. Front matter is trusted. No schema for `_data/author.yml`.
**Authentication:** Not applicable. Public static site. No login, no admin, no forms (`contact.md` is placeholder text).
**SEO and feeds:** Provided by plugins (`jekyll-seo-tag` in `head.html` is not included, so the tag must be added; `jekyll-feed` and `jekyll-sitemap` run automatically from `_config.yml`).
**Analytics:** None detected.

---

*Architecture analysis: 2026-10-10*
