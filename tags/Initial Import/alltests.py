import unittest

def suite():
    modules_to_test = ('test_pycron',
                       'test_crontab',
                       )
    alltests = unittest.TestSuite()
    for module in map(__import__, modules_to_test):
        alltests.addTest(module.suite())
    return alltests

if __name__ == '__main__':
    unittest.main(defaultTest = "suite")
    #import sys
    #if not unittest.TextTestRunner().run(suite()).wasSuccessful():
    #    sys.exit(1)
