# HaikunatorPY

[![Build Status](https://img.shields.io/travis/Atrox/haikunatorpy.svg?style=flat-square)](https://travis-ci.org/Atrox/haikunatorpy)
[![Latest Version](https://img.shields.io/pypi/v/haikunator.svg?style=flat-square)](https://pypi.python.org/pypi/haikunator)
[![Coverage Status](https://img.shields.io/coveralls/Atrox/haikunatorpy.svg?style=flat-square)](https://coveralls.io/r/Atrox/haikunatorpy)


Generate Heroku-like random names to use in your python applications.

## Installation
```
pip install haikunator
```

## Usage

Haikunator is pretty simple. There is nothing to configure and it only has a single method, `haikunate`:

```python
from haikunator import Haikunator

haikunator = Haikunator()
# haikunator = Haikunator(1234) # optional seed

# default usage
haikunator.haikunate() # => "wispy-dust-1337"

# custom length (default=4)
haikunator.haikunate(token_length=6) # => "patient-king-887265"

# use hex instead of numbers
haikunator.haikunate(token_hex=True) # => "purple-breeze-98e1"

# use custom chars instead of numbers/hex
haikunator.haikunate(token_chars='HAIKUNATE') # => "summer-atom-IHEA"

# don't include a token
haikunator.haikunate(token_length=0) # => "cold-wildflower"

# use a different delimiter
haikunator.haikunate(delimiter='.') # => "restless.sea.7976"

# no token, space delimiter
haikunator.haikunate(token_length=0, delimiter=' ') # => "delicate haze"

# no token, empty delimiter
haikunator.haikunate(token_length=0, delimiter='') # => "billowingleaf"
```

## Options

The following options are available:

```python
from haikunator import Haikunator

haikunator = Haikunator()
# haikunator = Haikunator(1234) # optional seed

haikunator.adjectives = ['custom', 'adjectives']
haikunator.nouns = ['custom', 'nouns']

haikunate(
  delimiter='-',
  token_length=4,
  token_hex=False,
  token_chars='0123456789'
)
```
*If ```token_hex``` is true, it overrides any tokens specified in ```token_chars```*

## Contributing

Everyone is encouraged to help improve this project. Here are a few ways you can help:

- [Report bugs](https://github.com/atrox/haikunatorpy/issues)
- Fix bugs and [submit pull requests](https://github.com/atrox/haikunatorpy/pulls)
- Write, clarify, or fix documentation
- Suggest or add new features

## Other Languages

Haikunator is also available in other languages. Check them out:

- Node: https://github.com/Atrox/haikunatorjs
- PHP: https://github.com/Atrox/haikunatorphp
- .NET: https://github.com/Atrox/haikunator.net
- Java: https://github.com/Atrox/haikunatorjava
- Go: https://github.com/Atrox/haikunatorgo
- Dart: https://github.com/Atrox/haikunatordart
- Ruby: https://github.com/usmanbashir/haikunator