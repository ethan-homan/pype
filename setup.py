from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pype",
    description="Run python one-liners on data in your terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    author="Ethan Homan",
    author_email="ethanwhoman@gmail.com",
    url="https://github.com/ethanwh/pype",
    license="Apache",
    scripts=['pype'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
