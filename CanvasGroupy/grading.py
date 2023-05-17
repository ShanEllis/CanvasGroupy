# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/04_project_grading.ipynb.

# %% auto 0
__all__ = ['Grading']

# %% ../nbs/api/04_project_grading.ipynb 3
from .github import GitHubGroup
from .canvas import CanvasGroup
import github
import canvasapi
from ast import literal_eval

# %% ../nbs/api/04_project_grading.ipynb 4
class Grading:
    def __init__(self,
                 gh: github.Github, # authenticated github object
                 canvas: canvasapi.canvas, # authenticated canvas object
                ):
        self.github = gh
        self.canvas = canvas

