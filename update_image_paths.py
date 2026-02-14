#!/usr/bin/env python3
"""
Update HTML files to use new image paths from images_by_page folder
Excludes homepage as requested by user
"""

import re
from pathlib import Path

# Define image path mappings for each page
IMAGE_MAPPINGS = {
    'pages/about_integrated.html': {
        'hero_banner': '../images_by_page/about/about_hero_banner.jpg',
        'vision_background': '../images_by_page/about/about_vision_background.jpg',
        'sidebar_image': '../images_by_page/about/about_sidebar_image.jpg',
    },
    'pages/medical_integrated.html': {
        'hero_banner': '../images_by_page/medical/medical_hero_banner.jpg',
        'gallery_background': '../images_by_page/medical/medical_gallery_background.jpg',
        'gallery_01': '../images_by_page/medical/medical_gallery_01.jpg',
        'gallery_02': '../images_by_page/medical/medical_gallery_02.jpg',
        'gallery_03': '../images_by_page/medical/medical_gallery_03.jpg',
        'support_image': '../images_by_page/medical/medical_support_image.jpg',
    },
    'pages/building_integrated.html': {
        'hero_banner': '../images_by_page/building/building_hero_banner.jpg',
        'school_main': '../images_by_page/building/building_school_main.jpg',
        'school_gallery_01': '../images_by_page/building/building_school_gallery_01.jpg',
        'school_gallery_02': '../images_by_page/building/building_school_gallery_02.jpg',
        'school_gallery_03': '../images_by_page/building/building_school_gallery_03.jpg',
        'school_gallery_04': '../images_by_page/building/building_school_gallery_04.jpg',
        'more_views_background': '../images_by_page/building/building_more_views_background.jpg',
        'more_views_01': '../images_by_page/building/building_more_views_01.jpg',
        'more_views_02': '../images_by_page/building/building_more_views_02.jpg',
        'more_views_03': '../images_by_page/building/building_more_views_03.jpg',
        'support_image': '../images_by_page/building/building_support_image.jpg',
    },
    'pages/education_integrated.html': {
        'hero_banner': '../images_by_page/education/education_hero_banner.jpg',
        'gallery_background': '../images_by_page/education/education_gallery_background.jpg',
        'gallery_01': '../images_by_page/education/education_gallery_01.jpg',
        'gallery_02': '../images_by_page/education/education_gallery_02.jpg',
        'gallery_03': '../images_by_page/education/education_gallery_03.jpg',
        'support_image': '../images_by_page/education/education_support_image.jpg',
    },
    'pages/mission_trips_integrated.html': {
        'hero_banner': '../images_by_page/expeditions/expeditions_hero_banner.jpg',
        '2023_hero': '../images_by_page/expeditions/expedition_2023_hero.jpg',
        '2023_gallery_01': '../images_by_page/expeditions/expedition_2023_gallery_01.jpg',
        '2023_gallery_02': '../images_by_page/expeditions/expedition_2023_gallery_02.jpg',
        '2023_gallery_03': '../images_by_page/expeditions/expedition_2023_gallery_03.jpg',
        '2024_hero': '../images_by_page/expeditions/expedition_2024_hero.jpg',
        '2024_gallery_01': '../images_by_page/expeditions/expedition_2024_gallery_01.jpg',
        '2024_gallery_02': '../images_by_page/expeditions/expedition_2024_gallery_02.jpg',
        '2024_gallery_03': '../images_by_page/expeditions/expedition_2024_gallery_03.jpg',
        '2025_hero': '../images_by_page/expeditions/expedition_2025_hero.jpg',
        '2025_gallery_01': '../images_by_page/expeditions/expedition_2025_gallery_01.jpg',
        '2025_gallery_02': '../images_by_page/expeditions/expedition_2025_gallery_02.jpg',
        '2025_gallery_03': '../images_by_page/expeditions/expedition_2025_gallery_03.jpg',
    },
    'pages/gallery_integrated.html': {
        'hero_banner': '../images_by_page/gallery/gallery_hero_banner.jpg',
        'medical_01': '../images_by_page/gallery/medical/gallery_medical_01.jpg',
        'medical_02': '../images_by_page/gallery/medical/gallery_medical_02.jpg',
        'medical_03': '../images_by_page/gallery/medical/gallery_medical_03.jpg',
        'medical_04': '../images_by_page/gallery/medical/gallery_medical_04.jpg',
        'medical_05': '../images_by_page/gallery/medical/gallery_medical_05.jpg',
        'medical_06': '../images_by_page/gallery/medical/gallery_medical_06.jpg',
        'education_01': '../images_by_page/gallery/education/gallery_education_01.jpg',
        'education_02': '../images_by_page/gallery/education/gallery_education_02.jpg',
        'education_03': '../images_by_page/gallery/education/gallery_education_03.jpg',
        'education_04': '../images_by_page/gallery/education/gallery_education_04.jpg',
        'education_05': '../images_by_page/gallery/education/gallery_education_05.jpg',
        'education_06': '../images_by_page/gallery/education/gallery_education_06.jpg',
        'building_01': '../images_by_page/gallery/building/gallery_building_01.jpg',
        'building_02': '../images_by_page/gallery/building/gallery_building_02.jpg',
        'building_03': '../images_by_page/gallery/building/gallery_building_03.jpg',
        'building_04': '../images_by_page/gallery/building/gallery_building_04.jpg',
        'building_05': '../images_by_page/gallery/building/gallery_building_05.jpg',
        'building_06': '../images_by_page/gallery/building/gallery_building_06.jpg',
        'outreach_01': '../images_by_page/gallery/outreach/gallery_outreach_01.jpg',
        'outreach_02': '../images_by_page/gallery/outreach/gallery_outreach_02.jpg',
        'outreach_03': '../images_by_page/gallery/outreach/gallery_outreach_03.jpg',
        'outreach_04': '../images_by_page/gallery/outreach/gallery_outreach_04.jpg',
        'outreach_05': '../images_by_page/gallery/outreach/gallery_outreach_05.jpg',
        'outreach_06': '../images_by_page/gallery/outreach/gallery_outreach_06.jpg',
        'team_01': '../images_by_page/gallery/team/gallery_team_01.jpg',
        'team_02': '../images_by_page/gallery/team/gallery_team_02.jpg',
        'team_03': '../images_by_page/gallery/team/gallery_team_03.jpg',
        'team_04': '../images_by_page/gallery/team/gallery_team_04.jpg',
        'team_05': '../images_by_page/gallery/team/gallery_team_05.jpg',
        'team_06': '../images_by_page/gallery/team/gallery_team_06.jpg',
    },
    'pages/support_integrated.html': {
        'hero_banner': '../images_by_page/support/support_hero_banner.jpg',
        'impact_background': '../images_by_page/support/support_impact_background.jpg',
        'give_financial': '../images_by_page/support/support_give_financial.jpg',
        'give_volunteer': '../images_by_page/support/support_give_volunteer.jpg',
        'give_prayer': '../images_by_page/support/support_give_prayer.jpg',
        'give_supplies': '../images_by_page/support/support_give_supplies.jpg',
    },
}

