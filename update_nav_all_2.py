import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

new_header_html = r'''<header class="shadow-md sticky top-0 z-50 w-full flex flex-col">
        <div class="bg-bgmain w-full border-b border-bordercol">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between items-center h-20">
                    <div class="flex-1 flex justify-start items-center">
                        <a href="index.html" class="text-3xl font-extrabold tracking-tight flex items-center">
                            <span class="text-headtext drop-shadow-sm">B2BLead</span><span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-green-400 drop-shadow-sm">Nex</span>
                        </a>
                    </div>
                    
                    <nav class="hidden lg:flex justify-center space-x-6 items-center h-full">
                        <a href="index.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors">Home</a>
                        <a href="about.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors">About Us</a>
                        
                        <div class="group relative flex items-center h-full cursor-pointer">
                            <a href="healthcare-list.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors flex items-center">Healthcare <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
                            <div class="hidden group-hover:block absolute top-[calc(100%-0.5rem)] left-0 w-48 pt-2 z-50">
                                <div class="bg-bgmain shadow-xl rounded-md border border-bordercol overflow-hidden py-1">
                                    <a href="dentist-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Dentists Email List</a>
                                    <a href="hospital-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Hospital Email List</a>
                                    <a href="nurses-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Nurses Email List</a>
                                    <a href="physician-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Physicians Email List</a>
                                    <a href="healthcare-more.html" class="block px-4 py-2 text-sm font-bold text-primary hover:bg-bgsec hover:text-primary border-t border-bordercol">And More...</a>
                                </div>
                            </div>
                        </div>

                        <div class="group relative flex items-center h-full cursor-pointer">
                            <a href="technology-list.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors flex items-center">Technology <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
                            <div class="hidden group-hover:block absolute top-[calc(100%-0.5rem)] left-0 w-48 pt-2 z-50">
                                <div class="bg-bgmain shadow-xl rounded-md border border-bordercol overflow-hidden py-1">
                                    <a href="aws-users-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">AWS Users List</a>
                                    <a href="crm-users-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">CRM Users List</a>
                                    <a href="technology-more.html" class="block px-4 py-2 text-sm font-bold text-primary hover:bg-bgsec hover:text-primary border-t border-bordercol">And More...</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="group relative flex items-center h-full cursor-pointer">
                            <a href="professionals-data-list.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors flex items-center">Professionals Data <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
                            <div class="hidden group-hover:block absolute top-[calc(100%-0.5rem)] left-0 w-48 pt-2 z-50">
                                <div class="bg-bgmain shadow-xl rounded-md border border-bordercol overflow-hidden py-1">
                                    <a href="ceo-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">CEO Email List</a>
                                    <a href="cfo-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">CFO Email List</a>
                                    <a href="cmo-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">CMO Email List</a>
                                    <a href="professionals-more.html" class="block px-4 py-2 text-sm font-bold text-primary hover:bg-bgsec hover:text-primary border-t border-bordercol">And More...</a>
                                </div>
                            </div>
                        </div>

                        <div class="group relative flex items-center h-full cursor-pointer">
                            <a href="industry-wise-data-list.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors flex items-center">Industry Wise Data <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
                            <div class="hidden group-hover:block absolute top-[calc(100%-0.5rem)] left-0 w-56 pt-2 z-50">
                                <div class="bg-bgmain shadow-xl rounded-md border border-bordercol overflow-hidden py-1">
                                    <a href="automotive-industry-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Automotive Industry</a>
                                    <a href="banking-finance-industry-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Banking & Finance Industry</a>
                                    <a href="oil-gas-industry-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Oil & Gas Industry</a>
                                    <a href="real-estate-industry-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Real Estate Industry</a>
                                    <a href="manufacturing-industry-list.html" class="block px-4 py-2 text-sm text-headtext hover:bg-bgsec hover:text-primary">Manufacturing Industry</a>
                                    <a href="industry-more.html" class="block px-4 py-2 text-sm font-bold text-primary hover:bg-bgsec hover:text-primary border-t border-bordercol">And More...</a>
                                </div>
                            </div>
                        </div>
                        
                        <a href="pricing.html" class="text-headtext hover:text-primary font-bold text-sm transition-colors">Pricing</a>
                    </nav>

                    <div class="flex-1 flex justify-end items-center space-x-5">
                        <a href="contact-us.html" class="hidden lg:flex bg-btnbg text-btntext px-6 py-2.5 rounded-full text-xs font-bold uppercase tracking-wider hover:bg-btnbg transition-colors shadow-md items-center"><svg class="w-3.5 h-3.5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg> Contact Us</a>
                        <button id="mobile-menu-btn" class="lg:hidden text-headtext hover:text-primary focus:outline-none p-2 ml-4"><svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path id="menu-icon" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /><path id="close-icon" class="hidden" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg></button>
                    </div>
                </div>
            </div>
        </div>

        <div id="mobile-menu" class="hidden lg:hidden bg-bgmain border-t border-bordercol shadow-xl absolute top-full w-full max-h-[85vh] overflow-y-auto pb-6">
            <div class="px-4 py-2 space-y-1">
                <a href="index.html" class="block px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors">Home</a>
                <a href="about.html" class="block px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors">About Us</a>
                
                <details class="group">
                    <summary class="flex justify-between items-center px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                        <a href="healthcare-list.html" class="flex-1">Healthcare</a>
                        <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <div class="pl-6 pb-2 space-y-1">
                        <a href="dentist-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Dentists Email List</a>
                        <a href="hospital-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Hospital Email List</a>
                        <a href="nurses-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Nurses Email List</a>
                        <a href="physician-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Physicians Email List</a>
                        <a href="healthcare-more.html" class="block px-3 py-2 rounded-md text-sm font-bold text-primary hover:text-hovercol transition-colors">And More...</a>
                    </div>
                </details>
                
                <details class="group">
                    <summary class="flex justify-between items-center px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                        <a href="technology-list.html" class="flex-1">Technology</a>
                        <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <div class="pl-6 pb-2 space-y-1">
                        <a href="aws-users-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">AWS Users List</a>
                        <a href="crm-users-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">CRM Users List</a>
                        <a href="technology-more.html" class="block px-3 py-2 rounded-md text-sm font-bold text-primary hover:text-hovercol transition-colors">And More...</a>
                    </div>
                </details>

                <details class="group">
                    <summary class="flex justify-between items-center px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                        <a href="professionals-data-list.html" class="flex-1">Professionals Data</a>
                        <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <div class="pl-6 pb-2 space-y-1">
                        <a href="ceo-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">CEO Email List</a>
                        <a href="cfo-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">CFO Email List</a>
                        <a href="cmo-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">CMO Email List</a>
                        <a href="professionals-more.html" class="block px-3 py-2 rounded-md text-sm font-bold text-primary hover:text-hovercol transition-colors">And More...</a>
                    </div>
                </details>

                <details class="group">
                    <summary class="flex justify-between items-center px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                        <a href="industry-wise-data-list.html" class="flex-1">Industry Wise Data</a>
                        <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <div class="pl-6 pb-2 space-y-1">
                        <a href="automotive-industry-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Automotive Industry</a>
                        <a href="banking-finance-industry-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Banking & Finance Industry</a>
                        <a href="oil-gas-industry-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Oil & Gas Industry</a>
                        <a href="real-estate-industry-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Real Estate Industry</a>
                        <a href="manufacturing-industry-list.html" class="block px-3 py-2 rounded-md text-sm font-medium text-headtext hover:text-primary transition-colors">Manufacturing Industry</a>
                        <a href="industry-more.html" class="block px-3 py-2 rounded-md text-sm font-bold text-primary hover:text-hovercol transition-colors">And More...</a>
                    </div>
                </details>
                
                <a href="pricing.html" class="block px-3 py-3 rounded-md text-base font-bold text-headtext hover:text-primary transition-colors">Pricing</a>
                <a href="contact-us.html" class="block mt-4 px-3 py-3 rounded-md text-base font-bold text-white bg-primary hover:bg-hovercol text-center transition-colors">Contact Us</a>
            </div>
        </div>
    </header>'''

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        # Replace the entire <header>...</header> block
        content = re.sub(r'<header.*?</header>', new_header_html, content, flags=re.DOTALL)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
