import re
import os

with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

# 1. Update services.html links
# from href="packages.html#web-development" to href="web-development.html"
def replace_link(match):
    s_id = match.group(1)
    return f'href="{s_id}.html"'

services_content = re.sub(r'href="packages\.html#(.*?)"', replace_link, services_content)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_content)

# 2. Extract sections from packages.html
with open('packages.html', 'r', encoding='utf-8') as f:
    packages_content = f.read()

# We know packages.html has <div id="service-id"> ... </div>\n\n for each service
# and a header and a footer.
# A better way is to split by `<div id="`
parts = packages_content.split('<div id="')
header = parts[0]

service_ids = [
    'web-development',
    'software-solutions',
    'ui-ux-design',
    'hosting-security',
    'seo-optimization',
    'e-commerce'
]

# The last part will contain the footer.
# Let's find the footer. In packages.html, after the last </div>\n\n we have <section class="faq-section">
# Wait, actually splitting by `<div id="` means the last part has `e-commerce">\n...</div>\n\n<section class="faq-section">...`

# Instead of relying on splits which could break, let's extract header and footer properly.
header_match = re.search(r'(.*?<header class="hero-header">.*?</header>)', packages_content, re.DOTALL)
header_str = header_match.group(1) if header_match else ''

footer_match = re.search(r'(<section class="faq-section">.*</html>)', packages_content, re.DOTALL)
footer_str = footer_match.group(1) if footer_match else ''

for s_id in service_ids:
    # extract the section for this service
    # It starts with <div id="s_id"> and ends with </div> before the next <div id= or footer
    section_match = re.search(rf'(<div id="{s_id}">.*?</div>\s*\n\s*\n)', packages_content, re.DOTALL)
    if not section_match:
        # Fallback if the regex doesn't catch it
        # Actually in modify.py I generated them like:
        # <div id="web-development">
        # ...
        # </div>\n\n
        # so this regex should work perfectly.
        section_match = re.search(rf'(<div id="{s_id}">.*?</div>)', packages_content, re.DOTALL)
    
    section_str = section_match.group(1) if section_match else ''
    
    # Change the inner <div id="..."> to <section class="packages-section" id="...">
    # Wait, the inner packages string already has `<section class="packages-section"`
    # because in modify.py I just wrapped the `<section class="packages-section">` in a `<div id="...">`.
    
    page_html = header_str + '\n\n' + section_str + '\n\n' + footer_str
    
    with open(f'{s_id}.html', 'w', encoding='utf-8') as f:
        f.write(page_html)

# Clean up packages.html
if os.path.exists('packages.html'):
    os.remove('packages.html')

print("Done creating separate pages.")
