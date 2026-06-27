import subprocess
import sys


packages = ['requests', 'colorama', 'pyperclip', 'pycryptodome']
for p in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", p])

subprocess.run([sys.executable, "dist/main.py"])