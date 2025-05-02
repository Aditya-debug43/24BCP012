import os
os.makedirs("new_dir", exist_ok=True)
with open("source.txt", "w") as f:
    f.write("This is source file.")
import shutil
shutil.copy("source.txt", "new_dir/copied.txt")