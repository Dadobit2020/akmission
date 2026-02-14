#!/usr/bin/env python3
"""
Fix the gallery page to show all gallery images organized by category
"""

from pathlib import Path

# Read the current gallery page
gallery_file = Path('pages/gallery_integrated.html')
content = gallery_file.read_text()

# Find the start and end markers
start_marker = '    </section>\n\n    <section class="quick_help_need" style="padding: 80px 0; background: #fff;">'
end_marker = '\n\n    <footer class="footer_area">'

# Find positions
start_pos = content.find(start_marker)
end_pos = content.find(end_marker)

if start_pos == -1 or end_pos == -1:
    print("Could not find markers in file")
    exit(1)

# Create the new gallery content
new_gallery = '''    </section>

    <section class="quick_help_need" style="padding: 80px 0; background: #fff;">
        <div class="container">
            <div style="text-align: center; max-width: 800px; margin: 0 auto 60px;">
                <h2>Our Story in Pictures</h2>
                <p class="lead" style="color: #D97706;">Every photo tells a story of transformation, hope, and God's love in action.</p>
                <p>Browse through our collection of images from our mission trips, medical clinics, education programs, building projects, and community outreach.</p>
            </div>

            <!-- Medical Gallery -->
            <div style="margin-bottom: 80px;">
                <h3 style="text-align: center; margin-bottom: 40px; color: #D97706;">🏥 Medical Ministry</h3>
                <div class="row">
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/medical/gallery_medical_01.jpg" alt="Medical 1" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/medical/gallery_medical_02.jpg" alt="Medical 2" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/medical/gallery_medical_03.jpg" alt="Medical 3" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/medical/gallery_medical_04.jpg" alt="Medical 4" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/medical/gallery_medical_05.jpg" alt="Medical 5" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/medical/gallery_medical_06.jpg" alt="Medical 6" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                </div>
            </div>

            <!-- Education Gallery -->
            <div style="margin-bottom: 80px;">
                <h3 style="text-align: center; margin-bottom: 40px; color: #D97706;">📚 Education Programs</h3>
                <div class="row">
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/education/gallery_education_01.jpg" alt="Education 1" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/education/gallery_education_02.jpg" alt="Education 2" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/education/gallery_education_03.jpg" alt="Education 3" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/education/gallery_education_04.jpg" alt="Education 4" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/education/gallery_education_05.jpg" alt="Education 5" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/education/gallery_education_06.jpg" alt="Education 6" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                </div>
            </div>

            <!-- Building Gallery -->
            <div style="margin-bottom: 80px;">
                <h3 style="text-align: center; margin-bottom: 40px; color: #D97706;">🏗️ Building Projects</h3>
                <div class="row">
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/building/gallery_building_01.jpg" alt="Building 1" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/building/gallery_building_02.jpg" alt="Building 2" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/building/gallery_building_03.jpg" alt="Building 3" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/building/gallery_building_04.jpg" alt="Building 4" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/building/gallery_building_05.jpg" alt="Building 5" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/building/gallery_building_06.jpg" alt="Building 6" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                </div>
            </div>

            <!-- Outreach Gallery -->
            <div style="margin-bottom: 80px;">
                <h3 style="text-align: center; margin-bottom: 40px; color: #D97706;">🤝 Community Outreach</h3>
                <div class="row">
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/outreach/gallery_outreach_01.jpg" alt="Outreach 1" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/outreach/gallery_outreach_02.jpg" alt="Outreach 2" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/outreach/gallery_outreach_03.jpg" alt="Outreach 3" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/outreach/gallery_outreach_04.jpg" alt="Outreach 4" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/outreach/gallery_outreach_05.jpg" alt="Outreach 5" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/outreach/gallery_outreach_06.jpg" alt="Outreach 6" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                </div>
            </div>

            <!-- Team Gallery -->
            <div style="margin-bottom: 80px;">
                <h3 style="text-align: center; margin-bottom: 40px; color: #D97706;">👥 Our Mission Team</h3>
                <div class="row">
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/team/gallery_team_01.jpg" alt="Team 1" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/team/gallery_team_02.jpg" alt="Team 2" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/team/gallery_team_03.jpg" alt="Team 3" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/team/gallery_team_04.jpg" alt="Team 4" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/team/gallery_team_05.jpg" alt="Team 5" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                    <div class="col-md-4 col-lg-2" style="margin-bottom: 20px;">
                        <img src="../images_by_page/gallery/team/gallery_team_06.jpg" alt="Team 6" class="img-fluid rounded" style="box-shadow: 0 3px 15px rgba(0,0,0,0.2);">
                    </div>
                </div>
            </div>

        </div>
    </section>'''

# Replace the content
new_content = content[:start_pos] + new_gallery + content[end_pos:]

# Write back
gallery_file.write_text(new_content)

print("✓ Gallery page updated successfully!")
print(f"  - Added 30 gallery images organized in 5 categories")
print(f"  - Medical: 6 images")
print(f"  - Education: 6 images")
print(f"  - Building: 6 images")
print(f"  - Outreach: 6 images")
print(f"  - Team: 6 images")
