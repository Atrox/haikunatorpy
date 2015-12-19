# HaikunatorPY

[![Build Status](https://img.shields.io/travis/Atrox/haikunatorpy.svg?style=flat-square)](https://travis-ci.org/Atrox/haikunatorpy)
[![Latest Version](https://img.shields.io/pypi/v/haikunator.svg?style=flat-square)](https://pypi.python.org/pypi/haikunator)


Generate Heroku-like random names to use in your python applications.

## Installation
```
pip install haikunator
```

## Usage

Haikunator is pretty simple. There is nothing to configure and it only has a single method, `haikunate`:

```python
from haikunator import haikunate

# default usage
haikunate() # => "wispy-dust-1337"

# custom length (default=4)
haikunate(tokenlength=6) # => "patient-king-887265"

# use hex instead of numbers
haikunate(tokenhex=True) # => "purple-breeze-98e1"

# use custom chars instead of numbers/hex
haikunate(tokenchars='HAIKUNATE') # => "summer-atom-IHEA"

# don't include a token
haikunate(tokenlength=0) # => "cold-wildflower"

# use a different delimiter
haikunate(delimiter='.') # => "restless.sea.7976"

# no token, space delimiter
haikunate(tokenlength=0, delimiter=' ') # => "delicate haze"

# no token, empty delimiter
haikunate(tokenlength=0, delimiter='') # => "billowingleaf"
```

## Options

The following options are available:

```python
haikunate(
  delimiter='-',
  tokenlength=4,
  tokenhex=False,
  tokenchars='0123456789',
  seed=None
)
```
*If ```tokenhex``` is true, it overrides any tokens specified in ```tokenchars```*

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
- Dart: https://github.com/Atrox/haikunatordart
- Ruby: https://github.com/usmanbashir/haikunator
- Go: https://github.com/yelinaung/go-haikunator
