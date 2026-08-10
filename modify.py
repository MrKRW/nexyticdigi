import re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract packages section, estimator section, and script
packages_match = re.search(r'(<section class="packages-section" id="packages">.*?</section>)', content, re.DOTALL)
estimator_match = re.search(r'(<!-- Cost Estimator Section -->\s*<section class="estimator-section".*?</section>)', content, re.DOTALL)
script_match = re.search(r'(<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?calculateTotal\(\);\s*}\);\s*</script>)', content, re.DOTALL)

packages_str = packages_match.group(1) if packages_match else ''
estimator_str = estimator_match.group(1) if estimator_match else ''
script_str = script_match.group(1) if script_match else ''

# 2. Modify services.html to remove these sections and script
new_services = content
if packages_str: new_services = new_services.replace(packages_str, '')
if estimator_str: new_services = new_services.replace(estimator_str, '')
if script_str: new_services = new_services.replace(script_str, '')

service_ids = [
    'web-development',
    'software-solutions',
    'ui-ux-design',
    'hosting-security',
    'seo-optimization',
    'e-commerce'
]

def wrap_card(match):
    idx = getattr(wrap_card, 'counter', 0)
    wrap_card.counter = idx + 1
    if idx < len(service_ids):
        return f'<a href="packages.html#{service_ids[idx]}" style="text-decoration: none; color: inherit; display: block;">\n{match.group(0)}\n</a>'
    return match.group(0)

wrap_card.counter = 0

new_services = re.sub(r'<div class="service-card">.*?</ul>\s*</div>', wrap_card, new_services, flags=re.DOTALL)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(new_services)

# 3. Create packages.html
header_match = re.search(r'(.*?<header class="hero-header">.*?</header>)', content, re.DOTALL)
header_str = header_match.group(1) if header_match else ''
header_str = header_str.replace('OUR Services', 'OUR Packages').replace('Comprehensive digital solutions.', 'Transparent pricing for all your needs.')

footer_match = re.search(r'(<section class="faq-section">.*</html>)', content, re.DOTALL)
footer_str = footer_match.group(1) if footer_match else ''
if script_str: footer_str = footer_str.replace(script_str, '')

packages_html = header_str + '\n\n'

packages_html += '<div id="web-development">\n'
packages_html += '<h2 class="services-title font-display" style="text-align: center; margin-top: 4rem;">Web Development Packages</h2>\n'
packages_html += packages_str + '\n' + estimator_str + '\n'
packages_html += '</div>\n\n'

for i in range(1, 6):
    s_name = service_ids[i].replace('-', ' ').title()
    if s_name == 'Ui Ux Design': s_name = 'UI/UX Design'
    if s_name == 'Seo Optimization': s_name = 'SEO Optimization'
    
    packages_html += f'<div id="{service_ids[i]}">\n'
    packages_html += f'<h2 class="services-title font-display" style="text-align: center; margin-top: 4rem; padding-top: 4rem; border-top: 1px solid #eaeaea;">{s_name} Packages</h2>\n'
    
    mod_packages = packages_str.replace('id="packages"', f'id="packages-{service_ids[i]}"')
    packages_html += mod_packages + '\n'
    packages_html += '</div>\n\n'

packages_html += footer_str
if script_str:
    packages_html = packages_html.replace('</body>', script_str + '\n</body>')

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(packages_html)

print("Done")
