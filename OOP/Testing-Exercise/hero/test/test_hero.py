from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Skillet", 5, 100, 1000)
        self.enemy_hero = Hero("Enemy", 1, 1, 1)

    def test_initializing(self):
        self.assertEqual(self.hero.username, "Skillet")
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 1000)

    def test_name_of_the_enemy_is_it_like_mine(self):
        self.enemy_hero.username = "Skillet"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_is_it_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_health_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_if_both_players_health_is_zero(self):
        self.hero.health = 1

        self.assertEqual(self.hero.battle(self.enemy_hero), "Draw")
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy_hero.health, -4999)

    def test_if_we_win(self):
        self.assertEqual(self.hero.battle(self.enemy_hero), "You win")
        self.assertEqual(self.hero.health, 104)
        self.assertEqual(self.enemy_hero.health, -4999)

    def test_if_enemy_win(self):
        self.hero.health = 1
        self.hero.level = 1
        self.hero.damage = 1
        self.enemy_hero.health = 100

        self.assertEqual(self.hero.battle(self.enemy_hero), "You lose")
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy_hero.health, 104)

    def test__str__(self):
        result = self.hero.__str__()
        expected = "Hero Skillet: 5 lvl\n" \
                   "Health: 100\n" \
                   "Damage: 1000\n"

        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
