# run_package.py
#!/usr/bin/env python

import os
import sys

# Add the directory containing your package to sys.path
current_dir = os.path.abspath(os.path.dirname(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from source import run

if __name__ == "__main__":
    run()
