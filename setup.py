from setuptools import setup
from src._version import __version__


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    # General infos
    name='mldoe',
    author='Alexandre Bohyn',
    author_email='alexandre.bohyn@kuleuven.be',
    url='https://github.com/ABohynDOE/mldoe',
    description='Tools to generate and enumerate mixed-level designs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Version infos
    version=__version__,
    # Files infos
    py_modules=["design"],
    package_dir={'': 'src'},
    # Classifiers
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    # Package requirements for installation
    install_requires=[
        "numpy>=1.19",
        "oapackage>=2.6.8"
    ],
    # Package requirements for testing
    extras_require={
        "dev": [
            "pytest>=6.2.2"
        ]
    }
)
