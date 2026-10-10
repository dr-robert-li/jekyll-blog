---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
<!-- refreshed: 2026-10-10 -->

# Coding Conventions

**Analysis Date:** 2026-10-10

## Naming Patterns

**Files:**
- Blog posts: `all_collections/_posts/YYYY-MM-DD-kebab-slug.md` (all lowercase kebab-case slug, e.g. `all_collections/_posts/2026-06-01-frontier-gtm-engineering.md`). Three legacy posts break the slug rule and should not be copied: `2024-04-09-cultural-differences-between-LLMs-and-shared-ethical-responsibilities.md`, `2025-02-02-DeepSeek.md`, `2025-03-26-ANT-and-LLMs.md`.
- Archived/working drafts live in `all_collections/_archive/` and may contain spaces (`Section 4 Amendment.md`) or " copy" suffixes; they are not published.
- Layouts, includes: lowercase kebab-case HTML (`_layouts/post.html`, `_includes/category-modal.html`).
- Stylesheets: lowercase single-word or kebab-case (`assets/css/common.css`, `assets/css/post.css`).
- Scripts: lowercase kebab-case, one concern per file (`assets/js/lbox.js`, `assets/js/mode.js`, `assets/js/categories.js`).
- Data files: `_data/author.yml` (single profile file read as `site.data.author`).
- Top-level pages: lowercase (`about.md`, `contact.md`, `404.md`, `blog.html`, `index.md`).

**Functions (JavaScript):**
- camelCase, verbs first: `switchTheme()` in `assets/js/mode.js`.
- Anonymous callbacks for DOM listeners (`document.querySelectorAll(...).forEach((image) => { ... })` in `assets/js/lbox.js`).

**Variables (JavaScript):**
- `const` by default; `let` only when reassigned (`let html = ...` in `assets/js/categories.js`).
- Do not use `var` (none present; keep it that way).
- DOM element handles named after their role: `toggleSwitch`, `lightbox`, `images`.

**CSS:**
- Class names: lowercase kebab-case, BEM-free, component-prefixed for nested parts: `.article-header`, `.article-title`, `.modal-article-date` (see `assets/css/blog.css`, `assets/css/common.css`).
- Custom properties: `--gray-1` ... `--gray-6`, `--white-1`, `--white-2` declared in `assets/css/common.css`. Use these tokens; do not hardcode new colors where a token fits. Note `--gray-2_5` uses an underscore; avoid copying that pattern.
- IDs for singletons: `#dark-mode-toggle`, `#category-modal`, `#category-modal-bg`, `#lightbox`, `#bio`, `#img-wrapper`.

**Liquid / front matter keys:**
- Lowercase, unquoted or double-quoted strings. Standard post keys used by all 31 posts: `layout`, `title`, `date`, `categories`.
- Post `layout: post` is required (the `_config.yml` `defaults` block sets `layout: "post"` and `permalink: /posts/:title/` for `_posts`, and `_includes/head.html` branches on `page.layout == "post"`).

**Categories (content taxonomy):**
- Title Case, free-form, multi-word allowed, comma-separated inline arrays: `categories: [GTM Engineering, Revenue Operations, Enterprise AI]`.
- Keep category names to the existing vocabulary where possible (grep `all_collections/_posts/*.md` before inventing one).
- Multi-word names with more than one space are a known breakage point. See Gotchas below.

## Code Style

**Formatting:**
- Prettier is the configured formatter. Config: `.prettierrc` sets `tabWidth: 2`, `printWidth: 80`, `singleQuote: false`.
- `.vscode/settings.json` enables `editor.formatOnSave` with `esbenp.prettier-vscode`. Format HTML, CSS, JS with Prettier on save.
- Indentation: 2 spaces everywhere. Tabs are not used in any tracked source file.
- Strings: double quotes in JS, HTML attributes, and CSS (`"JetBrains Mono"`, `@import url("...")`).
- Semicolons: present in JS (`assets/js/lbox.js`, `assets/js/mode.js`); `assets/js/categories.js` is inconsistent (missing semicolons inside template literals). Write semicolons.
- Trailing newline: required. `assets/js/categories.js` currently lacks one; do not reproduce this.

**Linting:**
- No ESLint, Stylelint, or HTML validator is configured (`.eslintrc*`, `.stylelintrc*` absent).
- No linter runs in CI. `.github/workflows/jekyll.yml` only builds and deploys (`bundle exec jekyll build` with `JEKYLL_ENV=production`).

