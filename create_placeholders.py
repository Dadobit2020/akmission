#!/usr/bin/env python3
"""
Create placeholder images for Addis Kidan Mission website
Based on IMAGE_PLACEHOLDERS_GUIDE.md specifications
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Define all placeholders with their specifications
PLACEHOLDERS = {
    'homepage': [
        ('hero_slide_01_mission_team.jpg', 1920, 800, 'Hero Slide 1\nMission Team'),
        ('hero_slide_02_medical_care.jpg', 1920, 800, 'Hero Slide 2\nMedical Care'),
        ('hero_slide_03_education.jpg', 1920, 800, 'Hero Slide 3\nEducation'),
        ('card_medical_dept.jpg', 800, 600, 'Medical\nDepartment'),
        ('card_education_dept.jpg', 800, 600, 'Education\nDepartment'),
        ('card_building_dept.jpg', 800, 600, 'Building\nDepartment'),
        ('card_outreach_dept.jpg', 800, 600, 'Outreach\nDepartment'),
        ('card_spiritual_dept.jpg', 800, 600, 'Spiritual\nDepartment'),
        ('section_living_gospel.jpg', 1200, 900, 'Living the Gospel\nSection'),
        ('expedition_2023_card.jpg', 600, 450, 'Expedition 2023\nCard'),
        ('expedition_2024_card.jpg', 600, 450, 'Expedition 2024\nCard'),
        ('expedition_2025_card.jpg', 600, 450, 'Expedition 2025\nCard'),
    ],
    'about': [
        ('about_hero_banner.jpg', 1920, 500, 'About Page\nHero Banner'),
        ('about_vision_background.jpg', 1920, 600, 'Vision Section\nBackground'),
        ('about_sidebar_image.jpg', 400, 300, 'About Sidebar\nImage'),
    ],
    'medical': [
        ('medical_hero_banner.jpg', 1920, 500, 'Medical Page\nHero Banner'),
        ('medical_gallery_background.jpg', 1920, 600, 'Medical Gallery\nBackground'),
        ('medical_gallery_01.jpg', 800, 600, 'Medical\nGallery 1'),
        ('medical_gallery_02.jpg', 800, 600, 'Medical\nGallery 2'),
        ('medical_gallery_03.jpg', 800, 600, 'Medical\nGallery 3'),
        ('medical_support_image.jpg', 1200, 900, 'Medical Support\nImage'),
    ],
    'building': [
        ('building_hero_banner.jpg', 1920, 500, 'Building Page\nHero Banner'),
        ('building_school_main.jpg', 1200, 900, 'School Building\nMain Image'),
        ('building_school_gallery_01.jpg', 1000, 750, 'School\nGallery 1'),
        ('building_school_gallery_02.jpg', 1000, 750, 'School\nGallery 2'),
        ('building_school_gallery_03.jpg', 1000, 750, 'School\nGallery 3'),
        ('building_school_gallery_04.jpg', 1000, 750, 'School\nGallery 4'),
        ('building_more_views_background.jpg', 1920, 600, 'More Views\nBackground'),
        ('building_more_views_01.jpg', 800, 600, 'Building\nView 1'),
        ('building_more_views_02.jpg', 800, 600, 'Building\nView 2'),
        ('building_more_views_03.jpg', 800, 600, 'Building\nView 3'),
        ('building_support_image.jpg', 1200, 900, 'Building Support\nImage'),
    ],
    'education': [
        ('education_hero_banner.jpg', 1920, 500, 'Education Page\nHero Banner'),
        ('education_gallery_background.jpg', 1920, 600, 'Education Gallery\nBackground'),
        ('education_gallery_01.jpg', 800, 600, 'Education\nGallery 1'),
        ('education_gallery_02.jpg', 800, 600, 'Education\nGallery 2'),
        ('education_gallery_03.jpg', 800, 600, 'Education\nGallery 3'),
        ('education_support_image.jpg', 1200, 900, 'Education Support\nImage'),
    ],
    'expeditions': [
        ('expeditions_hero_banner.jpg', 1920, 500, 'Expeditions Page\nHero Banner'),
        ('expedition_2023_hero.jpg', 1200, 900, 'Expedition 2023\nHero Image'),
        ('expedition_2023_gallery_01.jpg', 600, 450, 'Expedition 2023\nGallery 1'),
        ('expedition_2023_gallery_02.jpg', 600, 450, 'Expedition 2023\nGallery 2'),
        ('expedition_2023_gallery_03.jpg', 600, 450, 'Expedition 2023\nGallery 3'),
        ('expedition_2024_hero.jpg', 1200, 900, 'Expedition 2024\nHero Image'),
        ('expedition_2024_gallery_01.jpg', 600, 450, 'Expedition 2024\nGallery 1'),
        ('expedition_2024_gallery_02.jpg', 600, 450, 'Expedition 2024\nGallery 2'),
        ('expedition_2024_gallery_03.jpg', 600, 450, 'Expedition 2024\nGallery 3'),
        ('expedition_2025_hero.jpg', 1200, 900, 'Expedition 2025\nHero Image'),
        ('expedition_2025_gallery_01.jpg', 600, 450, 'Expedition 2025\nGallery 1'),
        ('expedition_2025_gallery_02.jpg', 600, 450, 'Expedition 2025\nGallery 2'),
        ('expedition_2025_gallery_03.jpg', 600, 450, 'Expedition 2025\nGallery 3'),
    ],
    'gallery': [
        ('gallery_hero_banner.jpg', 1920, 500, 'Gallery Page\nHero Banner'),
    ],
    'gallery/medical': [
        ('gallery_medical_01.jpg', 600, 450, 'Medical\nGallery 1'),
        ('gallery_medical_02.jpg', 600, 450, 'Medical\nGallery 2'),
        ('gallery_medical_03.jpg', 600, 450, 'Medical\nGallery 3'),
        ('gallery_medical_04.jpg', 600, 450, 'Medical\nGallery 4'),
        ('gallery_medical_05.jpg', 600, 450, 'Medical\nGallery 5'),
        ('gallery_medical_06.jpg', 600, 450, 'Medical\nGallery 6'),
    ],
    'gallery/education': [
        ('gallery_education_01.jpg', 600, 450, 'Education\nGallery 1'),
        ('gallery_education_02.jpg', 600, 450, 'Education\nGallery 2'),
        ('gallery_education_03.jpg', 600, 450, 'Education\nGallery 3'),
        ('gallery_education_04.jpg', 600, 450, 'Education\nGallery 4'),
        ('gallery_education_05.jpg', 600, 450, 'Education\nGallery 5'),
        ('gallery_education_06.jpg', 600, 450, 'Education\nGallery 6'),
    ],
    'gallery/building': [
        ('gallery_building_01.jpg', 600, 450, 'Building\nGallery 1'),
        ('gallery_building_02.jpg', 600, 450, 'Building\nGallery 2'),
        ('gallery_building_03.jpg', 600, 450, 'Building\nGallery 3'),
        ('gallery_building_04.jpg', 600, 450, 'Building\nGallery 4'),
        ('gallery_building_05.jpg', 600, 450, 'Building\nGallery 5'),
        ('gallery_building_06.jpg', 600, 450, 'Building\nGallery 6'),
    ],
    'gallery/outreach': [
        ('gallery_outreach_01.jpg', 600, 450, 'Outreach\nGallery 1'),
        ('gallery_outreach_02.jpg', 600, 450, 'Outreach\nGallery 2'),
        ('gallery_outreach_03.jpg', 600, 450, 'Outreach\nGallery 3'),
        ('gallery_outreach_04.jpg', 600, 450, 'Outreach\nGallery 4'),
        ('gallery_outreach_05.jpg', 600, 450, 'Outreach\nGallery 5'),
        ('gallery_outreach_06.jpg', 600, 450, 'Outreach\nGallery 6'),
    ],
    'gallery/team': [
        ('gallery_team_01.jpg', 600, 450, 'Team\nGallery 1'),
        ('gallery_team_02.jpg', 600, 450, 'Team\nGallery 2'),
        ('gallery_team_03.jpg', 600, 450, 'Team\nGallery 3'),
        ('gallery_team_04.jpg', 600, 450, 'Team\nGallery 4'),
        ('gallery_team_05.jpg', 600, 450, 'Team\nGallery 5'),
        ('gallery_team_06.jpg', 600, 450, 'Team\nGallery 6'),
    ],
    'support': [
        ('support_hero_banner.jpg', 1920, 500, 'Support Page\nHero Banner'),
        ('support_impact_background.jpg', 1920, 600, 'Impact Section\nBackground'),
        ('support_give_financial.jpg', 400, 300, 'Financial\nGiving'),
        ('support_give_volunteer.jpg', 400, 300, 'Volunteer\nSupport'),
        ('support_give_prayer.jpg', 400, 300, 'Prayer\nSupport'),
        ('support_give_supplies.jpg', 400, 300, 'Supplies\nDonation'),
    ],
}

def create_placeholder(width, height, text, output_path):
    """Create a placeholder image with text overlay"""
    # Create image with orange/brown gradient
    img = Image.new('RGB', (width, height), color='#8B4513')
    draw = ImageDraw.Draw(img)
    
    # Add gradient effect (darker at top)
    for y in range(height):
        darkness = int(139 * (1 - y / height * 0.3))
        color = (darkness, int(darkness * 0.3), int(darkness * 0.15))
        draw.line([(0, y), (width, y)], fill=color)
    
    # Add border
    border_width = 3
    draw.rectangle(
        [(border_width, border_width), (width - border_width, height - border_width)],
        outline='#FF8C00',
        width=border_width
    )
    
    # Add text
    try:
        font_size = min(width, height) // 10
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', font_size)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center text
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text with shadow
    shadow_offset = 2
    draw.text((x + shadow_offset, y + shadow_offset), text, fill='#000000', font=font, align='center')
    draw.text((x, y), text, fill='#FFFFFF', font=font, align='center')
    
    # Add dimension text at bottom
    dim_text = f'{width}x{height}px'
    try:
        dim_font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
    except:
        dim_font = ImageFont.load_default()
    
    dim_bbox = draw.textbbox((0, 0), dim_text, font=dim_font)
    dim_width = dim_bbox[2] - dim_bbox[0]
    dim_x = (width - dim_width) // 2
    dim_y = height - 40
    
    draw.text((dim_x + 1, dim_y + 1), dim_text, fill='#000000', font=dim_font)
    draw.text((dim_x, dim_y), dim_text, fill='#FFFFFF', font=dim_font)
    
    # Save image
    img.save(output_path, 'JPEG', quality=85, optimize=True)
    return output_path

def main():
    base_dir = Path('images_by_page')
    
    print(f"\n{'='*60}")
    print("Creating Placeholder Images for Addis Kidan Mission Website")
    print(f"{'='*60}\n")
    
    total_images = 0
    
    for folder, images in PLACEHOLDERS.items():
        folder_path = base_dir / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Creating folder: {folder_path}")
        
        for filename, width, height, text in images:
            output_path = folder_path / filename
            create_placeholder(width, height, text, output_path)
            file_size = output_path.stat().st_size / 1024
            print(f"  ✓ Created: {filename} ({width}x{height}px, {file_size:.1f}KB)")
            total_images += 1
        
        print()
    
    print(f"{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Total folders created: {len(PLACEHOLDERS)}")
    print(f"  ✓ Total placeholder images: {total_images}")
    print(f"  📁 Location: {base_dir.absolute()}")
    print(f"{'='*60}\n")
    
    print("✅ All placeholder images created successfully!")
    print("\nNext steps:")
    print("1. Replace placeholders with your actual images")
    print("2. Keep the same filenames for easy integration")
    print("3. Maintain the recommended dimensions")
    print("4. Update HTML files with new image paths\n")

if __name__ == '__main__':
    main()
