import re
import os

with open('services_original.html', 'r', encoding='utf-16') as f:
    content = f.read()

# 1. Extract sections
packages_match = re.search(r'(<section class="packages-section" id="packages">.*?</section>)', content, re.DOTALL)
estimator_match = re.search(r'(<!-- Cost Estimator Section -->\s*<section class="estimator-section".*?</section>)', content, re.DOTALL)
script_match = re.search(r'(<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?calculateTotal\(\);\s*}\);\s*</script>)', content, re.DOTALL)

packages_str = packages_match.group(1) if packages_match else ''
estimator_str = estimator_match.group(1) if estimator_match else ''
script_str = script_match.group(1) if script_match else ''

# 2. Extract header and footer
header_match = re.search(r'(.*?<header class="hero-header">.*?</header>)', content, re.DOTALL)
header_str = header_match.group(1) if header_match else ''
header_str = header_str.replace('OUR Services', 'OUR Packages').replace('Comprehensive digital solutions.', 'Transparent pricing for all your needs.')

footer_match = re.search(r'(<section class="faq-section">.*</html>)', content, re.DOTALL)
footer_str = footer_match.group(1) if footer_match else ''
if script_str: footer_str = footer_str.replace(script_str, '')

service_ids = [
    'web-development',
    'software-solutions',
    'ui-ux-design',
    'hosting-security',
    'seo-optimization',
    'e-commerce'
]

for s_id in service_ids:
    s_name = s_id.replace('-', ' ').title()
    if s_name == 'Ui Ux Design': s_name = 'UI/UX Design'
    if s_name == 'Seo Optimization': s_name = 'SEO Optimization'
    
    page_html = header_str + '\n\n'
    
    # We add a wrapper <div id="..."> so the anchor links jump here, or we can just use the section id.
    page_html += f'<div id="{s_id}">\n'
    page_html += f'<h2 class="services-title font-display" style="text-align: center; margin-top: 4rem;">{s_name} Packages</h2>\n'
    
    # modify packages_str to ensure IDs are unique if we want, but since it's a separate page, id="packages" is fine!
    page_html += packages_str + '\n'
    
    if s_id == 'web-development':
        page_html += estimator_str + '\n'
        
    page_html += '</div>\n\n'
    
    page_html += footer_str
    if s_id == 'web-development' and script_str:
        # the estimator script is only needed on the web-development page
        page_html = page_html.replace('</body>', script_str + '\n</body>')

    with open(f'{s_id}.html', 'w', encoding='utf-8') as f:
        f.write(page_html)

print("Fixed packages pages.")
