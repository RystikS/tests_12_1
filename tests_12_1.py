from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker1 = Runner('blade_walker')
        for i in range(10):
            walker1.walk()
        self.assertEqual(walker1.distance,50)

    def test_run(self):
        runner2 = Runner('blade_runner')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):

        walker = Runner('walker_1')
        runner = Runner('runner_2')
        for i in range(10):
            walker.run()
        for i in range(10):
            runner.walk()
        self.assertNotEqual(walker.distance, runner.distance)

if __name__ == "__main__":
    unittest.main()
