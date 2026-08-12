import os
import sys
import site


def checker() -> None:
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.environ.get('VIRTUAL_EN')} detected")
        print("\nWARNING: You're in the global environment!\n"
              "The machines can see everything you install\n")
        print("To enter the construct, run:\n")
        print("python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Virtual Environment: {os.environ.get('VIRTUAL_ENV')}\n")
        print("SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    checker()
