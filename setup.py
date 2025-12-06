from setuptools import setup, find_packages

setup(
    name="ditto",        # arbitrary package name (for pip)
    version="0.1.0",
    packages=find_packages(), # will pick up the `ditto` package
    py_modules=["matcher"]
)
