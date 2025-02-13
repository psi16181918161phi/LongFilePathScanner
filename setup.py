from setuptools import setup, find_packages
import os

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as fp:
        return fp.read()

setup(
    name="source",  # Replace with your project's name
    version="0.1.0",
    description="A project to scan long file paths in a directory.",
    long_description=read("README.md") if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="hadrian61816@gmail.com",
    url="https://github.com/psi16181918161phi/LongPathFileScarnner",  # Replace with your URL if any
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here, e.g.,
        "requests>=2.25.1",
        "numpy>=1.20.0",
        "behave>=1.2.6",
        "gherkin-official>=25.2.0",
        "pytest>=6.2.2"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change to your license if different
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)