# Haikunator

[![Build Status](https://img.shields.io/travis/AtroxDev/haikunator.svg?style=flat-square)](https://travis-ci.org/AtroxDev/haikunator)
[![Latest Version](https://img.shields.io/pypi/v/haikunator.svg?style=flat-square)](https://pypi.python.org/pypi/haikunator)


Generate Heroku-like random names to use in your applications.

## Installation
```
pip install haikunator
```

## Usage

Haikunator is pretty simple. There is nothing to configure and it only has a single method, `haikunate`:

```python
from haikunator import haikunate

haikunate() # => "caring-butterfly-0291"

# Hex
haikunate(True) # => "autumn-pine-c42c"
```

## Contributing

Everyone is encouraged to help improve this project. Here are a few ways you can help:

- [Report bugs](https://github.com/atroxdev/haikunator/issues)
- Fix bugs and [submit pull requests](https://github.com/atroxdev/haikunator/pulls)
- Write, clarify, or fix documentation
- Suggest or add new features

## Other Languages

Haikunator is also available in other languages. Check them out:

- Python: https://github.com/AtroxDev/haikunator
- Ruby: https://github.com/usmanbashir/haikunator
- Go: https://github.com/yelinaung/go-haikunator
