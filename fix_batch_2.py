import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

# 1. Kryptonite section replacement
old_kryptonite_regex = r'<h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-\[#0B6B3A\] tracking-tight leading-tight">\s*Our Professional Email List is the Kryptonite You Need to Engage with Influential Leads Successfully\s*</h2>\s*</div>\s*<div class="lg:col-span-7 space-y-6 text-paratext leading-relaxed">\s*<p>Put merely, C-suite executives are the torchbearers of their organizations.*?<a href="#" class="inline-block mt-4 text-primary font-bold tracking-widest uppercase text-sm hover:text-hovercol transition-colors">READ MORE</a>'

new_kryptonite_html = r'''<h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#0B6B3A] tracking-tight leading-tight">
                        Our Professional Email List Is the Key to Engaging Influential Leads
                    </h2>
                </div>
                <div class="lg:col-span-7 space-y-6 text-paratext leading-relaxed">
                    <p>Today's executives are busier than ever, making accurate contact data essential for successful outreach. Our verified professional email lists help sales and marketing teams connect with decision-makers across industries using reliable business contact information.</p>
                    <p>Whether you're generating new leads, expanding into new markets, or running targeted email campaigns, our database provides verified business emails, direct phone numbers, job titles, and company details to help you reach the right prospects faster.</p>
                    <p>With regularly updated data and advanced targeting options, you can build highly qualified prospect lists that improve engagement, increase conversions, and accelerate business growth.</p>'''


# 2. ceo-list.html updates
# A. Industry coverage
old_industries_regex = r'<span class="inline-block bg-\[#E8F8EA\] text-secondary text-xs font-bold px-4 py-1\.5 rounded-full uppercase tracking-widest mb-4">\s*TARGET INDUSTRIES\s*</span>\s*<h2 class="text-3xl lg:text-4xl font-extrabold text-headtext">Industries We Cover</h2>\s*<p class="mt-4 text-lg text-paratext max-w-2xl mx-auto">Find exact decision-makers in the verticals that matter most to your business.</p>\s*</div>\s*<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">\s*<div class="flex items-center p-5 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">.*?</div>\s*</div>'

new_industries_html = r'''<span class="inline-block bg-[#E8F8EA] text-secondary text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-4">
                    INDUSTRY COVERAGE
                </span>
                <h2 class="text-3xl lg:text-4xl font-extrabold text-headtext">List of CEOs Covered by Industry</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">List of Banking Industry CEOs</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Oil and Gas Industry CEO Leads</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Aerospace Industry C-Level Email Database</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Manufacturing Industry CEO Contact Lists</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Medical Industry CEO Marketing Data</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Education Services Industry CEO Database</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Call Center Industry CEO Contacts</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Insurance Industry CEO Database</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Media & Marketing Industry CEO Database</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Automotive Industry CEO Contacts</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Telecom Industry CEO Contacts</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Food and Beverage Industry CEO Leads</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">Telecom Industry CEO Marketing</span>
                </div>
                <div class="flex items-center p-4 border border-bordercol rounded-xl hover:border-primary hover:shadow-lg hover:bg-bgsec transition-all cursor-pointer group">
                    <div class="w-2 h-2 rounded-full bg-primary mr-3 group-hover:scale-150 transition-all"></div>
                    <span class="font-bold text-headtext text-sm">List of Core-Banking Industry CEOs</span>
                </div>
            </div>'''

# B. FAQ
old_ceo_faq_regex = r'<span class="text-sm">How frequently is the CEO email list updated\?</span>.*?<div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">\s*Our database is regularly updated and verified to ensure accurate business email addresses, job titles, company details, and contact information. We continuously maintain data quality so you receive reliable, up-to-date records for your sales and marketing campaigns.\s*</div>'
new_ceo_faq_html = r'''<span class="text-sm">How frequently is the CEO email list updated?</span>
                            <span class="transition-transform group-open:rotate-45 text-xl font-light">+</span>
                        </summary>
                        <div class="text-gray-600 text-xs sm:text-sm px-4 pb-6 leading-relaxed max-w-3xl">
                            Our database is regularly updated and verified to ensure accurate business email addresses, job titles, company details, and contact information. We continuously maintain data quality so you receive reliable, up-to-date records for your sales and marketing campaigns.
                        </div>'''

# C. Peek Inside the Database
old_ceo_peek_regex = r'<h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Peek Inside the <span class="text-primary">Database</span></h2>\s*<p class="text-paratext max-w-2xl mx-auto">From your prospect\'s email address to their direct calling number, you will find all legal and genuine information at your disposal.</p>'
new_ceo_peek_html = r'''<h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Peek Inside the <span class="text-primary">Database</span></h2>
                <p class="text-paratext max-w-2xl mx-auto">Explore verified business contact data, including email addresses, direct phone numbers, job titles, company information, and other essential details—ready to power your sales and marketing efforts.</p>'''


# 3. dentist-list.html update
old_dentist_regex = r'<h2 class="text-2xl font-bold text-primary mb-4">Grow Your Graph by Reaching Targeted Dentists with Our Sales Leads</h2>\s*<p class="text-paratext mb-4 leading-relaxed">\s*Our Opt-in Dentists Email List is a verified database that will help you target various dental professionals from across the globe. It is a premium service to provide B2B marketers an easy to use database of contacts that contains high-quality relevant details. You can customize the list on the basis of your expansion. Some of the parameters include state, zip code, email address, practice, phone number, clinic location, etc.\s*</p>\s*<p class="text-paratext leading-relaxed">\s*We have manually segmented the data in order to make it easy for you to reach the right audience and manage the best business opportunities. You can directly connect with the dental community.\s*</p>'
new_dentist_html = r'''<h2 class="text-2xl font-bold text-primary mb-4">Grow Your Graph by Reaching Targeted Dentists with Our Sales Leads</h2>
                    <h3 class="text-xl font-semibold text-headtext mb-3">Verified Dentist Contact Database</h3>
                    <p class="text-paratext mb-4 leading-relaxed">
                        Our Verified Dentist Contact Database helps you connect with dental professionals worldwide through accurate and regularly updated business contact data. Access valuable information such as business email addresses, direct phone numbers, specialties, years of experience, clinic names, practice locations, and other essential details to support your sales and marketing campaigns.
                    </p>
                    <p class="text-paratext leading-relaxed">
                        Whether you're promoting dental products, healthcare services, medical equipment, software solutions, or professional events, our targeted database helps you reach the right audience faster. With advanced segmentation and high-quality business data, you can improve outreach, generate qualified leads, and build meaningful business relationships.
                    </p>'''

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        old_content = content
        
        # 1. Kryptonite
        content = re.sub(old_kryptonite_regex, new_kryptonite_html, content, flags=re.DOTALL)
        
        # 2. ceo-list.html
        if filename == "ceo-list.html":
            content = re.sub(old_industries_regex, new_industries_html, content, flags=re.DOTALL)
            content = re.sub(old_ceo_faq_regex, new_ceo_faq_html, content, flags=re.DOTALL)
            content = re.sub(old_ceo_peek_regex, new_ceo_peek_html, content, flags=re.DOTALL)
            
        # 3. dentist-list.html
        if filename == "dentist-list.html":
            content = re.sub(old_dentist_regex, new_dentist_html, content, flags=re.DOTALL)
            
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
