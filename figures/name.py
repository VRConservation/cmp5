import os

folder = 'figures'
files = sorted(os.listdir(folder))  # sorts files alphabetically

for idx, filename in enumerate(files, start=1):
    old_path = os.path.join(folder, filename)
    if os.path.isfile(old_path):
        ext = os.path.splitext(filename)[1]
        new_name = f"fig{idx}{ext}"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {filename} -> {new_name}")
