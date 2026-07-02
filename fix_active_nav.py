import os
import re

directory = r"c:\Users\Aravind.R\OneDrive\Desktop\B2B Sowniya Project"

active_script = """
    <!-- Active Nav Highlight Script -->
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            let currentPath = window.location.pathname.split('/').pop();
            if (!currentPath) currentPath = 'index.html';
            
            const allLinks = document.querySelectorAll('header a, #mobile-menu a');
            allLinks.forEach(link => {
                if (link.getAttribute('href') === currentPath) {
                    // Skip if it's a solid button to avoid invisible text
                    if (link.classList.contains('bg-btnbg') || link.classList.contains('bg-primary')) {
                        return; 
                    }
                    
                    link.classList.remove('text-headtext', 'text-btntext');
                    link.classList.add('text-primary');
                    
                    if (link.closest('#mobile-menu') && !link.closest('summary')) {
                        link.classList.add('bg-primary/10');
                    }
                    
                    // Highlight parent dropdown in desktop
                    const desktopParent = link.closest('.group');
                    if (desktopParent && !link.closest('#mobile-menu')) {
                        const parentLink = desktopParent.querySelector('a');
                        if (parentLink) {
                            parentLink.classList.remove('text-headtext');
                            parentLink.classList.add('text-primary');
                        }
                    }
                    
                    // Highlight and open parent dropdown in mobile
                    const mobileDetails = link.closest('details');
                    if (mobileDetails) {
                        mobileDetails.setAttribute('open', '');
                        const summaryLink = mobileDetails.querySelector('summary a');
                        if (summaryLink && !summaryLink.classList.contains('bg-btnbg')) {
                            summaryLink.classList.remove('text-btntext', 'text-headtext');
                            summaryLink.classList.add('text-primary');
                        }
                    }
                }
            });
        });
    </script>
"""

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Remove old script if it already exists
        content = re.sub(r'<!-- Active Nav Highlight Script -->.*?</script>', '', content, flags=re.DOTALL)
        
        # Inject the script before </body>
        new_content = content.replace("</body>", active_script + "\n</body>")
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
