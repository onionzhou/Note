#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/3 16:59
# software: PyCharm

import testlink
from testlink_test.config import POST_URL, API_KEY

# tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
tls = testlink.TestlinkAPIClient(server_url=POST_URL, devKey=API_KEY)

# print (tls.whatArgs('createTestPlan'))

# 获取链接信息
# print(tls.connectionInfo())
# 获取工程数
# print(tls.countProjects())

# 工程创建
# tls.createTestProject(testprojectname='project_4', testcaseprefix='project',
#                       notes='描述信息用于project_4', active=1, public=1,
#                       options={'requirementsEnabled': 1, 'testPriorityEnabled': 1,
#                                'automationEnabled': 1, 'inventoryEnabled': 1}
#                       )
#删除工程
# tls.deleteTestProject(prefix='project')
#获取工程
# projects =tls.getProjects()
# for i in projects:
#     print(i.get('name'))

#测试计划
#@decoMakerApiCallWithArgs(['testplanname'],
#                    ['testprojectname', 'prefix', 'note', 'active', 'public'])
# s =tls.createTestPlan('testplan_2',testprojectname='project_4',notes='测试计划2的描述信息'
#                    ,active=1,public=1)
# print(s)

#删除测试计划
# s =tls.deleteTestPlan(testplanid=10)
# print(s)

# @decoMakerApiCallWithArgs(['testprojectname', 'testplanname'])
s=tls.getTestPlanByName('project_4','test_plan_1')
print(s)