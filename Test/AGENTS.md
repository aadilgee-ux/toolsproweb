# AGENTS.md ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Free Online Tools Corner

## READ THIS FIRST ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â WORKING DIRECTORY RULE (DO NOT IGNORE)
- **ONLY** work in: `E:\free online tools corner\Free Online Tools`
- `Free Online Tools` is the LIVE DEPLOYMENT output folder
- If in doubt about which folder to use, STOP and ask the user first

## Project Overview
Static website for "Free Online Tools Corner". The COMPLETE theme/website is `Free Online Tools.xml` (Blogger template) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â whatever tools exist in that XML = the FULL tool inventory of the site. Current inventory (2026-08): **~230 tools across 11 categories** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Binary (23), Converter Tools (11), Generators (18), Image/PDF (29), Online Calculators (13), SEO Tools (11), Text Tools (16), Units (28), Web Development (30), Web Tools (23), YouTube Tools (28). This matches the homepage stat "230+ Free Tools". No build system, no package manager. Pure HTML/CSS/JS with inline styles and scripts. Live site: `freeonlinetoolscorner.blogspot.com`.

## Architecture
- **Blogger Template**: `Free Online Tools.xml` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Blogger XML template used for blog posts
- **Homepage**: `Free Online Tools.html` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Tool grid, hero, categories slider
- **Tool Pages**: Standalone `.html` files, each self-contained (header + tool + footer)
- **Static Pages**: `about.html`, `contact.html`, `privacy.html`, `terms.html`, `disclaimer.html`
- **Assets**: `Tools Images/` directory for tool icons (`.webp` format)

## Critical: Massive Duplicate Code Problem

Every tool page copies the **entire** header, footer, dark mode JS, and mobile menu JS. This is the #1 issue to fix.

### Duplicated across ALL pages (~30+ files):
1. **Header HTML** (~60 lines) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â logo, search, nav, dark toggle, mobile toggle
2. **Footer HTML** (~30 lines) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 4-column grid with links
3. **Header CSS** (~120 lines) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `.tpw-header`, `.tpw-logo`, `.tpw-header-search`, `.tpw-nav`, `.tpw-actions`, dark mode variants
4. **Footer CSS** (~50 lines) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `.tpw-footer`, `.tpw-footer-grid`, etc.
5. **Dark mode JS** (~8 lines) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â localStorage theme toggle pattern
6. **Mobile menu JS** (~6 lines) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â toggle open/close pattern
7. **Year updater JS** (~1 line)

### The shared dark mode/mobile menu pattern (repeated in every file):
```js
(function(){
  var root=document.documentElement,s=localStorage.getItem('tpw-theme');
  if(s)root.setAttribute('data-theme',s);
  else if(window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches)root.setAttribute('data-theme','dark');
  var dt=document.getElementById('tpwDarkToggle');
  if(dt)dt.addEventListener('click',function(){var t=root.getAttribute('data-theme')==='dark'?'light':'dark';root.setAttribute('data-theme',t);localStorage.setItem('tpw-theme',t);});
  var mt=document.getElementById('tpwMobileToggle'),nav=document.getElementById('tpwNav');
  if(mt&&nav){mt.addEventListener('click',function(e){e.stopPropagation();nav.classList.toggle('tpw-open');mt.classList.toggle('active');});nav.querySelectorAll('.tpw-nav-link').forEach(function(l){l.addEventListener('click',function(){nav.classList.remove('tpw-open');mt.classList.remove('active');});});document.addEventListener('click',function(e){if(nav.classList.contains('tpw-open')&&!nav.contains(e.target)&&e.target!==mt){nav.classList.remove('tpw-open');mt.classList.remove('active');}});}
  var y=document.getElementById('tpwYear');if(y)y.textContent=new Date().getFullYear();
})();
```

## How to Add a New Tool Page

1. Copy any existing tool page (e.g., `Word Counter.html`)
2. Replace the tool-specific content (hero, form, logic, features section)
3. Keep header/footer/dark-mode JS identical
4. Add tool icon `.webp` to `Images/`

## CSS Custom Properties (Design Tokens)

All pages use the same theme variables. Dark mode toggles via `[data-theme="dark"]`:

| Variable | Light | Dark |
|----------|-------|------|
| `--brand` | `#6366F1` | `#818CF8` |
| `--brand-dark` | `#4F46E5` | `#6366F1` |
| `--bg` | `#F8FAFC` | `#0F0A1A` |
| `--surface` | `#FFFFFF` | `#1A1035` |
| `--text` | `#0F172A` | `#F0ECFF` |
| `--border` | `#E2E8F0` | `#2E2445` |

## External Libraries Used (CDN)
- **QR Code**: `qrcode@1.5.3` (qr-code-generator.html)
- **Barcode**: `jsbarcode@3.11.6` (barcode-generator.html)
- **PDF**: `jspdf@2.5.2` / `jspdf@2.5.1` (image-to-pdf, text-to-pdf, invoice-generator)
- **Fonts**: Google Fonts Inter (all pages)

## Conventions
- All JS is vanilla ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â no frameworks, no transpilation
- Tool pages follow a 2-column grid layout (`tool-layout`) on desktop
- Sidebar contains privacy info card + tool-specific options
- Features section at bottom with 3-column grid
- Responsive breakpoints: 1024px, 768px, 480px
- File names use spaces (e.g., `Word Counter.html`) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â unconventional but consistent

## New Theme ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Shared Files (Solution)

Three shared files eliminate ~200-300 lines of duplicate CSS/JS per tool page:

### `new-theme.css`
Shared CSS: variables, base reset, header, search, nav, mobile toggle, tool hero, tool layout, tool cards, form elements, action buttons, output area, stat cards, privacy card, features section, toast, footer, responsive breakpoints.

### `new-theme.js`
Shared JS (IIFE): dark mode init + toggle (localStorage + prefers-color-scheme), mobile nav toggle + click-outside-close + resize-close, year updater, `showToast(msg, duration)`, `copyToClipboard(btn, el)`.

### `new-theme.html`
Canonical template showing the exact header HTML, footer HTML, and how to include `new-theme.css` / `new-theme.js`. Use as reference when creating new tool pages.

## How to Add a New Tool Page (using New Theme)

1. Copy `new-theme.html` as your starting point
2. Add `<link rel="stylesheet" href="new-theme.css"/>` in `<head>`
3. Add `<script src="new-theme.js" defer></script>` before closing `</body>`
4. Copy the **header** block exactly (IDs `tpwDarkToggle`, `tpwMobileToggle`, `tpwNav`, `tpwHeaderSearchInput` are required)
5. Copy the **footer** block exactly (ID `tpwYear` is required)
6. Add `<div class="toast" id="toast"></div>` before the footer
7. Add tool-specific CSS in a `<style>` block (keep it minimal ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â shared styles are in `new-theme.css`)
8. Add tool-specific JS in a `<script>` block after `new-theme.js`
9. Add tool icon `.webp` to `Images/`

## Migrating Existing Tool Pages

For each existing tool page:
1. Remove the duplicated `<style>` block (keep ONLY tool-specific CSS)
2. Remove the duplicated header/footer HTML and replace with the canonical blocks from `new-theme.html`
3. Remove the duplicated dark mode / mobile nav / year updater JS (now in `new-theme.js`)
4. Add `<link rel="stylesheet" href="new-theme.css"/>` and `<script src="new-theme.js" defer></script>`
5. Keep only the tool-specific logic in a single `<script>` block

## Blogger Deployment (Live Site)

All files are in `Free Online Tools/` directory.

### Files for Blogger
| File | Purpose |
|------|---------|
| `Free Online Tools.xml` | **Main Blogger theme** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â upload via Theme > Edit HTML |
| `Tool Pages/*.txt` | **227 tool pages** (as of 2026-08-23) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â HTML for each tool page (authoritative source) |


### How to Deploy on Blogger
1. **Install theme**: Blogger Dashboard > Theme > Edit HTML > paste `Free Online Tools.xml` content > Save
2. **Create pages**: Pages > New Page > switch to HTML view (</>) > paste tool HTML from `Tool Pages/*.txt`
3. **Set labels**: Each tool page gets a category label (`text-tools`, `seo-tools`, `dev-tools`, `converter-tools`, `misc-tools`)
4. **Publish**: Set page slug (e.g., `word-counter`) > Publish

### Key Points
- `Free Online Tools.xml` contains ALL shared CSS (in `<b:skin>`) and JS (dark mode, mobile nav, search, year updater)
- Tool pages only contain tool-specific HTML + tool-specific JS
- Header/footer come from the template ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â do NOT include them in tool pages
- For CDN tools (QRCode, JsBarcode, jsPDF), add the `<script>` tag at the TOP of the tool page body
- Blogger strips `<style>` tags from post body ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â add tool-specific CSS to the tool page's own `<style>` block if needed (some browsers preserve them)
- Always paste tool HTML in the **HTML editor view** (</> button), NOT the Compose editor

### Blogger Page URL Pattern
- Homepage: `https://YOUR-BLOG.blogspot.com/`
- Tool page: `https://YOUR-BLOG.blogspot.com/p/word-counter.html`
- Category: `https://YOUR-BLOG.blogspot.com/search/label/text-tools`

# 2026 MASTER OVERRIDE ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â READ THIS AFTER ALL PREVIOUS SECTIONS

This section is the current operational policy for OpenCode. If an older section conflicts with this section, follow this section.

## 1. AUTHORITATIVE WORKING DIRECTORY

The ONLY development directory is:
`E:\free online tools corner\Free Online Tools`

Rules:
- Never create project files, temporary files, backups, logs, caches, exports, or generated copies outside the working directory.
- Work on the existing files in the working directory first; do not create parallel versions of the same theme/tool.
- Before every file operation, verify the target is inside the working directory.
- Do not blindly delete directories. Only delete an obsolete/generated artifact inside the working directory after verifying that it is not a real source, asset, or required deployment file.

