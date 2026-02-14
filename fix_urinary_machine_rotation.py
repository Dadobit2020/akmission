#!/usr/bin/env python3
"""
Fix the urinary machine image - rotate it 180 degrees back to the correct 90-degree orientation
"""

from PIL import Image
import os

# Path to the urinary machine image (IMG_4846)
image_dir = 'images/Clinic/optimized_images_20260119_153152_018348/IMG_4846/'

# Rotate all sizes of this image 180 degrees to get back to the 90-degree orientation
for filename in os.listdir(image_dir):
    if filename.endswith('.jpeg'):
        filepath = os.path.join(image_dir, filename)
        
        # Open image
        img = Image.open(filepath)
        
        # Rotate 180 degrees to undo the previous rotation
        rotated = img.rotate(180, expand=True)
        
        # Save back
        rotated.save(filepath, quality=95)
        print(f"✓ Fixed rotation: {filename}")

print("\n✅ Urinary machine image restored to correct 90-degree orientation!")
