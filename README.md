## ap

It's an attempt to port the Ruby's [awesome_print](https://github.com/awesome-print/awesome_print) to Python.

## Usage

```python
from ap import ap

ap(object, options = {})

# Options:
# sort_keys - boolean, set to sort the dictionary keys, default is False.
# indent - integer, set the width of indentation, default is 4 spaces.
# multiple_lines - boolean, set to print the fields for dict or list in multiple lines, default is True.
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
(env) $ pip install -r requirements.txt dev-requirements.txt
```

3. Make your awesome changes

4. Run test and coverage
```sh
pytest
```

5. Make your pull request

## License

Copyright (c) 2019 Kher Yee, Ting

Released under the MIT license. See [LICENSE](LICENSE) file for details.
