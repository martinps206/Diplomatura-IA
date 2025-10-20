import os
import sys

# Añadir la raíz del proyecto al sys.path para que `import core...` funcione
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
