import unittest
from game import cards

class TestCards(unittest.TestCase):
    def assertCard(self, card, **kwargs):
        for key, value in kwargs.items():
            self.assertEqual(value, getattr(card, key))

    def test_creating_each_card(self):
        action = cards.Action()
        ak = cards.Weapon(name='AK-47', damage=7, durability=3)
        stun = cards.BS(name='Stun')

        card_list = (action, ak, stun)
        expected_values = [{},
                           {'name': 'AK-47', 'damage': 7, 'durability':3},
                           {'name':'Stun'}]

        for card, expected_values in zip(card_list, expected_values):
            with self.subTest(card_name = repr(card)):
                self.assertCard(card, **expected_values)

    def test_use_weapon(self):
        ak = cards.Weapon(name='AK-47', damage=7, durability=3)
        ak.use()
        expected_value = {'name': 'AK-47', 'damage': 7, 'durability':2}
        self.assertCard(ak, **expected_value)

    def test_check_when_weapon_breaks(self):
        ak = cards.Weapon(name='AK-47', damage=7, durability=3)
        with self.assertRaises(AttributeError):
            while True:
                ak.use()
        self.assertTrue(ak.is_broken())

    def test_cannot_create_weapons_with_negative_damage(self):
        with self.assertRaises(ValueError):
            healing_pistol = cards.Weapon(name = 'healing_stim', damage = -5, durability = 3)

    def test_cannot_create_weapons_with_negative_durability(self):
        with self.assertRaises(ValueError):
            broken = cards.Weapon(name = 'what', damage = 4, durability = -3)


if __name__ == '__main__':
    unittest.main()