#!/usr/bin/env python3
"""
Update phone number across all HTML files
"""

from pathlib import Path

# Old and new phone numbers
old_phone = "+1 (555) 123-4567"
new_phone = "(720) 857-9402"

# Find all HTML files
html_files = list(Path('.').rglob('*.html'))

updated_files = []

for html_file in html_files:
    try:
        content = html_file.read_text(encoding='utf-8')
        
        if old_phone in content:
            new_content = content.replace(old_phone, new_phone)
            html_file.write_text(new_content, encoding='utf-8')
            updated_files.append(str(html_file))
            print(f"✓ Updated: {html_file}")
    except Exception as e:
        print(f"⚠️  Error processing {html_file}: {e}")

print(f"\n{'='*60}")
print(f"Phone Number Update Complete")
print(f"{'='*60}")
print(f"Updated {len(updated_files)} files")
print(f"Old: {old_phone}")
print(f"New: {new_phone}")
