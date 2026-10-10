---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
# Codebase Structure

**Analysis Date:** 2026-10-10

## Directory Layout

```
jekyll-blog/
├── all_collections/            # Content root (set by collections_dir in _config.yml)
│   ├── _posts/                 # Published posts (31 .md files) - rendered
│   ├── _archive/               # Old drafts, iterations, "copy" files (49) - not rendered
│   ├── _drafts/                # Editorial and writing guides (2) - not rendered
│   ├── _papers/                # Research PDFs, DOCX, dated notes (14) - not rendered
│   └── _worksheets/            # Templates worksheet .md and .pdf (2) - not rendered
├── _layouts/                   # Page shells: post.html, blog.html
├── _includes/                  # Partials: head, header, bio, footer, category-modal
├── _data/                      # author.yml (site.data.author)
├── assets/
│   ├── css/                    # common.css, blog.css, post.css, syntax.css
│   ├── js/                     # mode.js, categories.js, lbox.js
│   └── icons/                  # Social icons named by author.yml contact titles
├── images/                     # Post images (45 tracked files), referenced from posts
├── .github/
│   ├── workflows/jekyll.yml    # Build and deploy to GitHub Pages
│   └── FUNDING.yml
├── .vscode/settings.json       # Prettier on save
├── .planning/codebase/         # Generated codebase maps (this document)
├── index.md                    # Home page (layout: blog) -> /
├── index.html                  # Placeholder home page (layout: default) -> /  (conflicts with index.md)
├── blog.html                   # /blog.html listing (layout: default)
├── about.md                    # /about/ placeholder
├── contact.md                  # /contact/ placeholder
├── 404.md                      # /404.html
├── _config.yml                 # Jekyll configuration
├── Gemfile, Gemfile.lock       # Ruby dependencies
├── .prettierrc                 # Prettier settings (2-space, 80 cols, double quotes)
├── CNAME                       # Custom domain for GitHub Pages
├── LICENSE, README.md          # Excluded from the build
└── .gitignore                  # Excludes _site/, caches, secrets, editor files
```

## Directory Purposes

**`all_collections/_posts/`:**
- Purpose: The only rendered content collection.
- Contains: One Markdown file per article, filename `YYYY-MM-DD-slug.md`. Front matter has `layout: post`, `title`, `date`, `categories` (array). Posts without a `TL;DR` marker use the start of the body as the listing excerpt.
- Key files: `all_collections/_posts/2026-06-01-frontier-gtm-engineering.md` (most recent), `all_collections/_posts/2021-11-04-jekyll-markdown.md` (theme sample post, categories `jekyll`, `Test Post`, `first post`).

**`all_collections/_archive/`:**
- Purpose: Superseded versions of posts and working notes. Not built.
- Contains: Files with spaces and names such as `copy`, `final`, `refined`, `humanized`, `backup`. `Section 4 Amendment.md`, `Agentic Web Hypothesis Research Report.md`.
- Key files: Nothing here is linked. Treat as reference only.

**`all_collections/_drafts/`:**
- Purpose: Writing and editorial guidance used by agents and editors. Name is misleading, because Jekyll's `_drafts` convention does not apply under `collections_dir`.
- Contains: `EDITORIAL-GUIDE.md`, `WRITING-GUIDE.md`. Both are tracked in git, although `.gitignore` names `WRITING-GUIDE.md` and `EDITORIAL-GUIDE.md` (the patterns do not stop tracked files from being committed).
- Key files: `all_collections/_drafts/EDITORIAL-GUIDE.md`.

**`all_collections/_papers/`:**
- Purpose: Source research (PDFs and a DOCX) behind posts, plus three dated markdown notes.
- Contains: `2402.13753.pdf`, `2404.03626v1.pdf`, `2512.23676v1.pdf`, `w34255.pdf`, `meaning_sense_making_compression.docx`, `2026-01-04.md`, `2026-01-12.md`, `2026-01-19.md`.
- Key files: Binary assets. Not rendered. Do not edit.

**`all_collections/_worksheets/`:**
- Purpose: Downloadable templates.
- Contains: `3t-ready-to-use-templates.md` and `.pdf`.

