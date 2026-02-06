print("LOADING STATUS: Loading programs...")
try:
    import pandas as pd
    import requests as req
    import matplotlib.pyplot as plt
except ImportError as e:
    print(e)
    module = str(e).split("'")[-2]
    print("install module using: pip install", module)
    print("or you can use to install all dependencies: pip install -r requirement.txt")
else:
    packages = [pd, req]
    for pack in packages:
        print(f"[OK] {pack.__name__} {pack.__version__} - Data manipulation ready")

data = {"time": range(1, 11), "value": range(101, 111)}
df = pd.DataFrame(data)
print(df.head(6))

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 6, 5]


plt.plot(x, y)
plt.title("Sample Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.savefig("sample_plot.png")
print("Plot saved as sample_plot.png")

response = req.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    print("HTTP Request Successful")
    print("Response JSON:", response.json())
    

print("All programs loaded successfully.")