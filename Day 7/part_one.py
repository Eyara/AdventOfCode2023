def get_n_card_idx(hand, n):
    return custom_sort_arr.index(hand[n])


def get_type(d: dict):
    if sum(d.values()) != 5:
        raise 'Not enough cards in hands!'
    sorted_d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
    sorted_keys = list(sorted_d.keys())
    if sorted_d[sorted_keys[0]] == 5:
        return 7
    elif sorted_d[sorted_keys[0]] == 4:
        return 6
    elif sorted_d[sorted_keys[0]] == 3:
        if sorted_d[sorted_keys[1]] == 2:
            return 5
        return 4
    elif sorted_d[sorted_keys[0]] == 2:
        if sorted_d[sorted_keys[1]] == 2:
            return 3
        return 2
    return 1


def get_hand_dict(hand: str) -> dict:
    d = {}

    for card in hand:
        if card in d:
            d[card] += 1
        else:
            d[card] = 1

    return d


file1 = open('input.txt', 'r')
hands = [(x.replace('\n', '').split(' ')[0], int(x.replace('\n', '').split(' ')[1])) for x in file1.readlines()]

custom_sort_arr = [str(x) for x in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']

ranked_hands = []

for hand in hands:
    ranked_hands.append(
        (hand[1],
         get_type(get_hand_dict(hand[0])),
         get_n_card_idx(hand[0], 0),
         get_n_card_idx(hand[0], 1),
         get_n_card_idx(hand[0], 2),
         get_n_card_idx(hand[0], 3),
         get_n_card_idx(hand[0], 4),
         hand[0]
         ),
    )

ranked_hands = sorted(ranked_hands, key=lambda tup: (tup[1], tup[2], tup[3], tup[4], tup[5], tup[6]), reverse=True)
ranked_hands.reverse()

result = 0

print([x[7] for x in ranked_hands])

for i in range(1, len(ranked_hands) + 1):
    result += i * ranked_hands[i - 1][0]

print(result)
