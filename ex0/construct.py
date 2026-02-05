import sys
import os
import site

status = sys.prefix != sys.base_prefix
if status:
    print("MATRIX STATUS: Welcome to the construct")
    print("Current Python:", sys.executable)    
    print("Virtual Environment:",os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)
    print("SUCCESS: You're in an isolated environment!")
    print(
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting the global system.\n"
    )
    print("Package installation path:")
    print(site.getsitepackages()[0])

else:
    print("MATRIX STATUS: You're still plugged in")
    print("Current Python:", sys.executable)    
    print("Virtual Environment: None detected\n")
    print("You're in the global environment!")
    print("""The machines can see everything you install.\n
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate
# On Windows
Then run this program again.""")


