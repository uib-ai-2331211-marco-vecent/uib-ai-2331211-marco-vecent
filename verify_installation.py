"""
verify_installation.py
Run this script inside your environment to verify installed packages.
It will create verify_output.txt and verify_plot.png in the current folder.
"""
import importlib
import traceback

packages = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "sklearn": "sklearn",
    "skfuzzy": "skfuzzy",   # scikit-fuzzy
    "cv2": "cv2",           # opencv-python
    "nltk": "nltk",
    "torch": "torch",
    "tensorflow": "tensorflow"
}

results = []
for name, modname in packages.items():
    try:
        m = importlib.import_module(modname)
        ver = getattr(m, "__version__", "unknown")
        results.append(f"{modname}: OK (version {ver})")
    except Exception as e:
        results.append(f"{modname}: ERROR ({e.__class__.__name__}: {e})")

# quick plot check
try:
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 100)
    plt.figure()
    plt.plot(x, np.sin(x))
    plt.title("Verify Plot")
    plt.tight_layout()
    plt.savefig("verify_plot.png")
    results.append("Matplotlib: plot saved to verify_plot.png")
except Exception as e:
    results.append(f"Matplotlib plot error: {e}")

# iris dataset check
try:
    from sklearn import datasets
    X = datasets.load_iris().data
    results.append(f"Sklearn iris shape: {X.shape}")
except Exception as e:
    results.append(f"Sklearn iris error: {e}")

# write results to file and stdout
with open("verify_output.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")
print("\n".join(results))
