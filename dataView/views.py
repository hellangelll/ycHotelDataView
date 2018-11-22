# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
import json
from utils.sql_opt import SqlOpt

# Create your views here.
def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    list = [{'id': 1, 'name': 'Jack', 'age':'15'}, {'id': 2, 'name': 'Rose', 'age':'25'}]
    return render_to_response('student.html',{'students': list})

def index(request):
    if request.POST:
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
        context = {
            'startDate':startDate,
            'endDate':endDate
        }
    else:
        startDate = '2000-01'
        endDate = '2030-12'
        context = {}

    sql = '''SELECT "sum"(CASE WHEN t1.rzljz=0 THEN 1 ELSE 0 END)
            ,"sum"(CASE WHEN t1.rzljz > 0 AND t1.rzljz <= 10 THEN 1 ELSE 0 END)
            ,"sum"(CASE WHEN t1.rzljz > 10 AND t1.rzljz <= 20 THEN 1 ELSE 0 END)
            ,"sum"(CASE WHEN t1.rzljz > 20 AND t1.rzljz <= 30 THEN 1 ELSE 0 END)
            ,"sum"(CASE WHEN t1.rzljz > 30 AND t1.rzljz <= 40 THEN 1 ELSE 0 END) 
            ,"sum"(CASE WHEN t1.rzljz > 40 AND t1.rzljz <= 50 THEN 1 ELSE 0 END) 
            ,"sum"(CASE WHEN t1.rzljz > 50 AND t1.rzljz <= 60 THEN 1 ELSE 0 END) 
            ,"sum"(CASE WHEN t1.rzljz > 60 AND t1.rzljz <= 70 THEN 1 ELSE 0 END) 
            ,"sum"(CASE WHEN t1.rzljz > 70 AND t1.rzljz <= 80 THEN 1 ELSE 0 END) 
            ,"sum"(CASE WHEN t1.rzljz > 80 AND t1.rzljz <= 90 THEN 1 ELSE 0 END) 
            ,"sum"(CASE WHEN t1.rzljz > 90 AND t1.rzljz <= 100 THEN 1 ELSE 0 END) 
            FROM (SELECT qiyebianma, "sum"(average)/"count"(1) rzljz FROM hotel_ruzhulv_average WHERE 
            months>= '%s' AND months<= '%s' GROUP BY qiyebianma) t1;''' % (startDate,endDate)
    result = SqlOpt().select(sql)
    if context:
        result.append(context)
    return render(request, 'templates/index.html', {'result': json.dumps(result)})

def index_two(request):
    result = {}
    return render(request, 'templates/index_two.html', {'result': json.dumps(result)})

def index_check(request):
    if request.is_ajax() and request.method == 'POST':
        scqy = request.POST.getlist('scqy')[0]
        ymmc = request.POST.getlist('ymmc')[0]
        ympch = request.POST.getlist('ympch')[0]

        sql = '''SELECT vacc_name,gui_ge,pi_hao,you_xiao_qi,shen_chan_qi_ye,qian_fa_jie_lun FROM vaccine_detail WHERE vacc_name LIKE '%%%s%%' AND pi_hao LIKE '%%%s%%' AND shen_chan_qi_ye LIKE '%%%s%%' LIMIT 10;''' % (ymmc, ympch,scqy)
        # print(sql)
        result = SqlOpt().select(sql)
        # print(result)
        return HttpResponse(json.dumps(result, ensure_ascii=False))

def index_hotel(request):
    result = {}
    return render(request, 'templates/index_hotel.html', {'result': json.dumps(result)})


def index_hotel_check(req):
    if req.is_ajax() and req.method == 'POST':
        jdmc = req.POST.getlist('jdmc')[0]

        sql = '''select qiyemc,company_name,farenmc,lianxidh,xiangxidizhi,last_one_months_average,last_two_months_average,last_three_months_average,last_four_months_average,last_five_months_average,last_six_months_average,last_seven_months_average,last_eight_months_average,last_nine_months_average,last_ten_months_average,last_eleven_months_average,last_twelve_months_average,last_years_average,last_half_years_average,room_mean_price,room_median_price,dmzpmc from t_hotel_white_list where qiyemc like '%%%s%%' or dmzpmc like '%%%s%%' limit  10;''' % (jdmc,jdmc)

        result = SqlOpt().select(sql)
        return  HttpResponse(json.dumps(result, ensure_ascii=False))