---
last_mapped_commit: 28a202c137557de312a6ec6443ed52ecb735af8d
last_mapped_at: 2026-10-10
---
# Codebase Concerns

**Analysis Date:** 2026-10-10

## Tech Debt

**Gemfile and Gemfile.lock are out of sync:**
- Issue: `Gemfile` declares `gem "github-pages"` but `Gemfile.lock` contains no `github-pages` entry. The lock instead pins `jekyll (4.2.2)` directly and a single platform (`nokogiri (1.13.6-x86_64-linux)`). The author uses macOS (`.DS_Store` files are tracked), so the lock was generated on Linux and is not portable.
- Files: `Gemfile`, `Gemfile.lock`, `.github/workflows/jekyll.yml`
- Impact: `bundle install` re-resolves on each machine and in CI, so local builds and GitHub Pages builds can use different Jekyll/plugin versions. The CI step uses `bundler-cache: true` without `frozen`/`BUNDLE_DEPLOYMENT`, so the lock is silently rewritten at build time. Builds are not reproducible.
- Fix approach: Decide on one of (a) `github-pages` gem, which pins Jekyll to the Pages version, or (b) plain Jekyll plus the plugins listed in `_config.yml`. Regenerate the lock on the target platform with `bundle lock --add-platform x86_64-linux arm64-darwin`, commit it, and set `bundle config set --local deployment true` in CI.

**Pinned gem versions are old and carry known advisories:**
- Issue: `Gemfile.lock` pins `nokogiri 1.13.6`, `rexml 3.2.5`, `activesupport 7.0.2.3`, `kramdown 2.3.2`, `sassc 2.4.0` (libsass, deprecated upstream), and `jekyll 4.2.2`.
- Files: `Gemfile.lock`
- Impact: Several of these have published CVEs or are unmaintained. Since the site is static, runtime exposure is small, but the build toolchain runs on every deploy.
- Fix approach: After resolving the Gemfile conflict above, run `bundle update --conservative nokogiri rexml kramdown` and rebuild. Replace `sassc` with `sass-embedded` if the Sass pipeline is used.

**Duplicate and conflicting index pages:**
- Issue: Both `index.html` (`layout: default`) and `index.md` (`layout: blog`) map to the site root `/`. The `default` layout does not exist (no `_layouts/default.html`), and `blog.html` at the root has the same problem.
- Files: `index.html`, `index.md`, `blog.html`, `_layouts/blog.html`
- Impact: Jekyll emits a "destination shared by multiple files" conflict warning and only one file wins, which is nondeterministic from the author's point of view. Any page using `layout: default` will fail to render or render without a layout. `index.html` and `blog.html` look like unused template leftovers from the upstream theme.
- Fix approach: Keep `index.md` as the homepage and delete `index.html` and the root `blog.html`. Only one file may own `/`.

**Leftover upstream theme README and placeholder pages:**
- Issue: `README.md` is the upstream theme README (`sharadcodes/jekyll-theme-serial-programmer`), with "Live Demo" and install steps for someone else's theme. `about.md` and `contact.md` contain only template placeholder text ("Write your 'About Me' content here.").
- Files: `README.md`, `about.md`, `contact.md`, `index.html`
- Impact: The public repo describes a different project. `/about/` and `/contact/` are published with placeholder copy.
- Fix approach: Replace `README.md` with a project-specific description and write real content for `about.md` and `contact.md`, or remove them from the nav.

**Tracked files that the ignore rules say should not be tracked:**
- Issue: `.gitignore` lists `.DS_Store`, `.vscode/`, `WRITING-GUIDE.md`, `EDITORIAL-GUIDE.md`, `.claude/`, and `CLAUDE-TEMPLATE.md`. Git still tracks `.DS_Store`, `all_collections/.DS_Store`, `assets/.DS_Store`, `.vscode/settings.json`, `all_collections/_drafts/WRITING-GUIDE.md`, and `all_collections/_drafts/EDITORIAL-GUIDE.md` (confirmed with `git ls-files -ci --exclude-standard`).
- Files: `.gitignore`, `all_collections/_drafts/WRITING-GUIDE.md`, `all_collections/_drafts/EDITORIAL-GUIDE.md`, `.DS_Store`, `.vscode/settings.json`
- Impact: The `.gitignore` section titled "Sensitive files and templates" is ineffective for these paths. Internal editorial guides are in a public repository (`CNAME` indicates a public GitHub Pages site).
- Fix approach: `git rm --cached` each path, then commit. Consider moving the editorial guides out of the repo if they are not meant to be public.

