import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Logo
logo_pattern = r'<div class="nav-logo"[^>]*>.*?</div>'
new_logo = '''<div class="nav-logo" style="background: #1a1a1a; color: var(--accent); border-radius: 50%;">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
    </div>'''
content = re.sub(logo_pattern, new_logo, content, count=1)

# Also replace footer logo
footer_logo_pattern = r'<div class="logo"[^>]*>.*?</div>'
new_footer_logo = '''<div class="logo">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
      </div>'''
content = re.sub(footer_logo_pattern, new_footer_logo, content)

# 2. Add Offers tabs
offers_header_pattern = r'<h2 data-ar="عروض الأسبوع" data-nl="Aanbieding van de week">عروض الأسبوع</h2>\s*<p[^>]*>.*?</p>'
new_offers_header = '''<h2 data-ar="عروضنا" data-nl="Onze Aanbiedingen">عروضنا</h2>
      <p data-ar="استمتع بعروضنا اليومية، الأسبوعية، والشهرية!" data-nl="Geniet van onze dagelijkse, wekelijkse en maandelijkse aanbiedingen!">استمتع بعروضنا اليومية، الأسبوعية، والشهرية!</p>
      <div style="display: flex; gap: 0.5rem; margin-top: 1.5rem; flex-wrap: wrap;">
        <button style="background: var(--accent); color: #1a1a1a; border: none; padding: 0.5rem 1.5rem; border-radius: 20px; font-family: 'Cairo', sans-serif; font-weight: 700; cursor: pointer;">عروض يومية</button>
        <button style="background: transparent; color: var(--text2); border: 2px solid var(--border); padding: 0.5rem 1.5rem; border-radius: 20px; font-family: 'Cairo', sans-serif; font-weight: 700; cursor: pointer;">عروض أسبوعية</button>
        <button style="background: transparent; color: var(--text2); border: 2px solid var(--border); padding: 0.5rem 1.5rem; border-radius: 20px; font-family: 'Cairo', sans-serif; font-weight: 700; cursor: pointer;">عروض شهرية</button>
      </div>'''
content = re.sub(offers_header_pattern, new_offers_header, content)

# 3. Update links to .html files
content = content.replace('href="#weekly-offers"', 'href="offers.html"')
content = content.replace('href="#products"', 'href="products.html"')
content = content.replace('href="#hero"', 'href="index.html"')
# Leave about and contact as anchor links for now since they are on the homepage

# 4. Replace Contact Bar with Contact Section
contact_pattern = r'<!-- CONTACT INFO BAR -->.*?<!-- FOOTER -->'
new_contact = '''<!-- CONTACT SECTION -->
<section class="section" id="contact" style="background-color: var(--bg2);">
  <div class="contact-inner" style="max-width: 1200px; margin: 0 auto;">
    <div class="section-header" style="flex-direction: column; align-items: flex-start; margin-bottom: 2rem; max-width: 100%;">
      <div class="hero-badge" style="background-color: #fce6a8; color: #b18500; border: none; margin-bottom: 1rem; border-radius: 20px; padding: 0.4rem 1rem;">
        <span style="width: 6px; height: 6px; background: #b18500; border-radius: 50%; display: inline-block;"></span>
        <span data-ar="اتصل بنا" data-nl="Neem contact op" style="font-weight: 800; font-size: 0.9rem;">اتصل بنا</span>
      </div>
      <h2 style="font-size: 2.8rem; font-weight: 900; color: var(--text); margin-bottom: 0.5rem;" data-ar="اتصل بنا" data-nl="Neem contact op">اتصل بنا</h2>
      <p style="color: var(--text2); font-size: 1.1rem; margin: 0;" data-ar="زرنا أو تواصل معنا — يسعدنا خدمتك." data-nl="Bezoek ons of neem contact op — wij helpen u graag.">زرنا أو تواصل معنا — يسعدنا خدمتك.</p>
    </div>

    <div class="contact-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
      <!-- Cards -->
      <div class="contact-cards" style="display: flex; flex-direction: column; gap: 1.25rem;">
        
        <!-- Address Card -->
        <div class="contact-card" style="background: var(--card); border-radius: 20px; padding: 2rem; box-shadow: var(--shadow); border: 1px solid var(--border);">
          <h4 style="color: var(--text2); font-size: 0.9rem; margin-bottom: 0.5rem; font-weight: 600;" data-ar="العنوان" data-nl="Adres">العنوان</h4>
          <p style="font-size: 1.1rem; font-weight: 700; margin-bottom: 1.5rem; color: var(--text);">Bernadottelaan 3A, 2037GK Haarlem</p>
          <a href="https://maps.google.com/?q=Bernadottelaan+3A,+2037GK+Haarlem" target="_blank" class="btn-dark" style="background: #1a1a1a; color: #fff; padding: 0.75rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 700; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 0.5rem;">
            <span data-ar="الاتجاهات" data-nl="Route">الاتجاهات</span> 📍
          </a>
        </div>

        <!-- Phone Card -->
        <div class="contact-card" style="background: var(--card); border-radius: 20px; padding: 2rem; box-shadow: var(--shadow); border: 1px solid var(--border);">
          <h4 style="color: var(--text2); font-size: 0.9rem; margin-bottom: 0.5rem; font-weight: 600;" data-ar="الهاتف" data-nl="Telefoon">الهاتف</h4>
          <p style="font-size: 1.8rem; font-weight: 900; margin-bottom: 1.5rem; color: var(--text); direction: ltr; text-align: right;">23 12 71 17 06</p>
          <div style="display: flex; gap: 1rem;">
            <a href="https://wa.me/312312711706" target="_blank" class="btn-whatsapp" style="background: #25D366; color: #fff; padding: 0.75rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 700; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 0.5rem;">
              <span data-ar="واتساب" data-nl="WhatsApp">واتساب</span> 💬
            </a>
            <a href="tel:02312711706" class="btn-yellow" style="background: #f1c40f; color: #1a1a1a; padding: 0.75rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 700; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 0.5rem;">
              <span data-ar="اتصل بنا" data-nl="Bel ons">اتصل بنا</span> 📞
            </a>
          </div>
        </div>

        <!-- Hours Card -->
        <div class="contact-card" style="background: var(--card); border-radius: 20px; padding: 2rem; box-shadow: var(--shadow); border: 1px solid var(--border);">
          <h4 style="color: var(--text2); font-size: 0.9rem; margin-bottom: 0.5rem; font-weight: 600;" data-ar="ساعات العمل" data-nl="Openingstijden">ساعات العمل</h4>
          <p style="font-size: 1.1rem; font-weight: 700; color: var(--text); direction: rtl;"><span data-ar="يومياً" data-nl="Dagelijks">يومياً</span> • <span dir="ltr">08:00 – 22:00</span></p>
        </div>

      </div>

      <!-- Map -->
      <div class="contact-map" style="border-radius: 24px; overflow: hidden; box-shadow: var(--shadow); min-height: 400px; border: 1px solid var(--border);">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2435.53986968038!2d4.654388876483569!3d52.3787728720235!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47c5ef44265cc2f1%3A0x6e9a6a8b1a8d0529!2sBernadottelaan%203A%2C%202037%20GK%20Haarlem!5e0!3m2!1sen!2snl!4v1714654315220!5m2!1sen!2snl" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->'''
content = re.sub(contact_pattern, new_contact, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

