import os

# Read the contact.html to use as a template
with open('contact.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Extract header and footer
# We'll replace everything between <section class="contact-hero"> and </section>
# and <section class="contact-section"> and </section>

import re

# We will just replace the middle part.
def generate_page(filename, title, heading, sub_heading, content):
    html = template_content
    
    # Replace title
    html = re.sub(r'<title>Nexytic \| .*?</title>', f'<title>Nexytic | {title}</title>', html)
    
    # Replace the contact-hero section content
    hero_pattern = r'<section class="contact-hero">.*?</section>'
    hero_replacement = f'''<section class="contact-hero">
        <h1 class="contact-heading font-display">{heading}</h1>
        <span class="contact-sub font-handwriting">{sub_heading}</span>
    </section>'''
    html = re.sub(hero_pattern, hero_replacement, html, flags=re.DOTALL)
    
    # Replace the contact-section content
    section_pattern = r'<section class="contact-section">.*?</section>'
    section_replacement = f'''<section class="contact-section">
        <div class="contact-container" style="display: block;">
            <div class="contact-info-panel" style="max-width: 100%;">
                <h3 class="font-display">{title}</h3>
                {content}
            </div>
        </div>
    </section>'''
    html = re.sub(section_pattern, section_replacement, html, flags=re.DOTALL)
    
    # Save the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Generated {filename}')

pages = [
    {
        'filename': 'terms-of-service.html',
        'title': 'Terms of Service',
        'heading': 'Terms of Service',
        'sub_heading': 'Please read our terms carefully.',
        'content': '''<p>Welcome to Nexytic! These Terms of Service outline the rules and regulations for the use of our website and services.</p>
        <p>By accessing this website we assume you accept these terms and conditions. Do not continue to use Nexytic if you do not agree to take all of the terms and conditions stated on this page.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">1. Introduction</h4>
        <p>These terms will govern your use of our website. By using our website, you accept these terms in full.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">2. Intellectual Property Rights</h4>
        <p>Unless otherwise stated, Nexytic and/or its licensors own the intellectual property rights for all material on Nexytic. All intellectual property rights are reserved.</p>
        '''
    },
    {
        'filename': 'privacy-policy.html',
        'title': 'Privacy Policy',
        'heading': 'Privacy Policy',
        'sub_heading': 'How we handle your data.',
        'content': '''<p>At Nexytic, accessible from our website, one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by Nexytic and how we use it.</p>
        <p>If you have additional questions or require more information about our Privacy Policy, do not hesitate to contact us.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">Information we collect</h4>
        <p>The personal information that you are asked to provide, and the reasons why you are asked to provide it, will be made clear to you at the point we ask you to provide your personal information.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">How we use your information</h4>
        <p>We use the information we collect in various ways, including to:</p>
        <ul style="color: #e0e0e0; margin-left: 2rem; margin-bottom: 2rem; line-height: 1.6;">
            <li>Provide, operate, and maintain our website</li>
            <li>Improve, personalize, and expand our website</li>
            <li>Understand and analyze how you use our website</li>
        </ul>
        '''
    },
    {
        'filename': 'cookie-policy.html',
        'title': 'Cookie Policy',
        'heading': 'Cookie Policy',
        'sub_heading': 'Information about how we use cookies.',
        'content': '''<p>This is the Cookie Policy for Nexytic, accessible from our website.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">What Are Cookies</h4>
        <p>As is common practice with almost all professional websites this site uses cookies, which are tiny files that are downloaded to your computer, to improve your experience. This page describes what information they gather, how we use it and why we sometimes need to store these cookies.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">How We Use Cookies</h4>
        <p>We use cookies for a variety of reasons detailed below. Unfortunately, in most cases, there are no industry standard options for disabling cookies without completely disabling the functionality and features they add to this site.</p>
        '''
    },
    {
        'filename': 'faqs.html',
        'title': 'Frequently Asked Questions',
        'heading': 'FAQs',
        'sub_heading': 'We have answers to your questions.',
        'content': '''<p>Find answers to the most commonly asked questions below.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">What services do you provide?</h4>
        <p>We provide a range of digital services including Web Development, Software Solutions, UI/UX Design, Hosting & Security, and Digital Marketing.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">How can I start a project with you?</h4>
        <p>You can get in touch with us via our Contact Us page. Simply fill out the form or reach out via WhatsApp or email, and our team will get back to you promptly to discuss your requirements.</p>
        <br>
        <h4 style="color: #ffffff; margin-bottom: 1rem; font-size: 1.5rem;">Do you offer ongoing support?</h4>
        <p>Yes, we offer ongoing maintenance, support, and security services for all projects we undertake to ensure everything runs smoothly over time.</p>
        '''
    }
]

for page in pages:
    generate_page(page['filename'], page['title'], page['heading'], page['sub_heading'], page['content'])