## 2. SESSION RESET / MEMORY PROTECTION

OpenCode memory is NOT the source of truth. The files on disk are the source of truth.

A session reset, context compaction, restart, or 24-hour reset MUST NOT cause the theme to be regenerated, downgraded, reverted, or redesigned from memory.

At the beginning of EVERY task/session:
1. Read this entire `AGENTS.md`.
2. Scan the actual working-directory tree.
3. Identify the canonical current theme files and existing tools.
4. Inspect the current code before making assumptions.
5. Continue from the files that actually exist.
6. Never restore an older version from conversation memory.

If the project and memory disagree, trust the project files.

## 3. NO DUPLICATE / NO PARALLEL THEME RULE

The theme must have one canonical implementation.

Do NOT create:
- `theme-new`
- `theme-fixed`
- `theme-final`
- `theme-final2`
- backup copies
- duplicate CSS/JS frameworks
- duplicate headers/footers
- duplicate tool implementations
- duplicate tool pages
- duplicate library versions unless technically unavoidable

Before creating a new file, search the entire project for an existing equivalent.

If a shared feature is needed by multiple pages, fix/extend the canonical shared implementation rather than copying it into each page.

## 4. WHOLE-PROJECT SCAN IS MANDATORY FOR GLOBAL CHANGES

For any command involving:
- theme
- header
- footer
- navigation
- mobile menu
- dark mode
- search
- colors
- typography
- buttons
- cards
- responsive CSS
- shared utilities
- repeated errors
- duplicate code
- SEO defaults

FIRST scan the whole working directory.

Do not fix a global problem by editing only the first file where it appears.

After every global change, scan the whole project again and verify all affected pages.

## 5. REPEATED ERROR PROTOCOL

If the user reports an error that has happened before, or the same error appears on more than one page:

1. Search the entire project for the exact error text and related selector/function/ID.
2. Find every implementation of the problematic code.
3. Determine the shared/root cause.
4. Fix the canonical source once.
5. Remove obsolete duplicate workarounds.
6. Scan all pages again for the same defect.
7. Check console/runtime errors and broken references.
8. Check desktop, mobile, light mode, and dark mode where relevant.
9. Only then report the error as fixed.

NEVER repeatedly patch the first occurrence while leaving duplicate broken implementations elsewhere.

## 6. CODEBASE CLEANLINESS

Keep the project updated and clean.

Regularly scan for:
- duplicate CSS selectors
- duplicate JS functions
- duplicate IDs
- duplicate event listeners
- repeated header/footer markup
- repeated dark-mode logic
- repeated mobile-menu logic
- duplicate tool cards
- duplicate tool URLs
- duplicate CDN imports
- unused obsolete scripts/styles
- dead links
- broken relative paths
- stale placeholder code

When two implementations perform the same job, select one canonical implementation and migrate/remove the duplicate without breaking functionality.

## 7. CURRENT ARCHITECTURE

The existing architecture is the base and must be preserved:
- standalone `.html` files = tool pages
- `about.html`, `contact.html`, `privacy.html`, `terms.html`, `disclaimer.html` = static pages
- `Images/` = tool icons/assets

The shared header, footer, dark mode, mobile navigation, year updater, toast, clipboard behavior, and other global behavior must not be duplicated across every tool page.

Tool pages should contain tool-specific UI and tool-specific logic only.

## 8. COMPLETE 2026 WEBSITE TARGET

Upgrade Free Online Tools Corner into a professional production-quality 2026 online tools platform.

The website must be:
- modern
- premium-looking but lightweight
- responsive
- accessible
- SEO-friendly
- fast
- privacy-conscious
- AdSense-friendly in structure
- maintainable
- fully functional
- consistent across every page

Do not replace the existing identity with a generic AI template. Preserve the current brand/design language and modernize it consistently.

### Design goals
- refined SaaS-style interface
- excellent spacing and typography
- subtle borders and shadows
- polished cards and buttons
- consistent blue/brand palette already used by the project
- professional light mode
- professional dark mode
- clean responsive navigation
- subtle micro-interactions
- no excessive animation
- no visual clutter
- no fake statistics
- no fake functionality

Any global design change must be applied through the canonical design system rather than one-off page styles.

## 8a. CANONICAL HEADER DESIGN ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â DO NOT CHANGE COLORS

The header is a critical, user-approved brand element. Its identity is a BLUE GRADIENT and must stay that way.

- Header background: `linear-gradient(135deg,#2B83EB 0%,#6366F1 100%)` (light) / `linear-gradient(135deg,#0D1525 0%,#111D33 50%,#0F1A2E 100%)` (dark) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â on BOTH desktop and mobile.
- Logo text is WHITE. Logo icon is a white glass square (`rgba(255,255,255,0.2)`) with "F".
- Desktop search bar is WHITE with dark placeholder; nav links are WHITE (700 weight), hover = translucent white pill.
- Dark toggle is a white pill (`rgba(255,255,255,0.2)`), thumb white, slides on dark mode.
- Mobile search bar keeps the SAME blue gradient background as the header.
- Mobile nav open panel = translucent white/dark (same as it was originally approved).

RULES (learned from a rejected change):
- NEVER change the header from blue-gradient to a frosted/white/light background.
- NEVER change white header text/links to dark `--text` colors.
- NEVER change the dark toggle from its white pill design.
- Header "professionalization" = refine spacing, shadows, hover states, border-radius ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â NOT colors.
- If the user asks to "professionalize" the header, keep the existing blue-gradient + white-on-gradient styling intact.
- Any change to header colors requires explicit user confirmation first.

## 9. HOMEPAGE REQUIREMENTS

The homepage should provide:
- premium hero section
- clear value proposition
- global search
- featured tools
- category navigation
- complete tool directory
- useful trust/privacy section
- how-it-works section
- FAQ where useful
- professional footer

Tool counts must reflect real project data. Never invent user counts, downloads, ratings, or usage statistics.

Search must cover:
- tool name
- category
- description
- keywords

Every search result must point to a real working page.

## 10. TOOL REQUIREMENTS

Every existing tool must be audited and made genuinely functional.

Each tool should support, where applicable:
- clear input guidance
- validation
- processing
- accurate output
- copy
- download
- reset/clear
- useful error messages
- empty state
- mobile layout
- dark mode

Do not leave placeholder buttons.
Do not show fake success/results.
Do not silently fail.

Maintain the existing categories:
- Text Tools
- SEO Tools
- YouTube Tools
- Website Management
- Web Development
- Converter Tools
- Calculators
- Image/PDF Tools
- Generators/Misc

The tool list already present in the project is the primary inventory. Do not remove an existing working tool simply to reduce scope.

## 11. TOOL PAGE UX STANDARD

Every tool page should consistently provide:
1. breadcrumb
2. H1/title
3. short useful introduction
4. main tool interface
5. inputs
6. output/result area
7. primary action
8. copy/download/reset actions where applicable
9. validation/error feedback
10. how-to-use section
11. features section
12. FAQ when useful
13. related tools
14. footer

The tool itself remains the main focus of the page.

## 12. SEO STANDARD ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2026

For every important page implement, where applicable:
- unique title
- unique meta description
- canonical URL
- robots metadata
- Open Graph metadata
- Twitter/X metadata
- semantic headings
- breadcrumbs
- internal links
- appropriate Schema.org structured data

Use schema only when it accurately describes visible page content. Do not generate misleading FAQ or application schema.

Do not keyword-stuff pages.

## 13. PERFORMANCE

Prefer browser-native APIs.

Before adding a CDN/library:
- search for an existing implementation
- confirm it is actually needed
- use one consistent version
- ensure it is not loaded twice

Optimize:
- CSS
- JavaScript
- images
- font loading
- DOM size
- event listeners
- repeated calculations

Do not introduce React, Vue, Node build systems, package managers, or other frameworks unless explicitly requested.

## 14. SECURITY + PRIVACY

Never use:
- `eval()`
- exposed API secrets
- unsafe raw user HTML injection
- fake API responses
- unnecessary file uploads

Sanitize user-controlled HTML/content and validate inputs.

For browser/CORS/server limitations:
- never fake a result
- explain the limitation in the UI
- provide the best browser-only alternative
- clearly identify optional backend/API requirements

Process text/images/calculations locally whenever practical.

## 15. BLOGGER COMPATIBILITY

When editing `Free Online Tools.xml`:
- preserve valid Blogger XML
- preserve Blogger expressions and namespaces
- preserve `<b:skin>`
- do not introduce unsupported server-side code
- validate the resulting XML structure

For standalone pages:
- preserve current file naming/routing conventions
- preserve relative asset paths
- keep shared CSS/JS centralized

Do not mix Blogger template logic into standalone tool pages unless the existing architecture requires it.

## 16. RESPONSIVE / ACCESSIBILITY STANDARD

Check approximately:
- 360px
- 390px
- 480px
- 768px
- 1024px
- desktop widths

Verify:
- no horizontal overflow
- no clipped buttons
- no broken grids
- readable inputs
- correct navigation
- good dark-mode contrast
- keyboard navigation
- visible focus states
- semantic labels
- accessible error messages
- comfortable touch targets

Fix shared responsive problems centrally.

## 17. ADSENSE-READY QUALITY

Structure the website so ads can be added without harming usability.

Maintain:
- original useful content
- functional tools
- clear navigation
- legal pages
- privacy information
- non-deceptive controls
- no accidental-click layouts
- no intrusive overlays

Never claim guaranteed AdSense approval.

## 18. FINAL VALIDATION ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â REQUIRED BEFORE COMPLETION

Before declaring any major task complete, perform a whole-project validation:

### Files
- all changes are inside the working root
- no accidental outside files
- no duplicate theme copies
- no obsolete generated artifacts

### UI
- desktop
- tablet
- mobile
- light mode
- dark mode
- header/footer
- cards/buttons/forms

