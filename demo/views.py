# -*- coding: utf-8 -*-
from blueking.component.shortcuts import get_client_by_request
from common.mymako import render_mako_context, render_json


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

