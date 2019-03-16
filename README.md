# open-source

[How to create a sharable python package ?](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)

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