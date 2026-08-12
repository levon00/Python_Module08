import sys
import importlib
from importlib.metadata import version, PackageNotFoundError


PACKAGES = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies():
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_available = True

    for package, message in PACKAGES.items():
        try:
            importlib.import_module(package)
            package_version = version(package)
            print(
                f"[OK] {package} ({package_version}) - {message}"
            )
        except (ImportError, PackageNotFoundError):
            print(f"[MISSING] {package}")
            all_available = False

    if not all_available:
        print("\nSome dependencies are missing.")
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")
        print("python3 loading.py")
        print("\nOr with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")

    return all_available


def matrix_analysis():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    matrix = np.random.rand(1000, 3)

    print("Processing 1000 data points...")

    df = pd.DataFrame(
        matrix,
        columns=["A", "B", "C"]
    )

    print("\nGenerating visualization...")

    plt.plot(df["A"], label="A")
    plt.plot(df["B"], label="B")
    plt.plot(df["C"], label="C")

    plt.title("Matrix Data Analysis")
    plt.xlabel("Data Point")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    if not check_dependencies():
        sys.exit(1)

    matrix_analysis()


if __name__ == "__main__":
    main()
