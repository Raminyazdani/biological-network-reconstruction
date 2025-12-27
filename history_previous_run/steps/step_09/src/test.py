import glob
import os

files = glob.glob("./pickled/*.pkl")  # Assuming pickled files have .pkl extension

for f in files:
    # Extract the filename without the directory and extension
    print(f)
    filename = os.path.basename(f)
    print(filename)
    file_name_without_ext = os.path.splitext(filename)[0]
    print(file_name_without_ext)