import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"
contact_file = os.path.join(directory, "contact-us.html")
thankyou_file = os.path.join(directory, "thank-you.html")

with open(contact_file, "r", encoding="utf-8") as f:
    content = f.read()

thank_you_main = """
    <main class="flex-grow flex items-center justify-center min-h-[60vh] bg-bgsec relative">
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-[#09C000]/10 via-transparent to-transparent"></div>
        <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10 py-20">
            <div class="inline-flex items-center justify-center w-24 h-24 rounded-full bg-[#09C000]/20 text-[#09C000] mb-8 shadow-[0_0_30px_rgba(9,192,0,0.3)]">
                <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                </svg>
            </div>
            
            <h1 class="text-4xl sm:text-5xl font-extrabold text-headtext tracking-tight mb-4">
                Thank You!
            </h1>
            
            <p class="text-lg text-paratext mb-10 max-w-xl mx-auto">
                Your request has been successfully submitted. Our team will review your requirements and get back to you shortly.
            </p>
            
            <a href="index.html" class="inline-flex items-center justify-center bg-primary hover:bg-hovercol text-btntext font-bold py-3 px-8 rounded-full transition-colors uppercase tracking-wider shadow-md">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                Return to Home
            </a>
        </div>
    </main>
"""

# Replace everything between <main> and </main>
new_content = re.sub(r'<main class="flex-grow">.*?</main>', thank_you_main, content, flags=re.DOTALL)

with open(thankyou_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Created thank-you.html successfully.")
