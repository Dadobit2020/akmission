# Recommended Folder Structure for Addis Kidan Mission Website

## Proposed Directory Organization

```
akmission/
├── index.html                 (Keep in root)
├── README.md
├── .gitignore
│
├── css/
│   └── styles.css            (Move from root)
│
├── js/
│   ├── script.js             (Move from root)
│   └── gallery.js            (Move from root)
│
├── pages/
│   ├── about.html            (Move from root)
│   ├── expeditions.html      (Move from root)
│   ├── medical.html          (Move from root)
│   ├── education.html        (Move from root)
│   ├── building.html         (Move from root)
│   ├── gallery.html          (Move from root)
│   └── support.html          (Move from root)
│
└── images/
    ├── expeditions/
    │   ├── expedition1/
    │   │   └── (Place Expedition 1 photos here)
    │   └── expedition2/
    │       └── (Place Expedition 2 photos here)
    │
    ├── medical/
    │   └── (Medical clinic and healthcare photos)
    │
    ├── education/
    │   └── (Classroom, teacher training photos)
    │
    ├── building/
    │   └── (Construction and renovation photos)
    │
    ├── community/
    │   └── (Community gatherings, worship photos)
    │
    ├── team/
    │   └── (Mission team photos)
    │
    └── logos/
        └── (Church and mission logos)
```

## Manual Steps to Organize

### 1. Create Folders
Create these folders in your akmission directory:
- `css`
- `js`
- `pages`
- `images` (with subfolders: expeditions/expedition1, expeditions/expedition2, medical, education, building, community, team, logos)

### 2. Move Files

**Move to css folder:**
- `styles.css` → `css/styles.css`

**Move to js folder:**
- `script.js` → `js/script.js`
- `gallery.js` → `js/gallery.js`

**Move to pages folder:**
- `about.html` → `pages/about.html`
- `expeditions.html` → `pages/expeditions.html`
- `medical.html` → `pages/medical.html`
- `education.html` → `pages/education.html`
- `building.html` → `pages/building.html`
- `gallery.html` → `pages/gallery.html`
- `support.html` → `pages/support.html`

**Keep in root:**
- `index.html` (main homepage)
- `README.md`
- `.gitignore`

### 3. Update File Paths

After moving files, you'll need to update these paths:

**In index.html (stays in root):**
- Change: `<link rel="stylesheet" href="styles.css">` 
- To: `<link rel="stylesheet" href="css/styles.css">`
- Change: `<script src="script.js"></script>`
- To: `<script src="js/script.js"></script>`
- Change all page links: `about.html` → `pages/about.html`, etc.

**In all pages/ HTML files:**
- Change: `href="styles.css"` → `href="../css/styles.css"`
- Change: `src="script.js"` → `src="../js/script.js"`
- Change: `src="gallery.js"` → `src="../js/gallery.js"`
- Change: `href="index.html"` → `href="../index.html"`
- Change: `href="about.html"` → `href="about.html"` (same folder)

## Benefits of This Structure

✅ **Organized by file type** - CSS, JS, HTML pages separated
✅ **Image organization** - Easy to find photos by category
✅ **Scalable** - Easy to add more content
✅ **Professional** - Standard web development structure
✅ **Maintainable** - Clear where everything belongs

## Quick Terminal Commands (Optional)

If you want to use terminal commands to move files:

```bash
# Create folders
mkdir -p css js pages images/{expeditions/{expedition1,expedition2},medical,education,building,community,team,logos}

# Move CSS
mv styles.css css/

# Move JS
mv script.js gallery.js js/

# Move HTML pages
mv about.html expeditions.html medical.html education.html building.html gallery.html support.html pages/
```

Then manually update the file paths as described above.
