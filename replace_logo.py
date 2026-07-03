import os

directory = '.'

old_logo_pattern = '<span class="text-headtext drop-shadow-sm">B2BLead</span><span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-green-400 drop-shadow-sm">Nex</span>'
new_logo = '<img src="image/logo png.png" alt="B2BLeadNex Logo" class="h-10 w-auto drop-shadow-sm">'

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(old_logo_pattern, new_logo)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f'Updated {filename}')

print(f'Total files updated: {count}')
