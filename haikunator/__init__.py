from random import choice
from six.moves import range


def haikunate(hex=False):
    # example output:
    # 'dawn-ring-1337'
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
    if hex:
        suffix = '0123456789abcdef'
    else:
        suffix = '0123456789'
    return ('-'.join([choice(adjs), choice(nouns),
            ''.join(choice(suffix) for x in range(4))]))