**`_layouts/`:**
- Purpose: Full-page HTML shells.
- Contains: `post.html` (article page), `blog.html` (listing with article loop). No `default.html` exists, although four files reference `layout: default`.

**`_includes/`:**
- Purpose: Partials included by layouts.
- Contains: `head.html` (meta, CSS selection, theme bootstrap, MathJax for posts), `header.html` (site title and theme toggle), `bio.html` (author block), `footer.html` (copyright and `mode.js`), `category-modal.html` (modal markup).

**`_data/`:**
- Purpose: Structured site data.
- Contains: `author.yml` with name, avatar URL, bio HTML, email, and social `contact` list.

**`assets/css/`:**
- Purpose: Stylesheets. Only `common.css` is shared across all pages. `blog.css` is loaded on non-post pages, `post.css` and `syntax.css` on post pages (see `_includes/head.html`).
- Key files: `assets/css/common.css` (theme variables, category modal, `hr`), `assets/css/post.css` (article typography, `.content` rules), `assets/css/blog.css` (listing `.articles`, responsive breakpoints at 750px, 550px, 350px), `assets/css/syntax.css` (code highlight palette).

**`assets/js/`:**
- Purpose: Client scripts. Each is standalone, with no bundler or modules.
- Key files: `assets/js/mode.js` (theme toggle), `assets/js/categories.js` (generated category map and modal; contains `console.log`), `assets/js/lbox.js` (image lightbox, post pages only).

**`assets/icons/`:**
- Purpose: Social icon PNGs. Filenames must match the `title` values in `_data/author.yml` (`linkedin`, `github`, `email`, plus `twitter`, `dev`, `instagram`, `telegram` which are unused by the current data file).

**`images/`:**
- Purpose: Post images and banners (`images/gtm-eng.jpg`, `images/a2a.gif`, `images/barbell-graph.png`, and so on).
- Generated: No. Committed: Yes.
- Note: Several posts reference images through `https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/...`, not a relative path. Both forms exist in the post corpus.

**`.github/workflows/`:**
- Purpose: CI build and GitHub Pages deploy. `jekyll.yml` runs on push to `main`, Ruby 3.1, `JEKYLL_ENV=production`.

## Key File Locations

**Entry Points:**
- `index.md`: Home listing (`/`).
- `index.html`: Conflicting home placeholder (`/`).
- `blog.html`: `/blog.html` listing.
- `_config.yml`: Build configuration, collections, plugins, and the `defaults` block for posts.

**Configuration:**
- `_config.yml`: Site title, `timezone: Australia/Brisbane`, `markdown: kramdown`, plugins, collections, exclusions.
- `_data/author.yml`: Author identity and social links.
- `Gemfile`: Ruby gems (`github-pages`, `jemoji`, `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed`).
- `.prettierrc`: Formatter settings for HTML, CSS, and JS.
- `.vscode/settings.json`: Editor format-on-save (Prettier).
- `.gitignore`: `_site/`, `.jekyll-cache/`, secrets patterns, `.claude/`.

**Core Logic:**
- `_layouts/post.html`: Post page structure.
- `_layouts/blog.html`: Home page article loop.
- `_includes/head.html`: Stylesheet selection, MathJax, theme bootstrap.
- `assets/js/categories.js`: Category modal.
- `assets/js/mode.js`: Theme switching.

**Testing:**
- None. No test directory, no spec files, no CI test step. Verification is a manual `bundle exec jekyll serve` (see `README.md`).

## Naming Conventions

**Files:**
- Posts: `YYYY-MM-DD-kebab-slug.md`, for example `all_collections/_posts/2025-07-28-technology-adoption-innovation-curves-comprehensive-analysis.md`. The slug becomes the URL segment under `/posts/`.
- Layouts and includes: lowercase single word or hyphenated, for example `category-modal.html`, `post.html`.
- Assets: lowercase hyphenated (`common.css`, `categories.js`, `lbox.js`). Icons match provider names in lowercase.
- Images: mostly lowercase hyphenated (`ai-transformation-2020-2040.png`). Exceptions exist (`155333421.png`, `li-qr.jpeg`, `Section 4 Amendment.md` in `_archive`).
- Archive and papers: free-form names with spaces, `copy` suffixes, and version suffixes. Do not follow the post convention.

