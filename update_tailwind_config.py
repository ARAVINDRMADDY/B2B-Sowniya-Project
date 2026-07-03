import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

new_tailwind_script = """                <script>
        tailwind.config = {
            theme: { 
                screens: {
                    'mob-360': '360px',
                    'mob-390': '390px',
                    'mob-393': '393px',
                    'mob-412': '412px',
                    'tab-768': '768px',
                    'tab-800': '800px',
                    'tab-820': '820px',
                    'desk-1280': '1280px',
                    'desk-1366': '1366px',
                    'desk-1536': '1536px',
                    'desk-1920': '1920px',
                    'sm': '640px',
                    'md': '768px',
                    'lg': '1024px',
                    'xl': '1280px',
                    '2xl': '1536px',
                },
                extend: { 
                    colors: { 
                        primary: '#09C000',
                        secondary: '#0B6B3A',
                        bgmain: '#FFFFFF',
                        bgsec: '#F8F8F8',
                        bordercol: '#E5E7EB',
                        headtext: '#222222',
                        paratext: '#666666',
                        btnbg: '#09C000',
                        btntext: '#FFFFFF',
                        hovercol: '#2CCB1F',
                        darkbg: '#111111',
                    } 
                } 
            }
        }
    </script>"""

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_content = content
        
        # Regex to find the tailwind.config script block
        pattern = r'<script>\s*tailwind\.config = \{.*?\n\s*\}\s*</script>'
        
        content = re.sub(pattern, new_tailwind_script, content, flags=re.DOTALL)
        
        if content != old_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated tailwind config in {filename}")

print(f"Total files updated: {count}")
