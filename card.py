'''
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
 
metro_areas = [
    ['Tokyo', 'JP', 36.933, (35.689722, 139.691667)],
    ['Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)],
    ['Mexico City', 'MX', 20.142, (19.433333, -99.133333)],
    ['New York-Newark', 'US', 20.104, (40.808611, -74.020386)],
    ['Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)],
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

   '''
print(2*(6.41-3.73)/(6.41+3.73))

