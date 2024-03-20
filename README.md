# ✨ tech-leaders-project


This is a project with basic test automation to verify whether websites meet digital accessibility requirements.


# Directory structure
```
.
├── requirements.txt            # pip requirements file
└── README.md
```


# Technology stack
- Python
- PlayWright (axe-core)



# Local env setup


## Installing Python

To use this project Python 3.12 is required.

- Create a new environment
  
```
python -v venv .venv
```

- Activate the environment
  
``` sh
# Mac OS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

- Use pip to install libraries
  
```sh
# Newly install libraries
pip install <library name>

# Install libraries using requirements.txt
pip install -r requirements.txt

# Create requirements.txt
pip freeze > requirements.txt
```

## Installing Playwright Pytest

- Install the Pytest plugin:

```
pip install pytest-playwright
```

- Install the required browsers:
```
playwright install
```

# How to run the tests?

Just run a command:

```sh
pytest
```

in a main directory of the project

> Make sure your test name follows the `test_` prefix convention, for example `test_example.py`
