import random as rnd

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
card_values = (2,3,4,5,6,7,8,9,10,11,12,13,14)
card_dict = {}
for key, value in zip(cards, card_values):
    card_dict[key] = value



def check_straight(card1, card2, card3):
    card_list = [card1, card2, card3]
    card_list.sort()
    if card_list[-1] - card_list[0] == 2:
        return 7
    else:
        return 0

# print(check_straight(card_dict['S5'], card_dict['S6'], card_dict['S7']))
# print(check_straight(card_dict['SA'], card_dict['SK'], card_dict['SQ']))
# print(check_straight(card_dict['S2'], card_dict['S3'], card_dict['S6']))
def check_3ofa_kind(card1, card2, card3):
    card_list = [card1, card2, card3]
    card_list.sort()
    if card_list[0] == card_list[1] == card_list[2]:
        return 9
    else:
        return 0
# print(check_3ofa_kind(card_dict['S2'], card_dict['S2'], card_dict['S2']))
# print(check_3ofa_kind(card_dict['S2'], card_dict['S2'], card_dict['S3']))
def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3):
        card_list = [card1, card2, card3]
        card_list.sort()
        if card_list[2] == 14:
            return 14
        else:
            return 0
    else:
        return 0

# print(check_royal_flush(card_dict['SQ'], card_dict['SK'], card_dict['SA']))
# print(check_royal_flush(card_dict['S9'], card_dict['SK'], card_dict['SA']))
def play_cards(left1, left2, left3, right1, right2, right3):
    left_player = [check_straight(left1,left2,left3), check_3ofa_kind(left1,left2,left3), check_royal_flush(left1,left2,left3)]
    right_player = [check_straight(right1,right2,right3), check_3ofa_kind(right1,right2,right3), check_royal_flush(right1,right2,right3)]
    for left_hand in left_player:
        for right_hand in right_player:
            if left_hand == right_hand and right_hand != 0:
                left_list = [left1, left2, left3]
                right_list = [right1, right2, right3]
                left_list.sort()
                right_list.sort()
                if left_list[2] == right_list[2]:
                    return 0
                elif left_list[2] > right_list[2]:
                    return -1
                else:
                    return 1
            elif left_hand > right_hand:
                return -1
            elif left_hand == 0 and right_hand == 0:
                return 0
            else:
                return 1


# print(play_cards(card_dict['SQ'],card_dict['SJ'], card_dict['S10']
#                  , card_dict['S2'], card_dict['S2'], card_dict['S3']))


