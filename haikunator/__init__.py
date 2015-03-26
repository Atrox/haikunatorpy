from random import choice
from six.moves import range


def haikunate(delimiter='-', tokenLength=4, tokenHex=False, tokenChars='0123456789'):
    """
    Generate Heroku-like random names to use in your applications.
    :param delimiter:
    :param tokenLength:
    :param tokenHex:
    :param tokenChars:
    :return: string
    """
    adjs = ['afternoon', 'aged', 'ancient', 'autumn', 'billowing',
            'bitter', 'black', 'blue', 'bold', 'broken',
            'calm', 'caring', 'cold', 'cool', 'crimson',
            'damp', 'dark', 'dawn', 'delicate', 'divine',
            'dry', 'empty', 'ephemeral', 'evening', 'falling',
            'fathomless', 'floral', 'fragrant', 'frosty', 'golden',
            'green', 'hidden', 'holy', 'icy', 'imperfect',
            'impermanent', 'late', 'lingering', 'little', 'lively',
            'long', 'majestic', 'mindful', 'misty', 'morning',
            'muddy', 'nameless', 'noble', 'old', 'patient',
            'polished', 'proud', 'purple', 'quiet', 'red',
            'restless', 'rough', 'shy', 'silent', 'silvery',
            'slender', 'small', 'smooth', 'snowy', 'solitary',
            'sparkling', 'spring', 'stately', 'still', 'strong',
            'summer', 'timeless', 'twilight', 'unknowable', 'unmovable',
            'upright', 'wandering', 'weathered', 'white', 'wild',
            'winter', 'wispy', 'withered', 'young',
            ]
    nouns = ['bird', 'breeze', 'brook', 'brook', 'bush',
             'butterfly', 'chamber', 'chasm', 'cherry', 'cliff',
             'cloud', 'darkness', 'dawn', 'dew', 'dream',
             'dust', 'eye', 'feather', 'field', 'fire',
             'firefly', 'flower', 'foam', 'fog', 'forest',
             'frog', 'frost', 'glade', 'glitter', 'grass',
             'hand', 'haze', 'hill', 'horizon', 'lake',
             'leaf', 'lily', 'meadow', 'mist', 'moon',
             'morning', 'mountain', 'night', 'paper', 'pebble',
             'pine', 'planet', 'plateau', 'pond', 'rain',
             'resonance', 'ridge', 'ring', 'river', 'sea',
             'shadow', 'shape', 'silence', 'sky', 'smoke',
             'snow', 'snowflake', 'sound', 'star', 'stream',
             'sun', 'sun', 'sunset', 'surf', 'thunder',
             'tome', 'tree', 'violet', 'voice', 'water',
             'waterfall', 'wave', 'wave', 'wildflower', 'wind',
             'wood',
             ]

    if tokenHex:
        tokenChars = "0123456789abcdef"

    adj = choice(adjs)
    noun = choice(nouns)
    token = ''.join(choice(tokenChars) for _ in range(tokenLength))

    sections = [adj, noun, token]
    return delimiter.join(filter(None, sections))
