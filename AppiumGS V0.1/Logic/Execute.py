__author__ = 'shaonianshapnian'

from Logic import Analysis

class Test_Execute:

    def setup(self):
        analysis.connectAppium()

    def teardown(self):
        analysis.driver.quit()

    def action(self, case):
        for dic in case:
            if analysis.analysisYaml(dic)==False:
                analysis.saveScreenShot(case[0].get('case_name'))
                assert False

    @staticmethod
    def getTestFunc(case):
        def func(self):
            self.action(case)
        return func

def generateTestCases():
    case_list = analysis.getAllCase()
    for case in case_list:
        setattr(Test_Execute, 'test_%s' % (case[0].get('case_name')),Test_Execute.getTestFunc(case))

analysis = Analysis.Analysis()
generateTestCases()