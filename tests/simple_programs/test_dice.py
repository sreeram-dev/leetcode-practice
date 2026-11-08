from simple_programs.dice import roll_dice


class TestDice:

    def test_roll_within_six(self):
        for i in range(10):
            assert 1 <= roll_dice() <= 6