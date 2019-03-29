## Deployment guide

Long version [here](https://packaging.python.org/guides/). TL;DR; below:

1. Install Twine & Wheel
```sh
$ pip install twine wheel
```

2. Pypi configuration
```sh
# in $HOME/.pypirc
[pypi]
username = <username>
password = <password> # if not set here, you'll be prompt, which is preferable
```

3. Build
```sh
$ python setup.py bdist_wheel
```

4. Upload
```sh
$ twine upload dist/*
```
