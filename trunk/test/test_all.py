import sys
import unittest

sys.path.append("..")

def suite():
    modules_to_test = ("test_tools",
                       "test_crontab",
                       "test_pycron",
                      )
    alltests = unittest.TestSuite()
    for module in map(__import__, modules_to_test):
        alltests.addTest(module.suite())
    return alltests

if __name__ == "__main__":
    unittest.main(defaultTest = "suite")
