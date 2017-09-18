# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description
# file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
# If more than 3 tests fail, it should be because multiple of the test methods
# address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try
# to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

# I worked with Jacob Haspiel and Saul Hankins on the tests
# Lines 108-113 are the idea of Jacob HaspielS

###########


class Problem1(unittest.TestCase):
    def test_card_instance_vars(self):
        cd = Card()
        c = Card(3, 11)
        self.assertEqual(cd.suit, "Diamonds")
        self.assertEqual(cd.rank, 2)
        self.assertEqual(c.rank, "Jack")
        self.assertEqual(c.rank_num, 11)
        self.assertEqual(c.__str__(), "Jack of Spades")

    def test_card_class_vars(self):
        c = Card()
        self.assertEqual(type(c.suit_names), list)
        self.assertTrue("Hearts" in c.suit_names)
        self.assertEqual(type(c.rank_levels), list)
        self.assertEqual(len(c.rank_levels), 13)
        for e in c.rank_levels:
            self.assertTrue(type(e) is int)
        self.assertEqual(type(c.faces), dict)
        for k, v in c.faces.items():
            self.assertTrue(type(k) is int)
            self.assertTrue(type(v) is str)

    def test_deck_init(self):
        d = Deck()
        self.assertEqual(type(d.cards), list)
        for e in d.cards:
            self.assertIsInstance(e, type(Card()))
        self.assertIsInstance(d, type(Deck()))

    def test_deck_str_(self):
        d = Deck()
        self.assertEqual(len(d.__str__().split('\n')), 52)
        self.assertTrue("Jack of Spades" in d.__str__())

    def test_pop_card(self):
        d = Deck()
        dck = Deck()
        cd = d.cards[51]
        d.pop_card()
        for e in range(0, 52):
            dck.pop_card()
        self.assertEqual(len(d.cards), 51)
        self.assertNotEqual(d.cards[50], cd)
        self.assertEqual(len(dck.cards), 0)

    def test_shuffle(self):
        d = Deck()
        cd = d.cards[2]
        d.shuffle()
        self.assertNotEqual(d.cards[2], cd)

    def test_replace_card(self):
        d = Deck()
        c = Card(2, 5)
        d.replace_card(c)
        self.assertTrue(len(d.cards) == 52)
        cd = d.cards[4]
        d.pop_card(4)
        self.assertTrue(cd not in d.cards)
        d.replace_card(cd)
        self.assertTrue(cd in d.cards)

    def test_sort_cards(self):
        d = Deck()
        c = d.cards[5]
        d.pop_card(5)
        d.sort_cards()
        ct = 0
        for e in d.cards:
            if ct < 12:
                self.assertEqual(e.suit, "Diamonds")
            elif ct < 25:
                self.assertEqual(e.suit, "Clubs")
            elif ct < 38:
                self.assertEqual(e.suit, "Hearts")
            else:
                self.assertEqual(e.suit, "Spades")
            ct += 1
        self.assertTrue(len(d.cards) is 51)

    def test_deal_hand(self):
        d = Deck()
        hd = d.deal_hand(5)
        self.assertEqual(len(hd), 5)
        self.assertEqual(len(d.cards), 47)
        dd = Deck()
        try:
            hnd = dd.deal_hand(27)
            result = True
        except:
            result = False
        self.assertEqual(result, True)

    def test_war_game(self):
        pwg = play_war_game(testing=True)
        self.assertEqual(type(pwg), tuple)
        self.assertTrue(pwg[1] < 52)
        self.assertTrue(pwg[2] < 52)
        self.assertEqual(len(pwg), 3)
        self.assertTrue(pwg[0] in "Player1Player2Tie")

    def test_show_song(self):
        ss = show_song()
        ss1 = show_song('running')
        self.assertIsInstance(ss, helper_functions.Song)
        self.assertNotEqual(ss, ss1)

unittest.main(verbosity=2)
