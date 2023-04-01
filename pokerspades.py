
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
    if card_list[-1] - card_list[0] == 2 and card_list[-1] - card_list[1] == 1:
        return 7
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
    card_list.sort()
    if card_list[0] == card_list[1] == card_list[2]:
        return 9
    else:
        return 0
# print(check_3ofa_kind('S2', 'S2', 'S2'))
# print(check_3ofa_kind('S2', 'S3', 'S2'))
# print(check_3ofa_kind('S2', 'S2', 'S3'))
# print(check_3ofa_kind('SJ', 'SJ', 'SQ'))

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) and card_dict[card3] == 14:
        return 14
    else:
        return 0
# print(check_royal_flush('SQ', 'SK', 'SA'))
# print(check_royal_flush('SQ', 'SA', 'SK'))
# print(check_royal_flush('SJ', 'SQ', 'SK'))
# print(check_royal_flush('SQ', 'SQ', "SQ"))

def play_cards(left1, left2, left3, right1, right2, right3):
    left_player = [check_straight(left1,left2,left3), check_3ofa_kind(left1,left2,left3), check_royal_flush(left1,left2,left3)]
    right_player = [check_straight(right1,right2,right3), check_3ofa_kind(right1,right2,right3), check_royal_flush(right1,right2,right3)]
    left_player.sort(reverse=True), right_player.sort(reverse=True)
    if left_player[0] == right_player[0]:
        left_list = [left1, left2, left3]
        right_list = [right1, right2, right3]
        left_list.sort(), right_list.sort()
        if left_list[0] == right_list[0]:
            return 0
        elif left_list[0] > right_list[0]:
            return -1
        elif left_list[0] < right_list[0]:
            return 1
        else:
            return ValueError
    elif left_player[0] > right_player[0]:
        return -1
    elif left_player[0] > right_player[0]:
        return 1
    else:
        return ValueError



# print(play_cards('SQ','SJ', 'S10', 'S2', 'S2', 'S3'))
# print(play_cards('SQ','SJ', 'S10', 'SQ','SJ', 'S10'))



