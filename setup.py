from setuptools import setup

setup(
    name="pype",
    description="Run python one-liners on data in your terminal.",
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
