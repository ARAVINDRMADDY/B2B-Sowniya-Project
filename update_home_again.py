import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
index_file = os.path.join(directory, "index.html")

with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()

# --- 1. Redesign Hero Section ---
# The hero section starts at `<section class="relative bg-bgmain overflow-hidden py-20 lg:py-32 border-b border-bordercol">`
# and ends at the next `</section>`.
hero_start = content.find('<section class="relative bg-bgmain overflow-hidden py-20 lg:py-32 border-b border-bordercol">')
hero_end = content.find('</section>', hero_start) + len('</section>')

new_hero = """
    <!-- BEAUTIFUL HERO SECTION -->
    <section class="relative bg-black overflow-hidden py-24 lg:py-36 border-b border-bordercol">
        <!-- Stunning Background Image & Overlay -->
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop" alt="Hero Background" class="w-full h-full object-cover opacity-40 mix-blend-luminosity">
            <div class="absolute inset-0 bg-gradient-to-r from-black via-[#051C14]/90 to-[#09C000]/30"></div>
            <!-- Glowing Orbs -->
            <div class="absolute top-0 right-0 -mt-20 -mr-20 w-[500px] h-[500px] bg-[#09C000]/20 rounded-full blur-[100px] animate-pulse"></div>
            <div class="absolute bottom-0 left-0 -mb-20 -ml-20 w-[400px] h-[400px] bg-[#0B6B3A]/30 rounded-full blur-[100px]"></div>
        </div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="lg:grid lg:grid-cols-12 lg:gap-16 items-center">
                <div class="lg:col-span-6 text-center lg:text-left mb-16 lg:mb-0">
                    <div class="inline-flex items-center px-4 py-2 rounded-full bg-white/5 border border-white/10 text-white font-semibold text-xs uppercase tracking-widest mb-6 backdrop-blur-md">
                        <span class="flex w-2 h-2 rounded-full bg-[#09C000] mr-2 animate-pulse shadow-[0_0_8px_#09C000]"></span>
                        Next-Gen B2B Intelligence Live
                    </div>
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white tracking-tight leading-tight mb-6 drop-shadow-lg">
                        Fuel Your Pipeline With <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#09C000] to-green-300">Precision Data</span>
                    </h1>
                    <p class="text-lg text-gray-300 mb-8 max-w-2xl mx-auto lg:mx-0 leading-relaxed">
                        Access over 50 million highly verified B2B contacts. Stop guessing and start closing with direct dials, verified emails, and deep firmographic data.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
                        <a href="#form" class="bg-[#09C000] text-white px-8 py-4 rounded-md font-bold text-sm hover:bg-[#0B6B3A] transition-colors shadow-[0_0_20px_rgba(9,192,0,0.4)] flex justify-center items-center group">
                            Start Your Free Trial
                            <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                        <a href="pricing.html" class="bg-transparent text-white border-2 border-white/20 px-8 py-4 rounded-md font-bold text-sm hover:bg-white hover:text-black transition-colors flex justify-center items-center">
                            View Pricing
                        </a>
                    </div>
                    <div class="mt-10 flex items-center justify-center lg:justify-start space-x-4 text-sm text-gray-400 font-medium">
                        <span class="flex items-center"><svg class="w-4 h-4 text-[#09C000] mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> No credit card required</span>
                        <span class="flex items-center"><svg class="w-4 h-4 text-[#09C000] mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Cancel anytime</span>
                    </div>
                </div>
                
                <div class="lg:col-span-6 relative">
                    <!-- Glassmorphism Dashboard Mockup -->
                    <div class="relative bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.5)] overflow-hidden transform transition hover:-translate-y-2 duration-500 group">
                        <div class="h-12 bg-black/40 border-b border-white/10 flex items-center px-4 justify-between backdrop-blur-md">
                            <div class="flex space-x-2">
                                <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
                                <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
                                <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
                            </div>
                            <div class="text-xs text-white/50 font-mono tracking-widest">B2BLEADNEX_ENGINE_V2</div>
                        </div>
                        <div class="p-6 grid grid-cols-2 gap-4">
                            <!-- Chart -->
                            <div class="col-span-2 bg-black/30 rounded-xl p-5 border border-white/5 h-48 flex items-end space-x-2 relative overflow-hidden">
                                <div class="absolute inset-0 bg-gradient-to-t from-[#09C000]/10 to-transparent"></div>
                                <div class="w-full bg-[#09C000]/40 rounded-t h-[30%] hover:bg-[#09C000]/60 transition-colors relative z-10"></div>
                                <div class="w-full bg-[#09C000]/40 rounded-t h-[50%] hover:bg-[#09C000]/60 transition-colors relative z-10"></div>
                                <div class="w-full bg-[#09C000]/40 rounded-t h-[40%] hover:bg-[#09C000]/60 transition-colors relative z-10"></div>
                                <div class="w-full bg-[#09C000]/40 rounded-t h-[70%] hover:bg-[#09C000]/60 transition-colors relative z-10"></div>
                                <div class="w-full bg-[#09C000] rounded-t h-[90%] shadow-[0_0_15px_#09C000] relative z-10">
                                    <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 text-xs font-bold text-white bg-black px-2 py-1 rounded border border-white/10">99.8%</div>
                                </div>
                                <div class="w-full bg-[#09C000]/40 rounded-t h-[85%] hover:bg-[#09C000]/60 transition-colors relative z-10"></div>
                            </div>
                            <!-- Stats Cards -->
                            <div class="bg-black/30 rounded-xl p-5 border border-white/5 flex flex-col justify-center">
                                <span class="text-gray-400 text-xs font-bold uppercase tracking-wider mb-1">Total Verified</span>
                                <span class="text-2xl font-extrabold text-white">52,481,093</span>
                                <span class="text-xs text-[#09C000] mt-1 flex items-center font-medium"><svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg> +12.4% this week</span>
                            </div>
                            <div class="bg-black/30 rounded-xl p-5 border border-white/5 flex flex-col justify-center">
                                <span class="text-gray-400 text-xs font-bold uppercase tracking-wider mb-1">Active Queries</span>
                                <span class="text-2xl font-extrabold text-white">1,402</span>
                                <span class="text-xs text-[#09C000] mt-1 flex items-center font-medium animate-pulse"><span class="w-2 h-2 bg-[#09C000] rounded-full mr-1.5 shadow-[0_0_5px_#09C000]"></span> Live searching...</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Floating Mini Card -->
                    <div class="absolute -bottom-6 -right-6 bg-white p-4 rounded-xl shadow-2xl border border-gray-100 flex items-center space-x-4 animate-bounce hidden sm:flex z-20">
                        <div class="flex -space-x-2">
                            <img class="w-8 h-8 rounded-full border-2 border-white" src="https://i.pravatar.cc/100?img=1" alt="User">
                            <img class="w-8 h-8 rounded-full border-2 border-white" src="https://i.pravatar.cc/100?img=2" alt="User">
                            <img class="w-8 h-8 rounded-full border-2 border-white" src="https://i.pravatar.cc/100?img=3" alt="User">
                        </div>
                        <div>
                            <div class="text-xs font-bold text-gray-900">10k+ Sales Teams</div>
                            <div class="text-[10px] text-gray-500">Trust B2BLeadNex</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

content = content[:hero_start] + new_hero + content[hero_end:]

# --- 2. Inject 3 New Sections ---
# We'll inject them right after the newly placed hero section.
# We find the end of the new hero section.
new_hero_end = content.find('</section>', content.find('<!-- BEAUTIFUL HERO SECTION -->')) + len('</section>')

# Section A: Target Profiles (Grid) -> Target: ~60 lines
section_A = """
    <!-- SECTION A: TARGET PROFILES -->
    <section class="py-24 bg-bgsec border-b border-bordercol">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-end mb-12">
                <div class="max-w-2xl">
                    <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block">Target precision</span>
                    <h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Who do you want to reach?</h2>
                    <p class="text-paratext text-lg">Build lists based on exact buyer personas. We have mapped out entire organizational charts for Fortune 500s down to agile startups.</p>
                </div>
                <div class="mt-6 md:mt-0">
                    <a href="professionals-data-list.html" class="inline-flex items-center text-primary font-bold hover:text-hovercol transition-colors border-b-2 border-primary pb-1">
                        View All Categories <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Profile 1 -->
                <a href="ceo-list.html" class="bg-bgmain border border-bordercol rounded-xl p-6 hover:shadow-lg hover:border-primary transition-all group">
                    <div class="w-12 h-12 bg-bgsec rounded-full flex items-center justify-center mb-4 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    </div>
                    <h3 class="text-lg font-bold text-headtext mb-2">C-Suite & Founders</h3>
                    <p class="text-sm text-paratext mb-4">CEOs, Founders, Presidents, and Managing Directors.</p>
                    <span class="text-xs font-bold text-primary">2.4M+ Contacts &rarr;</span>
                </a>
                
                <!-- Profile 2 -->
                <a href="technology-list.html" class="bg-bgmain border border-bordercol rounded-xl p-6 hover:shadow-lg hover:border-primary transition-all group">
                    <div class="w-12 h-12 bg-bgsec rounded-full flex items-center justify-center mb-4 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 class="text-lg font-bold text-headtext mb-2">IT & Engineering</h3>
                    <p class="text-sm text-paratext mb-4">CTOs, CIOs, VP of Engineering, Developers, and DevOps.</p>
                    <span class="text-xs font-bold text-primary">8.1M+ Contacts &rarr;</span>
                </a>
                
                <!-- Profile 3 -->
                <a href="cmo-list.html" class="bg-bgmain border border-bordercol rounded-xl p-6 hover:shadow-lg hover:border-primary transition-all group">
                    <div class="w-12 h-12 bg-bgsec rounded-full flex items-center justify-center mb-4 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"></path></svg>
                    </div>
                    <h3 class="text-lg font-bold text-headtext mb-2">Marketing & Sales</h3>
                    <p class="text-sm text-paratext mb-4">CMOs, VP of Sales, SDR Managers, and Growth Leads.</p>
                    <span class="text-xs font-bold text-primary">6.5M+ Contacts &rarr;</span>
                </a>
                
                <!-- Profile 4 -->
                <a href="cfo-list.html" class="bg-bgmain border border-bordercol rounded-xl p-6 hover:shadow-lg hover:border-primary transition-all group">
                    <div class="w-12 h-12 bg-bgsec rounded-full flex items-center justify-center mb-4 group-hover:bg-primary/10 transition-colors">
                        <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 class="text-lg font-bold text-headtext mb-2">Finance & Ops</h3>
                    <p class="text-sm text-paratext mb-4">CFOs, COOs, VP of Finance, HR Directors, and Controllers.</p>
                    <span class="text-xs font-bold text-primary">4.2M+ Contacts &rarr;</span>
                </a>
            </div>
        </div>
    </section>
