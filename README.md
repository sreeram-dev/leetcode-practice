# LeetCode Practice

Python solutions and tests for LeetCode problems and small programming exercises.

## Requirements

- Python 3.15.2
- `pyenv` and `pyenv-virtualenv` (recommended)

## Setup with pyenv

Create the project environment and install the dependencies:

```bash
pyenv virtualenv 3.15.2 leetcode-practice
pyenv local leetcode-practice
python -m pip install -r requirements.txt
```

If the environment already exists, activate it with:

```bash
pyenv activate leetcode-practice
```

## Development container

Open the repository in VS Code and choose **Reopen in Container** when prompted. The dev container installs the dependencies and configures the recommended Python extensions.

## Running tests

```bash
pytest
```

## Project structure

```text
src/       Python source code
tests/     pytest test suites
```