**Large binaries committed to git history:**
- Issue: `all_collections/_papers/` holds PDFs and a DOCX that are not part of the site build (underscore-prefixed directories are not published). The largest blobs are `The-2025-AI-Visibility-Index-Study-Semrush-Enterprise-compressed.pdf` (~54 MB), `2512.23676v1.pdf` (~26 MB), and `w34255.pdf` (~10 MB). The `.git` directory is 112 MB.
- Files: `all_collections/_papers/*.pdf`, `all_collections/_papers/meaning_sense_making_compression.docx`
- Impact: Every clone pays this cost, and GitHub enforces a 100 MB per-file hard limit, so the 54 MB file is close to it. These binaries are not used by the site.
- Fix approach: Move the papers out of the repository (cloud storage or a release asset) and link to them. Use `git filter-repo` if history must be cleaned. Keep `_papers` out of the working tree only if it is not needed for the build.

**Snapshot and duplicate content in the archive:**
- Issue: `all_collections/_archive/` holds 49 files, including near-duplicate drafts with suffixes such as `-final`, `-humanized`, `-refined`, `-restructured`, `-backup`, and a file named `2025-07-28-technology-adoption-innovation-curves-comprehensive-analysis copy.md` (with a space). `all_collections/_posts/2025-07-28-technology-adoption-innovation-curves-comprehensive-analysis.md` also exists as a published version.
- Files: `all_collections/_archive/`, `all_collections/_posts/2025-07-28-technology-adoption-innovation-curves-comprehensive-analysis.md`
- Impact: Confusing for editors. Searches and greps return stale copies. The space in the filename breaks unquoted shell use.
- Fix approach: Keep a single canonical version in git history and delete the archive copies, or move them into a clearly named folder outside `all_collections/`.

**Test and placeholder content published as posts:**
- Issue: `all_collections/_posts/2021-11-04-jekyll-markdown.md` is the theme's markdown sample ("Jekyll Theme Markdown Guide") with the categories `"jekyll", "Test Post", "first post"`. It links to `./another-page.html`, which does not exist.
- Files: `all_collections/_posts/2021-11-04-jekyll-markdown.md`
- Impact: A test post appears in the blog listing and in the category modal (`"Test Post"`, `"first post"`, `"jekyll"` categories show up in `assets/js/categories.js`). The broken link is visible to readers.
- Fix approach: Delete the post or set `published: false`, and remove the test category links.

**Front matter dates do not match filenames:**
- Issue: The date in the filename and the front-matter `date:` differ for three posts.
- Files: `all_collections/_posts/2024-04-29-ai-training-data-model-collapse.md` (front matter 2024-05-05), `all_collections/_posts/2024-07-03-gen-ai-business.md` (front matter 2024-07-04), `all_collections/_posts/2024-09-22-reference-architecture.md` (front matter 2024-09-23)
- Impact: Jekyll uses the front-matter `date` for ordering and display, so the dates on the listing differ from the filename. This is confusing when editing, but not broken.
- Fix approach: Choose one source of truth and align them. The front matter wins at build time.

**Non-post files inside the Jekyll source tree:**
- Issue: `all_collections/_papers/2026-01-04.md`, `2026-01-12.md`, and `2026-01-19.md` have no front matter, no date, and no title. They are not built, but they sit beside real posts.
- Files: `all_collections/_papers/2026-01-04.md`, `all_collections/_papers/2026-01-12.md`, `all_collections/_papers/2026-01-19.md`
- Impact: Editor noise. The `_papers` folder is not a declared collection, so these files are never built.
- Fix approach: Move or delete them, or add front matter if they are meant to be published.

## Known Bugs

