from httprunner.api import HttpRunner
runner = HttpRunner(failfast=False)
runner.run("testsuites/testsuit_0530_homework05.yml")