### Functionality
- every tool link works
- every tool processes valid input
- invalid input is handled
- copy works
- downloads work where applicable
- reset works
- no fake output
- no obvious console-breaking errors

### Code
- no duplicate global functions
- no duplicate IDs
- no duplicate shared CSS
- no duplicate event listeners
- no conflicting library versions
- no unsafe `eval`
- no exposed secrets
- no obvious dead code

### SEO
- titles
- descriptions
- canonical
- OG
- Twitter/X
- structured data
- breadcrumbs
- internal links

### Regression
- search the whole project for the original error
- search all related selectors/functions/IDs
- confirm the root cause is fixed everywhere

## 19. IMPORTANT COMMAND BEHAVIOR

When the user gives a command that can affect the theme globally, do not immediately edit one file.

Use this sequence:

SCAN ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ IDENTIFY CANONICAL SOURCE ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ FIND ALL REFERENCES ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ FIX ROOT CAUSE ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ REMOVE DUPLICATES ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ RESCAN WHOLE PROJECT ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ VALIDATE ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ REPORT

If a problem repeats, restart from SCAN. Do not keep stacking patches.

## 20. FINAL PRINCIPLE

The project files are the truth.
`AGENTS.md` is the persistent project instruction.
OpenCode memory is temporary.

A session reset must never reset the website architecture.
A repeated error must be fixed at its root.
A shared feature must have one canonical implementation.
The theme must remain clean, current, professional, and consistent throughout 2026.

## 21. RESPONSIVE FIRST RULE (MANDATORY) — READ BEFORE EVERY CSS CHANGE
Every CSS change MUST be responsive across ALL breakpoints: desktop, tablet, mobile.
- ALWAYS add media queries for `768px` and `480px` when adding new CSS.
- NEVER add CSS that only works on desktop — every property must have a mobile fallback.
- Before finalizing any CSS change, mentally verify: 1440px, 1024px, 768px, 480px, 360px.
- If a new class/element is added, its responsive rules must be added in the SAME edit.
- Do NOT make separate "mobile fix" passes — build responsive from the start.
- Breakpoints: 1024px (tablet), 768px (mobile), 480px (small mobile), 360px (tiny mobile).

Live Blogger website: `freeonlinetoolscorner.blogspot.com`

Blogger is the deployment target and compatibility is mandatory.

- Preserve valid Blogger XML, `<b:skin>`, Blogger expressions, routing, and deployment requirements.
- Blogger Pages must remain usable.
- Do not introduce PHP, Node.js server requirements, or other server-side dependencies Blogger cannot run.
- Modern HTML/CSS/JavaScript is allowed only when compatible with the final Blogger deployment.
- Check Blogger compatibility before completion.

---


## 23. MOBILE SIZE FREEZE ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â All Tools / Sections (2026-08-12) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â READ BEFORE TOUCHING
These mobile values are app-approved and verified live. Do not change without explicit confirmation.

### All Tools section (mobile 768/480/360)
- 768px: card padding 11px 12px, gap 10px; badge 36x36px r9  .6rem; grid gap:8px;padding:12px; category h3 padding:12px 16px;font-size:0.92rem.
- 480px: card padding:10px 8px;gap:8px;font-size:0.78rem; badge 32x32px  .55rem; grid gap:6px;padding:10px.
- Tool title .tpw-tool-card span: mobile ** .88rem weight 600** (768 block, MUST be bigger than before ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â user asked bigger).
- Base span  .82rem 500 (desktop unaffected).

### Section title tagline ("Browse our growing collection of free online tools.")
- Base:  .9rem;line-height:1.5;max-width:500px.
- 480px:  .85rem;line-height:1.5;max-width:440px ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â renders clean 1-2 lines, no awkward wrap.

### Category slider (mobile, professional center look)
- .tpw-cat-item: BASE 110px flex column center; 480 width:72px;padding:10px 12px;flex column center; 360 width:64px;padding:8px 10px.
- Icon: BASE 52px (svg 24px); 480 40px (svg 18px); 360 36px (svg 16px). Icon margin:0 auto ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â always centered.
- Name: BASE  .82rem 700; 480  .62rem;font-weight:800; 360  .58rem;font-weight:800. (smaller + bolder on mobile per user.)
- "YTube Tools" label = **"YT Tools"** (renamed verbatim in HTML).

### Footer copyright line (mobile 2 lines, 2026-08-23)
- .tpw-footer-bottom p mobile (768px) par 2 lines: line1 = "©YEAR Free Online Tools Corner.", line2 = "All rights reserved."
- Implementation: <br class='tpw-footer-br'/> in footer HTML; base CSS .tpw-footer-br{display:none;} (desktop single line), inside 768 block .tpw-footer-br{display:inline;}. DO NOT revert to single-line on mobile.

### Stats (mobile 2x2 grid, FROZEN)
- 768: card padding:14px 8px;r12;flex column;align+justify center;text-align:center. num clamp(2rem,5vw,2.8rem) #000 line-height:1.1;margin-bottom:2px; label  .75rem #000 margin-top:0.
- 480: num 1.6rem, label  .68rem;margin-top:0. 360: num 1.5rem, label  .62rem.
- Numbers are BLACK on all mobile, gap between number+label is tiny (2px) on all sizes.

## 22. SESSION HISTORY / CURRENT STATE (updated 2026-08-24)

Live site: `freeonlinetoolscorner.blogspot.com` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â theme is deployed and working.

### Current theme state (`Free Online Tools.xml` == `.txt`, byte-identical, ~301,771 bytes)
- Homepage theme is the `.tpw-` preview-based theme, brand `#2B83EB`.
- Header is BLUE GRADIENT on desktop + mobile (see section 8a ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â never change).
- Responsive breakpoints: 1024px, 768px, 480px, 360px ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â all balanced, XML valid.
- Hero H1: `Your All-in-One<span> Free</span><br/><span>Online Tools</span> Platform` (2-line layout).
- CSS organized into 3 marked sections: HOMEPAGE / SHARED BASE, TOOL PAGES EXTENDED, STATIC PAGES.

### 22. APP-ROVED = CANONICAL SETTINGS FREEZE ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2026-08-12 (README BEFORE TOUCHING ANYTHING)
> These are the EXACT values currently live. If another AI model (or any tool) edits the theme,
> it MUST preserve these values verbatim. If in doubt, read these values from the XML and match them.
> This list is the user-approved design. Changes to ANY of these require explicit user confirmation.

**Header (desktop):**
- `.tpw-header` bg: `linear-gradient(135deg,#2B83EB 0%,#6366F1 100%)` (light) / `linear-gradient(135deg,#0D1525 0%,#111D33 50%,#0F1A2E 100%)` (dark wraps ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â dark variant comes AFTER dark block, must stay).
- `.tpw-header-inner`: `max-width:1200px;padding:0 28px;grid-template-columns:1fr auto 1fr;height:64px;gap:20px;` / 1024px `gap:14px`.
- `.tpw-logo`: `gap:10px;font-weight:800;font-size:1.12rem;letter-spacing:-0.02em;color:#fff;white-space:nowrap;` (desktop). Title = `Free Online <br/> Tools Corner` (SPACES REQUIRED on both sides of `<br/>` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â desktop hides the br, so without the spaces it renders "OnlineTools"; FIXED 2026-08-12).
- `.tpw-logo-icon`: `36x36px;border-radius:10px;background:rgba(255,255,255,0.2);font-weight:900;font-size:0.9rem;color:#fff;box-shadow:0 2px 8px rgba(0,0,0,0.12);`.
- Desktop search = `.tpw-header-search` (white field, dark placeholder): `height:38px;width:300px;max-width:320px;padding:0 16px;gap:8px` icon svg `15x15px` input `0.88rem` (REDUCED 2026-08-12 from 44px/360px to match nav/title size); 1024px `width:260px`. Nav `.tpw-nav-link` = `padding:10px 18px;border-radius:24px;font-size:0.95rem;font-weight:700` white, hover = translucent white pill (INCREASED 2026-08-12 from 0.84rem/8px-15px).
- `.tpw-dark-toggle` desktop: `52x28px` pill, white thumb.

**Header (mobile <=768px):**
- `.tpw-header-inner`: `height:52px;padding:0 16px;gap:10px;display:flex;justify-content:space-between;`.
- `.tpw-logo` mobile: `gap:8px;font-size:0.78rem;white-space:normal;line-height:1.2;min-width:0;` ; `br{display:block}` ; title span `max-width:150px;line-clamp:2` (768px) / `max-width:130px;font-size:0.9rem` (360-480px); `.tpw-logo-icon` 32x32px radius 9px (uniform mobile, REDUCED 2026-08-12).
- BUTTON SIZES (approved uniform 2026-08-12, DO NOT resize): `.tpw-search-btn` = `32x32px;border-radius:9px;background:rgba(255,255,255,0.14);border:1px solid rgba(255,255,255,0.25);color:#fff;` svg `15x15px`. `.tpw-mobile-toggle` = SAME `32x32px;radius 9px;same glass;gap:4px` ; hamburger lines: `16px wide;2px tall;background:#fff` ; active = rotate(45deg)/opacity0/rotate(-45) `translate(4px,4px)`. `.tpw-dark-toggle` mobile = `46x26px pill;background:rgba(255,255,255,0.3)`. 360px override keeps the SAME `32x32px` + `46x26px` (uniform on all phones).
- Mobile search strip `.tpw-mobile-search`: `padding:0 16px 12px;background:<header gradient>` (base `display:none`) ; 768px `display:none;padding:12px 16px 14px;` + `.tpw-search-open{display:block;animation:tpwSearchIn 0.25s ease}`. Same gradient for dark.
- Mobile menu `#tpwMobileMenu`: in-flow EMPTY div (see final pattern section below). `gap:1px`. Panel padding `10px 16px 14px` (base) blue gradient. Link `.tpw-mobile-menu .tpw-nav-link`: `width:100%;padding:9px 14px;font-size:0.88rem;font-weight:600;border-radius:8px;background:#F8FAFC;color:#0F172A !important;border:1px solid #E2E8F0;box-shadow:0 1px 2px rgba(0,0,0,0.04);` ; dark via `[data-theme="dark"]`: `background:rgba(255,255,255,0.07);color:#F0ECFF !important;border:1px solid rgba(255,255,255,0.1)`.
   - NOTE: an old `@media (prefers-color-scheme:dark){.tpw-mobile-menu...}` block exists ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â PREFERS-COLOR-SCHEME IS NOT USED, the `[data-theme="dark"]` rule is the one that applies. Keep `[data-theme="dark"]`, do not switch to prefers-color-scheme.

