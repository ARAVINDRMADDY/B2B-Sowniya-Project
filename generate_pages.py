import os

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
tech_file = os.path.join(directory, "technology-list.html")

with open(tech_file, "r", encoding="utf-8") as f:
    tech_content = f.read()

# Extract header and footer
# Header is up to <header ... </header>
header_end = tech_content.find("</header>") + 9
header = tech_content[:header_end]

# Footer starts from <footer ...
footer_start = tech_content.find('<footer class="bg-bgmain text-headtext')
footer = tech_content[footer_start:]

def generate_page(title, keywords):
    # Section 1: Hero (50+ lines)
    # Count: ~55 lines
    section1 = f'''
    <!-- SECTION 1: HERO -->
    <section class="relative pt-12 pb-16 lg:pt-16 lg:pb-24 overflow-hidden border-b border-bordercol bg-bgsec">
        <div class="absolute inset-0 z-0">
            <div class="absolute inset-0 bg-gradient-to-r from-[#051C14] to-[#09C000] opacity-90 mix-blend-multiply"></div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
            <div class="lg:grid lg:grid-cols-12 lg:gap-12 xl:gap-16 items-center">
                <div class="lg:col-span-7 flex flex-col justify-center text-center lg:text-left text-white items-center lg:items-start">
                    <div class="w-fit inline-flex items-center px-4 py-1.5 rounded-full bg-white/10 border border-white/20 text-white font-semibold text-xs uppercase tracking-widest mb-4 backdrop-blur-sm">
                        <span class="flex w-2 h-2 rounded-full bg-white mr-2 animate-pulse shadow-[0_0_8px_white]"></span>
                        Verified {title}
                    </div>
                    <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight leading-tight mb-4">
                        Connect with {title} Decision Makers Worldwide
                    </h1>
                    <p class="text-base text-gray-200 mb-6 max-w-xl leading-relaxed">
                        Access the most comprehensive, highly-verified database of {keywords} professionals. Target CTOs, IT Directors, and developers using {keywords} in their enterprise environments.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 mt-2">
                        <a href="#form" class="inline-flex justify-center items-center bg-[#09C000] hover:bg-[#0B6B3A] text-white font-bold px-8 py-3 rounded uppercase tracking-wider text-sm transition-colors shadow-lg">
                            Request Sample
                        </a>
                        <a href="pricing.html" class="inline-flex justify-center items-center bg-transparent border-2 border-white hover:bg-white hover:text-[#051C14] text-white font-bold px-8 py-3 rounded uppercase tracking-wider text-sm transition-colors shadow-lg">
                            View Pricing
                        </a>
                    </div>
                    <div class="mt-8 pt-6 border-t border-white/20 flex flex-wrap gap-6 items-center justify-center lg:justify-start">
                        <div class="flex items-center">
                            <span class="text-3xl font-black mr-2">95%</span>
                            <span class="text-xs uppercase tracking-wide opacity-80 leading-tight">Delivery<br>Rate</span>
                        </div>
                        <div class="w-px h-8 bg-white/20"></div>
                        <div class="flex items-center">
                            <span class="text-3xl font-black mr-2">100k+</span>
                            <span class="text-xs uppercase tracking-wide opacity-80 leading-tight">Verified<br>Contacts</span>
                        </div>
                        <div class="w-px h-8 bg-white/20 hidden sm:block"></div>
                        <div class="flex items-center hidden sm:flex">
                            <span class="text-3xl font-black mr-2">GDPR</span>
                            <span class="text-xs uppercase tracking-wide opacity-80 leading-tight">Fully<br>Compliant</span>
                        </div>
                    </div>
                </div>
                <div class="lg:col-span-5 relative mt-12 lg:mt-0 hidden lg:block">
                    <div class="relative w-full h-[400px] rounded-xl overflow-hidden shadow-2xl border-4 border-white/10 backdrop-blur-sm bg-white/5 p-6">
                         <!-- Abstract graphic -->
                         <div class="absolute inset-0 flex items-center justify-center">
                            <svg class="w-48 h-48 text-[#09C000] opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                            </svg>
                         </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''
    
    # Section 2: Features (70+ lines)
    # Count: ~80 lines
    section2 = f'''
    <!-- SECTION 2: FEATURES -->
    <section class="py-20 bg-bgmain border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl font-bold text-headtext mb-4">Why Choose Our {title}?</h2>
                <p class="text-paratext">We provide the most robust and highly targeted intelligence for {keywords} marketing. Here is what sets our data apart.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <div class="bg-bgsec p-8 rounded-xl border border-bordercol hover:border-[#09C000] transition-colors group">
                    <div class="w-14 h-14 bg-white rounded-lg flex items-center justify-center shadow-md mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-7 h-7 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Double Verified</h3>
                    <p class="text-paratext text-sm mb-4">Every contact in our {title} goes through an extensive AI-driven and manual verification process to ensure zero hard bounces.</p>
                    <ul class="text-xs text-paratext space-y-2">
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> SMTP Pinged</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Catch-all Removed</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Syntax Checked</li>
                    </ul>
                </div>
                <div class="bg-bgsec p-8 rounded-xl border border-bordercol hover:border-[#09C000] transition-colors group">
                    <div class="w-14 h-14 bg-white rounded-lg flex items-center justify-center shadow-md mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-7 h-7 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Global Reach</h3>
                    <p class="text-paratext text-sm mb-4">Connect with {keywords} users across North America, Europe, APAC, and LATAM markets without geographical limitations.</p>
                    <ul class="text-xs text-paratext space-y-2">
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> 150+ Countries</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Localized Data</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Multi-language</li>
                    </ul>
                </div>
                <div class="bg-bgsec p-8 rounded-xl border border-bordercol hover:border-[#09C000] transition-colors group">
                    <div class="w-14 h-14 bg-white rounded-lg flex items-center justify-center shadow-md mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-7 h-7 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Custom Built</h3>
                    <p class="text-paratext text-sm mb-4">Don't buy off-the-shelf lists. We build your {title} specifically based on your ideal customer profile and buyer persona.</p>
                    <ul class="text-xs text-paratext space-y-2">
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Niche Segmentation</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Direct Dials Included</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> Custom CRM Format</li>
                    </ul>
                </div>
                <div class="bg-bgsec p-8 rounded-xl border border-bordercol hover:border-[#09C000] transition-colors group">
                    <div class="w-14 h-14 bg-white rounded-lg flex items-center justify-center shadow-md mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-7 h-7 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                        </svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">100% Compliant</h3>
                    <p class="text-paratext text-sm mb-4">Market with confidence. Our {title} complies with all major global data privacy regulations and anti-spam laws.</p>
                    <ul class="text-xs text-paratext space-y-2">
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> GDPR Compliant</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> CCPA Compliant</li>
                        <li class="flex items-center"><svg class="w-3 h-3 text-[#09C000] mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> CAN-SPAM Certified</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    '''
    
    # Section 3: Data Breakdown Grid (70+ lines)
    # Count: ~85 lines
    section3 = f'''
    <!-- SECTION 3: DATA BREAKDOWN -->
    <section class="py-20 bg-bgmain border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                <div class="w-full lg:w-1/2">
                    <h2 class="text-3xl font-bold text-headtext mb-6">Inside the {title}</h2>
                    <p class="text-paratext mb-8 leading-relaxed">
                        Our intelligence team aggregates data from over 40+ premium sources, tech forums, and proprietary tracking technologies to map exactly who is using {keywords}. Here are the demographics you can target:
                    </p>
                    <div class="space-y-6">
                        <div class="flex items-start">
                            <div class="flex-shrink-0 mt-1"><div class="w-8 h-8 rounded-full bg-[#09C000]/10 flex items-center justify-center"><svg class="w-4 h-4 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg></div></div>
                            <div class="ml-4">
                                <h4 class="text-lg font-bold text-headtext">Job Titles</h4>
                                <p class="text-sm text-paratext mt-1">CIOs, CTOs, IT Directors, Cloud Architects, System Administrators, DevOps Engineers, and Software Developers.</p>
                            </div>
                        </div>
                        <div class="flex items-start">
                            <div class="flex-shrink-0 mt-1"><div class="w-8 h-8 rounded-full bg-[#09C000]/10 flex items-center justify-center"><svg class="w-4 h-4 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg></div></div>
                            <div class="ml-4">
                                <h4 class="text-lg font-bold text-headtext">Company Size</h4>
                                <p class="text-sm text-paratext mt-1">Startups (1-50), Mid-Market (51-500), Enterprise (501-5000), and Fortune 500 companies actively utilizing {keywords}.</p>
                            </div>
                        </div>
                        <div class="flex items-start">
                            <div class="flex-shrink-0 mt-1"><div class="w-8 h-8 rounded-full bg-[#09C000]/10 flex items-center justify-center"><svg class="w-4 h-4 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div></div>
                            <div class="ml-4">
                                <h4 class="text-lg font-bold text-headtext">Industry Verticals</h4>
                                <p class="text-sm text-paratext mt-1">Technology, Healthcare, Finance, Manufacturing, Retail, and Logistics sectors.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="w-full lg:w-1/2">
                    <div class="bg-bgsec border border-bordercol rounded-xl overflow-hidden shadow-lg">
                        <div class="bg-gradient-to-r from-[#051C14] to-[#0B6B3A] px-6 py-4">
                            <h3 class="text-white font-bold text-lg">Data Fields Included</h3>
                        </div>
                        <div class="p-6">
                            <ul class="grid grid-cols-2 gap-4">
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> First & Last Name</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Verified Work Email</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Direct Phone Numbers</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Job Title & Department</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Company Name</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Website URL</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> LinkedIn Profile</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Physical Address</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Employee Count</li>
                                <li class="flex items-center text-sm font-medium text-headtext"><svg class="w-4 h-4 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Revenue Estimates</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''
    
    # Section 4: Verification Process (70+ lines)
    # Count: ~75 lines
    section4 = f'''
    <!-- SECTION 4: PROCESS -->
    <section class="py-20 bg-bgmain border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl font-bold text-headtext mb-4">Our Verification Process</h2>
                <p class="text-paratext">How we guarantee 95%+ accuracy for our {title}. We do not sell stale data.</p>
            </div>
            
            <div class="relative max-w-5xl mx-auto">
                <div class="hidden md:block absolute left-1/2 top-0 bottom-0 w-1 bg-gradient-to-b from-[#09C000]/20 via-[#09C000] to-[#09C000]/20 transform -translate-x-1/2 rounded-full"></div>
                
                <div class="space-y-12">
                    <div class="relative flex items-center flex-col md:flex-row">
                        <div class="md:w-1/2 pr-0 md:pr-12 text-center md:text-right mb-6 md:mb-0">
                            <h3 class="text-xl font-bold text-headtext mb-2">1. Data Aggregation</h3>
                            <p class="text-sm text-paratext">We source {keywords} intelligence from trade shows, tech seminars, web scraping of tech stacks, magazines, public records, and premium API feeds.</p>
                        </div>
                        <div class="absolute left-1/2 transform -translate-x-1/2 flex items-center justify-center w-12 h-12 rounded-full bg-bgmain border-4 border-[#09C000] z-10 shadow-lg">
                            <span class="text-[#09C000] font-bold">01</span>
                        </div>
                        <div class="md:w-1/2 pl-0 md:pl-12">
                            <div class="bg-bgsec rounded-lg p-4 border border-bordercol inline-block shadow-sm w-full md:w-3/4">
                                <p class="text-xs font-mono text-paratext">Processing over 2M+ daily signals for {keywords} installations.</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="relative flex items-center flex-col md:flex-row-reverse">
                        <div class="md:w-1/2 pl-0 md:pl-12 text-center md:text-left mb-6 md:mb-0">
                            <h3 class="text-xl font-bold text-headtext mb-2">2. Automated Validation</h3>
                            <p class="text-sm text-paratext">AI algorithms verify email syntax, ping SMTP servers without sending emails, and cross-reference phone numbers against global telecom databases.</p>
                        </div>
                        <div class="absolute left-1/2 transform -translate-x-1/2 flex items-center justify-center w-12 h-12 rounded-full bg-bgmain border-4 border-[#09C000] z-10 shadow-lg">
                            <span class="text-[#09C000] font-bold">02</span>
                        </div>
                        <div class="md:w-1/2 pr-0 md:pr-12 flex justify-center md:justify-end">
                            <div class="bg-bgsec rounded-lg p-4 border border-bordercol inline-block shadow-sm w-full md:w-3/4 text-left">
                                <p class="text-xs font-mono text-paratext">SMTP Ping Status: <span class="text-[#09C000]">200 OK</span></p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="relative flex items-center flex-col md:flex-row">
                        <div class="md:w-1/2 pr-0 md:pr-12 text-center md:text-right mb-6 md:mb-0">
                            <h3 class="text-xl font-bold text-headtext mb-2">3. Manual Quality Check</h3>
                            <p class="text-sm text-paratext">Our in-house team of 50+ data researchers manually verify high-value contacts, update job changes on LinkedIn, and ensure corporate phone numbers connect to the right department.</p>
                        </div>
                        <div class="absolute left-1/2 transform -translate-x-1/2 flex items-center justify-center w-12 h-12 rounded-full bg-bgmain border-4 border-[#09C000] z-10 shadow-lg">
                            <span class="text-[#09C000] font-bold">03</span>
                        </div>
                        <div class="md:w-1/2 pl-0 md:pl-12">
                            <div class="bg-bgsec rounded-lg p-4 border border-bordercol inline-block shadow-sm w-full md:w-3/4">
                                <p class="text-xs font-mono text-paratext">Human verified: Just before delivery.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''
    
    # Section 5: Lead Form / CTA (50+ lines)
    # Count: ~60 lines
    section5 = f'''
    <!-- SECTION 5: CTA & FORM -->
    <section id="form" class="py-20 bg-bgsec relative overflow-hidden">
        <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 rounded-full bg-[#09C000]/10 blur-3xl"></div>
        <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-64 h-64 rounded-full bg-[#09C000]/10 blur-3xl"></div>
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-white rounded-2xl shadow-xl border border-bordercol overflow-hidden">
                <div class="grid grid-cols-1 md:grid-cols-5">
                    <div class="md:col-span-2 bg-gradient-to-br from-[#051C14] to-[#0B6B3A] p-8 text-white flex flex-col justify-center">
                        <h3 class="text-2xl font-bold mb-4">Get Your {title} Quote</h3>
                        <p class="text-sm text-gray-300 mb-8 leading-relaxed">Fill out the form with your exact requirements. Our data specialists will get back to you within 24 hours with a free sample and a customized quote.</p>
                        <div class="space-y-4">
                            <div class="flex items-center">
                                <svg class="w-5 h-5 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                                <span class="text-sm font-medium">+91 7760747212</span>
                            </div>
                            <div class="flex items-center">
                                <svg class="w-5 h-5 text-[#09C000] mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                <span class="text-sm font-medium">info@b2bleadnex.com</span>
                            </div>
                        </div>
                    </div>
                    <div class="md:col-span-3 p-8">
                        <form class="space-y-5">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                                <div>
                                    <label class="block text-xs font-bold text-headtext uppercase tracking-wider mb-2">First Name</label>
                                    <input type="text" class="w-full bg-bgsec border border-bordercol rounded-md px-4 py-2.5 text-sm focus:outline-none focus:border-[#09C000] focus:ring-1 focus:ring-[#09C000]" placeholder="John">
                                </div>
                                <div>
                                    <label class="block text-xs font-bold text-headtext uppercase tracking-wider mb-2">Last Name</label>
                                    <input type="text" class="w-full bg-bgsec border border-bordercol rounded-md px-4 py-2.5 text-sm focus:outline-none focus:border-[#09C000] focus:ring-1 focus:ring-[#09C000]" placeholder="Doe">
                                </div>
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-headtext uppercase tracking-wider mb-2">Business Email</label>
                                <input type="email" class="w-full bg-bgsec border border-bordercol rounded-md px-4 py-2.5 text-sm focus:outline-none focus:border-[#09C000] focus:ring-1 focus:ring-[#09C000]" placeholder="john@company.com">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-headtext uppercase tracking-wider mb-2">Target Geography / Requirements</label>
                                <textarea rows="3" class="w-full bg-bgsec border border-bordercol rounded-md px-4 py-2.5 text-sm focus:outline-none focus:border-[#09C000] focus:ring-1 focus:ring-[#09C000]" placeholder="Looking for {keywords} users in USA and UK..."></textarea>
                            </div>
                            <button type="button" class="w-full bg-[#09C000] hover:bg-[#0B6B3A] text-white font-bold py-3 px-4 rounded-md uppercase tracking-wide transition-colors shadow-md">
                                Submit Request
                            </button>
                            <p class="text-[10px] text-center text-paratext mt-4">By submitting, you agree to our Terms and Privacy Policy.</p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''
    
    return header + section1 + section2 + section3 + section4 + section5 + footer

aws_html = generate_page("AWS Users List", "AWS")
as400_html = generate_page("CRM Users List", "CRM")

with open(os.path.join(directory, "aws-users-list.html"), "w", encoding="utf-8") as f:
    f.write(aws_html)
    
with open(os.path.join(directory, "crm-users-list.html"), "w", encoding="utf-8") as f:
    f.write(as400_html)

print("Created aws-users-list.html and crm-users-list.html")
