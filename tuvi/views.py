import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from tuvi.forms import *
from tutru.models import *
from tuvi.models import *
# Create your views here.
from blog_feng_shui.AmLich import *
from django.core import *
import imgkit

# Create your views here.

def index(request):
    mform = TuViForm()
    
    can_ngay = ''
    chi_ngay = ''
    if request.method == "POST":
        print("Loading +++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(request.POST)
        print("Loading +++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        json_data = []
        dic_data = {}

        name = request.POST['name']
        year_birthday = int(request.POST['year'])
        month_birthday = int(request.POST['month'])
        day_birthday = int(request.POST['day'])
        timezone_TG = "7.0"
        timezone_text = request.POST['timezone_text']
        hours_birthday = int(request.POST['hours'])
        minute_birthday = int(request.POST['minute'])
        calendar = 'Dương Lịch'
        options = request.POST['options']

        year_to_see = int(request.POST['year'])
        month_to_see = int(request.POST['month'])
        day_to_see = int(request.POST['day'])
        get_lunar_day = int(request.POST['get_lunar_day'])
        get_lunar_month = int(request.POST['get_lunar_month'])
        get_lunar_year = int(request.POST['get_lunar_year'])
        try:
            timezone = int(float(timezone_TG))
        except:
            timezone = 0
        calendar_lunar = S2L(day_birthday, month_birthday, year_birthday, timezone)
        day_lunar = get_lunar_day
        month_lunar = get_lunar_month
        year_lunar = get_lunar_year

        calendar_lunar_to_see = S2L(day_to_see, month_to_see, year_to_see, timezone)
        day_lunar_to_see = calendar_lunar_to_see[0]
        month_lunar_to_see = calendar_lunar_to_see[1]
        year_lunar_to_see = calendar_lunar_to_see[2]

        can_ngay = day_can(day_birthday, month_birthday, year_birthday)
        chi_ngay = day_chi(day_birthday, month_birthday, year_birthday)
        can_thang = mont_can(month_lunar,year_lunar)
        chi_thang = mont_chi(month_lunar)
        can_thang_to_see = mont_can(month_lunar_to_see,year_lunar_to_see)
        chi_thang_to_see = mont_chi(month_lunar_to_see)
        can_nam = year_can(year_lunar)
        chi_nam = year_chi(year_lunar)
        can_nam_to_see = year_can(year_lunar_to_see)
        chi_nam_to_see = year_chi(year_lunar_to_see)
        can_gio = hours_can(hours_birthday ,can_ngay)
        chi_gio = hours_chi(hours_birthday)
        can_ngay_color = color_canchi(can_ngay)
        chi_ngay_color = color_canchi(chi_ngay)
        can_thang_color = color_canchi(can_thang)
        chi_thang_color = color_canchi(chi_thang)
        can_nam_color = color_canchi(can_nam)
        chi_nam_color = color_canchi(chi_nam)
        can_gio_color = color_canchi(can_gio)
        chi_gio_color = color_canchi(chi_gio)
        can_thap_thang = thapthan(can_ngay,can_thang)
        can_thap_nam = thapthan(can_ngay,can_nam)
        can_thap_gio = thapthan(can_ngay,can_gio)
        can_an_ngay = tangcang(chi_ngay)
        can_an_thang = tangcang(chi_thang)
        can_an_nam = tangcang(chi_nam)
        can_an_gio = tangcang(chi_gio)
        can_ngay_color = color_canchi(can_ngay)
        chi_ngay_color = color_canchi(chi_ngay)
        can_thang_color = color_canchi(can_thang)
        chi_thang_color = color_canchi(chi_thang)
        can_nam_color = color_canchi(can_nam)
        chi_nam_color = color_canchi(chi_nam)
        can_gio_color = color_canchi(can_gio)
        chi_gio_color = color_canchi(chi_gio)
        can_an_nam_thapthan = []
        can_an_thang_thapthan = []
        can_an_ngay_thapthan = []
        can_an_gio_thapthan = []
        for key,value in can_an_nam.items():
            can = thapthan(can_ngay,value)
            can_an_nam_thapthan.append(can)
        for key,value in can_an_thang.items():
            can = thapthan(can_ngay,value)
            can_an_thang_thapthan.append(can)
        for key,value in can_an_ngay.items():
            can = thapthan(can_ngay,value)
            can_an_ngay_thapthan.append(can)
        for key,value in can_an_gio.items():
            can = thapthan(can_ngay,value)
            can_an_gio_thapthan.append(can)
        thiencan_12cung = thiencan12cung(can_nam)
        cung_menhthan = cungmenhthan(chi_gio,int(month_lunar))
        cucso_nguhanh = cucsonguhanh(chi_gio,int(month_lunar),can_nam,chi_nam)
        ansao_tuvi = ansaotuvi(chi_gio,int(month_lunar),can_nam,chi_nam,int(day_lunar))
        vongtruong_sinhtuvi = vongtruongsinhtuvi(chi_gio,int(month_lunar),can_nam,chi_nam,options)
        vong_locton = vonglocton(can_nam,chi_nam,options)
        active_menh = activemenh(chi_gio,int(month_lunar))
        duongchi_cungmenh = duongchicungmenh(chi_gio,int(month_lunar))
        thienkhoi_thienviet = thienkhothienviet(can_nam)
        thienquan_thienphuc = thienquanthienphuc(can_nam)
        ansao_theochi = ansaotheochi(chi_nam)
        ansao_theothang = ansaotheothang(int(month_lunar))
        ansao_theongay = ansaotheongay(int(month_lunar),int(day_lunar))
        ansao_theogio = ansaotheogio(chi_gio,int(day_lunar),chi_nam,options)
        cacbo_saokhac = cacbosaokhac(chi_gio,int(month_lunar),can_nam,chi_nam,int(day_lunar),options)
        daivan_tuvi = daivantuvi(options,chi_gio,chi_nam,can_ngay,chi_ngay,day_lunar, month_lunar, year_lunar,hours_birthday,minute_birthday)
        tuoi_tuvi = tuoituvi(options,can_nam,chi_nam,month_lunar_to_see,year_lunar_to_see,year_birthday)
        tieuvan_tungnamtuvi = tieuvantungnamtuvi(options,chi_gio,chi_nam,can_ngay,chi_ngay,day_lunar, month_lunar, year_lunar,hours_birthday,minute_birthday,year_lunar_to_see)
        khong_tuantriet = khongtuantriet(can_nam,chi_nam)
        luuvong_locton = ansaoluunien(can_nam_to_see,chi_nam_to_see,options,month_lunar_to_see,day_lunar_to_see)
        print("tieu van tung nam: ",ansaoluunien(can_nam_to_see,chi_nam_to_see,options,month_lunar_to_see,day_lunar_to_see))

        dic_data['name'] = name
        dic_data['gio_tinh'] = options
        dic_data['day_birthday'] = day_birthday
        dic_data['month_birthday'] = month_birthday
        dic_data['year_birthday'] = year_birthday
        dic_data['hours_birthday'] = hours_birthday
        dic_data['minute_birthday'] = minute_birthday
        dic_data['day_lunar'] = day_lunar
        dic_data['month_lunar'] = month_lunar
        dic_data['year_lunar'] = year_lunar
        dic_data['can_ngay'] = can_ngay
        dic_data['chi_ngay'] = chi_ngay
        dic_data['can_thang'] = can_thang
        dic_data['chi_thang'] = chi_thang
        dic_data['can_nam'] = can_nam
        dic_data['chi_nam'] = chi_nam
        dic_data['can_gio'] = can_gio
        dic_data['chi_gio'] = chi_gio
        dic_data['can_ngay_color'] = can_ngay_color
        dic_data['chi_ngay_color'] = chi_ngay_color
        dic_data['can_thang_color'] = can_thang_color
        dic_data['chi_thang_color'] = chi_thang_color
        dic_data['can_nam_color'] = can_nam_color
        dic_data['chi_nam_color'] = chi_nam_color
        dic_data['can_gio_color'] = can_gio_color
        dic_data['chi_gio_color'] = chi_gio_color
        dic_data['timezone_text'] = timezone_text
        dic_data['can_thap_thang'] = can_thap_thang
        dic_data['can_thap_nam'] = can_thap_nam
        dic_data['can_thap_gio'] = can_thap_gio
        dic_data['can_an_ngay'] = can_an_ngay
        dic_data['can_an_thang'] = can_an_thang
        dic_data['can_an_nam'] = can_an_nam
        dic_data['can_an_gio'] = can_an_gio
        dic_data['can_an_nam_thapthan'] = can_an_nam_thapthan
        dic_data['can_an_thang_thapthan'] = can_an_thang_thapthan
        dic_data['can_an_ngay_thapthan'] = can_an_ngay_thapthan
        dic_data['can_an_gio_thapthan'] = can_an_gio_thapthan
        dic_data['thiencan_12cung'] = thiencan_12cung
        dic_data['cung_menhthan'] = cung_menhthan
        dic_data['cucso_nguhanh'] = cucso_nguhanh
        dic_data['ansao_tuvi'] = ansao_tuvi
        dic_data['vongtruong_sinhtuvi'] = vongtruong_sinhtuvi
        dic_data['vong_locton'] = vong_locton
        dic_data['luuvong_locton'] = luuvong_locton
        dic_data['active_menh'] = active_menh
        dic_data['duongchi_cungmenh'] = duongchi_cungmenh
        dic_data['thienkhoi_thienviet'] = thienkhoi_thienviet
        dic_data['thienquan_thienphuc'] = thienquan_thienphuc
        dic_data['ansao_theochi'] = ansao_theochi
        dic_data['ansao_theothang'] = ansao_theothang
        dic_data['ansao_theongay'] = ansao_theongay
        dic_data['ansao_theogio'] = ansao_theogio
        dic_data['cacbo_saokhac'] = cacbo_saokhac
        dic_data['daivan_tuvi'] = daivan_tuvi
        dic_data['tuoi_tuvi'] = tuoi_tuvi
        dic_data['tieuvan_tungnamtuvi'] = tieuvan_tungnamtuvi
        dic_data['khong_tuantriet'] = khong_tuantriet


        json_data.append(dic_data)

        return render(request, "tuvi/tuvi_partial.html",
        {
            'tuvi_array': json_data
        })


    return render(request, "tuvi/index.html", {
        'form': mform,
        'form_name': mform.__class__.__name__,
        # 'can_ngay': can_ngay,
        # 'chi_ngay': chi_ngay,
    })
