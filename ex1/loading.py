print("LOADING STATUS: Loading programs...")
try:
    import pandas as pd
    import requests as req
    import matplotlib
except ImportError as e:
    print(e)
    module = str(e).split("'")[-2]
    print("install module using: pip install",module)
    print(
        "or you can use to install all dependencies:" \
        " pip install -r requirement.txt"
          )
else:
    packages = [pandas,requests,matplotlib]
    for pack in packages:
        print(f"[OK] {pack.__name__} {pack.__version__} - Data manipulation ready")

data = {
    
}