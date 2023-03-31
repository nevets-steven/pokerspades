import pokerspades
import unittest


class MyTestCase(unittest.TestCase):

    def check_straight(self):
        self.assertEqual(pokerspades.check_straight(pokerspades.card_dict['S5'],
                                                    pokerspades.card_dict['S6'],
                                                    pokerspades.card_dict['S7']))
        self.assertEqual(pokerspades.check_straight(pokerspades.card_dict['S1'],
                                                    pokerspades.card_dict['S6'],
                                                    pokerspades.card_dict['S7']))




    def check_3ofa_kind(self):
        pass

if __name__ == '__main__':
    unittest.main()
