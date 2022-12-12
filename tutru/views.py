import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from tutru.forms import *
from tutru.models import *
# Create your views here.
from blog_feng_shui.AmLich import *
from django.core import *
import imgkit

def index(request):
    mform = TuTruForm()
    can_ngay = ''
    chi_ngay = ''
    title = 'Tứ Trụ'
    if request.method == "POST":
        objjson = {'success': False}
        print(request.POST)
        json_data = []
        dic_data = {}

        name = request.POST['name']
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        day = int(request.POST['day'])
        timezone_TG = "7.0"
        hours = int(request.POST['hours'])
        minute = int(request.POST['minute'])
        # calendar = request.POST['calendar']
        options = request.POST['options']
        get_lunar_day = int(request.POST['get_lunar_day'])
        get_lunar_month = int(request.POST['get_lunar_month'])
        get_lunar_year = int(request.POST['get_lunar_year'])
        day_thute = day

        if hours == 23:
            day += 1

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
        # k=int((day-calendar_Julius)/29.530588853)


        off = jdFromDate(31, 12, year) - 2415021;
        k = int(off / 29.530588853);
        a11 = jdToDate(getNewMoonDay(k, timezone))
        # print("tìm tiết khí getSunLongitude: ",getSunLongitude(calendar_Julius,timezone))
        # print("=======Tìm ngày bắt đầu tháng 11 âm lịch==== getLunarMonth11 ",day_LunarMonth11)
        # print("Xác định tháng nhuận-- getLeapMonthOffset ",getLeapMonthOffset(a11[0],timezone))

        # print("vvvvvv  ",getNewMoonDay(k, timezone))
        # print("NewMoon",NewMoon(2459134))
        # print("pppppppppppppp: ",  getNewMoonDay(k, timezone))


        off1 = jdFromDate(day, month, year) - 2415021;
        k1 = int(off1 / 29.530588853);
        a111 = jdToDate(getNewMoonDay(k1, timezone))
        # print("Tìm Ngày giờ Sóc:  ",a111)
        # print(SunLongitude(calendar_Julius))
        # print("Xác định tháng nhuận-- getLeapMonthOffset ",getLeapMonthOffset(a111[0],timezone))
        # year_daivan = LichTietKhi.objects.filter(year=year,month=month).values('daytiekhi')


        can_ngay = day_can(day,month,year)
        chi_ngay = day_chi(day,month,year)
        can_thang = mont_can(month_lunar,year_lunar)
        chi_thang = mont_chi(month_lunar)
        can_nam = year_can(year_lunar)
        chi_nam = year_chi(year_lunar)
        can_gio = hours_can(hours ,can_ngay)
        chi_gio = hours_chi(hours)
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
        T_Sinh_Thien_Can = []
        T_Sinh_Nam = truongsinh(can_nam,chi_thang)
        T_Sinh_Thien_Can.append(T_Sinh_Nam)
        T_Sinh_Thang = truongsinh(can_thang,chi_thang)
        T_Sinh_Thien_Can.append(T_Sinh_Thang)
        T_Sinh_Ngay = truongsinh(can_ngay,chi_thang)
        T_Sinh_Thien_Can.append(T_Sinh_Ngay)
        T_Sinh_Gio = truongsinh(can_gio,chi_thang)
        T_Sinh_Thien_Can.append(T_Sinh_Gio)
        T_Sinh_Can_An_Nam = []
        for k,v in can_an_nam.items():
            T_Sinh_an_nam = truongsinh(v,chi_thang)
            T_Sinh_Can_An_Nam.append(T_Sinh_an_nam)
        T_Sinh_Can_An_Thang = []
        for k,v in can_an_thang.items():
            T_Sinh_an_thang = truongsinh(v,chi_thang)
            T_Sinh_Can_An_Thang.append(T_Sinh_an_thang)
        T_Sinh_Can_An_Ngay = []
        for k,v in can_an_ngay.items():
            T_Sinh_an_ngay = truongsinh(v,chi_thang)
            T_Sinh_Can_An_Ngay.append(T_Sinh_an_ngay)
        T_Sinh_Can_An_Gio = []
        for k,v in can_an_gio.items():
            T_Sinh_an_gio = truongsinh(v,chi_thang)
            T_Sinh_Can_An_Gio.append(T_Sinh_an_gio)
        ngu_hanh_nap_am = []
        ngu_hanh_nam = nguhanhnapam(can_nam, chi_nam)
        ngu_hanh_nap_am.append(ngu_hanh_nam)
        ngu_hanh_thang = nguhanhnapam(can_thang, chi_thang)
        ngu_hanh_nap_am.append(ngu_hanh_thang)
        ngu_hanh_ngay = nguhanhnapam(can_ngay, chi_ngay)
        ngu_hanh_nap_am.append(ngu_hanh_ngay)
        ngu_hanh_gio = nguhanhnapam(can_gio, chi_gio)
        ngu_hanh_nap_am.append(ngu_hanh_gio)
        nam_kv = khongvong(can_ngay,chi_ngay,chi_nam)
        thang_kv = khongvong(can_ngay,chi_ngay,chi_thang)
        gio_kv = khongvong(can_ngay,chi_ngay,chi_gio)
        dai_van = daivan(options,can_thang,chi_thang,chi_nam,can_ngay,chi_ngay)
        namdaivan = namvaodaivan(chi_nam,options,hours,minute,day,month,year)
        tieuvan10nam = tieuvantungnam(namdaivan,year,options,can_ngay,chi_ngay)
        tieuvan20nam = tieuvantungnam(namdaivan+10,year,options,can_ngay,chi_ngay)
        tieuvan30nam = tieuvantungnam(namdaivan+20,year,options,can_ngay,chi_ngay)
        tieuvan40nam = tieuvantungnam(namdaivan+30,year,options,can_ngay,chi_ngay)
        tieuvan50nam = tieuvantungnam(namdaivan+40,year,options,can_ngay,chi_ngay)
        tieuvan60nam = tieuvantungnam(namdaivan+50,year,options,can_ngay,chi_ngay)
        tieuvan70nam = tieuvantungnam(namdaivan+60,year,options,can_ngay,chi_ngay)
        tieuvan80nam = tieuvantungnam(namdaivan+70,year,options,can_ngay,chi_ngay)

        thienat_quynhan = thienatquynhan(can_nam,can_ngay,chi_ngay,chi_thang,chi_nam,chi_gio)
        if namdaivan >= 1:
            tongdaivan = year + (namdaivan-1)
        else:
            tongdaivan = year
            namdaivan = namdaivan + 1

        khoi_canh = khoicanh(can_ngay,chi_ngay)

        thien_loc = thienloc(can_ngay,chi_ngay,chi_thang,chi_nam,chi_gio)
        kinh_duong = kinhduong(can_ngay,chi_ngay,chi_thang,chi_nam,chi_gio)
        kim_du = kimdu(can_ngay,chi_ngay,chi_thang,chi_nam,chi_gio)
        van_xuong = vanxuong(can_ngay,can_nam,chi_ngay,chi_thang,chi_nam,chi_gio)
        thien_y = thieny(chi_ngay,chi_thang,chi_nam,chi_gio)
        dich_ma = dichma(chi_ngay,chi_thang,chi_nam,chi_gio)
        hoa_cai = hoacai(chi_ngay,chi_thang,chi_nam,chi_gio)
        tuong_tinh = tuongtinh(chi_ngay,chi_thang,chi_nam,chi_gio)
        dao_hoa = daohoa(chi_ngay,chi_thang,chi_nam,chi_gio)
        dao_hoa_sat = daohoasat(can_ngay,chi_ngay,chi_thang,chi_nam,chi_gio)
        kiep_sat = kiepsat(chi_ngay,chi_thang,chi_nam,chi_gio)
        thien_xa = thienxa(chi_thang,can_ngay,chi_ngay)
        tai_sat = taisat(chi_ngay,chi_thang,chi_nam,chi_gio)
        quoc_an_quy_nhan = quocanquynhan(can_ngay,can_nam,chi_ngay,chi_thang,chi_nam,chi_gio)
        cothan_quatu = cothanquatu(chi_ngay,chi_thang,chi_nam,chi_gio)
        thapac_daibai = thapacdaibai(can_ngay,chi_ngay)
        tamky_quynhan = tamkyquynhan(can_ngay,can_thang,can_nam,can_gio,chi_thang)
        cung_menh = cungmenh(chi_thang, chi_gio, can_nam)
        thai_nguyen = thainguyen(can_thang,chi_thang)
        nien_khong = niennhatkhongvong(can_nam,chi_nam)
        nhat_khong = niennhatkhongvong(can_ngay,chi_ngay)

        dic_data['name'] = name
        dic_data['gio_tinh'] = options
        dic_data['day'] = day_thute
        dic_data['month'] = month
        dic_data['year'] = year
        dic_data['hours'] = hours
        dic_data['minute'] = minute
        dic_data['day_lunar'] = day_lunar
        dic_data['month_lunar'] = month_lunar
        dic_data['year_lunar'] = year_lunar
        dic_data['can_ngay'] = can_ngay
        dic_data['chi_ngay'] = chi_ngay
        dic_data['timezone_TG'] = timezone_TG
        dic_data['can_thang'] = can_thang
        dic_data['chi_thang'] = chi_thang
        dic_data['can_nam'] = can_nam
        dic_data['chi_nam'] = chi_nam
        dic_data['can_gio'] = can_gio
        dic_data['chi_gio'] = chi_gio
        dic_data['can_thap_thang'] = can_thap_thang
        dic_data['can_thap_nam'] = can_thap_nam
        dic_data['can_thap_gio'] = can_thap_gio
        dic_data['can_an_ngay'] = can_an_ngay
        dic_data['can_an_thang'] = can_an_thang
        dic_data['can_an_nam'] = can_an_nam
        dic_data['can_an_gio'] = can_an_gio
        dic_data['can_ngay_color'] = can_ngay_color
        dic_data['chi_ngay_color'] = chi_ngay_color
        dic_data['can_thang_color'] = can_thang_color
        dic_data['chi_thang_color'] = chi_thang_color
        dic_data['can_nam_color'] = can_nam_color
        dic_data['chi_nam_color'] = chi_nam_color
        dic_data['can_gio_color'] = can_gio_color
        dic_data['chi_gio_color'] = chi_gio_color
        dic_data['can_an_nam_thapthan'] = can_an_nam_thapthan
        dic_data['can_an_thang_thapthan'] = can_an_thang_thapthan
        dic_data['can_an_ngay_thapthan'] = can_an_ngay_thapthan
        dic_data['can_an_gio_thapthan'] = can_an_gio_thapthan
        dic_data['T_Sinh_Thien_Can'] = T_Sinh_Thien_Can
        dic_data['T_Sinh_Can_An_Nam'] = T_Sinh_Can_An_Nam
        dic_data['T_Sinh_Can_An_Thang'] = T_Sinh_Can_An_Thang
        dic_data['T_Sinh_Can_An_Ngay'] = T_Sinh_Can_An_Ngay
        dic_data['T_Sinh_Can_An_Gio'] = T_Sinh_Can_An_Gio
        dic_data['ngu_hanh_nap_am'] = ngu_hanh_nap_am
        dic_data['nam_kv'] = nam_kv
        dic_data['thang_kv'] = thang_kv
        dic_data['gio_kv'] = gio_kv
        dic_data['dai_van'] = dai_van
        dic_data['tongdaivan'] = tongdaivan
        dic_data['namdaivan'] = namdaivan
        dic_data['tieuvan10nam'] = tieuvan10nam
        dic_data['tieuvan20nam'] = tieuvan20nam
        dic_data['tieuvan30nam'] = tieuvan30nam
        dic_data['tieuvan40nam'] = tieuvan40nam
        dic_data['tieuvan50nam'] = tieuvan50nam
        dic_data['tieuvan60nam'] = tieuvan60nam
        dic_data['tieuvan70nam'] = tieuvan70nam
        dic_data['tieuvan80nam'] = tieuvan80nam
        dic_data['thienat_quynhan'] = thienat_quynhan
        dic_data['khoi_canh'] = khoi_canh
        dic_data['thien_loc'] = thien_loc
        dic_data['kinh_duong'] = kinh_duong
        dic_data['kim_du'] = kim_du
        dic_data['van_xuong'] = van_xuong
        dic_data['thien_y'] = thien_y
        dic_data['dich_ma'] = dich_ma
        dic_data['hoa_cai'] = hoa_cai
        dic_data['tuong_tinh'] = tuong_tinh
        dic_data['dao_hoa'] = dao_hoa
        dic_data['dao_hoa_sat'] = dao_hoa_sat
        dic_data['kiep_sat'] = kiep_sat
        dic_data['thien_xa'] = thien_xa
        dic_data['tai_sat'] = tai_sat
        dic_data['quoc_an_quy_nhan'] = quoc_an_quy_nhan
        dic_data['cothan_quatu'] = cothan_quatu
        dic_data['thapac_daibai'] = thapac_daibai
        dic_data['tamky_quynhan'] = tamky_quynhan
        dic_data['cung_menh'] = cung_menh
        dic_data['thai_nguyen'] = thai_nguyen
        dic_data['nien_khong'] = nien_khong
        dic_data['nhat_khong'] = nhat_khong
        json_data.append(dic_data)
        # return render(request, "tutru/tutru_partial.html",
        # {
        #     'tutru_array': json_data
        # })
        objjson = {'success': True,'check_field': json_data}
        return HttpResponse(json.dumps(objjson))


    return render(request, "tutru/index.html", {
        'form': mform,
        'form_name': mform.__class__.__name__,
        'can_ngay': can_ngay,
        'chi_ngay': chi_ngay,
        'title':title,
    })
