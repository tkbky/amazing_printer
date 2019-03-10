## ap

It's an attempt to port the Ruby's [awesome_print](https://github.com/awesome-print/awesome_print) to Python.

## Usage

```python
from ap import ap

ap(object, options = {})

# Options:
# sort_keys - boolean, default is False
```

## Contributing

0. Fork & clone the repository
```sh
$ git clone git@github.com:<your-github-handle>/ap.git
$ cd ap
```

1. Create a virtual environment and activate it
```sh
$ python -m venv env

# bash shell
$ source env/bin/activate

# fish shell
$ source env/bin/activate.fish
```

2. Install dependencies
```sh
(env) $ pip install -r requirements.txt
```

3. Make your awesome changes & pull request.
