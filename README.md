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
- Playwright



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

- Use requirements.txt to install libraries
  
```sh
# Install libraries using requirements.txt
pip install -r requirements.txt
```

## Installing Playwright With Pytest (make both steps)

- Install Pytest:

```
pip install pytest-playwright
```

- Install Playwright:
```
playwright install
```

# How to run the tests?

Just run a command:

```sh
pytest
```

in a main directory of the project.

> Make sure your test name follows the `test_` prefix convention, for example `test_example.py`
