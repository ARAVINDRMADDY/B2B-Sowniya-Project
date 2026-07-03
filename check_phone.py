import os

directory = '.'
count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            if 'name="phone"' in f.read():
                count += 1
                print(f"Has phone: {filename}")

print(f'Total files with phone input: {count}')