**Hero (all paddings frozen):**
- base: `.tpw-hero{padding:28px 0;...}` (center, gradient `180deg #BCD9F2/#D0E4F7/#E2EDF8` light; dark `#081422/#0D1A30/#0F1D33`).
- 768px: `.tpw-hero{padding:16px 24px 32px;...}`.
- 480px: `.tpw-hero{padding:16px 16px 32px;}` (this rule must stay ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â it OVERRIDES the 768 one; it used to be `40px 16px` and pushed hero too far down).
- 360px: h1 `1.3rem`, p `0.95rem`, badge `0.7rem;padding 6px 12px`.

**Hero H1 (FROZEN, 2026-08-12):**
- Markup: `<h1>Your All-in-One<span> Free</span><br/><span>Online Tools</span> Platform</h1>` (ALL breakpoints show 2 lines: "Your All-in-One Free" / "Online Tools Platform" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the `<br/>` is NOT hidden anywhere; mobile badge text "Free Online Tools, No Registration Required" is separate).
- Desktop h1 font: `clamp(1.5rem,3.5vw,2.6rem)`; 768px: `clamp(1.7rem,5.5vw,2.6rem)` `line-height:1.4`; 480px: `clamp(1.6rem,7vw,2rem)` `line-height:1.4`; 360px: `1.5rem` `line-height:1.4` (mobile 2-line h1, size + line gap INCREASED 2026-08-12).
- Hero badge (768px): `padding:8px 16px;font-size:0.75rem;font-weight:600;margin-bottom:20px;white-space:nowrap` (SINGLE LINE ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â mobile); 480px: `0.7rem;padding 6px 12px;nowrap`.
- Hero p: base `1rem;margin-bottom:28px;line-height:1.6`; 768px `0.98rem;mb 28px;lh 1.6`; 480px `0.82rem`; 360px `0.78rem` (kept small so it fits ~3 lines on mobile).

**Mobile tool-card fix (DO NOT remove):**
- `.tpw-tool-card span{display:block !important;visibility:visible !important;font-size:0.85rem;font-weight:500;color:var(--text) !important;opacity:1 !important;overflow:visible !important;white-space:normal !important;text-overflow:unset !important;max-width:none !important;width:auto !important;}` (768px block).

**Stats section ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â SINGLE LINE on mobile (FROZEN 2026-08-12):**
- Base: `repeat(4,1fr)`; 768px: `repeat(4,1fr);gap:10px` + `.tpw-stat{padding:14px 8px;border-radius:12px}` (removed min-height:120px, was 2ÃƒÆ’Ã¢â‚¬â€2); 480px: `repeat(4,1fr);gap:6px` + stat `padding:10px 4px`, num `1.1rem`, label `0.55rem`; 360px: num `1rem`, label `0.5rem`. All 4 cards stay on ONE row on every phone size. Do NOT revert to 2ÃƒÆ’Ã¢â‚¬â€2/stacked.

**Breakpoints:** 1024px, 768px, 480px, 360px (in that order, each @media block contains its overrides).

**JS FREEZE (dark mode / search / menu) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â file `Free Online Tools.xml`:**
- Put newlines around CDATA (NEVER put the whole script on one line ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `//` would comment it out):
  ```
  <script type='text/javascript'>
  //<![CDATA[
  ...script...
  //]]>
  </script>
  ```
- Dark mode toggles via `[data-theme="dark"]` attribute + localStorage key `tpw-theme`. NOT prefers-color-scheme.
- Search button toggles `.tpw-search-open` on WRAPPER `.tpw-mobile-search` (`msw = tpwMobileSearch.parentElement`), then `msi.focus()`.
- Menu: clones header nav links into `#tpwMobileMenu`, toggles `tpw-menu-open`; `position:static` (in-flow, pushes content down).
- Sync `.txt` byte-identical after EVERY `.xml` change.

### Critical bugs fixed this session ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â DO NOT REGRESS
1. **"Could not store" Blogger error** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â fixed by adding to the XML:
   - `<b:include data='blog' name='all-head-content'/>` inside `<head>` (REQUIRED by Blogger)
   - `<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' ...>`
   - Blog1 widget: `<b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='2' visible='true'/>`
2. **Search bar + dark mode not working** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â root cause: the whole JS was on ONE line:
   `//<![CDATA[ (function(){ ... })(); //]]>` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â the `//` commented out the entire script.
   Fix: newlines around the CDATA:
   ```
   <script type='text/javascript'>
   //<![CDATA[
   (function(){ ... })();
   //]]>
   </script>
   ```
   Verified via node syntax check + runtime test (dark toggle toggles dark/light, search + mobile nav listeners bound). DO NOT minify away these newlines.
3. **Mobile tool text hidden** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `.tpw-tool-card span{display:block !important; visibility:visible !important; color:var(--text) !important; opacity:1 !important; ...}` added in 768px block.

### Tool pages (`.tool-*` classes)
- `Tool Pages/*.txt` (227 files as of 2026-08-23; was 41 on 2026-08-13) use `.tool-hero`, `.tool-layout`, `.tool-card`, `.tool-textarea`, `.stat-row`, `.features-grid`, `.privacy-card` etc.
- **DONE (2026-08-13): shared `.tool-*` CSS now exists** inside `Free Online Tools.xml` `<b:skin>` (injected before `]]></b:skin>`). It covers `.tool-hero`/`-inner`, `.tool-badge`/`-dot`, `.tool-layout` (grid 1fr 340px), `.tool-main`, `.tool-sidebar`, `.tool-card` + header/title/actions/btn, `.tool-textarea`, `.stat-card`/`.stat-row`/`.stat-label`(+icon colors)/`.stat-value`, `.privacy-card`, `.features-section`/`-title`/`-grid`, `.feature-card`/`.feature-icon` (color variants), `.form-group/label/input/select/textarea`, `.form-row`, `.btn-row`, `.action-btn`, `.generate-btn`, `.copy-all-btn`, `.clear-btn`, `.copy-btn`, `.download-btn`, `.alt-btn`, `.tool-actions-bar`, `.output-area`, `.result-box`, `.result-card`; responsive @1024/768/480/360; uses theme tokens + `[data-theme="dark"]`. So tool pages render styled + responsive when published (they now inherit the homepage theme).
- **DONE (2026-08-13): duplicated shared JS removed from all tool pages.** The OLD per-page JS (theme init, `tpwDarkToggle` toggle, `tpwMobileToggle`/`tpw-open` mobile menu, `tpwYear` updater) is now central in the theme only. All 41 `Tool Pages/*.txt` scripts now contain ONLY tool-specific logic and pass `node --check`. Zero `tpwDarkToggle`/`tpw-theme`/`tpwMobileToggle`/`tpw-open`/`tpwYear` references remain in `Tool Pages/`.
- 5 pages were already clean (no shared JS): Color Picker, HEX to RGB Converter, Status Code Checker, Thumbnail Downloader, URL Redirect Checker.
- **Pre-existing tool bugs fixed (2026-08-13):** HEX to RGB (`function rgbToHex(...)=>` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `const rgbToHex=(...)=>`), MD5 SHA Hash Generator (SHA-1 rounds 40ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“59/60ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“79 paren imbalance `b(b(x,y,z),a[q])`ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢`b(x,y,z)),a[q]`), Text to Slug (copyBtn ending `)})};`ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢`)})}};`).
- **RESOLVED (2026-08-23):** Unit Converter and YouTube Description Generator both now have FULL working tool logic (Unit Converter: 8 categories, from/to selects, swap, live convert incl. temperature formulas, copy with fallback; YT Description Generator: keywords/tone/hook ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ description with chapters + hashtags + links, run/clear/copy/download). Both pass `node --check`. See section 27 for the related project-wide cleanup.
- **WARNING:** when stripping tool-page JS use a replacement FUNCTION in `String.replace`, NOT a string ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â JS string replacement treats `$'` as a special substitution pattern and silently deletes it. The working script is at `C:\Users\WATCHS~1.DES\AppData\Local\Temp\opencode\strip_shared.js`. Original pre-strip files are backed up at `C:\Users\WATCHS~1.DES\AppData\Local\Temp\opencode\toolpages_backup`.
- Live tool pages return 404 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â not yet published on Blogger.

### 2026-08-12 (NEW) - Mobile search + menu FINAL pattern - DO NOT REGRESS
User spent 4 hours fighting the old overlay menu. The approved final pattern:

**Mobile search (mirror-style):**
- `.tpw-mobile-search` strip = IN-FLOW div BELOW the header (inside the mobile gradient band), default `display:none`.
- Search button `#tpwSearchBtn` (768px only) toggles `.tpw-search-open` on the WRAPPER `.tpw-mobile-search` (NOT the inner input) via `msw.classList.toggle('tpw-search-open')` where `msw = tpwMobileSearch.parentElement`.
- Then `msi.focus()` opens the keyboard. Fade-in via `@keyframes tpwSearchIn`.
- Desktop header search untouched.