"""

# Section B: Data Enrichment Visual (Timeline/Process) -> Target: ~70 lines
section_B = """
    <!-- SECTION B: DATA ENRICHMENT PROCESS -->
    <section class="py-24 bg-bgmain border-b border-bordercol overflow-hidden relative">
        <div class="absolute right-0 top-1/2 transform -translate-y-1/2 w-1/3 h-full bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10 pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-primary font-bold tracking-widest uppercase text-sm mb-4 block">Data Enrichment</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-headtext mb-4">Turn Stale CRM Data into Gold</h2>
                <p class="text-paratext text-lg">Upload your outdated lists and let our AI engine fill in the blanks. We append missing emails, direct dials, and update job titles instantly.</p>
            </div>
            
            <div class="flex flex-col lg:flex-row items-center justify-center gap-8">
                <!-- Stale Data -->
                <div class="w-full lg:w-5/12 bg-bgsec border border-bordercol rounded-xl p-6 shadow-inner">
                    <div class="flex items-center mb-4">
                        <div class="w-3 h-3 rounded-full bg-red-500 mr-2"></div>
                        <h4 class="font-bold text-headtext">Your CRM (Before)</h4>
                    </div>
                    <div class="space-y-3 font-mono text-xs opacity-70">
                        <div class="p-3 bg-bgmain rounded border border-red-500/30 text-paratext flex justify-between">
                            <span>John Doe | Acme Corp</span>
                            <span class="text-red-500">Missing Email</span>
                        </div>
                        <div class="p-3 bg-bgmain rounded border border-red-500/30 text-paratext flex justify-between">
                            <span>Sarah Jenkins | TechGrowth</span>
                            <span class="text-red-500">Invalid Phone</span>
                        </div>
                        <div class="p-3 bg-bgmain rounded border border-red-500/30 text-paratext flex justify-between">
                            <span>Mike Ross | Specter Inc</span>
                            <span class="text-red-500">Job Changed</span>
                        </div>
                    </div>
                </div>
                
                <!-- The Engine Arrow -->
                <div class="hidden lg:flex flex-col items-center justify-center w-2/12">
                    <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center shadow-lg shadow-primary/30 animate-pulse z-10">
                        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    </div>
                    <div class="w-full h-1 bg-gradient-to-r from-transparent via-primary to-transparent -mt-6"></div>
                </div>
                <div class="lg:hidden flex justify-center py-4">
                    <svg class="w-8 h-8 text-primary animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
                </div>
                
                <!-- Enriched Data -->
                <div class="w-full lg:w-5/12 bg-bgsec border-2 border-primary rounded-xl p-6 shadow-[0_0_30px_rgba(9,192,0,0.1)] relative">
                    <div class="absolute -top-3 -right-3 bg-primary text-white text-xs font-bold px-3 py-1 rounded-full shadow-md">100% Match</div>
                    <div class="flex items-center mb-4">
                        <div class="w-3 h-3 rounded-full bg-primary mr-2"></div>
                        <h4 class="font-bold text-headtext">Enriched (After)</h4>
                    </div>
                    <div class="space-y-3 font-mono text-xs">
                        <div class="p-3 bg-bgmain rounded border border-primary/30 text-headtext flex flex-col">
                            <div class="flex justify-between mb-1"><span>John Doe | VP Sales</span><span class="text-primary font-bold">100% Valid</span></div>
                            <div class="text-paratext">john@acmecorp.com | +1 (555) 019-2831</div>
                        </div>
                        <div class="p-3 bg-bgmain rounded border border-primary/30 text-headtext flex flex-col">
                            <div class="flex justify-between mb-1"><span>Sarah Jenkins | CEO</span><span class="text-primary font-bold">100% Valid</span></div>
                            <div class="text-paratext">s.jenkins@techgrowth.io | +1 (555) 912-8822</div>
                        </div>
                        <div class="p-3 bg-bgmain rounded border border-primary/30 text-headtext flex flex-col">
                            <div class="flex justify-between mb-1"><span>Mike Ross | Partner</span><span class="text-primary font-bold">Updated Role</span></div>
                            <div class="text-paratext">mike.r@specterlaw.com | +1 (555) 332-9911</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="text-center mt-12">
                <a href="contact-us.html" class="inline-block bg-btnbg text-btntext px-8 py-3 rounded text-sm font-bold shadow-md hover:bg-btnbg/80 transition-colors uppercase tracking-wider">Try Data Enrichment</a>
            </div>
        </div>
    </section>
