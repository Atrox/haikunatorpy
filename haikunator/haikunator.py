from random import Random


class Haikunator:
    _adjectives = [
        'aged', 'ancient', 'autumn', 'billowing', 'bitter', 'black', 'blue', 'bold',
        'broad', 'broken', 'calm', 'cold', 'cool', 'crimson', 'curly', 'damp',
        'dark', 'dawn', 'delicate', 'divine', 'dry', 'empty', 'falling', 'fancy',
        'flat', 'floral', 'fragrant', 'frosty', 'gentle', 'green', 'hidden', 'holy',
        'icy', 'jolly', 'late', 'lingering', 'little', 'lively', 'long', 'lucky',
        'misty', 'morning', 'muddy', 'mute', 'nameless', 'noisy', 'odd', 'old',
        'orange', 'patient', 'plain', 'polished', 'proud', 'purple', 'quiet', 'rapid',
        'raspy', 'red', 'restless', 'rough', 'round', 'royal', 'shiny', 'shrill',
        'shy', 'silent', 'small', 'snowy', 'soft', 'solitary', 'sparkling', 'spring',
        'square', 'steep', 'still', 'summer', 'super', 'sweet', 'throbbing', 'tight',
        'tiny', 'twilight', 'wandering', 'weathered', 'white', 'wild', 'winter', 'wispy',
        'withered', 'yellow', 'young'
    ]

    _nouns = [
        'art', 'band', 'bar', 'base', 'bird', 'block', 'boat', 'bonus',
        'bread', 'breeze', 'brook', 'bush', 'butterfly', 'cake', 'cell', 'cherry',
        'cloud', 'credit', 'darkness', 'dawn', 'dew', 'disk', 'dream', 'dust',
        'feather', 'field', 'fire', 'firefly', 'flower', 'fog', 'forest', 'frog',
        'frost', 'glade', 'glitter', 'grass', 'hall', 'hat', 'haze', 'heart',
        'hill', 'king', 'lab', 'lake', 'leaf', 'limit', 'math', 'meadow',
        'mode', 'moon', 'morning', 'mountain', 'mouse', 'mud', 'night', 'paper',
        'pine', 'poetry', 'pond', 'queen', 'rain', 'recipe', 'resonance', 'rice',
        'river', 'salad', 'scene', 'sea', 'shadow', 'shape', 'silence', 'sky',
        'smoke', 'snow', 'snowflake', 'sound', 'star', 'sun', 'sun', 'sunset',
        'surf', 'term', 'thunder', 'tooth', 'tree', 'truth', 'union', 'unit',
        'violet', 'voice', 'water', 'waterfall', 'wave', 'wildflower', 'wind', 'wood'
    ]

    def __init__(self, seed=None, adjectives=None, nouns=None):
        """
        Initialize new haikunator

        :param seed: Seed for Random
        :param adjectives: Custom Adjectives
        :param nouns: Custom Nouns
        :type adjectives: list
        :type nouns: list
        """
        if adjectives is not None:
            self._adjectives = adjectives

        if nouns is not None:
            self._nouns = nouns

        self.random = Random(seed)

    def haikunate(self, delimiter='-', token_length=4, token_hex=False, token_chars='0123456789'):
        """
        Generate heroku-like random names to use in your python applications

        :param delimiter: Delimiter
        :param token_length: TokenLength
        :param token_hex: TokenHex
        :param token_chars: TokenChars
        :type delimiter: str
        :type token_length: int
        :type token_hex: bool
        :type token_chars: str
        :return: heroku-like random string
        :rtype: str
        """
        if token_hex:
            token_chars = '0123456789abcdef'

        adjective = self._random_element(self._adjectives)
        noun = self._random_element(self._nouns)
        token = ''.join(self._random_element(token_chars) for _ in range(token_length))

        sections = [adjective, noun, token]
        return delimiter.join(filter(None, sections))

    def _random_element(self, s):
        """
        Get random element from string or list

        :param s: Element
        :type s: str or list
        :return: str
        :rtype: str
        """
        if len(s) <= 0:
            return ''

        return self.random.choice(s)
