import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        maks = runner.Runner('Макс')
        for i in range(10):
            maks.walk()
        self.assertEqual(maks.distance, 50)

    def test_run(self):
        denis = runner.Runner('Денис')
        for i in range(10):
            denis.run()
        self.assertEqual(denis.distance, 100)

    def test_challenge(self):
        ivan = runner.Runner('Иван')
        sasha = runner.Runner('Саша')
        for i in range(10):
            ivan.run()
            sasha.walk()
        self.assertNotEqual(ivan.distance, sasha.distance)