**Mobile menu:**
- `#tpwMobileMenu` = EMPTY in-flow div placed after the mobile-search strip, before `<main>` (`<div class="tpw-mobile-menu" id="tpwMobileMenu"></div>`).
- Base CSS `.tpw-mobile-menu{display:none;}` ; 768px `.tpw-mobile-menu.tpw-menu-open{display:flex;flex-direction:column;gap:1px;animation:tpwSearchIn 0.25s ease;}` with `position:static` (in-flow). <== gap is `1px`, FROZEN by user (2026-08-12).
- JS clones header nav links into it on load: `mmenu.appendChild(l.cloneNode(true))` and toggles `tpw-menu-open` for `#tpwMobileToggle`.
- Menu OPENS IN FLOW -> pushes hero/content DOWN. Never a fixed overlay on top.
- `.tpw-nav-link` in the mobile menu: `padding:7px 12px;font-size:0.82rem;font-weight:600;border-radius:8px;background:#F8FAFC;color:#0F172A !important;border:1px solid #E2E8F0` (light) / `background:rgba(255,255,255,0.07);color:#F0ECFF !important;border:1px solid rgba(255,255,255,0.1)` (dark via `[data-theme="dark"]`, NOT prefers-color-scheme).
- Panel padding: `10px 16px 14px`, blue gradient background (matches header).
- The old `.tpw-nav.tpw-open{position:fixed;...}` overlay rules still exist but are DEAD (JS no longer toggles `tpw-open`). Do not revive them.

**Key lesson:** the site toggles dark mode via `[data-theme="dark"]` attributes, NOT `@media (prefers-color-scheme)`. Always use `[data-theme="dark"]` selectors.

**Mobile header buttons (approved sizes):** search + toggle menu = `34x34px`, radius 9px, white glass (`rgba(255,255,255,0.14)` + `1px solid rgba(255,255,255,0.25)`), hamburger lines 16px. Dark toggle = `50x28px` pill. 360px override: toggle `36x36px`. Keep all three visually consistent ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â do not resize without confirmation.

### AGENTS.md compliance reminder
- READ AGENTS.md fully at session start.
- NEVER change header colors without explicit user confirmation (section 8a).
- Follow the SCAN  FIX ROOT CAUSE  RESCAN whole-project protocol for repeated errors.
- Sync `.txt` after every `.xml` change (they must stay byte-identical).

## 24. STATIC PAGE FILES ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â UPDATED FROM MD SOURCES (2026-08-23)

The 5 static pages live as page-content `.txt` fragments in `Pages/` (paste into Blogger Pages HTML view; theme provides header/footer/CSS/JS). **NOTE: there are NO canonical `Pages/*.xml` files** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â earlier docs claiming so were stale. Reality: `Pages/*.txt` are the canonical editable sources.

Content source documents: `Pages/Blogger HTML ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â About Us.md`, `Blogger HTML ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Contact Us.md`, `Blogger HTML ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Disclaimer.md`, `Blogger HTML ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Privacy Policy.md`, `Blogger HTML ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Terms of Service.md` (em dash in filenames). On 2026-08-23 all five `.txt` pages were REWRITTEN from these md sources, adapted to the theme structure:

- Structure per page: `<section class="tool-hero">` (h1 + subtitle) ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `<section class="container {about|terms|privacy|contact}-content">` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ inner `<div class="{about|terms|privacy}-section">` blocks.
- Placeholders RESOLVED everywhere: `[WEBSITE OWNER NAME]` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ "Free Online Tools Corner"; `[CONTACT EMAIL]` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ support@freeonlinetoolscorner.com (mailto link where apt); `[EFFECTIVE DATE]`/`[LAST UPDATED]` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ August 23, 2026; `[GOVERNING LAW / JURISDICTION]` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ neutral sentence ("applicable laws of the website operator's jurisdiction"). Template-guidance sentences ("replace the placeholderÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦") were dropped.
- Internal links added: Contact Us / Privacy Policy / Terms of Service / Disclaimer / About Us point at their `/p/*.html` URLs (Contact Us "Before Contacting Us" list + About Us "Get in Touch").
- Old Contact Us form + its inline script REMOVED (fake-success form violated no-fake-results policy; new page is email-based, matching the md source).
- Theme skin additions (canonical, benefit all static pages): `list-style:disc;padding-left:6px` on `.privacy-section ul,.terms-section ul,.about-section ul`; added `.privacy-section a,.terms-section a,.about-section a{color:var(--brand);text-decoration:underline;}`.

Files (in `Pages/`):
- `Pages/About Us.txt`
- `Pages/Contact Us.txt`
- `Pages/Disclaimer.txt`
- `Pages/Privacy Policy.txt`
- `Pages/Terms of Service.txt`

**MEMORY RULE (user-confirmed):** When a static page is updated in the future, save the update to its respective `Pages/*.txt` file ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â it is the canonical source for that page's content. If the user provides new md/docx source docs, regenerate the `.txt` from them using the same theme structure above.

**Structure of each `Pages/*.txt`** (content-only, paste into Blogger Pages HTML view):
- `<head>`: meta + Google Fonts + `<style><![CDATA[ THEME_CSS + PAGE_CSS ]]></style>`.
- `<body>`: theme header ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ mobile search/menu ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `<main class="tpw-main"><![CDATA[ PAGE_CONTENT ]]></main>` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ theme footer ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ back-to-top + theme `<script>` (CDATA) + small page `<script>` (FAQ accordion + contact form success).
- PAGE_CSS styles: `.tool-hero`, `.tool-badge*`, `.feature-*`, `.why-*`, `.about-content`, `.privacy-*`, `.terms-*`, `.contact-*`, `.faq-*`, `.info-*`, `.social-link`, `.team-card`. It uses the theme tokens (`--brand`, `--surface`, `--text`, `--card-border`, etc.) and `[data-theme="dark"]` overrides ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â keep it in sync with the theme.
- The theme `<b:skin>` CSS and JS are extracted from `Free Online Tools.xml` at build time, so pages automatically inherit homepage fixes (dark mode, scrollbar, mobile menu, FAB). Rebuild after any theme change to keep pages current.

**WARNING:** Do NOT use `build_blogger.ps1` to regenerate these ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â it embeds STALE JS (`if` instead of `else if` for theme init, dead `tpw-open` nav) that would regress the dark-mode and mobile-menu fixes. Update `build_blogger.ps1` first, or rebuild via the extract-and-inject method described above.

- **STATUS (2026-08-13):** Theme work is COMPLETE through the static-page `.txt` creation step AND the category-slider reduction. Homepage theme (blue-gradient header/footer, dark mode via `[data-theme="dark"]`, custom scrollbar, FAB, in-flow mobile search + cloned-nav menu, reduced/flat category slider) and all 5 static page `.txt` files (About Us, Contact Us, Disclaimer, Privacy Policy, Terms of Service) are done and consistent. No further theme changes pending unless requested.

**2026-08-13 (LATE) — LINKAGE + PAGES AUDIT + FIXES:**
- Homepage links ALL real pages: 41 tools + 5 static = 46 `/p/*.html` links in `Free Online Tools.xml`. Verified one-to-one against `Tool Pages/*.txt` and `Pages/*.txt`.
- Removed orphan card: theme had `<a href='/p/image-converter.html'>Image Converter</a>` with NO matching page (only `image-converter-hub` is real). Deleted the stale card from the Converter Tools section. XML still valid, `.txt` resynced.
- **ADDED static-page CSS to theme `<b:skin>`:** the 5 static page `.txt` files share ONE identical PAGE CONTENT CSS block (6724 chars). Its 19 static-page selectors were NOT in the theme skin, so static pages would render UNSTYLED on Blogger (pages render inside the theme). The full PAGE CONTENT block is now injected into `<b:skin>` before `]]></b:skin>` (theme now 81,414 bytes, XML==TXT). This mirrors the earlier `.tool-*` CSS injection so tool pages + static pages both inherit all needed CSS from the theme on Blogger.
- Static page audits (all 5 PASS):
  - XML valid, no unclosed/mismatched tags in main content.
  - Embedded theme CSS in sync with `<b:skin>`; theme JS identical to theme script block; mobile toggle/search/back-top/year hooks present.
  - **Fixed mojibake in `About Us.txt`:** double-encoded em dash ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â proper `ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â`.
  - **Fixed weak SEO on legal pages:** titles + meta descriptions were `Last updated: January 2026` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â now real titles (`Privacy Policy - Free Online Tools Corner`, etc.) + descriptive meta descriptions. Dates updated January ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â **August 2026** (all 3 legal pages).
  - Titles normalized: `About Us - Free Online Tools Corner`, `Contact Us - Free Online Tools Corner`; H1s aligned.
  - Contact Us content verified: form + 4 FAQs + mailto + success box all present.
- Synced `Pages/*.txt` content sources to match the `.xml` changes.

**2026-08-24 — STATIC PAGES CSS ARCHITECTURE UPDATE:**
Static page CSS lives in theme `<b:skin>` as `/* ===== STATIC PAGES (about / contact / faq / legal) ===== */` marked section (~4588 chars). 5 `Pages/*.txt` files are content-only (no embedded `<style>`). All CSS inherited from theme. Content width: `max-width:900px`. Theme has 3 marked CSS sections: HOMEPAGE / SHARED BASE → TOOL PAGES EXTENDED → STATIC PAGES.

## 25. CANONICAL THEME BASELINE ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â FIXED / RESET POINT (2026-08-24, LIVE-SYNCED) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â NO TOUCH

`Free Online Tools.xml` (**~301,771 bytes** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2026-08-24: 3-section CSS architecture, footer sorted, tool card hover blue, static pages 900px) and its byte-identical sync `Free Online Tools.txt` are the **FIXED, authoritative theme baseline**. User-approved: **NO TOUCH** unless explicitly instructed.

- If the theme is ever **reset, regenerated, or rolled back**, it MUST reset to this exact file (current size, XML == TXT). Older baselines (299,515 / 299,740 / 289,469) are OBSOLETE.
- It must NOT be rebuilt from `preview.html`, via `build_blogger.ps1`, or from any View Source / rendered HTML dump.

