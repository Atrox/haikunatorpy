# Haikunator

[![Build Status](https://travis-ci.org/AtroxDev/haikunator.svg?branch=master)](https://travis-ci.org/atroxdev/haikunator)

Generate Heroku-like random names to use in your applications.

## Installation
*todo*

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