**Category modal breaks on titles containing backticks or `${`:**
- Symptoms: Clicking a category pill can throw a JavaScript syntax error in `categories.js`, and the modal does not open.
- Files: `assets/js/categories.js`
- Trigger: `categories.js` is generated by Liquid and inserts `{{post.title}}` raw into a JavaScript template literal (backtick string). Any post title containing `` ` `` or `${` produces invalid JavaScript for the whole file.
- Workaround: Avoid backticks in titles. The proper fix is to escape with `{{ post.title | jsonify }}` (and `| jsonify` for dates) instead of raw interpolation.

**Category lookup fails for multi-word names with more than one space:**
- Symptoms: `categories[e.target.innerText.replace(" ","_")]` replaces only the first space. Category names with two or more spaces (for example `"Digital Transformation Strategy"`) return `undefined`, and `posts.forEach` throws.
- Files: `assets/js/categories.js`, `_includes/head.html` (loads the script)
- Trigger: Click a category whose name has two or more spaces. The Liquid side builds keys with `replace: " ", "_"`, which replaces all spaces, so the key lookup is inconsistent with the JS side.
- Workaround: Use one-word categories or hyphenated names. The fix is `.replace(/ /g, "_")` in JS, or better, `jsonify` a map keyed by the same string.

**Category click target can be a child element:**
- Symptoms: `e.target.innerText` is read from the click target. If a future category pill contains a child element, the lookup fails.
- Files: `assets/js/categories.js`, `_layouts/blog.html`, `_layouts/post.html`
- Trigger: Nested markup in the `.category` anchor. Currently the anchor contains plain text, so this does not fire yet.
- Workaround: Use `e.currentTarget` instead of `e.target`.

**Post permalinks collide if titles repeat or change:**
- Symptoms: Permalinks are `/posts/:title/`, so the date is dropped. Two posts with the same title produce the same URL and one overwrites the other.
- Files: `_config.yml` (`defaults` for `_posts`)
- Trigger: Renaming a post title changes its URL and breaks inbound links. Duplicate titles collide. No duplicates exist today (checked with `uniq -d` on `title:`).
- Workaround: Keep titles unique and stable. Better fix: `permalink: /posts/:year/:month/:day/:title/`, or set explicit `permalink:` on each post.

**Broken local image reference in a published post:**
- Symptoms: The image does not render.
- Files: `all_collections/_posts/2024-08-27-compute-efficient-frontier.md` (line 84, external `museum.ipsj.or.jp` URL), `all_collections/_posts/2024-04-15-efficient-training-and-inferencing.md`, `all_collections/_posts/2024-08-27-compute-efficient-frontier.md`
- Trigger: Open the post. The local references `images/gtm-transformation.jpg`, `images/sales-revolution.jpg`, and `images/technology-adoption-curves.png` are not present in `images/` (only the archived copies reference these names). The `0008_01_l.jpg` reference is an external URL that may no longer resolve.
- Workaround: Add the missing files to `images/` or replace the references.

**Build-tool files are published as static files:**
- Symptoms: `Gemfile`, `Gemfile.lock`, and `.prettierrc` are not in the `exclude:` list in `_config.yml`. Jekyll copies files without front matter into `_site/`, so they are served publicly.
- Files: `_config.yml`
- Trigger: `bundle exec jekyll build` and inspection of `_site/`.
- Workaround: Add `Gemfile`, `Gemfile.lock`, `.prettierrc`, and `all_collections/_papers` to the `exclude:` list.

## Security Considerations

**Third-party MathJax loaded from a floating CDN URL without Subresource Integrity:**
- Risk: The site loads `https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js` on every post. The `@3` range is not pinned, so any new 3.x release runs on the site. No `integrity=` attribute is set. A compromised CDN or npm package would execute arbitrary JavaScript in the origin of every post page.
- Files: `_includes/head.html` (the `<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/...">` tag)
- Current mitigation: `defer` only. No CSP, no SRI.
- Recommendations: Pin an exact version and add `integrity="sha384-..."` with `crossorigin="anonymous"`. Or self-host the MathJax file under `assets/js/`.

**Chart.js loaded from an unpinned CDN in a post body:**
- Risk: `all_collections/_posts/2025-09-24-citation-attention.md` line 9 loads `https://cdn.jsdelivr.net/npm/chart.js` with no version and no SRI. It also contains four inline `<script>` blocks (lines 82, 190, 376, 544) that run in the page origin. Raw HTML in Markdown is not sanitized by Jekyll.
- Files: `all_collections/_posts/2025-09-24-citation-attention.md`, `all_collections/_posts/2026-06-01-frontier-gtm-engineering.md` (CDN reference in citations only, not loaded)
- Current mitigation: None.
- Recommendations: Pin `chart.js@<version>` and add SRI. Move the inline scripts into `assets/js/` and load them with a pinned, SRI-protected tag.

**No Content Security Policy or security headers:**
- Risk: GitHub Pages does not let the site set response headers. There is no `<meta http-equiv="Content-Security-Policy">` in `_includes/head.html`. Any injected script (for example through a future post with unsafe HTML) runs without restriction.
- Files: `_includes/head.html`
- Current mitigation: Static output, no user input.
- Recommendations: Add a `<meta http-equiv="Content-Security-Policy">` that restricts `script-src` to `'self'` and the pinned CDN hosts.

**Inline script reads localStorage in `<head>`:**
- Risk: `localStorage.getItem("theme")` is read in an inline `<script>` and written to `data-theme`. The value is not validated, so an unexpected value is written into an attribute. Low severity because only the page's own origin can write this key.
- Files: `_includes/head.html`, `assets/js/mode.js`
- Current mitigation: Only `"dark"` and `"light"` are written by `mode.js`.
- Recommendations: Whitelist the value before setting the attribute.

**Email address and contact details committed in public config:**
- Risk: `dr.robert.li.au@gmail.com` appears in `_config.yml` (`author.email`), `_data/author.yml` (`email`, `description`, `contact`), and the Atom feed. A second address (`robert.li@australiagtm.com`) is also public in `_data/author.yml`. Spam scraping is the realistic exposure.
- Files: `_config.yml`, `_data/author.yml`
- Current mitigation: None needed for an author bio; this is intentional for the blog.
- Recommendations: Confirm both addresses are meant to be public. Consider a contact form or obfuscated mailto if spam becomes an issue.

**Tracked private editorial material:**
- Risk: The `.gitignore` entries and the "Sensitive files and templates" comment show the author intended `WRITING-GUIDE.md` and `EDITORIAL-GUIDE.md` to stay out of the repository. Both are tracked (see Tech Debt). The file content is internal authoring guidance, not site content.
- Files: `all_collections/_drafts/WRITING-GUIDE.md`, `all_collections/_drafts/EDITORIAL-GUIDE.md`
- Current mitigation: None. The files are not published because `_drafts` is not built by default.
- Recommendations: Untrack and remove from history if the content is private.

**No secrets detected in the tracked tree:**
- Scan: `git ls-files` contains no `.env`, `*.pem`, `*.key`, or credential files. `.gitignore` covers these patterns. No API keys were found in `_config.yml`, `_data/`, or `_includes/`. Forbidden credential files were not read.

## Performance Bottlenecks

**Repository size from binary history:**
- Problem: `.git` is 112 MB, dominated by the three PDFs in `all_collections/_papers/`.
- Files: `all_collections/_papers/The-2025-AI-Visibility-Index-Study-Semrush-Enterprise-compressed.pdf`, `all_collections/_papers/2512.23676v1.pdf`, `all_collections/_papers/w34255.pdf`
- Cause: Binaries committed directly rather than linked.
- Improvement path: Move to external storage and purge history if needed (see Tech Debt).

**Large raw images in `images/`:**
- Problem: `images/a2a.gif` is ~3 MB, `images/gen-ai-in-business.png` ~2.6 MB, `images/importance-personal-branding.png` ~1.7 MB, `images/robots-rule.png` ~1.4 MB, `images/punch-card.jpg` ~1.1 MB. None are resized or converted.
- Files: `images/a2a.gif`, `images/gen-ai-in-business.png`, `images/importance-personal-branding.png`, `images/robots-rule.png`, `images/punch-card.jpg`
- Cause: No image pipeline. Images are used at full resolution inside post content.
- Improvement path: Convert photographic images to WebP or resized JPEG (target under 300 KB each), keep the GIF only if animation matters, and add `loading="lazy"` to `<img>` tags in `_layouts/post.html` via the markdown image output.

**Every post loads MathJax and the lightbox:**
- Problem: `_includes/head.html` loads MathJax (a large third-party bundle) on every post, including posts with no math.
- Files: `_includes/head.html`, `assets/js/lbox.js`
- Cause: The script is included unconditionally for `page.layout == "post"`.
- Improvement path: Gate the MathJax include on a front-matter flag (for example `math: true`) and include it only on posts that use it.

**Homepage renders every post in full:**
- Problem: `_layouts/blog.html` iterates over `site.posts` and calls `post.content | strip_html` on each full post body, then truncates. Build cost grows with total post length.
- Files: `_layouts/blog.html`, `index.md`
- Cause: Excerpt generated by stripping the whole post body.
- Improvement path: Use `post.excerpt` with an explicit `<!--more-->` marker in each post, or add a front-matter `description:`.

**Category data embeds full post list on every page:**
- Problem: `assets/js/categories.js` is generated from `site.categories` and contains every post's URL, date, and title. It is loaded synchronously in `<head>` on all pages, including the homepage.
- Files: `assets/js/categories.js`, `_includes/head.html`
- Cause: Data is inlined as a JS object rather than generated per category.
- Improvement path: Load it with `defer`, and move the category data to a JSON file fetched on click.

## Fragile Areas

**Dark mode depends on a global `const` shared between inline script and `mode.js`:**
- Files: `_includes/head.html` (declares `const currentTheme`), `assets/js/mode.js` (reads `currentTheme` as a global, comment on line 3 shows the removed declaration)
- Why fragile: `mode.js` reads a top-level `currentTheme` that is only defined by the inline script in `head.html`. If that inline block is removed or moved, `mode.js` throws `ReferenceError` before the toggle is wired up, so dark mode silently stops working.
- Safe modification: Keep the theme read in one place. Declare `currentTheme` inside `mode.js` (and remove the head copy) or export a small `initTheme()` function called from both places.
- Test coverage: None. No JS tests exist.

**Toggle assumes the header is present on every page:**
- Files: `assets/js/mode.js` (`document.querySelector("#dark-mode-toggle").addEventListener(...)`)
- Why fragile: The script calls `addEventListener` on `#dark-mode-toggle` with no null check. Every layout includes `header.html`, but a new layout that omits it throws on load.
- Safe modification: Guard with `if (toggleSwitch)`.

**Category script uses `window.onload` and assigns to a shared global:**
- Files: `assets/js/categories.js`
- Why fragile: `window.onload = function...` overwrites any other `onload` handler. Adding another script that sets `window.onload` silently removes the category click handlers. The script also calls `console.log(categories)` on every page load.
- Safe modification: Use `document.addEventListener("DOMContentLoaded", ...)`. Remove the `console.log`.

**Lightbox binds only to images present at load time:**
- Files: `assets/js/lbox.js`
- Why fragile: `document.querySelectorAll(".article .content img")` runs once. Images inserted later (for example by a script in a post) get no click handler. The `cursor: not-allowed` on the inner image contradicts the zoom-out behavior described by the container.
- Safe modification: Use event delegation on `.article .content`.

**Post excerpt depends on the literal string `TL;DR`:**
- Files: `_layouts/blog.html` and `blog.html` (`split: 'TL;DR' | last`)
- Why fragile: The excerpt logic splits on the exact text `TL;DR`. Posts without it fall back to the full body with `---` removed, which can show raw content from the start of the post. Fourteen of the 31 posts in `_posts` lack `TL;DR` (checked with `grep -L`). Note also that `replace: '---', ''` also strips any `---` inside prose.
- Safe modification: Replace with `post.excerpt` and an explicit excerpt separator, or a front-matter `description:`.

**Copyright year is hard-coded to start in 2022:**
- Files: `_includes/footer.html` (`&copy; 2022 - {{ 'now' | date: "%Y" }}`)
- Why fragile: The start year is a literal. It is harmless until the site is moved or relaunched.
- Safe modification: Read the start year from `_config.yml`.

**Upstream theme naming leaks into `_config.yml`:**
- Files: `_config.yml`, `_data/author.yml`
- Why fragile: Site title is `Dr. Robert Li` but the `README.md` describes `Serial Programmer` theme. The `jekyll-seo-tag` plugin is listed in `_config.yml` but the head template never calls `{% seo %}`, so no `<meta name="description">` or Open Graph tags are emitted.
- Safe modification: Either add `{% seo %}` to `_includes/head.html` or remove the plugin from `_config.yml` and `Gemfile`.

**Build depends on the `github-pages` gem resolution:**
- Files: `Gemfile`, `Gemfile.lock`
- Why fragile: See Tech Debt. Changing the Gemfile without regenerating the lock changes the Jekyll version used in CI.
- Safe modification: Regenerate the lock in the same change as any Gemfile edit and run `bundle exec jekyll build` locally before pushing.

## Scaling Limits

**Single-page category modal with all posts inlined:**
- Current capacity: 31 posts in `all_collections/_posts/`, roughly 14 categories per post on some posts, with many distinct category names overall.
- Limit: The inline `categories` object grows with every post and category, and is re-emitted on every page.
- Scaling path: Generate per-category JSON files or Jekyll category pages (`/categories/:name/`) and link to them without JavaScript.

**Git repository growth from PDFs:**
- Current capacity: 112 MB `.git`.
- Limit: GitHub warns at 50 MB per file and blocks files over 100 MB. The 54 MB PDF is over the warning threshold.
- Scaling path: Use Git LFS or external hosting for `_papers/`.

## Dependencies at Risk

**`sassc` (libsass):**
- Risk: `Gemfile.lock` pins `sassc 2.4.0`. libsass is deprecated and no longer maintained; Jekyll's Sass converter moved to Dart Sass.
- Impact: Build failures on newer Ruby or platforms. The site currently uses CSS only (`assets/css/*.css`), not SCSS, so the converter may not be needed.
- Migration plan: Remove `jekyll-sass-converter` if no `.scss` files are used, or move to `sass-embedded`.

**`nokogiri 1.13.6` and `rexml 3.2.5`:**
- Risk: Old versions with known advisories. `nokogiri` is also a native extension and this lock is platform-locked to `x86_64-linux`.
- Impact: The macOS development environment will fail to install from the lock. CI on `ubuntu-latest` installs but with old parser code.
- Migration plan: Update with `bundle update --conservative nokogiri rexml` after regenerating the lock for all platforms.

**Ruby version pinned in CI only:**
- Risk: `.github/workflows/jekyll.yml` sets `ruby-version: '3.1'`. Ruby 3.1 is end-of-life (March 2025). There is no `.ruby-version` file to make the local version explicit.
- Impact: CI runs an EOL Ruby. Local development may use a different Ruby, which the lock may not support.
- Migration plan: Set `ruby-version` to a supported release and add a `.ruby-version` file.

**Unpinned CDN dependencies in templates and posts:**
- Risk: MathJax (`mathjax@3`) and Chart.js (`chart.js`) are loaded from jsDelivr with floating version ranges.
- Impact: Upstream breaking changes or a compromised package change site behavior without a repo change.
- Migration plan: Pin exact versions and add SRI (see Security Considerations), or self-host.

## Missing Critical Features

**No automated build validation beyond `jekyll build`:**
- Problem: `.github/workflows/jekyll.yml` only builds and deploys. It does not check links, images, HTML validity, or front matter.
- Blocks: Broken links and missing images (listed above) reach production unnoticed. The workflow deploys on every push to `main`.
- Note: The CI step runs `bundle exec jekyll build` but does not use `--strict_front_matter` or fail on warnings. The `index.html`/`index.md` conflict produces a warning that CI does not treat as an error.

**No link checker, image checker, or spell/front-matter linter in CI:**
- Problem: Missing images and dead external links are not caught.
- Blocks: Reliable publishing of a long-form archive of posts with many external references.

**No RSS/Atom discovery link in the layout:**
- Problem: `jekyll-feed` is in `_config.yml`, but the templates do not call `{% feed_meta %}`, so `<link rel="alternate" type="application/atom+xml">` is not emitted in `_includes/head.html`.
- Blocks: Feed readers cannot auto-discover the feed from the homepage.

## Test Coverage Gaps

**No tests of any kind:**
- What's not tested: Layout rendering, category modal, dark mode toggle, lightbox, excerpt extraction, all front-matter conventions.
- Files: `_layouts/blog.html`, `_layouts/post.html`, `_includes/head.html`, `assets/js/categories.js`, `assets/js/mode.js`, `assets/js/lbox.js`
- Risk: Changes to the Liquid templates or JS can break the site without any signal. The categories JS failure modes above are invisible until a reader hits them.
- Priority: High for the category modal (known bugs), Medium for dark mode.

**No front-matter validation:**
- What's not tested: Presence of `title`, `date`, `layout`, and unique titles across `all_collections/_posts/`.
- Files: `all_collections/_posts/*.md`
- Risk: A post without `date` or with a title that collides on permalink silently overwrites or is misordered (see Known Bugs).
- Priority: Medium. A short script run in CI would cover this.

**No check of internal and external links or image references:**
- What's not tested: Local `images/` references and external URLs in `all_collections/_posts/*.md`. About 50 external URLs are used, including `media.licdn.com` and `discourse-cdn` links with expiring tokens.
- Files: `all_collections/_posts/*.md`
- Risk: Images and references silently rot.
- Priority: Medium. Consider an automated link check on a schedule.

---

*Concerns audit: 2026-10-10*
