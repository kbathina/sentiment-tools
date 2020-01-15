import unittest
import test_afinn
import test_anew
import test_gpoms
import test_opinionfinder
import test_vader

loader = unittest.TestLoader()
suite  = unittest.TestSuite()


suite.addTests(loader.loadTestsFromModule(test_afinn))
suite.addTests(loader.loadTestsFromModule(test_gpoms))
suite.addTests(loader.loadTestsFromModule(test_anew))
suite.addTests(loader.loadTestsFromModule(test_opinionfinder))
suite.addTests(loader.loadTestsFromModule(test_vader))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)