## Import Organization

**Ordering (Liquid includes in layouts):**
1. `{% include head.html %}` first inside `<html>`.
2. `{% include header.html %}` next, then page-specific partials (`bio.html`), then the `<section>` body, then `{% include footer.html %}`, then `{% include category-modal.html %}` last.
- See `_layouts/post.html` and `_layouts/blog.html` as the reference.

**Script loading in `_includes/head.html`:**
- Non-deferred blocking scripts first (`categories.js`, the inline theme-restore snippet).
- `defer` for DOM-touching scripts (`lbox.js`, `mode.js`, MathJax). `lbox.js` and `mode.js` are only safe with `defer` because they query DOM nodes at load time.
- Post-only assets are gated with `{% if page.layout == "post" %}`.

**Path Aliases:**
- None. Asset URLs are always `{{site.baseurl}}/assets/...`. Never hardcode a leading `/` for internal assets, because the site is served from a GitHub Pages baseurl.

## Liquid and Template Conventions

- Prefix every internal URL with `{{site.baseurl}}` (see `_includes/header.html`, `_layouts/blog.html`).
- Date output: `{{ page.date | date_to_string }}` (blog listing and post header).
- Excerpt pattern (copy exactly for listings): `{{ post.content | strip_html | split: 'TL;DR' | last | replace: '---', '' | strip | truncatewords: 40 }}`. This assumes every post has a `TL;DR` heading. See `_layouts/blog.html` and `blog.html`.
- Whitespace: the existing templates use `{%` and `%}` with inline spacing inconsistently (`{%endfor%}` in `_layouts/blog.html`, `{% endfor %}` elsewhere). Prefer the spaced form.
- Inline `style=` attributes are rare (one occurrence, `_includes/header.html`). Put new styling in `assets/css/*.css`.

## Markdown and Content Conventions

**Post structure (pattern used by 31 posts):**

```markdown
---
layout: post
title: "Title in Title Case"
date: 2026-06-01
categories: [Category One, Category Two, ...]
---

![Alt text](https://raw.githubusercontent.com/dr-robert-li/jekyll-blog/main/images/<file>)

---

### ***TL;DR***

* *Bullet summary point.*

---

Body text...

## Section Heading

```

- Quote the title when it contains a colon or a quote character; otherwise leave it bare.
- Use `YYYY-MM-DD` for `date:`. It must match the filename date (3 posts currently do not; see Gotchas).
- Hero images are hosted in `images/` and referenced by absolute raw GitHub URL. Follow that rather than relative paths, because the post pages render at `/posts/:title/`.
- Bold and italic inside TL;DR bullets are used for emphasis; keep the `### ***TL;DR***` heading exact, since the excerpt logic keys off `TL;DR`.
- Markdown processor is kramdown (`_config.yml`). Use `##` for sections; `###` for the TL;DR block only.
- Math is rendered by MathJax (`_includes/head.html`): `$...$` inline and `$$...$$` display. Do not escape `$` in code blocks, since MathJax skips `<pre>` and `<code>`.
- Chart.js is loaded per post via an inline `<script src="https://cdn.jsdelivr.net/npm/chart.js">` tag at the top of the post body (see `all_collections/_posts/2025-09-24-citation-attention.md`). Only add this when a post needs it.

**Content style guide:**
- `all_collections/_drafts/WRITING-GUIDE.md` and `all_collections/_drafts/EDITORIAL-GUIDE.md` are the working editorial standards (tense, hyperbole levels, readability, fact-check protocol). They are gitignored (`.gitignore`) and are not published, so treat them as reference only.

## JavaScript Patterns

**DOM access:**
- `document.querySelector` / `querySelectorAll` with CSS selectors; never `getElementById` mixed in. Use `.forEach` on NodeLists.
- Event listeners via `addEventListener` (never inline `onclick=`). Exception: `window.onload` assignment in `assets/js/categories.js`. Do not add more `window.onload` assignments; use `DOMContentLoaded` or `defer` scripts.

**Theme handling (`assets/js/mode.js`, `_includes/head.html`):**
- Theme is stored in `localStorage` under the key `theme` with values `"light"` and `"dark"`.
- The inline snippet in `_includes/head.html` restores it before paint to avoid a flash. Keep that snippet in `<head>`.
- The `data-theme` attribute on `<html>` drives CSS overrides (`[data-theme="light"]`, `[data-theme="dark"]` in `assets/css/common.css`).