### Structure of this baseline (why it works on Blogger)
- `<html>` with all 4 Blogger namespaces; uploads fine via Backup/Restore or Edit-HTML paste.
- `<head>`: metas + Google Fonts Inter + `<b:include data='blog' name='all-head-content'/>` + `<b:skin><![CDATA[ ... ]]></b:skin>` containing ALL CSS in 3 marked sections (see below).
- `<body>` (header/footer on ALL pages):
  - SVG icon sprite ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬â„¢ `<header class='tpw-header'>` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬â„¢ `.tpw-mobile-search` strip ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬â„¢ `#tpwMobileMenu` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬â„¢ rendered ALWAYS (every page/post).
  - `<b:if cond='data:blog.url == data:blog.homepageUrl'>` wraps ONLY `<main class='tpw-main'>` (hero, stats, category slider, ALL tool grids).
  - `<b:if cond='data:blog.url != data:blog.homepageUrl'>` wraps `<div class='tpw-post-outer'>` + `<b:section id='blogger-required-section'>` containing full Blog1 widget. Section must NOT have `maxwidgets`/`showaddelement` attrs.
  - `<footer class='tpw-footer'>` + back-to-top FAB ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬â„¢ ALWAYS.
  - Theme JS at end in `//<![CDATA[ ... //]]>` (newlines around CDATA MANDATORY).
- **CRITICAL Blogger quirk:** `expr:` attributes are NOT evaluated on `<b:section>` tags. Conditional classes must go on a plain wrapper `<div expr:class='...'>` around the section.
- Key IDs required by JS: `tpwDarkToggle`, `tpwMobileToggle`, `tpwNav`, `tpwMobileMenu`, `tpwHeaderSearchInput`, `tpwSearchDropdown`, `tpwMobileSearchInput`, `tpwMobileSearchDropdown`, `tpwYear`, `tpwCatScroll`, `catPrev`, `catNext`, `tpwBackTop`.
- Desktop tool grid (frozen): `.tpw-tool-grid{grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;padding:10px;}` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 5 columns desktop, 2 mobile.
- Header/footer stay BLUE GRADIENT per Ãƒâ€šÃ‚Â§8a ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â never recolor without explicit confirmation.

### 3 CSS Sections in `<b:skin>` (FROZEN ARCHITECTURE ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2026-08-24)
1. **`HOMEPAGE / SHARED BASE`** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `:root` vars, header, footer, hero, stats, categories, tool grids, `.container` (2400px), `.tpw-post` (2400px), base responsive
2. **`TOOL PAGES EXTENDED`** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `.tool-hero` (2000px), `.tool-layout`, `.tool-card` + hover (blue border), `.tool-crumbs-wrap`, `.tool-crumbs`, `.generate-btn`/`.action-btn`/`.clear-btn`/`.copy-btn`/`.download-btn`, responsive
3. **`STATIC PAGES`** ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `.about-content`/`.contact-content`/`.privacy-content`/`.terms-content` (900px), `.faq-section` (900px), `.tool-hero` scoped 900px via `:has(~)`, `.why-grid`, `.why-card`, `.info-grid`, `.info-card`, `.contact-card`, `.form-success`, `.submit-btn`, `.social-links`, `.social-link`, `.team-card`, `.privacy-section ul` (list-style:disc), responsive

### Key widths (FROZEN)
- `.container` = `max-width:2400px`
- `.tpw-post` = `max-width:2400px` (Blogger content wrapper)
- `.tool-hero` = `max-width:2000px` (tool pages)
- `.tool-hero` static pages = `max-width:900px` (scoped via `:has(~)`)
- `.about-content` etc = `max-width:900px`
- `.faq-section` = `max-width:900px`
- `.tpw-header-inner` = `max-width:1200px` (header only)
- `.tpw-footer .container` = `max-width:1200px` (footer only)

### Tool card hover
- `.tpw-tool-card:hover{...border-color:var(--brand);}` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â blue border on hover (NOT `var(--border)`)

### Footer
- Categories and Legal links sorted **alphabetically** (FROZEN).

### Static Pages (`Pages/*.txt`)
- 5 files: About Us, Contact Us, Disclaimer, Privacy Policy, Terms of Service
- Content-ONLY (no embedded `<style>` blocks) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â all CSS inherited from theme
- Hero descriptions are original text, NOT shortened

### Tool Pages (`Tool Pages/`)
- 225 files organized into **11 category folders**: Binary (23), Converter Tools (11), Generators (18), Image/PDF (29), Online Calculators (13), SEO Tools (11), Text Tools (16), Units (28), Web Development (27), Web Tools (22), YouTube Tools (27)
- 2 duplicate files DELETED: `Electric Charge Converter.txt`, `Parts-Per Converter.txt`
- `Publish Checklist.txt` updated with `Category/FileName.txt` paths

## 26. CATEGORY SLIDER ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â REDUCED / FLAT (2026-08-13) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â DO NOT REGRESS

Merged a compact flat-card design into the existing `.tpw-cat-*` selectors. Desktop BASE was reduced in size; mobile 480/360 are FROZEN (only `min-height:auto` added to neutralize the new base `min-height`).

### Base (desktop) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â reduced + flat
- `.tpw-cat-scroll`: `gap:14px;padding:10px 20px;background:var(--bg-alt);scroll-behavior:smooth;` (was none of these).
- `.tpw-cat-item`: `width:92px;min-height:88px;padding:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;border:1px solid var(--border);border-radius:14px;background:var(--surface);color:var(--text);transition:transform var(--transition),box-shadow var(--transition),border-color var(--transition);` (reduced from 110px/52px-icon/0.82rem; flat, no rotate).
- `.tpw-cat-item:hover`: `border-color:var(--border);transform:translateY(-3px);box-shadow:0 6px 16px rgba(15,23,42,0.08);` (flat lift; NOT the old `translateY(-6px) rotateX(8deg) rotateY(-3deg)` 3D).
- `.tpw-cat-icon`: `width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:var(--bg-alt);color:var(--brand);font-size:1.1rem;margin:0 0 8px;` (reduced from 52px).
- `.tpw-cat-item:hover .tpw-cat-icon`: `transform:scale(1.05);` (reduced from 1.08).
- `.tpw-cat-name`: `font-size:12px;font-weight:600;line-height:1.2;letter-spacing:-0.01em;color:var(--text);text-align:center;` (reduced from 0.82rem 700; smaller + lighter per user).
- `.tpw-cat-item.tpw-cat-active`: keep `border-color:var(--brand);background:rgba(43,131,235,0.08);` (unchanged).

### Mobile (FROZEN ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 480px / 360px)
- `.tpw-cat-item` 480: `width:72px;padding:10px 12px;` + `min-height:auto;` (added to neutralize base min-height). 360: `width:64px;padding:8px 10px;` + `min-height:auto;`.
- Icon 480: `40px` (svg 18px). 360: `36px` (svg 16px). Icon `margin:0 auto` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â always centered.
- Name 480: `0.62rem;font-weight:800`. 360: `0.58rem;font-weight:800`. (smaller + bolder on mobile, per user).

### Notes
- The old `preview.html` still has the legacy 110px + 3D-hover category CSS ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â it is STALE and must NEVER be used as the source. The canonical category CSS lives only in `Free Online Tools.xml`.
- No `.category-*` selector exists in the project; search would confirm zero matches.

---
## 27. 2026-08-23 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â TOOL PAGES: PENDING JS RESOLVED + PROJECT-WIDE DEAD-CODE CLEANUP

- **Unit Converter.txt / YouTube Description Generator.txt:** full tool logic present and verified (see RESOLVED note in section 22). No empty scaffold scripts remain.
- **Batch cleanup (root-cause fix per section 5/6):** the stale scaffold pattern `var addBtn=document.getElementById('addBtn'),gBtn=...,bBtn=...,dBtn=...; var copyParamsBtn=document.getElementById('copyParamsBtn');` (getElementById on IDs that do not exist on most tool pages) existed in 174 of 227 `Tool Pages/*.txt`. Removed via usage-detecting Node script: a var is kept ONLY if genuinely referenced elsewhere in that file. Correctly preserved: Google Index Checker (`gBtn`,`bBtn`,`dBtn` all used), UTM Builder (`copyParamsBtn` = real Copy Params button), Website Ranking Checker (`addBtn` = real Add Entry button).
- Unused single-line helper declarations (`escHtml`/`normUrl`/`getYtId`) removed only where unreferenced; ~51 files keep them because they ARE used for output escaping.
- YouTube Description Generator also had an unrelated leftover `<style>` block (rank-table/twitter-card CSS) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â trimmed to only `.empty-state`/`.muted` which its JS actually uses.
- **Validation:** all 227 tool page inline scripts pass `node --check` (0 failures) after cleanup.
- Pre-cleanup backup (transient): `%TEMP%\opencode\toolpages_cleanup_backup`.
- **Still pending:** publishing the tool pages on Blogger (live `/p/*.html` URLs return 404). Requires Blogger dashboard action or user-approved browser automation.

### 2026-08-23 (EVENING) — PUBLISH CHECKLIST + HOMEPAGE DEDUPE
- Created `Publish Checklist.txt` (project root): all 225 homepage tool cards mapped to `Tool Pages/*.txt` with EXACT Blogger slug to use (`*` = slug differs from filename - copy exactly), category labels, per-page steps, plus 5 static pages section and orphan-files section.
- Removed 5 duplicate/legacy cards from theme homepage (root-cause fix per §3/§6): md5sha-hash-generator-generate, web-utilities-url-encoder-decoder, html-encoderdecoder-encode-special, web-development-base64-encoder-decoder ("Base64 Convertor" — base64-converter already exists), youtube-description-generator-generate ("Description Generator"). XML valid, `.txt` resynced (297,495 bytes). Homepage now has 225 unique tool cards.
- ~~Orphan files (exist locally, NO homepage card — do NOT publish blindly): `Electric Charge Converter.txt` (dup variant of Charge Converter.txt), `Parts-Per Converter.txt` (dup variant of Parts Per Converter.txt).~~ **DELETED 2026-08-23** — duplicates of Charge Converter.txt and Parts Per Converter.txt respectively.
- Tool pages still NOT published on Blogger (user chose MANUAL publishing using this checklist).

