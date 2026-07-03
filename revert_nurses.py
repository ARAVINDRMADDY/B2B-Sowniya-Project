import re

with open('nurses-list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace everything from `<section class="relative bg-slate-900 overflow-hidden min-h-[calc(100vh-124px)] flex items-center py-16 lg:py-0">`
# up to `<div class="text-center mb-10">` (exclusive).

section_regex = re.compile(r'<section class="relative bg-slate-900 overflow-hidden min-h-\[calc\(100vh-124px\)\] flex items-center py-16 lg:py-0">.*?(?=<div class="text-center mb-10">)', re.DOTALL)

new_sections = '''<section class="relative bg-slate-900 overflow-hidden min-h-[calc(100vh-124px)] flex items-center py-10 lg:py-0">
        <div class="absolute inset-0 opacity-40 bg-cover bg-center" style="background-image: url('image/nurse.jpg');"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
            <div class="lg:grid lg:grid-cols-12 lg:gap-16 items-center">
                <div class="lg:col-span-7 flex flex-col justify-center text-center lg:text-left text-white mb-10 lg:mb-0">
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight leading-tight mb-6">
                        Nurses Contact Intelligence
                    </h1>
                    <p class="text-lg mb-8 max-w-xl mx-auto lg:mx-0 leading-relaxed font-light">
                        Get 100% Verified Nurses Email Database From Our Datasets Ranging - 1,215,800 + Records
                    </p>
                    <div>
                        <button class="bg-primary hover:bg-secondary text-white font-bold py-3 px-8 rounded-sm text-sm tracking-wider uppercase transition">
                            BOOK YOUR DATA
                        </button>
                    </div>
                </div>
                
                <div class="lg:col-span-5 relative w-full max-w-md mx-auto lg:max-w-none">
                    <div class="bg-white rounded-xl shadow-2xl p-6 lg:p-8 relative z-20">
                        <div class="text-center mb-5">
                            <h3 class="text-2xl font-extrabold text-headtext mb-1">Get a Free Sample</h3>
                            <p class="text-sm text-paratext">We have got you covered on all your email and direct marketing needs</p>
                        </div>
                        <form action="https://formsubmit.co/92bc52dd5b9811169d0d5b50c735950e" method="POST" class="space-y-3">
                        <input type="hidden" name="_next" value="https://b2-b-sowniya-project.vercel.app/thank-you.html">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="_subject" value="New Lead from B2BLeadNex Website">

                        <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg class="w-4 h-4 text-paratext" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                </div>
                                <input name="name" type="text" placeholder="Full Name*" required class="w-full pl-10 pr-4 py-2.5 bg-bgsec border border-transparent rounded-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors">
                            </div>
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg class="w-4 h-4 text-paratext" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                </div>
                                <input name="email" type="email" placeholder="Business Email*" required class="w-full pl-10 pr-4 py-2.5 bg-bgsec border border-transparent rounded-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors">
                            </div>
                            <div class="relative w-full">
                                <input name="phone" type="tel" placeholder="Business Phone*" required class="block w-full pr-4 py-2.5 bg-bgsec border border-transparent rounded-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors">
                            </div>
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg class="w-4 h-4 text-paratext" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                                </div>
                                <input name="company" type="text" placeholder="Company Name" class="w-full pl-10 pr-4 py-2.5 bg-bgsec border border-transparent rounded-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors">
                            </div>
                            <div class="relative">
                                <textarea name="message" rows="2" placeholder="Describe Your Requirements*" required class="w-full p-3 py-2.5 bg-bgsec border border-transparent rounded-md text-sm text-headtext focus:outline-none focus:border-primary transition-colors resize-none"></textarea>
                            </div>
                            <div class="flex items-start pb-1">
                                <div class="flex items-center h-5">
                                    <input id="newsletter" type="checkbox" checked class="w-4 h-4 bg-bgsec border-bordercol rounded text-primary">
                                </div>
                                <label for="newsletter" class="ml-2 text-xs font-medium text-paratext">I would like to subscribe to your Newsletter.</label>
                            </div>
                            <button type="submit" class="w-full text-white bg-primary hover:bg-secondary font-bold rounded-md text-sm px-5 py-3.5 text-center transition-colors shadow-md">
                                GET A FREE SAMPLE
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="bg-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="lg:grid lg:grid-cols-2 lg:gap-12 items-center mb-16">
                <div>
                    <h2 class="text-4xl font-extrabold text-secondary leading-tight">
                        Nurses Contact Intelligence
                    </h2>
                </div>
                <div class="mt-6 lg:mt-0">
                    <p class="text-sm text-headtext leading-relaxed mb-4">
                        Our Verified Nurses Contact Database helps you connect with nursing professionals worldwide through accurate and regularly updated business contact data. Access valuable information, including business email addresses, direct phone numbers, specialties, years of experience, healthcare facility details, job titles, and geographic locations to support your sales and marketing efforts.
                    </p>
                    <p class="text-sm text-headtext leading-relaxed mb-4">
                        Whether you're promoting healthcare products, medical devices, staffing solutions, software, training programs, or professional services, our targeted database helps you reach the right nursing professionals faster. Build qualified prospect lists, improve campaign performance, and generate meaningful business opportunities with confidence.
                    </p>
                    <a href="#" class="text-primary font-bold text-sm tracking-widest uppercase mt-2 inline-block hover:text-secondary">READ MORE</a>
                </div>
            </div>

            '''

new_content = section_regex.sub(new_sections, content)

with open('nurses-list.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Reverted nurses-list.html hero section and applied ONLY h1 content change.")
