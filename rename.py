import os

parent = r"c:\Mrityunjay\PythonLessons"

folders = [
    "1. String",
    "2. Integers and Floats",
    "3. Lists, Tuples and Sets",
    "4. Dictionary",
    "5. Conditionals and Booleans",
    "6. Loops and Iterations",
    "7. Functions",
    "8. Import Modules and Standard Library",
    "9. Virtual Environment"
]

def rename_folders(parent, folders):
    for folder in folders:
        # extract number and name
        parts = folder.split(". ", 1)        # split at first ". "
        number = parts[0].zfill(2)           # 1 → 01, 2 → 02
        name = parts[1].replace(" ", "_")    # spaces → underscores

        new_name = f"{number}_{name}"        # 01_String

        old_path = os.path.join(parent, folder)
        new_path = os.path.join(parent, new_name)

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"✅ {folder} → {new_name}")
        else:
            print(f"❌ Not found: {folder}")

rename_folders(parent, folders)