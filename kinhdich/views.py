import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from kinhdich.forms import *
from tutru.models import *
from tuvi.models import *
from kinhdich.models import KINHDICH
# Create your views here.
from blog_feng_shui.AmLich import *
from django.core import *


def index(request):
  mform = KinhDichForm()
  title = 'Kinh Dịch'

  if request.method == "POST":
    # json_data.append(dic_data)
    print(request.POST)
    dic_data = {}
    vieccanhoi = request.POST['vieccanhoi']
    year = int(request.POST['year'])
    month = int(request.POST['month'])
    day = int(request.POST['day'])
    hours = int(request.POST['hours'])
    minute = int(request.POST['minute'])
    timezone_TG = "7.0"
    tietkhi = request.POST['tietkhi']
    get_lunar_day = int(request.POST['get_lunar_day'])
    get_lunar_month = int(request.POST['get_lunar_month'])
    get_lunar_year = int(request.POST['get_lunar_year'])

    if vieccanhoi == '':
        vieccanhoi = 'Tham gia Nguyên Cát hội quán để được hỗ trợ luận giải miễn phí'
    # Đổi ngày dd/mm/yyyy ra số ngày Julius jd
    calendar_Julius = jdFromDate(day,month,year)
    try:
        timezone = int(float(timezone_TG))
    except:
        timezone = 0
    calendar_lunar = S2L(day, month, year, timezone)

    day_lunar = get_lunar_day
    month_lunar = get_lunar_month
    year_lunar = get_lunar_year
    # Tìm ngày bắt đầu tháng 11 âm lịch
    day_LunarMonth11 = getLunarMonth11(year_lunar,timezone)
    can_ngay = day_can(day,month,year)
    chi_ngay = day_chi(day,month,year)
    can_thang = mont_can(month_lunar,year_lunar)
    chi_thang = mont_chi(month_lunar)
    can_nam = year_can(year_lunar)
    chi_nam = year_chi(year_lunar)
    can_gio = hours_can(hours ,can_ngay)
    chi_gio = hours_chi(hours)

    que_ho = KINHDICH.tongquehaohotro(chi_gio,day_lunar,month_lunar,chi_nam)
    que_kq = KINHDICH.tongquehaoketqua(chi_gio,day_lunar,month_lunar,chi_nam)
    ten_que = KINHDICH.tenque(chi_gio,day_lunar,month_lunar,chi_nam,can_ngay,chi_ngay)
    amdong_haodong = KINHDICH.amdonghaodong(chi_gio,day_lunar,month_lunar,chi_nam,can_ngay,chi_ngay,chi_thang)
    luc_thu = KINHDICH.lucthu(can_ngay)
    que_chinh = KINHDICH.amdonghaodong(chi_gio,day_lunar,month_lunar,chi_nam,can_ngay,chi_ngay,chi_thang)
    quai_than = KINHDICH.quaithan(chi_gio,day_lunar,month_lunar,chi_nam,can_ngay,chi_ngay)
    print("lichtietkhi : ",KINHDICH.lichtietkhi(hours,minute,day,month,year))
    kv_quechinh = {}
    for key,val in ten_que['quechinh'][6].items():
        chi_khac = (val[0]).upper()
        kv_quechinh[key] = KINHDICH.khongvong(can_ngay,chi_ngay,chi_khac)
    kv_quekq = {}
    for key,val in ten_que['quekq'][6].items():
        chi_khac = (val[0]).upper()
        kv_quekq[key] = KINHDICH.khongvong(can_ngay,chi_ngay,chi_khac)
    nguyet_lenh = KINHDICH.xacdinhnguhanh(chi_thang)
    nhat_than = KINHDICH.xacdinhnguhanh(chi_ngay)
    lich_tiet_khi = KINHDICH.lichtietkhi(hours,minute,day,month,year)

    dic_data['vieccanhoi'] = vieccanhoi
    dic_data['year'] = year
    dic_data['month'] = month
    dic_data['day'] = day
    dic_data['hours'] = hours
    dic_data['minute'] = minute
    dic_data['day_lunar'] = day_lunar
    dic_data['month_lunar'] = month_lunar
    dic_data['year_lunar'] = year_lunar
    dic_data['can_ngay'] = can_ngay.capitalize()
    dic_data['chi_ngay'] = chi_ngay.capitalize()
    dic_data['can_thang'] = can_thang.capitalize()
    dic_data['chi_thang'] = chi_thang.capitalize()
    dic_data['can_nam'] = can_nam.capitalize()
    dic_data['chi_nam'] = chi_nam.capitalize()
    dic_data['can_gio'] = can_gio.capitalize()
    dic_data['chi_gio'] = chi_gio.capitalize()
    # dic_data['tietkhi'] = tietkhi.capitalize()
    dic_data['que_chinh'] = que_chinh
    dic_data['que_ho'] = que_ho
    dic_data['que_kq'] = que_kq
    dic_data['ten_que'] = ten_que
    dic_data['luc_thu'] = luc_thu
    dic_data['kv_quechinh'] = kv_quechinh
    dic_data['kv_quekq'] = kv_quekq
    dic_data['nguyet_lenh'] = lich_tiet_khi
    dic_data['nhat_than'] = nhat_than

    # return render(request, "kinhdich/kinhdich_partial.html",
    # {
    #     'kinhdich_array': dic_data
    # })
    objjson = {'success': True,'check_field': dic_data}
    return HttpResponse(json.dumps(objjson))
  return render(request, "kinhdich/index.html", {
        'form': mform,
        'form_name': mform.__class__.__name__,
        'title':title,
        # 'can_ngay': can_ngay,
        # 'chi_ngay': chi_ngay,
    })

# https://github.com/baothi/phongthuy/commit/4d37fd9ebd755cfb2b2f5e5f0f125b85a8114f80
# https://pdfcrowd.com/doc/api/html-to-image/python/
