# Path Updates for HTML Files in pages/ Folder

All HTML files in the `pages/` folder need these path updates:

## Changes Required for Each HTML File

### 1. CSS Path
**Change:** `href="styles.css"`
**To:** `href="../css/styles.css"`

### 2. JavaScript Paths
**Change:** `src="script.js"`
**To:** `src="../js/script.js"`

**Change:** `src="gallery.js"` (in gallery.html)
**To:** `src="../js/gallery.js"`

### 3. Navigation Links to Home
**Change:** `href="index.html"`
**To:** `href="../index.html"`

### 4. Navigation Links to Other Pages (stay in same folder)
**Keep as is:** `href="about.html"`, `href="medical.html"`, etc.
These files are in the same `pages/` folder, so relative paths don't change.

## Files That Need Updates

1. ✅ index.html (already updated - in root)
2. ⏳ pages/about.html
3. ⏳ pages/expeditions.html
4. ⏳ pages/medical.html
5. ⏳ pages/education.html
6. ⏳ pages/building.html
7. ⏳ pages/gallery.html
8. ⏳ pages/support.html

## Summary of Changes

- CSS: Add `../` prefix
- JS: Add `../` prefix  
- Home link: Add `../` prefix
- Other page links: No change (same folder)