**Directories:**
- Jekyll-reserved underscore prefixes: `_posts`, `_layouts`, `_includes`, `_data`. Content collections are `_archive`, `_drafts`, `_papers`, `_worksheets`, but only `_posts` is registered in `_config.yml`.
- Lowercase, no spaces: `assets`, `images`, `css`, `js`, `icons`.

**Front matter:**
- Keys: `layout`, `title`, `date`, `categories`. Category strings use title case with spaces (`GTM Engineering`). Avoid hyphens and multiple spaces in category names, because `assets/js/categories.js` breaks on them (see ARCHITECTURE.md Anti-Patterns).

## Where to Add New Code

**New post:**
- File: `all_collections/_posts/YYYY-MM-DD-slug.md`
- Front matter: `layout: post`, `title`, `date`, `categories: [Title Case, Single Spaces Only]`.
- Images: add to `images/` and reference relatively (`![alt](/images/name.png)` with `baseurl` if needed) or use the raw GitHub URL pattern already used by recent posts. Keep one convention per post.
- Excerpt: include a `TL;DR` line in the body if you want the listing to show a summary; the excerpt is the text after `TL;DR`.

**New static page:**
- File: `<name>.md` at repo root with front matter `layout: blog` (for listings) or `layout: post` (for an article-style page). Do not use `layout: default` until `_layouts/default.html` exists.
- Permalink: defaults to `/<name>.html`. Set `permalink:` in front matter for clean URLs.

**New layout:**
- File: `_layouts/<name>.html`. Include the shared shell pieces from `_includes/` rather than duplicating markup.

**New partial:**
- File: `_includes/<name>.html`. Reference it with `{% include <name>.html %}`.

**New stylesheet:**
- File: `assets/css/<name>.css`. Link it from `_includes/head.html` (the selection is `page.layout == "post"` or else). Put theme variables in `common.css` under `[data-theme="light"]` and `[data-theme="dark"]` to keep both themes consistent.

**New client script:**
- File: `assets/js/<name>.js`. Load with `<script defer>` from `_includes/head.html` (or `_includes/footer.html` for scripts that need the DOM). Keep it standalone; the project has no bundler.

**New social link:**
- Edit `_data/author.yml` `contact` list. Add the icon at `assets/icons/<title>.png` with the same `title`.

**New author data or bio text:**
- `_data/author.yml`. The `description` field is raw HTML.

**Utilities and helpers:**
- None exist. No shared JS module directory. Shared logic belongs in an `_includes/` partial for markup or a new file under `assets/js/` for behaviour.

## Special Directories

**`_site/`:**
- Purpose: Jekyll output.
- Generated: Yes. Committed: No (`.gitignore`).

**`.jekyll-cache/`, `.sass-cache/`, `.jekyll-metadata`:**
- Purpose: Build caches.
- Generated: Yes. Committed: No (`.gitignore`).

**`all_collections/_archive/`, `all_collections/_papers/`, `all_collections/_worksheets/`, `all_collections/_drafts/`:**
- Purpose: Authoring source, research, and reference material.
- Generated: No. Committed: Yes. `_drafts/` guides are tracked despite `.gitignore` naming them.
- Build effect: None. These folders are not declared in `_config.yml`, so they are not rendered.

**`.planning/`:**
- Purpose: GSD planning and codebase-map output. `.planning/codebase/` holds these analysis documents.
- Generated: Yes (by mapping tooling). Committed: Decide per workflow.

**`.DS_Store` files:**
- Purpose: macOS Finder metadata.
- Committed: Yes (3 tracked files), despite `.gitignore` listing `.DS_Store`. Remove with `git rm --cached` if unwanted.

**`.claude/`:**
- Purpose: Local Claude Code settings. Excluded by `.gitignore`.
- Generated: No. Committed: No.

---

*Structure analysis: 2026-10-10*
