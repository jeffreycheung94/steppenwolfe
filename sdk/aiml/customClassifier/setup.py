from setuptools import setup, find_packages

setup(
    name='cc',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "torchvision",
        "torch"
    ],
)