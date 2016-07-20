# blackjack.py written by Seth Guberman for Coder Radio ep. 214 challenge
# https://www.reddit.com/r/CoderRadio/comments/4t7oyt/episode_214_coding_challenge/


def build_strategy():
    '''Build the strategy lookup table from http://www.blackjack-chart.com/'''

    # Player hands are 'rows' from the table
    hands = dict()
    hands['8'] = 'H H H H H H H H H H'
    hands['9'] = 'H D D D D H H H H H'
    hands['10'] = 'D D D D D D D D H H'
    hands['11'] = 'D D D D D D D D D D'
    hands['12'] = 'H H S S S H H H H H'
    hands['13'] = 'S S S S S H H H H H'
    hands['14'] = 'S S S S S H H H H H'
    hands['15'] = 'S S S S S H H H XH XH'
    hands['16'] = 'S S S S S H H XH XH XH'
    hands['17'] = 'S S S S S S S S S XS'
    hands['A2'] = 'H H H D D H H H H H'
    hands['A3'] = 'H H H D D H H H H H'
    hands['A4'] = 'H H D D D H H H H H'
    hands['A5'] = 'H H D D D H H H H H'
    hands['A6'] = 'H D D D H H H H H H'
    hands['A7'] = 'S DS DS DS DS S S H H H'
    hands['A8'] = 'S S S S S S S S S S'
    hands['A9'] = 'S S S S S S S S S S'
    hands['22'] = 'SP SP SP SP SP SP H H H H'
    hands['33'] = 'SP SP SP SP SP SP H H H H'
    hands['44'] = 'H H H SP SP H H H H H'
    hands['55'] = 'D D D D D D D D H H'
    hands['66'] = 'SP SP SP SP SP H H H H H'
    hands['77'] = 'SP SP SP SP SP SP H H H H'
    hands['88'] = 'SP SP SP SP SP SP SP SP SP XP'
    hands['99'] = 'SP SP SP SP SP S SP SP S S'
    hands['1010'] = 'S S S S S S S S S S'
    hands['AA'] = 'SP SP SP SP SP SP SP SP SP SP'

    # Dealer cards are the 'column' headers
    dealer_head = '2 3 4 5 6 7 8 9 10 A'

    # Make one big nested dict by zipping dealer and player cards
    strategy = {k: dict(zip(dealer_head.split(), v.split()))
                for k, v in hands.items()}

    return strategy


# Build the lookup tables at import so we only have to do it once
strategy = build_strategy()
strategy_key = {
    'H': 'Hit',
    'S': 'Stand',
    'D': 'Double if allowed, otherwise Hit',
    'DS': 'Double if allowed, otherwise Stand',
    'SP': 'Split',
    'XH': 'Surrender if allowed, otherwise Hit',
    'XP': 'Surrender if allowed, otherwise Split',
    'XS': 'Surrender if allowed, otherwise Stand',
    }


def get_strategy(your_hand, dealer_card):
    '''Get the strategy from the table.

    your_hand (string): can be total hand or two cards
    dealer_card (string): card that the dealer is showing
    '''

    return strategy_key[strategy[your_hand][dealer_card]]


def get_input():
    '''Get and sanitize user input for lookup.'''

    your_hand = input('Enter your total or two cards separated by a space: ')
    delim = ',' if ',' in your_hand else ' '  # just in case they enter a comma
    your_hand = ''.join(your_hand.split(delim)).upper()  # match strategy keys
    dealer_card = input('Enter dealer card: ')

    return your_hand, dealer_card


if __name__ == '__main__':

    while True:
        try:
            advice = get_strategy(*get_input())
            print('You should {}.\n'.format(advice))
        except KeyError:  # input cards are not in the table
            print('That card combination is not valid, try again.\n')
