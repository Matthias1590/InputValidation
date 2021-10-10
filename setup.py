from setuptools import setup


def readme():
    with open("README.md", "r") as f:
        return f.read()

setup(
    name="inputvalidation",
    version="1.1.3",
    description="A python module to validate input.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matthias1590/InputValidation",
    author="Matthias Wijnsma",
    author_email="matthiasx95@gmail.com",
    license="MIT",
    packages=["inputvalidation"]
)