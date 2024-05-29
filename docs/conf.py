# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Relatório de estágio em {NOME_EMPRESA}'
copyright = '2024, {NOME_COMPLETO}'
author = '{NOME_COMPLETO}'
release = '{ANO}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'author_year'


templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = html_short_title = project

html_context = {
  'display_github': True,
  'github_user': 'portif',
  'github_repo': 'relestagio',
  'github_version': 'main/docs/',
}