import os
import glob

target_content = '''                <div class="footer-links">
                    <ul>
                        <li><a href="#">Terms of Service</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">Cookie Policy</a></li>
                        <li><a href="#">FAQs</a></li>
                    </ul>
                </div>'''

replacement_content = '''                <div class="footer-links">
                    <ul>
                        <li><a href="terms-of-service.html">Terms of Service</a></li>
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="cookie-policy.html">Cookie Policy</a></li>
                        <li><a href="faqs.html">FAQs</a></li>
                    </ul>
                </div>'''

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_content in content:
        content = content.replace(target_content, replacement_content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filepath}')
    else:
        print(f'Target not found in {filepath}')