"""

# Section C: Advanced Data Search CTA (Large Banner) -> Target: ~50 lines
section_C = """
    <!-- SECTION C: ADVANCED SEARCH BANNER -->
    <section class="py-24 relative overflow-hidden bg-[#051C14]">
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop" class="w-full h-full object-cover opacity-20 mix-blend-screen" alt="Network Background">
            <div class="absolute inset-0 bg-gradient-to-t from-[#051C14] via-transparent to-[#051C14]"></div>
        </div>
        
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center text-white border border-white/10 bg-black/40 backdrop-blur-md rounded-3xl p-10 md:p-16 shadow-2xl">
            <div class="w-16 h-16 bg-[#09C000]/20 rounded-full flex items-center justify-center mx-auto mb-6 border border-[#09C000]/50 shadow-[0_0_15px_#09C000]">
                <svg class="w-8 h-8 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </div>
            <h2 class="text-3xl md:text-5xl font-extrabold mb-6 tracking-tight">Stop Hunting.<br>Start Closing.</h2>
            <p class="text-lg text-gray-300 mb-10 max-w-2xl mx-auto leading-relaxed">
                Join thousands of modern sales teams who use B2BLeadNex to instantly access the most accurate contact data on the market. Generate your first targeted list in minutes.
            </p>
            <form class="flex flex-col sm:flex-row gap-3 justify-center max-w-xl mx-auto">
                <input type="email" placeholder="Enter your work email..." class="flex-1 bg-white/10 border border-white/20 text-white px-6 py-4 rounded-md focus:outline-none focus:border-[#09C000] focus:ring-1 focus:ring-[#09C000] placeholder-gray-400">
                <button type="button" class="bg-[#09C000] hover:bg-[#0B6B3A] text-white px-8 py-4 rounded-md font-bold text-sm transition-colors shadow-lg shadow-[#09C000]/30 uppercase tracking-wider whitespace-nowrap">
                    Get Free Sample
                </button>
            </form>
            <p class="text-xs text-gray-400 mt-4">100% free test drive. No credit card required.</p>
        </div>
    </section>
"""

new_content = section_A + section_B + section_C

content = content[:new_hero_end] + "\n" + new_content + "\n" + content[new_hero_end:]

with open(index_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully redesigned the hero and injected 3 more sections.")
