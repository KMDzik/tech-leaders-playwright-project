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
## Installing requirements.txt

```
pip install -r requirements.txt
```


## Installing Playwright Pytest
Install the Pytest plugin:

```
pip install pytest-playwright
```

Install the required browsers:

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
