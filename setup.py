import subprocess
import shutil
import sys
python_311 = shutil.which("py")
if not python_311:
    print("ERROR: Python Launcher (py) was not found.")
    print("Please ensure that Python 3.11 is correctly installed.")
    sys.exit(1)
packages = ['requests', 'colorama', 'pyperclip', 'pycryptodome']
print("--- Installing dependencies for Python 3.11 ---")
for p in packages:
    subprocess.check_call([python_311, "-3.11", "-m", "pip", "install", p])
print("\n--- Starting script with Python 3.11 ---")
subprocess.run([python_311, "-3.11", "dist/c.py"])
