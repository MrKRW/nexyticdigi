import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if this is a package page (i.e. has package-btn)
    if 'package-btn' not in content:
        continue

    # Update button text to ENQUIRE NOW
    content = re.sub(r'(<button class="package-btn"[^>]*>)[^<]*(</button>)', r'\1ENQUIRE NOW\2', content, flags=re.IGNORECASE)
    
    # Update base package-btn CSS (make background white, text black)
    # The original was:
    # background: transparent;
    # color: var(--text-primary);
    content = re.sub(r'(\.package-btn\s*\{[^}]*)background:\s*transparent;', r'\1background: #ffffff;', content)
    # Note: color might not match exactly if we do two passes, so let's use a simpler regex that just updates the color if it's the package-btn class.
    # Using a callback is safer.
    
    def replace_base_btn(m):
        block = m.group(0)
        block = re.sub(r'background:\s*[^;]+;', r'background: #ffffff;', block)
        block = re.sub(r'color:\s*[^;]+;', r'color: #000000;', block)
        return block
        
    content = re.sub(r'\.package-btn\s*\{[^}]*\}', replace_base_btn, content)
    
    # Update popular package-btn CSS (make background white, text black)
    def replace_popular_btn(m):
        block = m.group(0)
        block = re.sub(r'background:\s*[^;]+;', r'background: #ffffff;', block)
        block = re.sub(r'color:\s*[^;]+;', r'color: #000000;', block)
        return block

    content = re.sub(r'\.package-card\.popular \.package-btn\s*\{[^}]*\}', replace_popular_btn, content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated {len(html_files)} files.")
