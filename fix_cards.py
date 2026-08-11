import glob

html_files = glob.glob('c:/xampp/htdocs/nexyticdigi/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add .why-card to the reset block
    content = content.replace('.service-card,\n        .value-card {', '.service-card,\n        .why-card,\n        .value-card {')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed .why-card in all HTML files.")
