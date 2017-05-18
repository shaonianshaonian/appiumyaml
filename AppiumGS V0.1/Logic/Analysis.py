__author__ = 'shaonianshaonian'

from Logic import Base
from time import sleep
import yaml
import os

class Analysis(Base.Base):
    value_list = [] #用来存储读取的属性值

    def analysisYaml(self,dic):
        if dic['test_action'] == 'click':
            # 点击
            test_control_id = dic['test_control_id']
            test_control_type = dic['test_control_type']
            return self.clickButton((test_control_type,test_control_id))
        elif dic['test_action'] == 'write':
            # 发送文本
            test_control_type = dic['test_control_type']
            test_control_id = dic['test_control_id']
            test_value = dic['test_value']
            return self.sendKeys((test_control_type,test_control_id), str(test_value))
        elif dic['test_action'] == 'swipeUp':
            # 向上滑动
            self.swipeUp()
        elif dic['test_action'] == 'swipeDown':
            # 向下滑动
            self.swipeDown()
        elif dic['test_action'] == 'swipeLeft':
            # 向左滑动
            self.swipeLeft()
        elif dic['test_action'] == 'swipeRight':
            # 向右滑动
            self.swipeRight()
        elif dic['test_action'] == 'sleep':
            # 等待
            test_value = dic['test_value']
            sleep(test_value)
        elif dic['test_action'] == 'assert':
            # 断言
            if dic['test_assert_type'] == 'control':
                test_control_id = dic['test_control_id']
                test_control_type = dic['test_control_type']
                test_assert_result = dic['test_assert_result']
                if self.find_element((test_control_type,test_control_id)):
                    if test_assert_result == 'no':
                        return False
                    else:
                        return True
                else:
                    if test_assert_result == 'no':
                        return True
                    else:
                        return False
            elif dic['test_assert_type'] == 'compare':
                test_list_id1 = dic['test_list_id1']
                test_list_id2 = dic['test_list_id2']
                test_assert_result = dic['test_assert_result']
                if self.value_list[test_list_id1] == self.value_list[test_list_id2]:
                    if test_assert_result == 'no':
                        return False
                    else:
                        return True

        elif dic['test_action'] == 'read':
            # 读属性值并写入List
            test_control_id = dic['test_control_id']
            test_control_type = dic['test_control_type']
            test_list_id = dic['test_list_id']
            if self.getAttribute((test_control_type,test_control_id))!=False:
                self.value_list.insert(test_list_id,self.getAttribute((test_control_type,test_control_id)))
                return True
            else:
                return False
        elif dic['test_action'] == 'addValue':
            # 给list增加value
            test_value = dic['test_value']
            test_list_id = dic['test_list_id']
            self.value_list.insert(test_list_id,str(test_value))

    def getCase(self,path_yaml):
        case = []
        with open(path_yaml,encoding='utf-8') as f:
            for dic in yaml.load(f):
                if isinstance(dic, dict):
                    case.append(dic)
                else:
                    print('getCase:error')
        return case

    def getAllCase(self):
        case_list = []
        for filename in os.listdir('../TestCase'):
            if not filename.endswith('.yaml'):
                continue
            case = self.getCase('../TestCase/'+filename)
            case[0]['case_name']=filename #首dic中存放用例名
            case_list.append(case)
        return case_list