**Modal and lightbox pattern (`assets/js/lbox.js`, `assets/js/categories.js`):**
- Open/close is toggled with `classList.toggle("open")` or `classList.add("active")` / `remove("active")`. Use these, not `style.display`.
- Build markup with template literals and assign via `innerHTML` only from trusted, build-generated data (the `categories` object is emitted by Liquid).

**Error handling:**
- No `try`/`catch` and no `onerror` handlers exist in the codebase. Null checks are also absent (see Gotchas). Add a guard before dereferencing a `querySelector` result if you touch these scripts.

**Logging:**
- Framework: none. The only log is a debug `console.log(categories)` in `assets/js/categories.js`. Remove it instead of copying it.

**Comments:**
- Sparse. One-line `//` comments for non-obvious intent only. The commented-out `// const currentTheme = localStorage.getItem("theme");` in `assets/js/mode.js` is dead code; do not extend that pattern.

## CSS Patterns

**Structure:**
- Global reset at top of `assets/css/blog.css` and `assets/css/post.css`: `* { font-family: inherit; text-decoration: none; margin: 0; padding: 0; }`.
- Theme variables first, then element selectors, then class selectors, then `@media` queries at the bottom.
- Responsive breakpoints are `@media` blocks inside each stylesheet (5 in `assets/css/blog.css`, 3 in `assets/css/post.css`). Do not introduce a new breakpoint without checking the existing ones first.

**Color:**
- Always use CSS variables (`var(--white-2)`, `var(--gray-6)`) so dark and light modes both work. Light-only overrides go in `@media (prefers-color-scheme: light)` and `[data-theme="light"]` blocks, matching the existing pattern.

**Fonts:**
- JetBrains Mono loaded from Google Fonts with `@import url(...)` at the top of `blog.css` and `post.css`. Font family string: `"JetBrains Mono", monospace`.

**Syntax highlighting:**
- `assets/css/syntax.css` provides the `.highlight` classes emitted by the kramdown syntax highlighter for fenced code. Only add rules here for token colors.

## Function and Module Design

- JS functions are small, single-purpose, and attached to one DOM concern per file. Keep that scope: one file per feature, loaded only on pages that need it (see the `page.layout` gate in `_includes/head.html`).
- No module system, bundler, or `import`/`export`. All JS is global-scope script tags. Do not introduce `import` statements without also adding a build step.
- Share values between Liquid and JS only through Liquid-generated code (see the `categories` object in `assets/js/categories.js`), not through hand-maintained duplicates.

## Data and Config Conventions

- Site-wide config lives in `_config.yml`. Add plugins to the `plugins:` list and to `Gemfile` together.
- Author/profile fields live in `_data/author.yml`; reference via `site.data.author.*`. Social icons are loaded from `assets/icons/<title>.png`, so a new contact entry needs a matching icon file of the same name (`title:` value).
- Gemfile pins `github-pages`; do not add gems that GitHub Pages does not support.

## Gotchas Observed

- **Category lookup with multiple spaces:** Liquid's `replace: " ", "_"` in `assets/js/categories.js` replaces every space, but the client-side lookup `e.target.innerText.replace(" ","_")` replaces only the first. Any category with two or more spaces (e.g. "Top of Funnel") will not match and `posts.forEach` will throw. Fix the lookup with `replace(/ /g, "_")` when touching this file.
- **Date mismatch:** front matter `date` disagrees with the filename date in three posts: `2024-04-29-ai-training-data-model-collapse.md` (front matter 2024-05-05), `2024-07-03-gen-ai-business.md` (2024-07-04), `2024-09-22-reference-architecture.md` (2024-09-23). Jekyll sorts posts and sets their dates from front matter, so keep the two in sync when editing.
- **Missing TL;DR:** 14 of 31 posts do not contain the `TL;DR` marker, so their listing excerpt falls back to the full body text (`split: 'TL;DR' | last`). Add the TL;DR block to new posts.
- **Missing EOL:** `assets/js/categories.js` has no trailing newline.
- **Global variables:** `currentTheme` in `_includes/head.html` is a top-level `const` in an inline script and is read again in `assets/js/mode.js`. Do not rename it without updating both.
- **Excluded from build:** `exclude:` in `_config.yml` omits `LICENSE` and `README.md`. Keep new non-site docs out of the root unless they are meant to be served.

---

*Convention analysis: 2026-10-10*
