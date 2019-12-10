#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/9 16:25
# software: PyCharm

import testlink
from testlink_test.config import POST_URL, API_KEY


def con_testlink():
    '''正常连接使用'''
    tl = testlink.TestLinkHelper(server_url=POST_URL, devkey=API_KEY)
    tls = tl.connect(testlink.TestlinkAPIClient)

    s = tls.getTestPlanByName('project_4', 'test_plan_1')

    print(s)


def con_testlink():
    '''直接使用api 连接'''
    tls = testlink.TestlinkAPIClient(server_url=POST_URL, devKey=API_KEY)
    return tls


def create_platform(tls):
    tls.createPlatform('project_4', 'windows', notes='用于windows平台')


def create_build(tls):
    '''
    :param tls:
    :return:
    '''
    ret = tls.getTestPlanByName('project_4', 'test_plan_1')
    testplanid = ret[0].get('id')
    buildname = 'v2.0.0'
    buildnotes = '这是第二个版本'
    releasedate = '2019-12-10'

    # @decoMakerApiCallWithArgs(['testplanid', 'buildname'],
    #                          ['buildnotes', 'active', 'open', 'releasedate',
    #                          'copytestersfrombuild'])
    ret = tls.createBuild(testplanid, buildname, buildnotes, releasedate=releasedate)
    print(ret)
    # ret
    # [{'id': 2, 'operation': 'createBuild', 'status': True, 'message': 'Success!'}]


def create_testsuit(tls):
    project_name = 'project_4'
    project_id = tls.getProjectIDByName(project_name)
    # print(project_id)
    # @decoMakerApiCallWithArgs(['testprojectid', 'testsuitename', 'details'],
    #                           ['parentid', 'order', 'checkduplicatedname',
    #                            'actiononduplicatedname'])
    testsuitename = '控制'
    details = '控制模块测试'
    ret = tls.createTestSuite(project_id, testsuitename, details)
    print(ret)
    # ret =
    # [{'id': 46, 'message': 'ok', 'operation': 'createTestSuite',
    # 'status': True, 'additionalInfo': '', 'name': '', 'name_changed': False}]


def del_testsuit(tls):
    pass


def get_testsuitid(tls):
    project_name = 'project_4'
    prefix = 'project'
    testsuitname = 'http'
    ret =tls.getTestSuite(testsuitname,prefix)
    return ret[0]['id']
    # print(ret)

def create_testcase(tls):
    MANUAL = 1
    AUTOMATED = 2
    LOW=1
    MEDIUM=2
    HIGH=3
    rework=4
    projectname = 'project_4'
    prefix = 'project'
    testsuitname = 'http'

    testcasename = 'http_ip'
    authorlogin = 'onion'
    test_suites = tls.getTestSuite(testsuitname, prefix)
    test_suite_id = test_suites[0]['id']
    project_id = tls.getProjectIDByName(projectname)


    tls.initStep("Step action 1", "Step result 1", AUTOMATED)
    tls.appendStep("Step action 2", "Step result 2", AUTOMATED)
    tls.appendStep("Step action 3", "Step result 3", AUTOMATED)
    tls.appendStep("Step action 4", "Step result 4", AUTOMATED)
    tls.appendStep("Step action 5", "Step result 5", AUTOMATED)

    # @decoMakerApiCallWithArgs(['testcasename', 'testsuiteid', 'testprojectid',
    # 'authorlogin', 'summary', 'steps'],
    # ['preconditions', 'importance', 'executiontype', 'order',
    #  'internalid', 'checkduplicatedname', 'actiononduplicatedname',
    #  'status', 'estimatedexecduration'])

    # status: 1(draft) 草稿
    # 2(readyForReview) 待评审
    # 3(reviewInProgress) 评审中
    # 4(rework) 重做
    # 5(obsolete) 过时的
    # 6(future)
    # 7(final) 终稿
    ret = tls.createTestCase(testcasename, test_suite_id, project_id, authorlogin
                             , 'http_ip 使用', preconditions='先决调解',importance=MEDIUM,
                             executiontype=AUTOMATED,status=rework)

def create_testcase2(tls):
    MANUAL = 1
    AUTOMATED = 2
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    rework = 4
    projectname = 'project_4'
    prefix = 'project'
    testsuitname = 'http'

    testcasename = 'http_ip2'
    authorlogin = 'onion'
    test_suites = tls.getTestSuite(testsuitname, prefix)
    test_suite_id = test_suites[0]['id']
    project_id = tls.getProjectIDByName(projectname)
    steps=[ {'step_number': 1, 'actions': "action A",'expected_results': "result A", 'execution_type': 2},
            {'step_number': 2, 'actions': "action B",'expected_results': "result B", 'execution_type': 1},
            {'step_number': 3, 'actions': "action C",'expected_results': "result C", 'execution_type': 2}
          ]
    ret = tls.createTestCase(testcasename, test_suite_id, project_id, authorlogin
                             , 'http_ip 使用',steps=steps ,preconditions='先决调解', importance=MEDIUM,
                             executiontype=AUTOMATED, status=rework)
    print(ret)
    # ret=
    # [{'id': 62, 'status': True, 'message': 'Success!',
    #   'additionalInfo': {'external_id': '4', 'has_duplicate': False, 'external_id_already_exists': False, 'id': 62,
    #                      'version_number': 1, 'status_ok': 1, 'tcversion_id': 63, 'msg': 'ok', 'new_name': '',
    #                      'update_name': False}, 'operation': 'createTestCase'}]

def del_testcase(tls):
    pass


if __name__ == '__main__':
    tls = con_testlink()
    # create_platform(tls)
    # create_build(tls)
    # create_testsuit(tls)
    # get_testsuitid(tls)
    # create_testcase(tls)
    # create_testcase2(tls)
    r=get_testsuitid(tls)
    print(r)
    print(tls.countTestSuites())