import unittest
import main
#proper name here also starts with Test...
class TestPenis(unittest.TestCase): #This in brackets makes the class have this function of Testcase
    def setUp(self):
        print("about to test the function")

    def test_do_stuff(self): ## Test method must start with 'test_'
        """PENIS ICH WILL PENIS"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self): ## Test method must start with 'test_'
        test_param = "hkgvjhg"
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self): ## Test method must start with 'test_'
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self): ## Test method must start with 'test_'
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(selfself):
        print("cleaning up")

if __name__ == "__main__":
    unittest.main()# main here has nothing to do with main
                    # it means run the file (test is main here)