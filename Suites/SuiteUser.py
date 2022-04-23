import unittest

import users
import searchUser

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(users))
suite.addTests(loader.loadTestsFromModule(searchUser))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
