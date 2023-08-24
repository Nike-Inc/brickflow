### How do imports work?

!!! warning

    **This is very important to understand how imports work for mono repos. Please read this carefully. Otherwise you might run into issues during deployments.**

When using brickflow projects every project will have a `.brickflow-project-root.yml` file. When you import brickflow,
which you will
in your entrypoint or workflows, brickflow will inspect all paths all stackframes during the import and recursively go
up the path until it finds the `.brickflow-project-root.yml` file.
The first instance of brickflow-project-root.yml will be added to the sys.path to help with module imports.

Let us take a quick example of how to get imports to properly work!

Let us say you have a project structure like this:

```
    repo-root/
    ├── .git
    ├── projects/
    │   ├── project_abc/
    │   │   ├── lib/
    │   │   │   ├── __init__.py
    │   │   │   └── shared_functions.py
    │   │   ├── workflows/
    │   │   │   ├── __init__.py
    │   │   │   ├── entrypoint.py
    │   │   │   └── workflow_abc.py
    │   │   ├── setup.py
    │   │   └── .brickflow-project-root.yml
    │   └── project_xyz/
    │       ├── workflows_geo_b/
    │       │   ├── entrypoint.py
    │       │   └── workflow_xyz.py
    │       ├── workflows_geo_a/
    │       │   ├── entrypoint.py
    │       │   └── workflow_xyz.py
    │       └── .brickflow-project-root.yml
    ├── .gitignore
    ├── brickflow-multi-project.yml
    └── README.md
```

If let us say you are looking at adding imports from lib into `workflow_abc.py`, you need to:

```python
from lib import share_functions

share_functions.some_function(....)
```

Since in the project structure the `.brickflow-project-root.yml` is at `repo-root/projects/project_abc` then everything
in that `project_abc` folder is
added to sys.path in python. So you can import any of the folders under there.