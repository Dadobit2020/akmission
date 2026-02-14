#!/usr/bin/env python3
"""
Rotate the clinic image that appears sideways
"""

from PIL import Image
import os

# Path to the image that needs rotation
image_dir = 'images/Clinic/optimized_images_20260119_153152_018348/IMG_4846/'

# Rotate all sizes of this image 90 degrees clockwise (or -90 for counter-clockwise)
for filename in os.listdir(image_dir):
    if filename.endswith('.jpeg'):
        filepath = os.path.join(image_dir, filename)
        
        # Open image
        img = Image.open(filepath)
        
        # Rotate 90 degrees counter-clockwise (to fix the sideways orientation)
        rotated = img.rotate(90, expand=True)
        
        # Save back
        rotated.save(filepath, quality=95)
        print(f"✓ Rotated: {filename}")

print("\n✅ All image sizes rotated successfully!")
