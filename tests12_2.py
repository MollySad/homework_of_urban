import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first_runner = runner_and_tournament.Runner('Усэйн', 10)
        self.second_runner = runner_and_tournament.Runner('Андрей', 9)
        self.third_runner = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                print(f'{key}: {value.name}')

    def test_run1(self):
        race = runner_and_tournament.Tournament(90, self.first_runner, self.third_runner)
        result = race.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['run1'] = result


    def test_run2(self):
        race = runner_and_tournament.Tournament(90, self.second_runner, self.third_runner)
        result = race.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['run2'] = result

    def test_run3(self):
        race = runner_and_tournament.Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        result = race.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['run3'] = result
