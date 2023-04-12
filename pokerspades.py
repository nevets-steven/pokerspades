
card_dict = {'S2': 2,
             'S3': 3,
             'S4': 4,
             'S5': 5,
             'S6': 6,
             'S7': 7,
             'S8': 8,
             'S9': 9,
             'S10': 10,
             'SJ': 11,
             'SQ': 12,
             'SK': 13,
             'SA': 14}




def check_straight(card1, card2, card3):
    card_list = [card_dict[card1], card_dict[card2], card_dict[card3]]
    card_list.sort()
    if card_list[0] + 1 == card_list[1] and card_list[1] + 1 == card_list[2]:
        return card_list[2]
    else:
        return 0

# print(check_straight('S5', 'S6', 'S7'))
# print(check_straight('S7', 'S6', 'S5'))
# print(check_straight('S5', 'S5', 'S7'))
# print(check_straight('S7', 'S5', 'S7'))
# print(check_straight('S5', 'S7', 'S9'))
# print(check_straight('S5', 'S7', 'S9'))

def check_3ofa_kind(card1, card2, card3):
    card_list = [card_dict[card1], card_dict[card2], card_dict[card3]]
    if card_list[0] == card_list[1] == card_list[2]:
        return card_list[0]
    else:
        return 0
# print(check_3ofa_kind('S2', 'S2', 'S2'))
# print(check_3ofa_kind('S2', 'S3', 'S2'))
# print(check_3ofa_kind('S2', 'S2', 'S3'))
# print(check_3ofa_kind('SJ', 'SJ', 'SQ'))

def check_royal_flush(card1, card2, card3):
    card_list = [card_dict[card1], card_dict[card2], card_dict[card3]]
    if check_straight(card1, card2, card3) and 14 in card_list:
        return 14
    else:
        return 0
# print(check_royal_flush('SQ', 'SK', 'SA'))
# print(check_royal_flush('SQ', 'SA', 'SK'))
# print(check_royal_flush('SJ', 'SQ', 'SK'))
# print(check_royal_flush('SQ', 'SQ', "SQ"))

def play_cards(left1, left2, left3, right1, right2, right3):
    left_str = check_straight(left1, left2, left3)
    left_3kind = check_3ofa_kind(left1, left2, left3)
    left_royal = check_royal_flush(left1, left2, left3)
    right_str = check_straight(right1, right2, right3)
    right_3kind = check_3ofa_kind(right1, right2, right3)
    right_royal = check_royal_flush(right1, right2, right3)

    if left_royal == 14 and right_royal == 0:
        return -1
    if right_royal == 14 and left_royal == 0:
        return 1
    if left_3kind > 0 and right_3kind > 0:
        if right_3kind > right_3kind:
            return -1
        elif left_3kind < right_3kind:
            return 1
        else:
            return 0
    if left_str > 0 and right_3kind > 0:
        return -1
    if right_str > 0 and left_3kind > 0:
        return 1

    # all else game ends in draw

    return 0

# print(play_cards('SQ','SJ', 'S10', 'S2', 'S2', 'S3'))
# print(play_cards('SQ','SJ', 'S10', 'SQ','SJ', 'S10'))



