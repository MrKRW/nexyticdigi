import glob
import re

html_files = glob.glob('c:/xampp/htdocs/nexyticdigi/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the color
    content = re.sub(r'--bg-card:\s*#2e2e2e;', '--bg-card: #212121;', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated background color to #212121 in all HTML files.")
