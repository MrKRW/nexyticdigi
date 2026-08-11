import os
import glob
import re
import shutil

dir_path = r'c:\xampp\htdocs\nexyticdigi'

shutil.copy(os.path.join(dir_path, 'seo-optimization.html'), os.path.join(dir_path, 'digital-marketing.html'))

with open(os.path.join(dir_path, 'digital-marketing.html'), 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<title>Services | Nexytic</title>', '<title>Digital Marketing | Nexytic</title>')
content = content.replace('id="seo-optimization"', 'id="digital-marketing"')
content = content.replace('SEO Optimization Packages', 'Digital Marketing Services')

match = re.search(r'<section class="packages-section" id="packages">.*?</section>', content, re.DOTALL)
if match:
    new_html = '''<section class="packages-section" id="packages">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 4rem; width: 100%;">
        
        <div style="text-align: center;">
            <h3 style="font-size: 3rem; color: var(--text-primary); margin-bottom: 1rem;" class="font-display">Social Media & Marketing</h3>
            <p style="font-size: 1.5rem; color: var(--text-secondary); margin-bottom: 2rem;" class="font-handwriting">A Smarter Way to Build Your Online Presence</p>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto; line-height: 1.6;">
                We help businesses stay active, look professional, and connect with the right audience through creative content, social media management, and targeted advertising.
            </p>
        </div>

        <div class="package-card" style="padding: 4rem;">
            <h3 class="package-title font-display" style="text-align: center; font-size: 2.5rem; margin-bottom: 4rem;">Included in the Package</h3>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem;">
                <!-- Social Media -->
                <div>
                    <h4 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-primary); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">Social Media</h4>
                    <ul class="package-features">
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Instagram, Facebook & TikTok account setup</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Profile optimization and basic brand setup</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Social media management</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Comment and message handling</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Customer inquiries directed to WhatsApp or phone</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Post scheduling and publishing</li>
                    </ul>
                </div>

                <!-- Content -->
                <div>
                    <h4 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-primary); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">Content</h4>
                    <ul class="package-features">
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to <strong>16 short-form videos / reels per month</strong></li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to <strong>8 designed posts per month</strong></li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Monthly content ideas and planning</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Monthly content calendar</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Promotional and seasonal content</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Special occasion and event-related posts</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Content tailored to your products, services, and target audience</li>
                    </ul>
                </div>

                <!-- Video & Creative Production -->
                <div>
                    <h4 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-primary); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">Video & Creative Production</h4>
                    <ul class="package-features">
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Professional video shooting</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Video editing and post-production</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Reels and short-form content</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Captions, transitions and motion elements</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Color correction and visual enhancement</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Drone photography and video when required</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Model-based promotional content <i>(model costs not included)</i></li>
                    </ul>
                </div>

                <!-- Advertising -->
                <div>
                    <h4 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-primary); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">Advertising</h4>
                    <ul class="package-features">
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Meta Business & Ads Manager setup</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Campaign planning</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Audience research and targeting</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Ad creative planning</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Campaign monitoring and optimization</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to <strong>4 high-performing reels re-promoted per month</strong></li>
                    </ul>
                </div>

                <!-- Events -->
                <div>
                    <h4 style="font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text-primary); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">Events</h4>
                    <ul class="package-features">
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Event photography</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Event videography</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Product launches and promotional shoots</li>
                        <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Corporate and special occasion coverage</li>
                    </ul>
                </div>
            </div>

            <div style="margin-top: 4rem; padding-top: 3rem; border-top: 1px solid var(--border-color); text-align: center;">
                <h4 style="font-size: 1.8rem; margin-bottom: 1rem; color: var(--text-primary);">Built Around Your Business</h4>
                <p style="color: var(--text-secondary); max-width: 800px; margin: 0 auto 2.5rem; line-height: 1.6;">
                    Every month, we plan content around your business goals, promotions, audience, and upcoming activities — giving your brand a consistent and professional presence across social platforms.
                </p>
                
                <h5 style="font-size: 1.2rem; color: var(--text-primary); margin-bottom: 1rem;">Best For</h5>
                <p style="color: var(--text-light); font-weight: 500; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 2.5rem;">
                    Small Businesses • Startups • Restaurants • Retail Brands • Real Estate • Hotels • Personal Brands • Service Businesses
                </p>

                <h4 class="font-display" style="font-size: 2rem; color: var(--text-primary); margin-bottom: 1rem;">One Package. Complete Social Presence.</h4>
                <p style="color: var(--text-secondary); max-width: 800px; margin: 0 auto; line-height: 1.6;">
                    From planning and content production to publishing, community management, and advertising, we take care of your social media so you can focus on running your business.
                </p>
                
                <button class="package-btn" style="max-width: 300px; margin: 3rem auto 0;" onclick="window.location.href='index.html#contact'">Contact Us to Start</button>
            </div>
        </div>
    </div>
</section>'''
    content = content[:match.start()] + new_html + content[match.end():]

content = content.replace('SEO Optimization', 'Digital Marketing')

with open(os.path.join(dir_path, 'digital-marketing.html'), 'w', encoding='utf-8') as f:
    f.write(content)

for file in glob.glob(os.path.join(dir_path, '*.html')):
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()

    file_content = file_content.replace('href="seo-optimization.html"', 'href="digital-marketing.html"')
    file_content = file_content.replace('SEO Optimization <svg', 'Digital Marketing <svg')

    if 'services.html' in file:
        file_content = file_content.replace('<h3 class="service-name font-display">SEO Optimization</h3>', '<h3 class="service-name font-display">Digital Marketing</h3>')
        file_content = file_content.replace('<p class="service-desc">Enhance your visibility on search engines. We use proven strategies to rank your website higher and attract organic, high-quality traffic.</p>', '<p class="service-desc">We help businesses stay active, look professional, and connect with the right audience through creative content, social media management, and targeted advertising.</p>')
        
        file_content = file_content.replace('<li>On-Page & Off-Page SEO</li>', '<li>Social Media Management</li>')
        file_content = file_content.replace('<li>Keyword Research</li>', '<li>Content & Video Production</li>')
        file_content = file_content.replace('<li>Analytics & Reporting</li>', '<li>Advertising & Campaigns</li>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(file_content)

if os.path.exists(os.path.join(dir_path, 'seo-optimization.html')):
    os.remove(os.path.join(dir_path, 'seo-optimization.html'))
