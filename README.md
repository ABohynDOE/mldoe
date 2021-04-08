# MLDOE

![PyPI - License](https://img.shields.io/pypi/l/mldoe)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mldoe)
![PyPI](https://img.shields.io/pypi/v/mldoe)
[![Requirements Status](https://requires.io/github/ABohynDOE/mldoe/requirements.svg?branch=master)](https://requires.io/github/ABohynDOE/mldoe/requirements/?branch=master)
[![Documentation Status](https://readthedocs.org/projects/mldoe/badge/?version=latest)](https://mldoe.readthedocs.io/en/latest/?badge=latest)

<!-- Add badges for:
-cover (coveralls.io)
-CI (travis.org) -->

This package provides the tools to enumerate and characterize regular mixed-level designs (with four and two-level factors).

## Installation

Run the following to install:

```python
pip install mldoe
```

## Usage

```python
from mldoe import design

# Generate a two-level design by columns
D = TLdesign(16,[1,2,4,8,6])

# Print the design matrix
print(D.array)

# Compute its word-length pattern
print(D.wlp())

```

## Developing mldoe

To install mldoe, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
```

## Contributors

Want to contribute ? 
Don't hesitate to create a pull request.