import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if this is a package page
    if 'package-btn' not in content:
        continue

    # Update hover state for base package-btn
    def replace_base_hover(m):
        block = m.group(0)
        block = re.sub(r'background:\s*[^;]+;', r'background: #000000;', block)
        block = re.sub(r'color:\s*[^;]+;', r'color: #ffffff;', block)
        block = re.sub(r'border-color:\s*[^;]+;', r'border-color: #000000;', block)
        return block
        
    content = re.sub(r'\.package-btn:hover\s*\{[^}]*\}', replace_base_hover, content)
    
    # Actually, wait, let's just use string replacement or regex for the specific lines to avoid breaking anything else.
    # The current hover block is:
    # @media (hover: hover) {
    #             .package-btn:hover {
    #     background: var(--text-primary);
    #     color: var(--bg-color);
    #     border-color: var(--text-primary);
    # }
    
    # And the popular one is:
    # .package-card.popular @media (hover: hover) {
    #   .package-btn:hover {
    #         background: transparent;
    #         color: var(--text-primary);
    #         border-color: var(--border-color);
    #     }
    # }

    # Let's just fix both blocks!
    # Update base hover
    content = re.sub(r'(\.package-btn:hover\s*\{.*?background:\s*)[^;]+(;.*?color:\s*)[^;]+(;.*?border-color:\s*)[^;]+(;.*?\})', 
                     r'\g<1>#000000\g<2>#ffffff\g<3>#000000\g<4>', content, flags=re.DOTALL)
    
    # The regex above will match `.package-btn:hover { ... }` and replace the values.
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated {len(html_files)} files for hover state.")
