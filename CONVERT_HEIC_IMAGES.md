# Converting HEIC Images to JPG/PNG for Web Use

## Why Convert HEIC Files?

**HEIC (High Efficiency Image Container)** is Apple's image format, but it's **NOT supported by most web browsers**:
- ❌ Chrome, Firefox, Safari (on Windows), Edge don't support HEIC
- ✅ Only Safari on macOS/iOS supports HEIC natively
- ⚠️ Your website visitors won't be able to see HEIC images

**You MUST convert HEIC to JPG or PNG for web use.**

## Quick Conversion Methods

### Method 1: Using Mac Preview (Built-in, Free)
1. Open the HEIC file in **Preview** app
2. Go to **File → Export**
3. Choose format: **JPEG** or **PNG**
4. Set quality (80-90% for JPEG is good)
5. Click **Save**

### Method 2: Batch Convert with Mac Automator (Free)
1. Open **Automator** app
2. Create new **Quick Action**
3. Add action: **Change Type of Images**
4. Set to: **JPEG** (or PNG)
5. Save as "Convert to JPEG"
6. Right-click HEIC files → Quick Actions → Convert to JPEG

### Method 3: Using Terminal (Batch Convert All)
```bash
# Install ImageMagick (if not installed)
brew install imagemagick

# Convert all HEIC files to JPG in current directory
for file in *.HEIC; do
    magick "$file" "${file%.HEIC}.jpg"
done

# Or convert entire folder recursively
find /Users/admin/akmission/images -name "*.HEIC" -exec sh -c 'magick "$0" "${0%.HEIC}.jpg"' {} \;
```

### Method 4: Online Converters (No Installation)
- https://heictojpg.com/
- https://convertio.co/heic-jpg/
- Upload HEIC files, download JPG

## Recommended Settings for Web Images

**For Photos (JPG):**
- Quality: 80-85%
- Max width: 1920px (for full-screen)
- Max width: 800px (for thumbnails)

**For Graphics/Screenshots (PNG):**
- Use PNG for images with text or transparency
- Compress with tools like TinyPNG

## Your Current HEIC Files

You have HEIC files in these folders:
- `images/expeditions/expedition2/team/` - 22 HEIC files
- `images/medical/clinic/` - 8 HEIC files

**Total: ~30 HEIC files need conversion**

## Recommended Action

1. **Convert all HEIC to JPG** using one of the methods above
2. **Delete original HEIC files** after conversion
3. **Optimize JPG files** to reduce file size (use ImageOptim or TinyJPG)
4. **Update HTML** to reference the new JPG files

## Quick Terminal Command for Your Project

```bash
# Navigate to images folder
cd /Users/admin/akmission/images

# Convert all HEIC to JPG (requires ImageMagick)
find . -name "*.HEIC" -exec sh -c 'magick "$0" "${0%.HEIC}.jpg" && rm "$0"' {} \;

# This will:
# 1. Find all HEIC files
# 2. Convert each to JPG
# 3. Delete the original HEIC file
```

**Note:** Test on a few files first before batch converting!
