import re
import glob
import urllib.parse

# 1. Update contact.html to handle whatsapp submit and URL parameters
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

# Replace form with whatsapp logic
form_pattern = r'<form class="contact-form" onsubmit="event\.preventDefault\(\);">(.*?)</form>'
new_form = """<form class="contact-form" id="whatsapp-form">
                <div class="form-group">
                    <label for="package">Selected Package / Service</label>
                    <input type="text" id="package" class="form-control" placeholder="General Inquiry" readonly style="background-color: #f5f5f5; color: #555; pointer-events: none;">
                </div>
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" class="form-control" placeholder="John Doe" required>
                </div>
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" class="form-control" placeholder="john@example.com" required>
                </div>
                <div class="form-group">
                    <label for="subject">Subject</label>
                    <input type="text" id="subject" class="form-control" placeholder="How can we help?" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" class="form-control" placeholder="Tell us about your project..." required></textarea>
                </div>
                <div class="submit-btn-container">
                    <button type="submit" class="preorder-btn" style="padding: 1rem 2.5rem; font-size: 1rem;">SEND VIA WHATSAPP</button>
                </div>
            </form>

            <script>
                // Auto-fill package from URL
                document.addEventListener('DOMContentLoaded', function() {
                    const urlParams = new URLSearchParams(window.location.search);
                    const packageParam = urlParams.get('package');
                    if (packageParam) {
                        document.getElementById('package').value = packageParam;
                        document.getElementById('subject').value = "Inquiry about " + packageParam;
                    }

                    // Handle WhatsApp Submission
                    document.getElementById('whatsapp-form').addEventListener('submit', function(e) {
                        e.preventDefault();
                        const pkg = document.getElementById('package').value;
                        const name = document.getElementById('name').value;
                        const email = document.getElementById('email').value;
                        const subject = document.getElementById('subject').value;
                        const message = document.getElementById('message').value;

                        let waText = `*New Inquiry*\\n\\n`;
                        if (pkg && pkg !== "General Inquiry") {
                            waText += `*Package:* ${pkg}\\n`;
                        }
                        waText += `*Name:* ${name}\\n`;
                        waText += `*Email:* ${email}\\n`;
                        waText += `*Subject:* ${subject}\\n`;
                        waText += `*Message:* ${message}`;

                        const encodedText = encodeURIComponent(waText);
                        const whatsappUrl = `https://wa.me/94703232462?text=${encodedText}`;
                        window.open(whatsappUrl, '_blank');
                    });
                });
            </script>"""

updated_contact = re.sub(form_pattern, new_form, contact_content, flags=re.DOTALL)
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(updated_contact)

print("Updated contact.html")

# 2. Update all service pages
js_script = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const enquireButtons = document.querySelectorAll('.package-btn');
            enquireButtons.forEach(btn => {
                // If it already goes to contact, modify it
                if (btn.tagName.toLowerCase() === 'a' && btn.getAttribute('href') === 'index.html#contact') {
                    btn.setAttribute('href', 'contact.html');
                }

                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    
                    let packageCard = this.closest('.package-card');
                    let pkgName = packageCard ? packageCard.querySelector('.package-title').innerText : '';
                    let serviceTitleEl = document.querySelector('.services-title');
                    let serviceName = serviceTitleEl ? serviceTitleEl.innerText.replace(' Packages', '').replace(' Packages.', '') : '';
                    
                    if (!pkgName && !serviceName) {
                        let h1 = document.querySelector('h1.hero-heading');
                        serviceName = h1 ? h1.innerText : document.title.split('|')[1]?.trim() || document.title;
                    }
                    
                    let fullPackageName = pkgName ? `${serviceName} - ${pkgName}` : serviceName;
                    window.location.href = `contact.html?package=${encodeURIComponent(fullPackageName.trim())}`;
                });
                
                // Remove inline onclick if it exists so our event listener takes over
                if (btn.hasAttribute('onclick')) {
                    btn.removeAttribute('onclick');
                }
            });
        });
    </script>
</body>"""

html_files = glob.glob('*.html')
for file in html_files:
    if file == 'contact.html' or file == 'index.html' or file == 'about.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "enquireButtons.forEach" not in content:
        content = content.replace('</body>', js_script)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
