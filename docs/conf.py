import os
import sys
from datetime import datetime

project = "Pyro-Ops"
author = "Pyro-Ops Contributors"
current_year = datetime.now().year
copyright = f"{current_year}, {author}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

autodoc_typehints = "description"
html_theme = "furo"

# Ensure src on path
sys.path.insert(0, os.path.abspath("../src"))
