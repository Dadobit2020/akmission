#!/usr/bin/env python3
"""
Batch update all remaining HTML pages with new image paths
"""

import re
from pathlib import Path

def update_file(file_path, replacements):
    """Update a file with multiple replacements"""
    path = Path(file_path)
    
    if not path.exists():
        print(f"⚠️  File not found: {file_path}")
        return False
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    if content != original_content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated: {file_path}")
        return True
    else:
        print(f"⚠️  No changes made to: {file_path}")
        return False

# Mission Trips (Expeditions) page
mission_trips_replacements = [
    ("url('../images/AKEC%20Mission%20team%202025%20Mission%20Trip/optimized_images_20260119_152615_164114/Our_Medical_Team/Our_Medical_Team_large.jpeg')", 
     "url('../images_by_page/expeditions/expeditions_hero_banner.jpg')"),
    ("src=\"../images/AKEC%20Mission%20team%202025%20Mission%20Trip/optimized_images_20260119_152615_164114/Our_Medical_Team/Our_Medical_Team_medium.jpeg\"",
     "src=\"../images_by_page/expeditions/expedition_2023_hero.jpg\""),
    ("src=\"../images/AKEC%20Mission%20team%202025%20Mission%20Trip/optimized_images_20260119_152615_164114/IMG_4207_2/IMG_4207_2_medium.jpeg\"",
     "src=\"../images_by_page/expeditions/expedition_2024_hero.jpg\""),
    ("src=\"../images/AKEC%20Mission%20team%202025%20Mission%20Trip/optimized_images_20260119_152615_164114/IMG_4207_2/IMG_4207_2_large.jpeg\"",
     "src=\"../images_by_page/expeditions/expedition_2025_hero.jpg\""),
]

# Gallery page - simplified, will need manual review
gallery_replacements = [
    ("url('../images/AKEC%20Mission%20team%202025%20Mission%20Trip/optimized_images_20260119_152615_164114/azeb/azeb_large.jpeg')",
     "url('../images_by_page/gallery/gallery_hero_banner.jpg')"),
]

# Support page
support_replacements = [
    ("url('../images/Clinic/optimized_images_20260119_153152_018348/IMG_4368/IMG_4368_large.jpeg')",
     "url('../images_by_page/support/support_hero_banner.jpg')"),
    ("url('../images/Clinic/optimized_images_20260119_153152_018348/IMG_4847/IMG_4847_large.jpeg')",
     "url('../images_by_page/support/support_impact_background.jpg')"),
]

print("\n" + "="*60)
print("Batch Updating Remaining HTML Pages")
print("="*60 + "\n")

update_file('pages/mission_trips_integrated.html', mission_trips_replacements)
update_file('pages/gallery_integrated.html', gallery_replacements)
update_file('pages/support_integrated.html', support_replacements)

print("\n" + "="*60)
print("Batch Update Complete")
print("="*60 + "\n")
