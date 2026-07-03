import re

with open('contact-us.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the form HTML
form_match = re.search(r'<form action="https://formsubmit\.co/.*?<\/form>', content, re.DOTALL)
if not form_match:
    print("Could not find form")
    exit()
form_html = form_match.group(0)

# Replace the whole <main> section with the new layout
main_regex = re.compile(r'<main class="flex-grow">.*?</main>', re.DOTALL)

new_main = f'''<main class="flex-grow">
        <section class="relative bg-[#021f15] overflow-hidden min-h-[calc(100vh-124px)] flex items-center py-10 lg:py-16">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#09C000]/15 via-transparent to-transparent"></div>
            
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
                <div class="lg:grid lg:grid-cols-12 lg:gap-16 items-center">
                    <div class="lg:col-span-7 flex flex-col justify-center text-center lg:text-left text-white mb-10 lg:mb-0">
                        <div class="inline-flex items-center px-4 py-2 rounded-full bg-white/5 border border-[#09C000]/30 text-[#09C000] font-semibold text-xs uppercase tracking-widest mb-8 backdrop-blur-sm shadow-[0_0_15px_rgba(9,192,0,0.15)] self-center lg:self-start">
                            <span class="flex w-2 h-2 rounded-full bg-[#09C000] mr-2 animate-pulse"></span>
                            Global Data Experts Available 24/7
                        </div>
                        
                        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white tracking-tight leading-tight mb-6">
                            Let's Build Your Next <br class="hidden sm:block" />
                            <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#09C000] to-[#2CCB1F]">Data-Driven Strategy</span>
                        </h1>
                        
                        <p class="text-lg mb-8 max-w-xl mx-auto lg:mx-0 leading-relaxed font-light text-gray-300">
                            Whether you need custom datasets, direct dials, or complex email appending, our team of data scientists and marketing experts are ready to help you scale your outreach.
                        </p>
                        
                        <div class="flex flex-wrap justify-center lg:justify-start gap-6 text-sm text-gray-400 font-medium">
                            <div class="flex items-center">
                                <svg class="w-5 h-5 text-[#09C000] mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                95% Accuracy Guarantee
                            </div>
                            <div class="flex items-center">
                                <svg class="w-5 h-5 text-[#09C000] mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                24 Hour Response Time
                            </div>
                            <div class="flex items-center">
                                <svg class="w-5 h-5 text-[#09C000] mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                Global Coverage
                            </div>
                        </div>
                    </div>
                    
                    <div class="lg:col-span-5 relative w-full max-w-md mx-auto lg:max-w-none">
                        <div class="bg-white rounded-xl shadow-2xl p-6 lg:p-8 relative z-20 text-black">
                            <div class="text-center mb-5">
                                <h3 class="text-2xl font-extrabold text-headtext mb-1 uppercase tracking-wide">Connect With Us</h3>
                                <p class="text-sm text-paratext">Place your query in the form, and our representatives will get in touch with you within 24 hours!</p>
                            </div>
                            {form_html}
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Address Cards Section -->
        <section class="py-16 bg-white border-t border-gray-100">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="max-w-3xl mx-auto">
                    <!-- Single Worldwide Serving Card -->
                    <div class="bg-[#f4f4f4] rounded-xl p-10 flex flex-col items-center text-center border border-gray-200 shadow-sm">
                        <div class="w-20 h-20 bg-white shadow-sm border border-gray-100 rounded-full flex items-center justify-center mb-8">
                            <svg class="w-10 h-10 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        </div>
                        <h3 class="text-3xl font-bold text-[#044c3c] mb-6">Serving Businesses Worldwide</h3>
                        <p class="text-gray-700 text-lg sm:text-xl font-medium tracking-wide mb-8">
                            🇺🇸 United States &nbsp;|&nbsp; 🇨🇦 Canada &nbsp;|&nbsp; 🇪🇺 Europe &nbsp;|&nbsp; 🇮🇳 India
                        </p>
                        <a href="mailto:lucybrady012@yahoo.com" class="inline-flex items-center justify-center text-gray-700 text-lg hover:text-[#09C000] underline decoration-gray-400 underline-offset-4 transition-colors font-medium">
                            <svg class="w-6 h-6 mr-3 flex-shrink-0 text-[#09C000]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            lucybrady012@yahoo.com
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>'''

new_content = main_regex.sub(new_main, content)

with open('contact-us.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated contact-us.html")
