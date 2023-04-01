from pokerspades import *
import unittest


class MyTestCase(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S5', 'S7', 'S6'), 7)
        self.assertEqual(check_straight('S5', 'S7', 'S7'), 7)  # fail
        self.assertEqual(check_straight('S7', 'S7', 'S7'), 7)  # fail

    def test_check_3kind(self):
        self.assertEqual(check_3ofa_kind('S7', 'S7', 'S7'), 9)
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('S9', 'S2', 'S9'), 0)
        self.assertEqual(check_3ofa_kind('S9', 'S2', 'S9'), 9)  # fail
        self.assertEqual(check_3ofa_kind('S7', 'S7', 'S2'), 9)  # fail

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SQ', 'SK', 'SA'), 14)
        self.assertEqual(check_royal_flush('SQ', 'SA', 'SA'), 14)
        self.assertEqual(check_royal_flush('SQ', 'SK', 'SA'), 14)
        self.assertEqual(check_royal_flush('SQ', 'S2', 'SA'), 0)
        self.assertEqual(check_royal_flush('SA', 'SK', 'SA'), 14)  # fail
        self.assertEqual(check_royal_flush('SQ', 'SK', 'SA'), 0)  # fail

    def test_play_cards(self):
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S3', 'S4', 'S5'), 1)
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S2', 'S3', 'S4'), 0)
        self.assertEqual(play_cards('SQ', 'SK', 'SA', 'SQ', 'SK', 'SA'), 1)  # fail, correct 0
        self.assertEqual(play_cards('S3', 'S4', 'S5', 'S2', 'S3', 'S4'), 1)  # fail, correct: 1
        self.assertEqual(play_cards('S2', 'S2', 'S2', 'S3', 'S3', 'S3'), 1)
        self.assertEqual(play_cards('S4', 'S4', 'S4', 'S4', 'S4', 'S4'), 1)  # fail, correct 0

        self.assertEqual(play_cards('SA', 'SA', 'SA', 'SA', 'SK', 'SQ'), 1)
        self.assertEqual(play_cards('S3', 'S4', 'S5', 'SA', 'SK', 'SQ'), 0)  # fail, correct 1

        self.assertEqual(play_cards('S3', 'S4', 'S5', 'S2', 'S2', 'S2'), 1)
        self.assertEqual(play_cards('S3', 'S4', 'S5', 'S2', 'S2', 'S2'), -1)  # fail, correct 1
        self.assertEqual(play_cards('S6', 'S8', 'S7', 'S9', 'S9', 'S9'), 0)  # fail, correct 1

if __name__ == '__main__':
    unittest.main()