### 2026-08-23 (NIGHT) — TOOL PAGE STANDARDIZATION PASS (professional UI)
- **Root cause of "demo-looking pages":** 24/227 files had NO category badge, 18 different inconsistent badge values, 26 missing features-section, 226 missing How-to-Use, many terse 1-line intros. Also 2 files used a completely different (un-styled) class system and had mojibake.
- **Batch transformer** (backup at `%TEMP%\opencode\toolpages_std_backup`) applied per-file with a category map (225 files → canonical 11 categories):
  - Badges: normalized 203 existing + added 22 missing (now ALL 227 show a canonical `.tool-badge` category label; 2 files without `tool-hero-inner` handled separately below).
  - Breadcrumbs: added `.tool-crumbs` nav (Home › Category › Tool) to 225 pages.
  - How-to-Use: added `.tool-card.howto-card` + `<ol class="howto-steps">` to ALL 227 pages.
  - Features: added `.features-section` (3 cards) to 26 pages that lacked one.
  - Intros: enriched 70 terse 1-line intros into 2-line useful descriptions.
- **2 structurally-broken pages rebuilt** (root-cause fix): `YouTube Tag Extractor.txt` (used un-styled `tpw-*` homepage classes + `???` mojibake emojis) and `YT Video Downloader.txt` (used bare `hero`/`main` + un-styled `tpw-btn`/`tpw-input`). Both rebuilt into the standard `tool-hero`/`tool-layout`/`.tool-card` structure, JS logic preserved & verified, theme classes used, sidebar `privacy-card` added.
- **Theme skin additions** (`Free Online Tools.xml` `<b:skin>`, synced to `.txt` 297,992 bytes): `.tool-crumbs`, `.crumb-sep`, `.howto-card`, `.howto-steps` (list-style decimal). Breadcrumbs + how-to now render styled on Blogger.
- **Validation:** 227/227 inline scripts pass `node --check` (0 failures). Tag-balance: 225/227 balanced; the 2 mismatches (`Base64 Converter.txt` div 26/25, `Markdown to HTML.txt` p 9/6) are PRE-EXISTING in source (confirmed against backup) — caused by `<div>`/`<p>` inside JS-generated markup strings, not introduced by this pass; benign.
- **Still pending:** publish tool pages on Blogger (manual, via `Publish Checklist.txt`); also re-upload updated `Free Online Tools.xml` to apply new skin CSS + fix mobile (Blogger Mobile settings → "No. Show desktop theme").

### 2026-08-23 (LATE NIGHT) — BREADCRUMB REBUILD + PROFESSIONAL BUTTONS + BREADCRUMB OUTSIDE HERO
- **Root cause:** the standardization pass produced broken breadcrumbs (category text was stripped, leaving empty `<span>` with newlines). Also badge removal left stray fragments.
- **Fix:** PowerShell batch script rebuilt all 225 breadcrumbs from category map (`filecat.json`) + h1 title extraction. Each breadcrumb shows: `Home › Category › Tool Name`.
- **Breadcrumb moved OUTSIDE hero** (user request): now in `<div class="tool-crumbs-wrap"><div class="container">...</div></div>` before `<section class="tool-hero">`. Hero only contains h1 + description.
- **Category links**: currently point to homepage `/` (temporarily — `/search/label/...` returns empty until pages are published with labels). Category link styled as `.crumb-cat` pill badge (brand bg, 20px radius).
- **Badge removed** from all 227 files.
- **Theme CSS** (`Free Online Tools.xml` synced `.txt` 301,605 bytes):
  - `.tool-crumbs-wrap`: padding 18px, bg, border-bottom
  - `.tool-crumbs`: 0.95rem, flex, gap
  - `.tool-crumbs a`: brand color, 600 weight, underline hover
  - `.tool-crumbs .crumb-cat`: brand pill badge, hover bg
  - `.generate-btn`/`.action-btn`: gradient brand bg, 12px radius, shadow, hover lift
  - `.clear-btn`: neutral bg, border, secondary text
  - `.copy-btn`/`.download-btn`/`.alt-btn`: brand-tinted bg, border, hover lift
  - `.tool-card`: 16px radius, subtle shadow, hover lift
  - `.tool-card-header`: bottom border separator
  - `.tool-card-title`: flex with brand-colored SVG icon
  - Dark mode variants for buttons and cards
- **Validation:** 227/227 scripts pass `node --check` (0 failures). XML valid, byte-identical sync confirmed.

---
## 28. 2026-08-24 — CURRENT SESSION STATE (SAVE POINT)

### Theme file
- `Free Online Tools.xml` = `Free Online Tools.txt` = **~301,771 bytes** (byte-identical) — ⚠️ STALE FIGURE. **ACTUAL on-disk size = 280,525 bytes (2026-08-29 scan).** The 301,771 baseline is NOT present in this working dir; the real file is ~21 KB smaller. See §30 for the verified current state.
- 3 marked CSS sections: HOMEPAGE / SHARED BASE → TOOL PAGES EXTENDED → STATIC PAGES
- XML valid, responsive breakpoints balanced at 1024/768/480/360

### Frozen widths (DO NOT CHANGE)
- `.container` = `max-width:2400px`
- `.tpw-post` = `max-width:2400px` (Blogger content wrapper)
- `.tool-hero` = `max-width:2000px` (centered, light+dark gradients working)
- `.tpw-header-inner` = `max-width:1200px`
- `.tpw-footer .container` = `max-width:1200px`
- Static page hero + content = `max-width:900px` (scoped via `:has(~)`)

### Frozen design elements
- Header: BLUE GRADIENT light+dark, white text, white pill buttons
- Footer: BLUE GRADIENT light+dark, links sorted alphabetically
- Tool card hover: `border-color:var(--brand)` (blue border)
- Breadcrumbs: centered, `.crumb-cat` pill badge, outside hero
- Buttons: `.generate-btn`/`.action-btn` gradient brand, `.copy-btn`/`.download-btn` brand-tinted
- Dark mode: `[data-theme="dark"]` attribute + localStorage `tpw-theme`
- Mobile menu: in-flow, pushes content down, gap:1px
- Mobile search: mirror-style strip below header, same gradient

### Static pages
- 5 files: `Pages/*.txt` (content-only, no embedded CSS)
- All CSS inherited from theme `<b:skin>` STATIC PAGES section
- Content width: 900px
- Hero scoped to 900px via `:has(~ .about-content)` etc.
- `<p>` max-width:100% override (was 600px causing wrap)

### Tool pages
- 225 files in 11 category folders: `Tool Pages/{Category}/*.txt`
- All scripts pass `node --check`
- Breadcrumbs outside hero, how-to sections, features sections
- 2 broken pages rebuilt: `YouTube Tag Extractor.txt`, `YT Video Downloader.txt`
- `Publish Checklist.txt` maps all 225 homepage cards to exact filenames + Blogger slugs

### Critical rules for future resets
- NEVER change header colors without explicit confirmation
- NEVER add `@media (prefers-color-scheme)` — use `[data-theme="dark"]` only
- NEVER minify JS across CDATA — newlines around `//<![CDATA[` are MANDATORY
- ALWAYS sync `.txt` after `.xml` changes (byte-identical)
- ALWAYS add responsive rules for 768px + 480px with any CSS change

### Backup files (pre-reset safety net)
- `E:\free online tools corner\tools-website-blogger\Free Online Tools Backup..xml` — **301,296 bytes** (12:04 PM backup — current state, `.tpw-tool-category` deduped)
- `E:\free online tools corner\tools-website-blogger\Free Online Tools Backup..txt` — byte-identical sync
- `%TEMP%\opencode\toolpages_cleanup_backup` — pre-dead-code-cleanup tool pages
- `%TEMP%\opencode\toolpages_std_backup` — pre-standardization tool pages
- `%TEMP%\opencode\static_page_css.css` — extracted static page CSS (now in theme)
- `%TEMP%\opencode\filecat.json` — category map (filename → `{cat, name}`)

## 29. PUBLISHING SLUG DEFECT + FIX (2026-08-24) - CRITICAL

