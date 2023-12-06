def load_input():
    parts = open('input.txt', 'r').readlines()
    parts = list(map(lambda x: x.strip(), parts))
    parts = list(map(lambda x: x.split(), parts))
    parts = list(map(lambda x: [x[0].strip(), int(x[1].strip())], parts))
    parts = list(map(lambda x: [[x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]], x[1]], parts))
    return parts


def freq(cards):
    res = {}
    for card in cards:
        res[card] = res.get(card, 0) + 1
    return res


def rank_cards(cards, jokers=False):
    fr = freq(cards)
    if jokers:
        jokers = fr.get('J', 0)
        if jokers > 0:
            del fr['J']
        if jokers == 5:
            return 10
        max_key = max(fr, key=fr.get)
        fr[max_key] += jokers
    vals = fr.values()
    if 3 in vals and 2 in vals:
        return 7
    if 2 in vals and len(vals) == 3:
        return 5
    return max(vals) * 2


def rank_card(card, jokers=False):
    if card == 'T':
        return 10
    if card == 'J':
        if jokers:
            return 0
        return 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14
    return int(card)


def rank_hand(cards, jokers=False):
    return (
        rank_cards(cards, jokers),
        rank_card(cards[0], jokers),
        rank_card(cards[1], jokers),
        rank_card(cards[2], jokers),
        rank_card(cards[3], jokers),
        rank_card(cards[4], jokers)
    )


def calc_winnings(hands):
    winnings = []
    for i, hand in enumerate(hands):
        winnings.append(hand[1] * (i + 1))
    return winnings


def part_1(hands):
    sorted_hands = sorted(hands, key=lambda x: rank_hand(x[0]))
    winnings = calc_winnings(sorted_hands)
    return sum(winnings)


def part_2(hands):
    sorted_hands = sorted(hands, key=lambda x: rank_hand(x[0], True))
    winnings = calc_winnings(sorted_hands)
    return sum(winnings)


assert part_1(load_input()) == 250347426
assert part_2(load_input()) == 251224870
