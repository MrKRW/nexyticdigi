import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace:
    # .package-card.popular @media (hover: hover) {
    #       .package-btn:hover {
    #             background: #000000;
    #             color: #ffffff;
    #             border-color: #000000;
    #         }
    #  }
    # With:
    # @media (hover: hover) {
    #       .package-card.popular .package-btn:hover {
    #             background: #000000;
    #             color: #ffffff;
    #             border-color: #000000;
    #         }
    #  }
    
    # Let's use a regex that matches this exact malformed block
    pattern = r'\.package-card\.popular\s+@media\s+\(hover:\s*hover\)\s*\{\s*\.package-btn:hover\s*\{([^}]+)\}\s*\}'
    replacement = r'@media (hover: hover) {\n        .package-card.popular .package-btn:hover {\g<1>}\n    }'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print(f"Fixed syntax in HTML files.")
