import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="amazing_printer",
    version="0.1.0",
    author="Kher Yee, Ting",
    author_email="infcurious@gmail.com",
    description="A python package that pretty prints Python objects with colors and proper indentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tkbky/amazing_printer",
    packages=setuptools.find_packages(),
    install_requires=[
        'colorama>=0.4.0',
        'pyyaml>=5.1.1'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest>=4.3.0',
        'pytest-cov>=2.6.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