def update_html_file(file_path):
    """Update a single HTML file with new image paths"""
    path = Path(file_path)
    
    if not path.exists():
        print(f"⚠️  File not found: {file_path}")
        return False
    
    print(f"\n📄 Processing: {file_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    updates_made = 0
    
    # Find all image references in the file
    # Pattern matches: src="..." or url('...') or url("...")
    image_patterns = [
        (r'src=["\']([^"\']*images/[^"\']*)["\']', 'src'),
        (r'url\(["\']?([^"\'()]*images/[^"\'()]*)["\']?\)', 'url'),
    ]
    
    # Extract all current image paths
    current_images = set()
    for pattern, _ in image_patterns:
        matches = re.findall(pattern, content)
        current_images.update(matches)
    
    print(f"  Found {len(current_images)} image references")
    
    # For now, just report what was found
    # Manual mapping will be needed based on context
    for img_path in sorted(current_images):
        if 'logo' not in img_path.lower():  # Skip logo
            print(f"    - {img_path}")
    
    return True

def main():
    print(f"\n{'='*60}")
    print("Updating Image Paths in HTML Files")
    print("(Excluding homepage as requested)")
    print(f"{'='*60}\n")
    
    files_to_update = [
        'pages/about_integrated.html',
        'pages/medical_integrated.html',
        'pages/building_integrated.html',
        'pages/education_integrated.html',
        'pages/mission_trips_integrated.html',
        'pages/gallery_integrated.html',
        'pages/support_integrated.html',
    ]
    
    for file_path in files_to_update:
        update_html_file(file_path)
    
    print(f"\n{'='*60}")
    print("Analysis Complete")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
