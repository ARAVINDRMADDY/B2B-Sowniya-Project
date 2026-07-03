import re

with open('nurses-list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the content from <div class="lg:grid lg:grid-cols-12 lg:gap-16 items-center">
# to its closing </div> which is just before </div>\n        </section>

# Let's use a simpler regex by capturing the whole <section class="relative bg-slate-900 overflow-hidden...
# until </section>

section_regex = re.compile(r'<section class="relative bg-slate-900 overflow-hidden min-h-\[calc\(100vh-124px\)\] flex items-center py-10 lg:py-0">.*?</section>', re.DOTALL)

new_section = '''<section class="relative bg-slate-900 overflow-hidden min-h-[calc(100vh-124px)] flex items-center py-16 lg:py-0">
        <div class="absolute inset-0 opacity-40 bg-cover bg-center" style="background-image: url('image/nurse.jpg');"></div>
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full text-center">
            <div class="flex flex-col justify-center items-center text-white mt-10">
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight leading-tight mb-8">
                    Nurses Contact Intelligence
                </h1>
                <p class="text-base sm:text-lg mb-6 leading-relaxed font-light text-gray-200">
                    Our Verified Nurses Contact Database helps you connect with nursing professionals worldwide through accurate and regularly updated business contact data. Access valuable information, including business email addresses, direct phone numbers, specialties, years of experience, healthcare facility details, job titles, and geographic locations to support your sales and marketing efforts.
                </p>
                <p class="text-base sm:text-lg mb-10 leading-relaxed font-light text-gray-200">
                    Whether you're promoting healthcare products, medical devices, staffing solutions, software, training programs, or professional services, our targeted database helps you reach the right nursing professionals faster. Build qualified prospect lists, improve campaign performance, and generate meaningful business opportunities with confidence.
                </p>
                <div>
                    <button class="bg-primary hover:bg-secondary text-white font-bold py-4 px-10 rounded-sm text-base tracking-wider uppercase transition">
                        BOOK YOUR DATA
                    </button>
                </div>
            </div>
        </div>
    </section>'''

new_content = section_regex.sub(new_section, content)

with open('nurses-list.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated nurses-list.html hero section")
