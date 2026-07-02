import os

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
index_file = os.path.join(directory, "index.html")

with open(index_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the insertion point (line 251 is index 250 in 0-based array)
# It's right after </section> at line 250.
insertion_index = 0
for i, line in enumerate(lines):
    if "<!-- Replaced Sections End -->" in line:
        insertion_index = i
        break

if insertion_index == 0:
    print("Could not find insertion point.")
    exit(1)

# Section 1: Trusted By (50+ lines) -> Target: ~60 lines
section1 = """
    <!-- SECTION 1: TRUSTED BY (50+ lines) -->
    <section class="py-12 bg-bgsec border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <p class="text-center text-sm font-bold tracking-widest text-paratext uppercase mb-8">Trusted by industry leaders worldwide</p>
            <div class="flex flex-wrap justify-center items-center gap-8 md:gap-16 opacity-60 hover:opacity-100 transition-opacity duration-500">
                <div class="flex items-center justify-center w-32 h-12 grayscale hover:grayscale-0 transition-all duration-300">
                    <svg class="w-full h-8 text-headtext" viewBox="0 0 100 30" fill="currentColor">
                        <rect x="0" y="5" width="20" height="20" rx="4" />
                        <text x="30" y="22" font-size="20" font-weight="bold">Acme Corp</text>
                    </svg>
                </div>
                <div class="flex items-center justify-center w-32 h-12 grayscale hover:grayscale-0 transition-all duration-300">
                    <svg class="w-full h-8 text-headtext" viewBox="0 0 100 30" fill="currentColor">
                        <circle cx="15" cy="15" r="10" />
                        <text x="35" y="22" font-size="20" font-weight="bold">GlobalNet</text>
                    </svg>
                </div>
                <div class="flex items-center justify-center w-32 h-12 grayscale hover:grayscale-0 transition-all duration-300">
                    <svg class="w-full h-8 text-headtext" viewBox="0 0 100 30" fill="currentColor">
                        <polygon points="10,25 20,5 30,25" />
                        <text x="40" y="22" font-size="20" font-weight="bold">VertexTech</text>
                    </svg>
                </div>
                <div class="flex items-center justify-center w-32 h-12 grayscale hover:grayscale-0 transition-all duration-300">
                    <svg class="w-full h-8 text-headtext" viewBox="0 0 100 30" fill="currentColor">
                        <path d="M5,15 Q15,5 25,15 T45,15" fill="none" stroke="currentColor" stroke-width="4"/>
                        <text x="55" y="22" font-size="20" font-weight="bold">FlowData</text>
                    </svg>
                </div>
                <div class="flex items-center justify-center w-32 h-12 grayscale hover:grayscale-0 transition-all duration-300">
                    <svg class="w-full h-8 text-headtext" viewBox="0 0 100 30" fill="currentColor">
                        <rect x="5" y="5" width="10" height="20" />
                        <rect x="20" y="5" width="10" height="20" />
                        <text x="40" y="22" font-size="20" font-weight="bold">TwinSoft</text>
                    </svg>
                </div>
            </div>
            
            <div class="mt-16 bg-bgmain rounded-2xl p-8 border border-bordercol shadow-sm max-w-4xl mx-auto relative">
                <div class="absolute -top-6 left-1/2 transform -translate-x-1/2">
                    <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center border-4 border-bgsec">
                        <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
                    </div>
                </div>
                <div class="text-center pt-6">
                    <p class="text-lg md:text-xl text-headtext font-medium leading-relaxed mb-6">"B2BLeadNex transformed our outbound strategy. We saw a 300% increase in meeting booked within the first month. The accuracy of their data is completely unmatched in the industry."</p>
                    <div class="flex flex-col items-center">
                        <h4 class="font-bold text-primary">Sarah Jenkins</h4>
                        <p class="text-sm text-paratext">VP of Sales, TechGrowth Solutions</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Section 2: Features Grid (70+ lines) -> Target: ~85 lines
section2 = """
    <!-- SECTION 2: FEATURES GRID (70+ lines) -->
    <section class="py-24 bg-bgmain border-b border-bordercol relative overflow-hidden">
        <div class="absolute top-0 right-0 -mr-20 -mt-20 w-72 h-72 rounded-full bg-primary/5 blur-3xl"></div>
        <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-72 h-72 rounded-full bg-primary/5 blur-3xl"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block">The B2BLeadNex Advantage</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Why our data converts better</h2>
                <p class="text-paratext text-lg">We don't just scrape the web. We aggregate, clean, and verify data through a multi-step human-in-the-loop process.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Feature 1 -->
                <div class="bg-bgsec rounded-2xl p-8 border border-bordercol hover:border-primary/50 transition-colors group">
                    <div class="w-14 h-14 bg-bgmain rounded-xl flex items-center justify-center border border-bordercol mb-6 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">99% Delivery Guarantee</h3>
                    <p class="text-paratext text-sm mb-4 leading-relaxed">Every email address is SMTP pinged in real-time just before delivery. If more than 1% bounces, we replace those credits instantly.</p>
                    <ul class="space-y-2 text-xs font-medium text-headtext">
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Live Server Ping</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Catch-All Resolution</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Spam Trap Removal</li>
                    </ul>
                </div>
                
                <!-- Feature 2 -->
                <div class="bg-bgsec rounded-2xl p-8 border border-bordercol hover:border-primary/50 transition-colors group">
                    <div class="w-14 h-14 bg-bgmain rounded-xl flex items-center justify-center border border-bordercol mb-6 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Hyper-Targeted Filters</h3>
                    <p class="text-paratext text-sm mb-4 leading-relaxed">Filter your lists using 50+ data points including tech stack, revenue, employee count, recent funding, and precise job titles.</p>
                    <ul class="space-y-2 text-xs font-medium text-headtext">
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Technographic Data</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Firmographic Details</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Intent Signals</li>
                    </ul>
                </div>
                
                <!-- Feature 3 -->
                <div class="bg-bgsec rounded-2xl p-8 border border-bordercol hover:border-primary/50 transition-colors group">
                    <div class="w-14 h-14 bg-bgmain rounded-xl flex items-center justify-center border border-bordercol mb-6 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Direct Mobile Dials</h3>
                    <p class="text-paratext text-sm mb-4 leading-relaxed">Reach decision makers directly at their desk or mobile. Our tele-verification team constantly calls and updates numbers.</p>
                    <ul class="space-y-2 text-xs font-medium text-headtext">
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Direct Mobile Lines</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> HQ & Switchboard</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Global Dialing Codes</li>
                    </ul>
                </div>
                
                <!-- Feature 4 -->
                <div class="bg-bgsec rounded-2xl p-8 border border-bordercol hover:border-primary/50 transition-colors group">
                    <div class="w-14 h-14 bg-bgmain rounded-xl flex items-center justify-center border border-bordercol mb-6 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Data Enrichment</h3>
                    <p class="text-paratext text-sm mb-4 leading-relaxed">Upload your stale CRM lists and we will append missing emails, update changed jobs, and fill in revenue data instantly.</p>
                    <ul class="space-y-2 text-xs font-medium text-headtext">
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> CSV / Excel Upload</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Match & Append</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Job Title Updates</li>
                    </ul>
                </div>
                
                <!-- Feature 5 -->
                <div class="bg-bgsec rounded-2xl p-8 border border-bordercol hover:border-primary/50 transition-colors group">
                    <div class="w-14 h-14 bg-bgmain rounded-xl flex items-center justify-center border border-bordercol mb-6 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">100% Compliant Data</h3>
                    <p class="text-paratext text-sm mb-4 leading-relaxed">Our databases strictly follow global privacy laws, meaning your campaigns run smoothly without blacklisting risks.</p>
                    <ul class="space-y-2 text-xs font-medium text-headtext">
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> GDPR Compliant</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> CCPA Compliant</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> CAN-SPAM Certified</li>
                    </ul>
                </div>
                
                <!-- Feature 6 -->
                <div class="bg-bgsec rounded-2xl p-8 border border-bordercol hover:border-primary/50 transition-colors group">
                    <div class="w-14 h-14 bg-bgmain rounded-xl flex items-center justify-center border border-bordercol mb-6 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-headtext mb-3">Custom CRM Formats</h3>
                    <p class="text-paratext text-sm mb-4 leading-relaxed">Get your data delivered exactly how you need it. We format exports to map seamlessly with Salesforce, HubSpot, or Outreach.</p>
                    <ul class="space-y-2 text-xs font-medium text-headtext">
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> CRM Ready Files</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Easy API Integration</li>
                        <li class="flex items-center"><svg class="w-4 h-4 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Custom Headers</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

# Section 3: Interactive UI Preview (70+ lines) -> Target: ~75 lines
section3 = """
    <!-- SECTION 3: HOW IT WORKS / UI MOCKUP (70+ lines) -->
    <section class="py-24 bg-bgsec border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="lg:grid lg:grid-cols-2 gap-16 items-center">
                <div class="mb-16 lg:mb-0">
                    <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block">The Platform</span>
                    <h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-6 leading-tight">Data Intelligence at your fingertips</h2>
                    <p class="text-paratext text-lg mb-8 leading-relaxed">
                        Requesting highly specific, verified lists has never been easier. Our platform maps the global B2B ecosystem.
                    </p>
                    
                    <div class="space-y-8">
                        <div class="flex">
                            <div class="flex-shrink-0 mt-1">
                                <div class="w-8 h-8 rounded-full bg-btnbg text-btntext flex items-center justify-center font-bold text-sm">1</div>
                            </div>
                            <div class="ml-4">
                                <h4 class="text-lg font-bold text-headtext mb-1">Define your ICP</h4>
                                <p class="text-sm text-paratext">Tell us exactly who you want to target using our 50+ data filters including NAICS codes, tech installs, and job functions.</p>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 mt-1">
                                <div class="w-8 h-8 rounded-full bg-btnbg text-btntext flex items-center justify-center font-bold text-sm">2</div>
                            </div>
                            <div class="ml-4">
                                <h4 class="text-lg font-bold text-headtext mb-1">AI & Human Verification</h4>
                                <p class="text-sm text-paratext">Our systems pull the raw data, run it through AI syntax checks, and our QA team manually verifies critical records.</p>
                            </div>
                        </div>
                        <div class="flex">
                            <div class="flex-shrink-0 mt-1">
                                <div class="w-8 h-8 rounded-full bg-btnbg text-btntext flex items-center justify-center font-bold text-sm">3</div>
                            </div>
                            <div class="ml-4">
                                <h4 class="text-lg font-bold text-headtext mb-1">Download & Launch</h4>
                                <p class="text-sm text-paratext">Receive your clean list in a CRM-ready format, fully compliant and ready for your outbound sales team.</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-10">
                        <a href="contact-us.html" class="inline-flex items-center text-primary font-bold hover:text-hovercol transition-colors">
                            Build Your List Now <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                        </a>
                    </div>
                </div>
                
                <div class="relative">
                    <!-- Fake UI Mockup -->
                    <div class="bg-bgmain rounded-xl shadow-2xl border border-bordercol overflow-hidden transform rotate-2 hover:rotate-0 transition-transform duration-500">
                        <div class="bg-bgsec border-b border-bordercol p-3 flex items-center justify-between">
                            <div class="flex space-x-2">
                                <div class="w-3 h-3 rounded-full bg-red-400"></div>
                                <div class="w-3 h-3 rounded-full bg-yellow-400"></div>
                                <div class="w-3 h-3 rounded-full bg-green-400"></div>
                            </div>
                            <div class="text-xs text-paratext font-mono">B2BLeadNex Dashboard</div>
                        </div>
                        <div class="p-6">
                            <div class="flex items-center justify-between border-b border-bordercol pb-4 mb-4">
                                <div class="font-bold text-headtext">List Builder</div>
                                <div class="bg-primary/10 text-primary text-xs px-3 py-1 rounded-full font-bold">52,481 Contacts Found</div>
                            </div>
                            
                            <div class="space-y-4">
                                <div class="flex justify-between items-center bg-bgsec p-3 rounded border border-bordercol">
                                    <span class="text-sm text-headtext font-medium">Industry: Software (NAICS 5112)</span>
                                    <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                </div>
                                <div class="flex justify-between items-center bg-bgsec p-3 rounded border border-bordercol">
                                    <span class="text-sm text-headtext font-medium">Job Title: CTO, VP of Engineering</span>
                                    <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                </div>
                                <div class="flex justify-between items-center bg-bgsec p-3 rounded border border-bordercol">
                                    <span class="text-sm text-headtext font-medium">Company Size: 500 - 1000</span>
                                    <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                </div>
                            </div>
                            
                            <div class="mt-6 pt-4 border-t border-bordercol flex justify-between items-center">
                                <div class="text-xs text-paratext">Est. Match Rate: 99%</div>
                                <div class="bg-btnbg text-btntext px-4 py-2 rounded text-xs font-bold cursor-pointer hover:bg-btnbg/80">Export to CRM</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="absolute -bottom-6 -left-6 bg-white dark:bg-gray-800 p-4 rounded-xl shadow-xl border border-gray-100 dark:border-gray-700 flex items-center space-x-4 animate-bounce">
                        <div class="w-10 h-10 bg-green-100 dark:bg-green-900 rounded-full flex items-center justify-center text-green-600 dark:text-green-400">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        </div>
                        <div>
                            <div class="text-sm font-bold text-gray-900 dark:text-white">List Generated</div>
                            <div class="text-xs text-gray-500 dark:text-gray-400">2 seconds ago</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Section 4: Statistics Grid (70+ lines) -> Target: ~80 lines
section4 = """
    <!-- SECTION 4: DATA COVERAGE GRID (70+ lines) -->
    <section class="py-24 bg-bgmain border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block">Global Coverage</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Unmatched Database Scale</h2>
                <p class="text-paratext text-lg max-w-2xl mx-auto">We maintain the most accurate B2B contact graph in the world, constantly updating across millions of corporate nodes.</p>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-px bg-bordercol border border-bordercol rounded-2xl overflow-hidden">
                <div class="bg-bgmain p-8 flex flex-col items-center justify-center text-center hover:bg-bgsec transition-colors cursor-default">
                    <svg class="w-8 h-8 text-primary mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                    <div class="text-3xl font-extrabold text-headtext mb-2">52M+</div>
                    <div class="text-sm font-medium text-paratext">B2B Contacts</div>
                </div>
                <div class="bg-bgmain p-8 flex flex-col items-center justify-center text-center hover:bg-bgsec transition-colors cursor-default">
                    <svg class="w-8 h-8 text-primary mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    <div class="text-3xl font-extrabold text-headtext mb-2">12M+</div>
                    <div class="text-sm font-medium text-paratext">Companies</div>
                </div>
                <div class="bg-bgmain p-8 flex flex-col items-center justify-center text-center hover:bg-bgsec transition-colors cursor-default">
                    <svg class="w-8 h-8 text-primary mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                    <div class="text-3xl font-extrabold text-headtext mb-2">18M+</div>
                    <div class="text-sm font-medium text-paratext">Direct Dials</div>
                </div>
                <div class="bg-bgmain p-8 flex flex-col items-center justify-center text-center hover:bg-bgsec transition-colors cursor-default">
                    <svg class="w-8 h-8 text-primary mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
                    <div class="text-3xl font-extrabold text-headtext mb-2">150+</div>
                    <div class="text-sm font-medium text-paratext">Countries</div>
                </div>
            </div>
            
            <div class="mt-16 flex flex-col md:flex-row items-center justify-between bg-bgsec border border-bordercol rounded-xl p-8 shadow-sm">
                <div class="mb-6 md:mb-0">
                    <h3 class="text-xl font-bold text-headtext mb-2">Need a very specific niche?</h3>
                    <p class="text-paratext text-sm max-w-xl">From "Cloud Architects in Seattle" to "CFOs of manufacturing companies over $50M revenue", we can pull it.</p>
                </div>
                <div>
                    <a href="contact-us.html" class="inline-block bg-btnbg hover:bg-btnbg/80 text-btntext font-bold px-8 py-3 rounded text-sm transition-colors uppercase tracking-wider">Talk to a Data Expert</a>
                </div>
            </div>
        </div>
    </section>
"""

# Section 5: FAQ (50+ lines) -> Target: ~60 lines
section5 = """
    <!-- SECTION 5: FAQ (50+ lines) -->
    <section class="py-24 bg-bgsec border-b border-bordercol">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Frequently Asked Questions</h2>
                <p class="text-paratext text-lg">Everything you need to know about our data quality and delivery process.</p>
            </div>
            
            <div class="space-y-4">
                <details class="group bg-bgmain rounded-lg border border-bordercol p-6 cursor-pointer open:bg-bgsec transition-colors">
                    <summary class="flex justify-between items-center font-bold text-headtext text-lg list-none [&::-webkit-details-marker]:hidden">
                        What is your data accuracy guarantee?
                        <svg class="w-5 h-5 text-primary transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <p class="mt-4 text-paratext text-sm leading-relaxed">We guarantee a minimum of 95% deliverability on all our email data. We run all exports through a final real-time SMTP ping process. If you experience a hard bounce rate higher than 5%, we will gladly replace those bad contacts for free.</p>
                </details>
                
                <details class="group bg-bgmain rounded-lg border border-bordercol p-6 cursor-pointer open:bg-bgsec transition-colors">
                    <summary class="flex justify-between items-center font-bold text-headtext text-lg list-none [&::-webkit-details-marker]:hidden">
                        In what format will I receive the data?
                        <svg class="w-5 h-5 text-primary transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <p class="mt-4 text-paratext text-sm leading-relaxed">Your data will be delivered via a secure download link in .CSV or .XLSX format. The file is structured to be easily imported into any major CRM or marketing automation platform like Salesforce, HubSpot, or Outreach.</p>
                </details>
                
                <details class="group bg-bgmain rounded-lg border border-bordercol p-6 cursor-pointer open:bg-bgsec transition-colors">
                    <summary class="flex justify-between items-center font-bold text-headtext text-lg list-none [&::-webkit-details-marker]:hidden">
                        Is your data GDPR and CCPA compliant?
                        <svg class="w-5 h-5 text-primary transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <p class="mt-4 text-paratext text-sm leading-relaxed">Yes, entirely. We strictly adhere to the General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA). We provide only business-to-business (B2B) contact information and include necessary opt-out mechanisms in our sourcing.</p>
                </details>
                
                <details class="group bg-bgmain rounded-lg border border-bordercol p-6 cursor-pointer open:bg-bgsec transition-colors">
                    <summary class="flex justify-between items-center font-bold text-headtext text-lg list-none [&::-webkit-details-marker]:hidden">
                        Can you enrich my existing CRM data?
                        <svg class="w-5 h-5 text-primary transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </summary>
                    <p class="mt-4 text-paratext text-sm leading-relaxed">Absolutely. Our Data Appending service allows you to upload your stale lists. We will match your records against our master database, fill in missing emails and phone numbers, update job titles, and remove contacts who have left their companies.</p>
                </details>
            </div>
        </div>
    </section>
"""

new_content = section1 + section2 + section3 + section4 + section5

lines.insert(insertion_index, new_content)

with open(index_file, "w", encoding="utf-8") as f:
    f.write("".join(lines))

print("Successfully injected 5 sections into index.html")
