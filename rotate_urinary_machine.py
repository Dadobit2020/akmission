#!/usr/bin/env python3
"""
Rotate the urinary machine image 180 degrees
"""

from PIL import Image
import os

# Path to the urinary machine image (IMG_4846 - the first image in the gallery)
image_dir = 'images/Clinic/optimized_images_20260119_153152_018348/IMG_4846/'

# Rotate all sizes of this image 180 degrees
for filename in os.listdir(image_dir):
    if filename.endswith('.jpeg'):
        filepath = os.path.join(image_dir, filename)
        
        # Open image
        img = Image.open(filepath)
        
        # Rotate 180 degrees
        rotated = img.rotate(180, expand=True)
        
        # Save back
        rotated.save(filepath, quality=95)
        print(f"✓ Rotated 180°: {filename}")

print("\n✅ Urinary machine image rotated 180 degrees successfully!")
