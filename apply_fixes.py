import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

footer_loc_replacement = r'''<div class="mt-4"><span class="text-sm font-bold text-headtext">Serving Businesses Worldwide</span><br/><span class="text-xs text-paratext">🇺🇸 United States | 🇨🇦 Canada | 🇪🇺 Europe | 🇮🇳 India</span></div>'''

simple_pricing_regex = r'<!-- Simple and Transparent Pricing Section -->\s*<section class="py-16 text-center max-w-4xl mx-auto px-4 bg-bgmain">.*?</section>'

faq_html = r'''
        <!-- FAQ Section -->
        <section class="bg-bgsec py-20 px-4 mt-8 border-t border-bordercol">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-xl sm:text-2xl font-bold text-headtext mb-8 px-4">Frequently Asked Questions</h2>
                
                <div class="space-y-0">
                    <details class="group border-b border-bordercol bg-transparent" open>
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">1. What services do you provide?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            We provide verified B2B business email lists, AI-powered CRM data enrichment, lead generation solutions, direct phone numbers, company information, and custom prospect lists to help businesses connect with the right decision-makers.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">2. How accurate is your data?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            Our database is continuously updated and verified to provide accurate business email addresses, direct phone numbers, job titles, and company information. We strive to deliver high-quality data that improves your outreach success.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">3. Can I upload my CRM for data enrichment?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            Yes. You can upload your existing CRM or contact list, and our AI-powered data enrichment service will update missing information such as business emails, direct phone numbers, job titles, and company details.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">4. Is your data GDPR and CAN-SPAM compliant?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            Yes. We are committed to responsible data practices and provide business contact information in accordance with applicable data privacy regulations, including GDPR and CAN-SPAM.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">5. Do you offer custom email lists?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            Yes. We can build custom prospect lists based on industry, company size, location, job title, technology used, revenue, and many other targeting criteria.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">6. Do you offer a free trial or sample data?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            Yes. We can provide a sample dataset or demo so you can evaluate the quality of our data before purchasing.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">7. What payment methods do you accept?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            We accept secure online payments through major credit/debit cards and other supported payment methods. Contact our sales team for enterprise billing options.
                        </div>
                    </details>
                    
                    <details class="group border-b border-bordercol bg-transparent">
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-headtext py-5 px-4 outline-none hover:text-primary transition-colors">
                            <span class="text-sm font-bold">8. Do you offer a money-back guarantee?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            If you experience data quality issues, please contact our support team. We review each case individually and work to resolve it through data replacement, credits, or other appropriate solutions in accordance with our refund policy.
                        </div>
                    </details>
                </div>
            </div>
        </section>
'''

faq_regex = r'<!-- FAQ Section -->\s*<section class="bg-bgsec py-20 px-4 mt-8 border-t border-bordercol">.*?</section>'

old_address_regex = r'<span class="flex items-center text-paratext transition group">\s*<div class="flex-shrink-0 w-8 h-8 rounded-full bg-bgmain flex items-center justify-center border border-bordercol group-hover:border-primary transition-colors mr-3">\s*<svg class="w-4 h-4 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">\s*<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z">\s*</path>\s*<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z">\s*</path>\s*</svg>\s*</div>\s*<span class="text-sm">Texas, USA</span>\s*</span>'
alt_old_address_regex = r'<p class="text-gray-700 text-sm leading-relaxed">\s*Texas, USA\s*</p>'
footer_loc_replacement_2 = r'<div class="text-gray-700 text-sm leading-relaxed mt-2"><span class="font-bold">Serving Businesses Worldwide</span><br/>🇺🇸 United States | 🇨🇦 Canada | 🇪🇺 Europe | 🇮🇳 India</div>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        old_content = content
        
        # 1. Update text in index.html
        if filename == "index.html":
            content = content.replace("Turn Stale CRM Data into Gold", "Transform Outdated CRM Data into Accurate, Actionable Insights")
            content = content.replace("Upload your outdated lists and let our AI engine fill in the blanks. We append missing emails, direct dials, and update job titles instantly.", "Our AI-powered data enrichment solution updates outdated records by adding verified business emails, direct phone numbers, current job titles, and other essential contact details—so your team can reach the right prospects with confidence.")
            
        # 2. Update pricing.html FAQ and Simple pricing
        if filename == "pricing.html":
            content = re.sub(simple_pricing_regex, '', content, flags=re.DOTALL)
            content = re.sub(faq_regex, faq_html, content, flags=re.DOTALL)
            
        # 3. Replace Span Global Services globally
        content = content.replace("Span Global Services'", "Our")
        content = content.replace("Span Global Services’", "Our")
        content = content.replace("Span Global Services", "our platform")
        content = content.replace("Choose our platform to Enjoy Premium Company", "Partner with us to Enjoy Premium Company") 
        content = content.replace("Benefits of Procuring our platform Automotive", "Benefits of Procuring Our Automotive") 
        
        # 4. Update address
        content = re.sub(old_address_regex, footer_loc_replacement, content, flags=re.DOTALL)
        content = re.sub(alt_old_address_regex, footer_loc_replacement_2, content, flags=re.DOTALL)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
