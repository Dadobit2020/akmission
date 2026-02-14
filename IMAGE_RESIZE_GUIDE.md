# Image Resizing Guide

## Quick Start

### 1. Install Required Package
```bash
pip install Pillow
```

### 2. Put Your Images in a Folder
Create a folder with your images, for example:
```
/Users/admin/Desktop/new_photos/
  - photo1.jpg
  - photo2.jpg
  - photo3.png
```

### 3. Run the Resize Script
```bash
python resize_images.py /Users/admin/Desktop/new_photos
```

## What It Does

The script will automatically:
- ✅ Resize each image to 5 different sizes:
  - **thumbnail**: 150px (for previews)
  - **small**: 400px (for mobile)
  - **medium**: 800px (for tablets)
  - **large**: 1200px (for desktop)
  - **xlarge**: 1920px (for full screen)
- ✅ Optimize images for web (85% quality, progressive JPEG)
- ✅ Maintain aspect ratios
- ✅ Convert all to JPEG format
- ✅ Organize into timestamped folders

## Output Structure

```
images/
  └── new_photos/
      └── optimized_images_20260214_091234_567890/
          ├── photo1/
          │   ├── photo1_thumbnail.jpeg
          │   ├── photo1_small.jpeg
          │   ├── photo1_medium.jpeg
          │   ├── photo1_large.jpeg
          │   └── photo1_xlarge.jpeg
          ├── photo2/
          │   ├── photo2_thumbnail.jpeg
          │   └── ...
          └── photo3/
              └── ...
```

## Advanced Usage

### Custom Output Location
```bash
python resize_images.py /path/to/images custom_output_folder
```

### Process Multiple Folders
```bash
python resize_images.py /path/to/medical_photos
python resize_images.py /path/to/school_photos
python resize_images.py /path/to/building_photos
```

## Supported Formats

**Input:** JPG, JPEG, PNG, WEBP, GIF, BMP
**Output:** JPEG (optimized for web)

## Tips

1. **Original images stay untouched** - the script only creates new resized versions
2. **Larger originals = better quality** - start with high-resolution images
3. **Batch processing** - put all related images in one folder
4. **Automatic organization** - each run creates a timestamped folder

## Example Workflow

1. Take photos on your phone/camera
2. Transfer to a folder on your computer
3. Run the resize script on that folder
4. Copy the optimized images to your website's images directory
5. Update your HTML to reference the new images

## Troubleshooting

**"No module named 'PIL'"**
```bash
pip install Pillow
```

**"Folder does not exist"**
- Check the folder path is correct
- Use absolute paths: `/Users/admin/Desktop/photos`

**Images look blurry**
- Start with higher resolution originals
- Adjust QUALITY setting in resize_images.py (line 16)

## Need Help?

The script shows detailed progress for each image:
- Original dimensions
- Each size created
- File sizes
- Success/failure status
