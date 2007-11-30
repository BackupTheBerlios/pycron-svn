import unittest
import sys

sys.path.append("..")

import tools

class ToolsTestCase(unittest.TestCase):
    def check_getValueStringFromValues(self):
        """ getValueStringFromValues """
        values = [False,True,True,False,True,True,True]
        self.assertEqual(tools.getValueStringFromValues(values, 0, 6), "1-2,4-6")

def makeTestSuite():
    return unittest.makeSuite(ToolsTestCase, "check")

def suite():
    return makeTestSuite()

if __name__ == "__main__":
    unittest.main(defaultTest = "suite")
