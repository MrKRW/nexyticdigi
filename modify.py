import os
import glob
import re

html_files = glob.glob('c:/xampp/htdocs/nexyticdigi/*.html')

injection = """
        /* Dark mode overrides for bg-card sections */
        .services-overview,
        .package-card,
        .process-card,
        .faq-item,
        .why-choose-us,
        .step-card,
        .contact-info,
        .values-section {
            --text-primary: #ffffff;
            --text-secondary: #e0e0e0;
        }

        .service-card,
        .value-card {
            --text-primary: #0a0a0a;
            --text-secondary: #444444;
        }
        
        .service-icon, .feature-icon, .value-icon {
            color: #ffffff !important;
        }
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update --bg-card
    content = re.sub(r'--bg-card:\s*#[a-fA-F0-9]{6};', '--bg-card: #2e2e2e;', content)
    
    # Check if injection already exists
    if 'Dark mode overrides for bg-card sections' not in content:
        # Inject after :root { ... }
        # Find the closing brace of :root
        root_end_match = re.search(r':root\s*\{[^}]*\}', content)
        if root_end_match:
            insert_pos = root_end_match.end()
            content = content[:insert_pos] + '\n' + injection + content[insert_pos:]
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files.")
