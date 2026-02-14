#!/usr/bin/env python3
"""
Image Resizing and Optimization Script for Addis Kidan Mission
Processes images in folders and creates multiple optimized sizes
"""

import os
import sys
from pathlib import Path
from PIL import Image
from datetime import datetime

IMAGE_SIZES = {
    'thumbnail': 150,
    'small': 400,
    'medium': 800,
    'large': 1200,
    'xlarge': 1920
}

QUALITY = 85

def resize_and_optimize_image(input_path, output_dir, base_name):
    """Resize image to multiple sizes and optimize for web"""
    try:
        with Image.open(input_path) as img:
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            original_width, original_height = img.size
            print(f"  Original size: {original_width}x{original_height}")
            
            for size_name, max_dimension in IMAGE_SIZES.items():
                if original_width <= max_dimension and original_height <= max_dimension:
                    if size_name == 'thumbnail':
                        resized = img.copy()
                        resized.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
                    else:
                        print(f"  Skipping {size_name} (original is smaller)")
                        continue
                else:
                    resized = img.copy()
                    resized.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
                
                output_filename = f"{base_name}_{size_name}.jpeg"
                output_path = output_dir / output_filename
                
                resized.save(
                    output_path,
                    'JPEG',
                    quality=QUALITY,
                    optimize=True,
                    progressive=True
                )
                
                file_size = output_path.stat().st_size / 1024
                print(f"  ✓ Created {size_name}: {resized.size[0]}x{resized.size[1]} ({file_size:.1f}KB)")
            
            return True
            
    except Exception as e:
        print(f"  ✗ Error processing image: {e}")
        return False

def process_folder(input_folder, output_base='images'):
    """Process all images in a folder"""
    input_path = Path(input_folder)
    
    if not input_path.exists():
        print(f"Error: Folder '{input_folder}' does not exist")
        return
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp'}
    image_files = [f for f in input_path.iterdir() 
                   if f.is_file() and f.suffix.lower() in image_extensions]
    
    if not image_files:
        print(f"No images found in '{input_folder}'")
        return
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    folder_name = input_path.name
    output_base_path = Path(output_base) / folder_name / f"optimized_images_{timestamp}"
    
    print(f"\n{'='*60}")
    print(f"Processing folder: {input_folder}")
    print(f"Found {len(image_files)} images")
    print(f"Output directory: {output_base_path}")
    print(f"{'='*60}\n")
    
    processed = 0
    failed = 0
    
    for image_file in image_files:
        print(f"Processing: {image_file.name}")
        
        base_name = image_file.stem
        output_dir = output_base_path / base_name
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if resize_and_optimize_image(image_file, output_dir, base_name):
            processed += 1
        else:
            failed += 1
        
        print()
    
    print(f"{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Successfully processed: {processed}")
    if failed > 0:
        print(f"  ✗ Failed: {failed}")
    print(f"  Output location: {output_base_path}")
    print(f"{'='*60}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python resize_images.py <folder_path> [output_base]")
        print("\nExample:")
        print("  python resize_images.py /path/to/images")
        print("  python resize_images.py /path/to/images custom_output")
        print("\nThis will create multiple sizes:")
        for size_name, dimension in IMAGE_SIZES.items():
            print(f"  - {size_name}: max {dimension}px")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_base = sys.argv[2] if len(sys.argv) > 2 else 'images'
    
    process_folder(input_folder, output_base)

if __name__ == '__main__':
    main()
