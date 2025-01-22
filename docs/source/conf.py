#!/usr/bin/env python
#
# rl_salamandra_alignment documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('..'))
print("ABSPATH: ", os.path.abspath('../..'))
sys.path.insert(
    0, 
    os.path.abspath(os.path.join('..', '..', 'rl_salamandra_alignment'))
    )
sys.path.insert(
    0,
    # Absolute path used in GitHubActions pages, after cloning the repository
    "/home/runner/work/rl_salamandra_alignment_docs/rl_salamandra_alignment_docs/rl_salamandra_alignment/src"
)

print("EXECUTABLE")
print("HERE:",sys.executable)
print("PATH:", "\n".join(sys.path))
import time
time.sleep(5)

import rl_salamandra_alignment

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.viewcode',
    "sphinx.ext.napoleon",  # For Google-style and NumPy-style docstrings
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",  # For type hints in docstrings
    "myst_parser",  # For Markdown support
    'sphinx_rtd_theme'
]

templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# General information about the project.
project = 'RL - Salamandra Alignment'
copyright = '2025, LangTech BSC'
author = 'LangTech BSC'

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = rl_salamandra_alignment.__version__
# The full version, including alpha/beta/rc tags.
release = rl_salamandra_alignment.__version__


# The master toctree document.
master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_#theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'rl_salamandra_alignmentdoc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'rl_salamandra_alignment.tex',
     'RL - Salamandra Alignment Documentation',
     'LangTech BSC', 'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'rl_salamandra_alignment',
     'RL - Salamandra Alignment Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'rl_salamandra_alignment',
     'RL - Salamandra Alignment Documentation',
     author,
     'rl_salamandra_alignment',
     'One line description of project.',
     'Miscellaneous'),
]



