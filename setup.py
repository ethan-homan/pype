from setuptools import setup

setup(
    name="pype",
    version="0.0.1",
    packages=["pype"],
    author="Ethan Homan",
    author_email="ethanwhoman@gmail.com",
    license="Apache",
    entry_points={"console_scripts": ["pype=pype:main"]},
)