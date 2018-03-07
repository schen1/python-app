from setuptools import setup, find_packages


setup (
    name             = "python-app",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["flask", "redis"],
)