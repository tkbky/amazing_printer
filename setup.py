import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ap",
    version="0.0.1",
    author="Kher Yee, Ting",
    author_email="infcurious@gmail.com",
    description="A python package that pretty prints Python objects with colors and proper indentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tkbky/ap",
    packages=setuptools.find_packages(),
    install_requires=[
        'colorama==0.4.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
