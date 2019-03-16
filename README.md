# open-source

## References
[How to create a sharable python package ?](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)

[CI and Code Coverage](https://towardsdatascience.com/10-steps-to-set-up-your-python-project-for-success-14ff88b5d13)

[![Coverage Status](https://coveralls.io/repos/github/jkalwar/open-source/badge.svg?branch=master)](https://coveralls.io/github/jkalwar/open-source?branch=master)

## Tips for using this library on windows

### Creating a virtual environment

```python
python -m venv my_env
pip install -r requirements_dev.txt
```

### Importing this library to use

```python
import importlib
mod = importlib.import_module("path.to.my-module")
mod.yourmethod()
```