### What happened
- Bulk-published ~100 tool pages via Blogger API v3 pages.insert (script publish_all.js).
- Pages ARE live (public, content + JS correct), BUT Blogger IGNORED the url slug passed and auto-generated UGLY slugs like /p/home-binary-ascii-to-binary-binary.html.
- Root cause: page Title was empty (user directive: don't set a page Title - it shows a duplicate heading). With empty title Blogger derives an ugly slug.
- Result: homepage tool-card links use clean checklist slugs (/p/ascii-to-binary.html) which 404, because real published URLs don't match. Tools look broken from homepage though the tool works at its real URL.

### Confirmed (2026-08-24)
- pages.list = 100 live pages at ugly auto-slugs. Pages PUBLIC (webfetch 200 on real slug).
- Tool JS verified correct from source (ASCII to Binary: Hello -> 8-bit binary). No JS bug on first audited tool.
- Blogger API write-quota (429) exhausts daily ~midnight Pacific; ~130 pages still unpublished.

### THE FIX (do not repeat the defect)
1. Edit theme Free Online Tools.xml: in Blog1 widget REMOVE the duplicate <h1><data:post.title/></h1> (line ~549) - every page already renders its own h1 in .tool-hero/content. Removes the duplicate heading the user objected to.
2. Re-publish with a real Title: keep title: e.title (NOT blank). Blogger derives a CLEAN slug from title (e.g. ASCII to Binary -> /p/ascii-to-binary.html), matching homepage links. The url field is ignored anyway.
3. After quota resets (~midnight Pacific): delete the 100 ugly-slug pages (or pages.update with title) and re-insert all 225 with titles. Idempotent skip must compare pathname slugs (already fixed in listExistingUrls).
4. Re-upload Free Online Tools.xml to Blogger (Theme > Edit HTML) so the duplicate-h1 removal applies.

### Rules added
- NEVER publish a Blogger page with empty Title when the slug must match homepage links. Set Title AND remove theme duplicate h1, OR accept ugly auto-slugs.
- Blogger API pages.insert url field is effectively IGNORED for slug - slug comes from Title.
- Always verify a published page is reachable at the EXPECTED slug (not just exists in API list) before calling it live.

### STATUS (2026-08-24 evening) — user chose "Dono karo"
- Duplicate <h1> REMOVED from theme (line 549) — clean Titles won't double up. Synced .txt (301,268b).
- Built slug_map.json via map_slugs.js: 100 live pages mapped by their <h1> -> actual (ugly) relative slug. 1 manual add: /p/base64-converter.html -> /p/home-converter-tools-base64-encoder.html.
- Applied IMMEDIATE ugly-link fix via pply_slug_fix.js: 99 homepage tool-card hrefs now point to the actual live (ugly) slugs. XML validated (well-formed, 2875 nodes), .txt synced (302,790b).
- Backup Free Online Tools.clean.xml saved = clean-links version (for revert after clean re-publish).
- **USER MUST RE-UPLOAD Free Online Tools.xml to Blogger** for the ugly-link fix to go live (tools clickable but URLs stay ugly).
- ~125 tool pages still NOT published (quota) -> their homepage cards still 404 until published.

### CLEAN RE-PUBLISH (do after quota resets ~midnight Pacific)
1. Delete the 100 ugly-slug live pages (or pages.update each with a real title to regenerate a clean slug).
2. Re-run publish_all.js (default: 	itle: e.title, NO --blank-title) -> creates all 225 with clean slugs matching homepage.
3. Revert theme hrefs to clean slugs: restore Free Online Tools.clean.xml (or invert slug_map.json: value->key) and re-upload theme.
4. Verify a sample tool at its clean /p/<slug>.html returns 200 and converts correctly.

### Key script files
- publish_all.js (publisher; idempotent skip on slug; --limit, --blank-title, --dry-run)
- map_slugs.js (builds slug_map.json from live pages' h1)
- pply_slug_fix.js (repoints homepage hrefs to actual slugs; makes clean-links backup)

### Stray category-label cleanup (2026-08-24)
- Found 51 tool pages with a leftover raw category text line inside .tool-hero-inner BEFORE the <h1> (e.g. Binary Converter, Unit Converter), making the tool name render as 'Decimal to TextBinary Converter'.
- Removed those standalone lines from all 51 files via script (23 Binary + 28 Units). Other categories had none.
- This is CONTENT (not theme) — goes live only after those pages are re-published (batched with the slug/clean-republish after quota).

### Uniformity sweep (2026-08-24)
- All 226 tool pages now structurally standard: 	ool-crumbs-wrap + breadcrumb, 	ool-hero, howto-card, eatures-section present in every file (verified by audit).
- Fixed 2 deviating files: Color Picker.txt and Online Calculators\AdSense Calculator.txt had breadcrumb INSIDE hero — moved to standard .tool-crumbs-wrap before hero.
- Theme Free Online Tools.xml already contains ALL shared CSS (breadcrumbs, hero, layout, cards, howto, features, buttons) and JS — confirmed in <b:skin> (lines 441-456 for breadcrumbs). No theme change needed for uniformity.
- Verified via live webfetch: Blogger PRESERVES <style> blocks in post body (theme CSS served as page-skin-1 + page's own styles intact). So 188 tool pages with tool-specific <style> blocks are safe; relocation to theme not required.
- Stray category labels removed from 51 files earlier (Binary/Unit Converter).

### Premium 2026 tool-page design system (2026-08-24)
- Replaced the entire TOOL PAGES EXTENDED CSS block in Free Online Tools.xml (and synced .txt + .clean.xml) with a cohesive 2026 design system covering ALL .tool-* shared classes (breadcrumbs, hero, layout, cards, inputs, buttons, stats, privacy, features, howto, output).
- One CSS change applies to all 226 tool pages automatically (theme is the single source via <b:skin>).
- Features: refined tool hero with subtle radial glow + gradient border, glassy tool cards with hover-lift, brand-gradient primary buttons (generate/copy-all/action), tinted secondary buttons, sticky sidebar, polished inputs with focus ring, gradient feature-icon badges, pill breadcrumbs, full light+dark via [data-theme="dark"], responsive at 1024/768/480/360.
- Header / homepage left FROZEN (blue-gradient, approved) per section 8a — NOT changed.
- Live effect: re-upload Free Online Tools.xml via Blogger Theme > Edit HTML; all published tool pages inherit the new design immediately (no re-publish needed for CSS).
- Caveat: ~159 tool pages contain tool-specific INLINE style= attributes on internal elements (e.g. color-picker flex layout, copy buttons) that will partially retain their own styling. Full 100% uniformity would require a separate inline-style normalization sweep (optional, larger task).

## 30. ACTUAL CURRENT DISK STATE (2026-08-29 SCAN — SOURCE OF TRUTH)

This section records the REAL contents of `E:\free online tools corner\Free Online Tools` as scanned on 2026-08-29. Where it conflicts with earlier sections, THIS section wins (project rule: files on disk are the truth).

### Verified file inventory (root)
- `AGENTS.md` — this file (72,626 bytes).
- `Free Online Tools.xml` = `Free Online Tools.txt` = **280,525 bytes** (byte-identical, valid XML, 965 lines). NOTE: this is NOT the 301,771 baseline claimed in §25/§28 — that baseline is absent from disk.
- `MASTER PROMPT — COMPLETE FREE ONLINE TOOLS WEBSITE.txt` — 21,477 bytes. Master planning/prompt doc for the whole site. NOT previously listed in AGENTS.md; treat as project context, not a deployment file.
- `Pages/` — 5 content-only `.txt` files: About Us, Contact Us, Disclaimer, Privacy Policy, Terms of Service. Match §28 inventory.
- `Tool Pages/` — 225 `.txt` files in 11 category folders (Binary 23, Converter Tools 11, Generators 18, Image 29, Online Calculators 13, SEO Tools 11, Text Tools 16, Units 28, Web Development 27, Web Tools 22, YouTube Tools 27). Match §28 inventory exactly.
- `Image/` — `Categories/` (category webp + 2 large png), `Tools Cards/` (per-tool webp icons, plus duplicate kebab-case copies for many tools), and `images blogger.txt` (image inventory, 39,319 bytes). See duplicate-icon note below.

### Theme markers confirmed present in the 280,525-byte file
- 3 marked CSS sections present: `HOMEPAGE / SHARED BASE`, `TOOL PAGES EXTENDED` (2 hits), `STATIC PAGES (about / contact / faq / legal)`.
- `tool-crumbs-wrap`, `tpw-tool-grid`, `generate-btn` (premium/shared design classes) all present.
- `tpw-tool-category` present (4 hits) — dedupe applied.
- Blog1 widget still renders post title: `<data:post.title/>` at line ~809 inside an `<a expr:href=...>` (lines 804-809). The "duplicate `<h1>` removed at line 549" claim in §29 could NOT be confirmed from this file (no `<h1><data:post.title/></h1>` found at line 549) — verify before trusting §29's publish-fix status.

### Artifacts referenced in §27/§29 that are ABSENT from this working dir
- `Publish Checklist.txt` — MISSING (§27/§28 reference it as the slug map source).
- `slug_map.json` — MISSING.
- `publish_all.js`, `map_slugs.js`, `apply_slug_fix.js` — MISSING.
- `Free Online Tools.clean.xml` — MISSING.
- `build_blogger.ps1` — MISSING.
- Backups under `E:\free online tools corner\tools-website-blogger\` — NOT in this working dir (separate folder; unverified here).
- `%TEMP%\opencode\*` backups — transient; not guaranteed to exist.

Implication: the publishing/slug-fix pipeline described in §29 cannot be re-run from this folder as-is. If a clean re-publish is needed, those scripts must be recovered/recreated first.

### Duplicate tool-icon webp files (housekeeping note)
`Image/Tools Cards/` contains both Title-Case and kebab-case copies for many tools (e.g. `ASCII to Binary.webp` + `ascii-to-binary.webp`). These are byte-identical duplicates. Not harmful, but a cleanup candidate per §6 (codebase cleanliness). Decide canonical naming before any future icon rework.

### Live Blogger publishing status — UNKNOWN from this scan
- No `/p/*.html` link evidence inside the theme (only 3 `href='/p/` refs, which are static-page nav, not tool cards).
- Whether tool pages are live on Blogger (and at which slugs) could NOT be verified from disk alone. §29 implies ~100 were published at ugly auto-slugs, but the scripts/clean.xml needed to confirm or fix that are absent here. Treat live publishing state as unverified.

### Corrected rules for this session
- Restore-from-baseline commands in §25 ("reset to 301,771") are VOID — that file is not on disk. The real canonical theme is the 280,525-byte `Free Online Tools.xml`/`.txt`.
- Always re-scan the actual folder before acting; do not assume §28's size/artifact claims hold.

## 31. COMMUNICATION PREFERENCE (user directive 2026-08-29)

- **Reply to the user in Roman Urdu** (English words allowed where natural, e.g. tool/file names, code). This is a standing preference — apply it to all conversational replies unless the user switches language.
- Code, file paths, commands, and technical identifiers stay in their original form; only the explanatory prose should be Roman Urdu.
- Keep replies concise per the base system prompt (short, direct), even in Roman Urdu.
