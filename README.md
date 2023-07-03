# Quickstart PyTube

This is a repository using pytube package.

This repository is setup for Python 3.10.

## Development instructions

## Without devcontainer

Create a virtual environment:

``` sh
py -3.10 -m venv venv
source venv/scripts/activate
```

Then install the packages:

```sh
pip install -r requirements.txt
```

## Adding code and tests

This repository starts with a very simple `main.py`.

# File breakdown

Here's a short explanation of each file/folder in this template:

* `.devcontainer`: Folder containing files used for setting up a devcontainer
  * `devcontainer.json`: File configuring the devcontainer, includes VS Code settings
  * `Dockerfile`: File with commands to build the devcontainer's Docker image
* `.github`: Folder for Github-specific files and folders
  * `workflows`: Folder containing Github actions config files
    * `python.yaml`: File configuring Github action that runs tools and tests
* `tests`: Folder containing Python tests
* `.gitignore`: File describing what file patterns Git should never track
* `.pre-commit-config.yaml`: File listing all the pre-commit hooks and args
* `main.py`: The main (and currently only) Python file for the program
* `pyproject.toml`: File configuring most of the Python dev tools
* `README.md`: You're reading it!
* `requirements-dev.txt`: File listing all PyPi packages required for development
* `requirements.txt`: File listing all PyPi packages required for production

## Resources
For python template explanation, read [this blog post](http://blog.pamelafox.org/2022/09/how-i-setup-python-project.html).

Original pytube post [click here](https://www.linkedin.com/feed/update/urn:li:activity:7080976967759474688/).

Pytube RegexMatchError issue [click here](https://github.com/pytube/pytube/issues/1678)
