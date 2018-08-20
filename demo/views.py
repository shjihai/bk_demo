# -*- coding: utf-8 -*-
from blueking.component.shortcuts import get_client_by_request
from common.mymako import render_mako_context, render_json
from common.log import logger

def index(request):
    """
    jobs
    """
    return render_mako_context(request, '/demo/index.html')


def apps(request):
    """
    apps
    """
    return render_mako_context(request, '/demo/apps.html')


def app_list(request):
    """
    获取业务
    """
    # 默认从django settings中获取APP认证信息：应用ID和应用TOKEN
    # 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 组件参数
    kwargs = {}
    result = client.cc.get_app_list(kwargs)
    return render_json(result)

# http://bk.tencent.com/document/bkapi/ce/system/job/get_job_list/
def job_list(request):
    """
    get jobs
    """
    # 默认从django settings中获取APP认证信息：应用ID和应用TOKEN
    # 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 组件参数
    kwargs = { "bk_biz_id": 2 }
    result = client.job.get_job_list(kwargs)
    return render_json(result)

def job_run(request):
    """
    run jobs
    """
    bk_job_id = None
    if request.POST:
        req_job_id = request.POST['bk_job_id']
        bk_job_id = int(req_job_id)
    # 默认从django settings中获取APP认证信息：应用ID和应用TOKEN
    # 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 组件参数
    if bk_job_id:
        kwargs = { "bk_biz_id": 2, "bk_job_id": bk_job_id }
        # result = {}
        result = client.job.execute_job(kwargs)
        logger.info("execute job: %s" % result)
        mail = client.cmsi.send_mail({
          "sender": "root@localhost.localdomain", 
          "receiver": "root@localhost.localdomain", 
          "title": ("run job - %s - %s" % (result['data']['job_instance_name'], result['result'])),
          "content": ("<html>%s</html>" % result)
        })
        logger.info("send mail: %s" % mail)
    else:
        result = {}
    return render_json(result)
