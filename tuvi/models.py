from django.db import models
from django.db.models import Model
from blog_feng_shui.AmLich import *
from tutru.models import *
import datetime
from collections import defaultdict
# Create your models here.


chi_duong = ('TÝ','DẦN','THÌN','NGỌ','THÂN','TUẤT')
chi_am = ('SỬU','MÃO','TỴ','MÙI','DẬU','HỢI')
dia_chi = ('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
thien_can = ('GIÁP','ẤT','BÍNH','ĐINH','MẬU','KỶ','CANH','TÂN','NHÂM','QUÝ')
saotuvi=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')

def thiencan12cung(can_nam):
    dic_thiencan = {}
    if can_nam == 'GIÁP' or can_nam == 'KỶ':
        dic_thiencan={'DẦN':"B",'MÃO':"Đ",'THÌN':"M",'TỴ':"K",'NGỌ':"C",'MÙI':"T",'THÂN':"N",'DẬU':"Q",'TUẤT':"G",'HỢI':"Ấ",'TÝ':"B",'SỬU':"Đ"}
    elif can_nam == 'ẤT' or can_nam == 'CANH':
        dic_thiencan={'DẦN':"M",'MÃO':"K",'THÌN':"C",'TỴ':"T",'NGỌ':"N",'MÙI':"Q",'THÂN':"G",'DẬU':"Ấ",'TUẤT':"B",'HỢI':"Đ",'TÝ':"M",'SỬU':"K"}
    elif can_nam == 'BÍNH' or can_nam == 'TÂN':
        dic_thiencan={'DẦN':"C",'MÃO':"T",'THÌN':"N",'TỴ':"Q",'NGỌ':"G",'MÙI':"Ấ",'THÂN':"B",'DẬU':"Đ",'TUẤT':"M",'HỢI':"K",'TÝ':"C",'SỬU':"T"}
    elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
        dic_thiencan={'DẦN':"N",'MÃO':"Q",'THÌN':"G",'TỴ':"Ấ",'NGỌ':"B",'MÙI':"Đ",'THÂN':"M",'DẬU':"K",'TUẤT':"C",'HỢI':"T",'TÝ':"N",'SỬU':"Q"}
    else:
        dic_thiencan={'DẦN':"G",'MÃO':"Ấ",'THÌN':"B",'TỴ':"Đ",'NGỌ':"M",'MÙI':"K",'THÂN':"C",'DẬU':"T",'TUẤT':"N",'HỢI':"Q",'TÝ':"G",'SỬU':"Ấ"}
    return dic_thiencan

def cungmenhthan(chi_gio,thang_am):
    dic_cungmenh = {}
    if chi_gio == 'TÝ':
        if thang_am == 1:
            dic_cungmenh ={'DẦN':"MỆNH<THÂN>",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'MÃO':"MỆNH<THÂN>",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'THÌN':"MỆNH<THÂN>",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'TỴ':"MỆNH<THÂN>",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'NGỌ':"MỆNH<THÂN>",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'MÙI':"MỆNH<THÂN>",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'THÂN':"MỆNH<THÂN>",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'DẬU':"MỆNH<THÂN>",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'TUẤT':"MỆNH<THÂN>",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'HỢI':"MỆNH<THÂN>",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'TÝ':"MỆNH<THÂN>",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'SỬU':"MỆNH<THÂN>",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
    elif chi_gio == 'SỬU':
        if thang_am == 1:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"P ĐỨC<THÂN>",'DẦN':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"P ĐỨC<THÂN>",'MÃO':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"P ĐỨC<THÂN>",'THÌN':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"P ĐỨC<THÂN>",'TỴ':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"P ĐỨC<THÂN>",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"P ĐỨC<THÂN>",'MÙI':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"P ĐỨC<THÂN>",'THÂN':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"P ĐỨC<THÂN>",'DẬU':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"P ĐỨC<THÂN>",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"P ĐỨC<THÂN>",'HỢI':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"P ĐỨC<THÂN>",'TÝ':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"P ĐỨC<THÂN>",'SỬU':"PHỤ MẪU"}
    elif chi_gio == 'DẦN':
        if thang_am == 1:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"Q LỘC<THÂN>",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"Q LỘC<THÂN>",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"Q LỘC<THÂN>",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"Q LỘC<THÂN>",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"Q LỘC<THÂN>",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"Q LỘC<THÂN>",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"Q LỘC<THÂN>",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"Q LỘC<THÂN>",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"Q LỘC<THÂN>",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"Q LỘC<THÂN>",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"Q LỘC<THÂN>",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"Q LỘC<THÂN>",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
    elif chi_gio == 'MÃO':
        if thang_am == 1:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"T DI<THÂN>",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"T DI<THÂN>",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"T DI<THÂN>",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"T DI<THÂN>",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"T DI<THÂN>",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"T DI<THÂN>",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"T DI<THÂN>",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"T DI<THÂN>",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"T DI<THÂN>",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"T DI<THÂN>",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"T DI<THÂN>",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"T DI<THÂN>",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
    elif chi_gio == 'THÌN':
        if thang_am == 1:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"T BẠCH<THÂN>",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"T BẠCH<THÂN>",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"T BẠCH<THÂN>",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"T BẠCH<THÂN>",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"T BẠCH<THÂN>",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"T BẠCH<THÂN>",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"T BẠCH<THÂN>",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"T BẠCH<THÂN>",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"T BẠCH<THÂN>",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"T BẠCH<THÂN>",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"T BẠCH<THÂN>",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"T BẠCH<THÂN>",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
    elif chi_gio == 'TỴ':
        if thang_am == 1:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"P THÊ<THÂN>",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"P THÊ<THÂN>",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"P THÊ<THÂN>",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"P THÊ<THÂN>",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"P THÊ<THÂN>",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"P THÊ<THÂN>",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"P THÊ<THÂN>",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"P THÊ<THÂN>",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"P THÊ<THÂN>",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"P THÊ<THÂN>",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"P THÊ<THÂN>",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"P THÊ<THÂN>",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
    elif chi_gio == 'NGỌ':
        if thang_am == 1:
            dic_cungmenh ={'THÂN':"MỆNH<THÂN>",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'DẬU':"MỆNH<THÂN>",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'TUẤT':"MỆNH<THÂN>",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'HỢI':"MỆNH<THÂN>",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'TÝ':"MỆNH<THÂN>",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'SỬU':"MỆNH<THÂN>",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'DẦN':"MỆNH<THÂN>",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'MÃO':"MỆNH<THÂN>",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'THÌN':"MỆNH<THÂN>",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'TỴ':"MỆNH<THÂN>",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'NGỌ':"MỆNH<THÂN>",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'MÙI':"MỆNH<THÂN>",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
    elif chi_gio == 'MÙI':
        if thang_am == 1:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"P ĐỨC<THÂN>",'THÂN':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"P ĐỨC<THÂN>",'DẬU':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"P ĐỨC<THÂN>",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"P ĐỨC<THÂN>",'HỢI':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"P ĐỨC<THÂN>",'TÝ':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"P ĐỨC<THÂN>",'SỬU':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"P ĐỨC<THÂN>",'DẦN':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"P ĐỨC<THÂN>",'MÃO':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"P ĐỨC<THÂN>",'THÌN':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"P ĐỨC<THÂN>",'TỴ':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"P ĐỨC<THÂN>",'NGỌ':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"P ĐỨC<THÂN>",'MÙI':"PHỤ MẪU"}
    elif chi_gio == 'THÂN':
        if thang_am == 1:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"T DI<THÂN>",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"T DI<THÂN>",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"T DI<THÂN>",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"T DI<THÂN>",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"T DI<THÂN>",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"T DI<THÂN>",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"T DI<THÂN>",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"T DI<THÂN>",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"T DI<THÂN>",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"T DI<THÂN>",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"T DI<THÂN>",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"T DI<THÂN>",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
    elif chi_gio == 'DẬU':
        if thang_am == 1:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"T DI<THÂN>",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"T DI<THÂN>",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"T DI<THÂN>",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"T DI<THÂN>",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"T DI<THÂN>",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"T DI<THÂN>",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"T DI<THÂN>",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"T DI<THÂN>",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"T DI<THÂN>",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"T DI<THÂN>",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"T DI<THÂN>",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"T DI<THÂN>",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
    elif chi_gio == 'TUẤT':
        if thang_am == 1:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"PHU THÊ",'SỬU':"TỬ TỨC",'TÝ':"T BẠCH<THÂN>",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"PHU THÊ",'DẦN':"TỬ TỨC",'SỬU':"T BẠCH<THÂN>",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"PHU THÊ",'MÃO':"TỬ TỨC",'DẦN':"T BẠCH<THÂN>",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"PHU THÊ",'THÌN':"TỬ TỨC",'MÃO':"T BẠCH<THÂN>",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"PHU THÊ",'TỴ':"TỬ TỨC",'THÌN':"T BẠCH<THÂN>",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"PHU THÊ",'NGỌ':"TỬ TỨC",'TỴ':"T BẠCH<THÂN>",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"PHU THÊ",'MÙI':"TỬ TỨC",'NGỌ':"T BẠCH<THÂN>",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"PHU THÊ",'THÂN':"TỬ TỨC",'MÙI':"T BẠCH<THÂN>",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"PHU THÊ",'DẬU':"TỬ TỨC",'THÂN':"T BẠCH<THÂN>",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"PHU THÊ",'TUẤT':"TỬ TỨC",'DẬU':"T BẠCH<THÂN>",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"PHU THÊ",'HỢI':"TỬ TỨC",'TUẤT':"T BẠCH<THÂN>",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"PHU THÊ",'TÝ':"TỬ TỨC",'HỢI':"T BẠCH<THÂN>",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
    elif chi_gio == 'HỢI':
        if thang_am == 1:
            dic_cungmenh ={'MÃO':"MỆNH",'DẦN':"HUYNH ĐỆ",'SỬU':"P THÊ<THÂN>",'TÝ':"TỬ TỨC",'HỢI':"TÀI BẠCH",'TUẤT':"TẬT ÁCH",'DẬU':"THIÊN DI",'THÂN':"NÔ BỘC",'MÙI':"QUAN LỘC",'NGỌ':"ĐIỀN TRẠCH",'TỴ':"PHÚC ĐỨC",'THÌN':"PHỤ MẪU"}
        elif thang_am == 2:
            dic_cungmenh ={'THÌN':"MỆNH",'MÃO':"HUYNH ĐỆ",'DẦN':"P THÊ<THÂN>",'SỬU':"TỬ TỨC",'TÝ':"TÀI BẠCH",'HỢI':"TẬT ÁCH",'TUẤT':"THIÊN DI",'DẬU':"NÔ BỘC",'THÂN':"QUAN LỘC",'MÙI':"ĐIỀN TRẠCH",'NGỌ':"PHÚC ĐỨC",'TỴ':"PHỤ MẪU"}
        elif thang_am == 3:
            dic_cungmenh ={'TỴ':"MỆNH",'THÌN':"HUYNH ĐỆ",'MÃO':"P THÊ<THÂN>",'DẦN':"TỬ TỨC",'SỬU':"TÀI BẠCH",'TÝ':"TẬT ÁCH",'HỢI':"THIÊN DI",'TUẤT':"NÔ BỘC",'DẬU':"QUAN LỘC",'THÂN':"ĐIỀN TRẠCH",'MÙI':"PHÚC ĐỨC",'NGỌ':"PHỤ MẪU"}
        elif thang_am == 4:
            dic_cungmenh ={'NGỌ':"MỆNH",'TỴ':"HUYNH ĐỆ",'THÌN':"P THÊ<THÂN>",'MÃO':"TỬ TỨC",'DẦN':"TÀI BẠCH",'SỬU':"TẬT ÁCH",'TÝ':"THIÊN DI",'HỢI':"NÔ BỘC",'TUẤT':"QUAN LỘC",'DẬU':"ĐIỀN TRẠCH",'THÂN':"PHÚC ĐỨC",'MÙI':"PHỤ MẪU"}
        elif thang_am == 5:
            dic_cungmenh ={'MÙI':"MỆNH",'NGỌ':"HUYNH ĐỆ",'TỴ':"P THÊ<THÂN>",'THÌN':"TỬ TỨC",'MÃO':"TÀI BẠCH",'DẦN':"TẬT ÁCH",'SỬU':"THIÊN DI",'TÝ':"NÔ BỘC",'HỢI':"QUAN LỘC",'TUẤT':"ĐIỀN TRẠCH",'DẬU':"PHÚC ĐỨC",'THÂN':"PHỤ MẪU"}
        elif thang_am == 6:
            dic_cungmenh ={'THÂN':"MỆNH",'MÙI':"HUYNH ĐỆ",'NGỌ':"P THÊ<THÂN>",'TỴ':"TỬ TỨC",'THÌN':"TÀI BẠCH",'MÃO':"TẬT ÁCH",'DẦN':"THIÊN DI",'SỬU':"NÔ BỘC",'TÝ':"QUAN LỘC",'HỢI':"ĐIỀN TRẠCH",'TUẤT':"PHÚC ĐỨC",'DẬU':"PHỤ MẪU"}
        elif thang_am == 7:
            dic_cungmenh ={'DẬU':"MỆNH",'THÂN':"HUYNH ĐỆ",'MÙI':"P THÊ<THÂN>",'NGỌ':"TỬ TỨC",'TỴ':"TÀI BẠCH",'THÌN':"TẬT ÁCH",'MÃO':"THIÊN DI",'DẦN':"NÔ BỘC",'SỬU':"QUAN LỘC",'TÝ':"ĐIỀN TRẠCH",'HỢI':"PHÚC ĐỨC",'TUẤT':"PHỤ MẪU"}
        elif thang_am == 8:
            dic_cungmenh ={'TUẤT':"MỆNH",'DẬU':"HUYNH ĐỆ",'THÂN':"P THÊ<THÂN>",'MÙI':"TỬ TỨC",'NGỌ':"TÀI BẠCH",'TỴ':"TẬT ÁCH",'THÌN':"THIÊN DI",'MÃO':"NÔ BỘC",'DẦN':"QUAN LỘC",'SỬU':"ĐIỀN TRẠCH",'TÝ':"PHÚC ĐỨC",'HỢI':"PHỤ MẪU"}
        elif thang_am == 9:
            dic_cungmenh ={'HỢI':"MỆNH",'TUẤT':"HUYNH ĐỆ",'DẬU':"P THÊ<THÂN>",'THÂN':"TỬ TỨC",'MÙI':"TÀI BẠCH",'NGỌ':"TẬT ÁCH",'TỴ':"THIÊN DI",'THÌN':"NÔ BỘC",'MÃO':"QUAN LỘC",'DẦN':"ĐIỀN TRẠCH",'SỬU':"PHÚC ĐỨC",'TÝ':"PHỤ MẪU"}
        elif thang_am == 10:
            dic_cungmenh ={'TÝ':"MỆNH",'HỢI':"HUYNH ĐỆ",'TUẤT':"P THÊ<THÂN>",'DẬU':"TỬ TỨC",'THÂN':"TÀI BẠCH",'MÙI':"TẬT ÁCH",'NGỌ':"THIÊN DI",'TỴ':"NÔ BỘC",'THÌN':"QUAN LỘC",'MÃO':"ĐIỀN TRẠCH",'DẦN':"PHÚC ĐỨC",'SỬU':"PHỤ MẪU"}
        elif thang_am == 11:
            dic_cungmenh ={'SỬU':"MỆNH",'TÝ':"HUYNH ĐỆ",'HỢI':"P THÊ<THÂN>",'TUẤT':"TỬ TỨC",'DẬU':"TÀI BẠCH",'THÂN':"TẬT ÁCH",'MÙI':"THIÊN DI",'NGỌ':"NÔ BỘC",'TỴ':"QUAN LỘC",'THÌN':"ĐIỀN TRẠCH",'MÃO':"PHÚC ĐỨC",'DẦN':"PHỤ MẪU"}
        else:
            dic_cungmenh ={'DẦN':"MỆNH",'SỬU':"HUYNH ĐỆ",'TÝ':"P THÊ<THÂN>",'HỢI':"TỬ TỨC",'TUẤT':"TÀI BẠCH",'DẬU':"TẬT ÁCH",'THÂN':"THIÊN DI",'MÙI':"NÔ BỘC",'NGỌ':"QUAN LỘC",'TỴ':"ĐIỀN TRẠCH",'THÌN':"PHÚC ĐỨC",'MÃO':"PHỤ MẪU"}
    return dic_cungmenh

def cucnguhanh(*nguhanh):
    chi_gio = nguhanh[0]
    thang_am = nguhanh[1]
    can_nam = nguhanh[2]
    chi_nam = nguhanh[3]
    cung_menhthan = cungmenhthan(chi_gio,thang_am)
    ngu_hanh = ''
    for key,value in cung_menhthan.items():
        if value.find("MỆNH",0,4) == 0:
            if key == 'TÝ'or key == 'SỬU':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 'THỦY NHỊ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 'HỎA LỤC CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 'THỔ NGỦ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 'MỘC TAM CỤC'
                else:
                    nguhanh = 'KIM TỨ CỤC'
            elif key == 'DẦN'or key == 'MÃO':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 'HỎA LỤC CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 'THỔ NGỦ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 'MỘC TAM CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 'KIM TỨ CỤC'
                else:
                    nguhanh = 'THỦY NHỊ CỤC'
            elif key == 'THÌN'or key == 'TỴ':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 'MỘC TAM CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 'KIM TỨ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 'THỦY NHỊ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 'HỎA LỤC CỤC'
                else:
                    nguhanh = 'THỔ NGỦ CỤC'
            elif key == 'NGỌ'or key == 'MÙI':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 'THỔ NGỦ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 'MỘC TAM CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 'KIM TỨ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 'THỦY NHỊ CỤC'
                else:
                    nguhanh = 'HỎA LỤC CỤC'
            elif key == 'THÂN'or key == 'DẬU':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 'KIM TỨ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 'THỦY NHỊ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 'HỎA LỤC CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 'THỔ NGỦ CỤC'
                else:
                    nguhanh = 'MỘC TAM CỤC'
            else:
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 'HỎA LỤC CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 'THỔ NGỦ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 'MỘC TAM CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 'KIM TỨ CỤC'
                else:
                    nguhanh = 'THỦY NHỊ CỤC'
    return nguhanh

def activemenh(chi_gio,thang_am):
    cungmenh = {}
    cung_menhthan = cungmenhthan(chi_gio,thang_am)
    for key,value in cung_menhthan.items():
        if value.find("MỆNH",0,4) == 0:
            if key == 'TÝ':
                cungmenh = {'TÝ':'active'}
            elif key == 'SỬU':
                cungmenh = {'SỬU':'active'}
            elif key == 'DẦN':
                cungmenh = {'DẦN':'active'}
            elif key == 'MÃO':
                cungmenh = {'MÃO':'active'}
            elif key == 'THÌN':
                cungmenh = {'THÌN':'active'}
            elif key == 'TỴ':
                cungmenh = {'TỴ':'active'}
            elif key == 'NGỌ':
                cungmenh = {'NGỌ':'active'}
            elif key == 'MÙI':
                cungmenh = {'MÙI':'active'}
            elif key == 'THÂN':
                cungmenh = {'THÂN':'active'}
            elif key == 'DẬU':
                cungmenh = {'DẬU':'active'}
            elif key == 'TUẤT':
                cungmenh = {'TUẤT':'active'}
            else:
                cungmenh = {'HỢI':'active'}
    return cungmenh

def duongchicungmenh(chi_gio,thang_am):
    cungmenh = {}
    cung_menhthan = cungmenhthan(chi_gio,thang_am)
    for key,value in cung_menhthan.items():
        if value.find("MỆNH",0,4) == 0:
            if key == 'TÝ':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="0" y1="158" x2="279" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="90" y1="0" x2="279" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
               '<line x1="391" y1="0" x2="279" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'SỬU':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="391" y1="137" x2="112" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="300" y1="0" x2="113" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
               '<line  x1="0" y1="0" x2="112" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'DẦN':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="392" y1="442" x2="0" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="390" y1="0" x2="0" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
               '<line x1="90" y1="0" x2="0" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'MÃO':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="391" y1="643" x2="0" y2="500" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="391" y1="120" x2="0" y2="500" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
               '<line x1="300" y1="0" x2="0" y2="500" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'THÌN':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="390" y1="0" x2="0" y2="155" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="399" y1="461" x2="0" y2="155" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="304" y1="645" x2="0" y2="155" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'TỴ':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="0" y1="0" x2="391" y2="194" style="stroke: rgb(97 94 94);stroke-width: 1;" />'
              '<line x1="0" y1="0" x2="390" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;" />'
              '<line x1="0" y1="0" x2="98" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;" /></svg>'}
            elif key == 'NGỌ':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="90" y1="0" x2="486" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="90" y1="0" x2="279" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="90" y1="0" x2="0" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'MÙI':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="300" y1="0" x2="390" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="300" y1="0" x2="113" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="300" y1="0" x2="0" y2="505" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'THÂN':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="390" y1="0" x2="290" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="390" y1="0" x2="0" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="390" y1="0" x2="0" y2="189" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'DẬU':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="445" y1="0" x2="107" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="448" y1="40" x2="0" y2="486" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="409" y1="104" x2="0" y2="0" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            elif key == 'TUẤT':
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="391" y1="438" x2="0" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="391" y1="438" x2="0" y2="155" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="391" y1="438" x2="91" y2="0" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
            else:
                cungmenh = {'menh':'<svg style="position: absolute; top:0; left: 0; width: 391px; height: 645px;">'
              '<line x1="0" y1="444" x2="391" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
              '<line x1="0" y1="0" x2="391" y2="645" style="stroke: rgb(243 150 150);stroke-width: 1;"></line>'
              '<line x1="270" y1="0" x2="391" y2="645" style="stroke: rgb(97 94 94);stroke-width: 1;"></line>'
            '</svg>'}
    return cungmenh

# Cục Số Ngũ Hành
def cucsonguhanh(*nguhanh):
    chi_gio = nguhanh[0]
    thang_am = nguhanh[1]
    can_nam = nguhanh[2]
    chi_nam = nguhanh[3]
    nguhanh_napam = nguhanhnapam(can_nam,chi_nam)
    cung_menhthan = cungmenhthan(chi_gio,thang_am)
    ngu_hanh = ''
    for key,value in cung_menhthan.items():
        if value.find("MỆNH",0,4) == 0:
            if key == 'TÝ'or key == 'SỬU':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                else:
                    nguhanh = f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
            elif key == 'DẦN'or key == 'MÃO':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                else:
                    nguhanh = f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
            elif key == 'THÌN'or key == 'TỴ':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                else:
                    nguhanh = f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
            elif key == 'NGỌ'or key == 'MÙI':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                else:
                    nguhanh = f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
            elif key == 'THÂN'or key == 'DẬU':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                else:
                    nguhanh = f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
            else:
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                else:
                    nguhanh = f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
    return nguhanh

def ansaotuvi(*tuvi):
    chi_gio = tuvi[0]
    thang_am = tuvi[1]
    can_nam = tuvi[2]
    chi_nam = tuvi[3]
    ngay_am = tuvi[4]
    nguhanh_napam = nguhanhnapam(can_nam,chi_nam)
    cung_menhthan = cungmenhthan(chi_gio,thang_am)

    ngu_hanh = 0
    ansaochutinh = {}
    for key,value in cung_menhthan.items():
        if value.find("MỆNH",0,4) == 0:
            if key == 'TÝ'or key == 'SỬU':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh =  2  #f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh =  6 #f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 5  #f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 3  #f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                else:
                    nguhanh =  4 #f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
            elif key == 'DẦN'or key == 'MÃO':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 6  #f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 5  #f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 3  #f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 4  #f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                else:
                    nguhanh = 2  #f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
            elif key == 'THÌN'or key == 'TỴ':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 3  #f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 4  #f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 2  #f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 6  #f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                else:
                    nguhanh = 5  #f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
            elif key == 'NGỌ'or key == 'MÙI':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 5  #f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 3  #f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 4  #f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 2  #f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                else:
                    nguhanh = 6  #f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
            elif key == 'THÂN'or key == 'DẬU':
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 4  #f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 2  #f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 6  #f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 5  #f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                else:
                    nguhanh = 3  #f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
            else:
                if can_nam == 'GIÁP' or can_nam == 'KỶ':
                    nguhanh = 6  #f'{nguhanh_napam.upper()} - HỎA LỤC CỤC'
                elif can_nam == 'ẤT' or can_nam == 'CANH':
                    nguhanh = 5  #f'{nguhanh_napam.upper()} - THỔ NGỦ CỤC'
                elif can_nam == 'BÍNH' or can_nam == 'TÂN':
                    nguhanh = 3  #f'{nguhanh_napam.upper()} - MỘC TAM CỤC'
                elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
                    nguhanh = 4  #f'{nguhanh_napam.upper()} - KIM TỨ CỤC'
                else:
                    nguhanh = 2  #f'{nguhanh_napam.upper()} - THỦY NHỊ CỤC'
    socongthem = (0,1,2,3,4,5)
    print("index dan : ",saotuvi.index('DẦN'))
    for x in socongthem:
        if (ngay_am + x)%nguhanh == 0:
            thuongso = int((ngay_am + x)/nguhanh)
            if x % 2 == 0:
                print("an sao tu vi : ", chi_gio)
                print("an sao tu vi cung_menhthan: ", nguhanh)
                print("an sao XXXX : ", x)
                print("an sao thuong so: ", thuongso)
                index = int((saotuvi.index('DẦN') + thuongso) + x) - 1
                print("index % 2:: ",index)
                if index > 11:
                    index -= 12
                dia_chi = saotuvi[index]
                if dia_chi == 'TÝ':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div>','DẦN':'<div class="line black size2 bol">Phá Quân(H)</div>',"THÌN":'<div class="line red size2 bol">Liêm Trinh(M)</div><div class="line organ size2 bol">Thiên Phủ(V)</div>',"TỴ":'<div class="line black size2 bol">Thái Âm(H)</div>',"NGỌ":'<div class="line black size2 bol">Tham Lang(M)</div>',"Mùi":'<div class="line black size2 bol">Thiên Đồng(H)</div><div class="line black size2 bol">Cự Môn(H)</div>',"THÂN":'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line black size2 bol">Thiên Tướng(M)</div>',"DẬU":'<div class="line red size2 bol">Thái Dương(H)</div><div class="line green size2 bol">Thiên Lương(H)</div>',"TUẤT":'<div class="line grey size2 bol">Thất Sát(H)</div>',"HỢI":'<div class="line green size2 bol">Thiên Cơ(H)</div>'}
                elif dia_chi == 'SỬU':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(Đ)</div><div class="line black size2 bol">Phá Quân(V)</div>','MÃO':'<div class="line organ size2 bol">Thiên Phủ(B)</div>',"THÌN":'<div class="line black size2 bol">Thái Âm(H)</div>',"TỴ":'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Tham Lang(H)</div>',"NGỌ":'<div class="line black size2 bol">Cự Môn(V)</div>',"Mùi":'<div class="line black size2 bol">Thiên Tướng(Đ)</div>',"THÂN":'<div class="line black size2 bol">Thiên Đồng(M)</div><div class="line green size2 bol">Thiên Lương(V)</div>',"DẬU":'<div class="line grey size2 bol">Vũ Khúc(Đ)</div><div class="line grey size2 bol">Thất Sát(H)</div>',"TUẤT":'<div class="line grey size2 bol">Thái Dương(H)</div>'}
                elif dia_chi == 'DẦN':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div><div class="line black size2 bol">Thiên Phủ(M)</div>','SỬU':'<div class="line green size2 bol">Thiên Cơ(Đ)</div>','TÝ':'<div class="line black size2 bol">Phá Quân(M)</div>','MÃO':'<div class="line black size2 bol">Thái Âm(H)</div>',"THÌN":'<div class="line black size2 bol">Tham Lang(V)</div>',"TỴ":'<div class="line black size2 bol">Cự Môn(H)</div>',"NGỌ":'<div class="line red size2 bol">Liêm Trinh(V)</div><div class="line black size2 bol">Thiên Tướng(V)</div>',"Mùi":'<div class="line green size2 bol">Thiên Lương(Đ)</div>',"THÂN":'<div class="line grey size2 bol">Thất Sát(M)</div>',"DẬU":'<div class="line black size2 bol">Thiên Đồng(H)</div>',"TUẤT":'<div class="line grey size2 bol">Vũ Khúc(M)</div>',"HỢI":'<div class="line red size2 bol">Thái Dương(H)</div>'}
                elif dia_chi == 'MÃO':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div><div class="line black size2 bol">Tham Lang(H)</div>','DẦN':'<div class="line green size2 bol">Thiên Cơ(H)</div><div class="line black size2 bol">Thái Âm(H)</div>','SỬU':'<div class="line organ size2 bol">Thiên Phủ(B)</div>','TÝ':'<div class="line red size2 bol">Thái Dương(H)</div>',"THÌN":'<div class="line black size2 bol">Cự Môn(H)</div>',"TỴ":'<div class="line black size2 bol">Thiên Tướng(Đ)</div>',"NGỌ":'<div class="line green size2 bol">Thiên Lương(M)</div>',"Mùi":'<div class="line red size2 bol">Liêm Trinh(Đ)</div><div class="line grey size2 bol">Thất Sát(Đ)</div>',"TUẤT":'<div class="line black size2 bol">Thiên Đồng(H)</div>',"HỢI":'<div class="line green size2 bol">Vũ Khúc(H)</div><div class="line black size2 bol">Phá Quân(H)</div>'}
                elif dia_chi == 'THÌN':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(V)</div><div class="line black size2 bol">Thiên Tướng(V)</div>','DẦN':'<div class="line black size2 bol">Tham Lang(Đ)</div>','SỬU':'<div class="line red size2 bol">Thái Dương(Đ)</div><div class="line black size2 bol">Thái Âm(Đ)</div>','TÝ':'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line organ size2 bol">Thiên Phủ(V)</div>',"MÃO":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line black size2 bol">Cự Môn(M)</div>',"TỴ":'<div class="line green size2 bol">Thiên Lương(H)</div>',"NGỌ":'<div class="line grey size2 bol">Thất Sát(M)</div>',"THÂN":'<div class="line red size2 bol">Liêm Trinh(V)</div>',"TUẤT":'<div class="line black size2 bol">Phá Quân(Đ)</div>',"HỢI":'<div class="line black size2 bol">Thiên Đồng(Đ)</div>'}
                elif dia_chi == 'TỴ':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div><div class="line grey size2 bol">Thất Sát(V)</div>','DẦN':'<div class="line red size2 bol">Thái Dương(V)</div><div class="line black size2 bol">Cự Môn(V)</div>','SỬU':'<div class="line grey size2 bol">Vũ Khúc(M)</div><div class="line black size2 bol">Tham Lang(M)</div>','TÝ':'<div class="line black size2 bol">Thiên Đồng(V)</div><div class="line black size2 bol">Thái Âm(V)</div>','MÃO':'<div class="line black size2 bol">Thiên Tướng(H)</div>',"THÌN":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line green size2 bol">Thiên Lương(M)</div>',"DẬU":'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Phá Quân(H)</div>',"HỢI":'<div class="line organ size2 bol">Thiên Phủ(Đ)</div>'}
                elif dia_chi == 'NGỌ':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div>','DẦN':'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line black size2 bol">Thiên Tướng(M)</div>','SỬU':'<div class="line black size2 bol">Thiên Đồng(H)</div><div class="line black size2 bol">Cự Môn(H)</div>','TÝ':'<div class="line black size2 bol">Tham Lang(H)</div>','MÃO':'<div class="line red size2 bol">Thái Dương(V)</div><div class="line green size2 bol">Thiên Lương(V)</div>',"THÌN":'<div class="line green size2 bol">Thất Sát(H)</div>',"TỴ":'<div class="line green size2 bol">Thiên Cơ(V)</div>',"THÂN":'<div class="line black size2 bol">Phá Quân(H)</div>',"TUẤT":'<div class="line red size2 bol">Liêm Trinh(M)</div><div class="line organ size2 bol">Thiên Phủ(V)</div>',"HỢI":'<div class="line black size2 bol">Thái Âm(M)</div>'}
                elif dia_chi == 'MÙI':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(Đ)</div><div class="line black size2 bol">Phá Quân(V)</div>','DẦN':'<div class="line black size2 bol">Thiên Đồng(M)</div><div class="line green size2 bol">Thiên Lương(V)</div>','MÃO':'<div class="line grey size2 bol">Vũ Khúc(M)</div><div class="line gray size2 bol">Thất Sát(H)</div>','SỬU':'<div class="line black size2 bol">Thiên Tướng(Đ)</div>','TÝ':'<div class="line black size2 bol">Cự Môn(V)</div>',"THÌN":'<div class="line red size2 bol">Thái Dương(V)</div>',"NGỌ":'<div class="line green size2 bol">Thiên Cơ(Đ)</div>',"DẬU":'<div class="line organ size2 bol">Thiên Phủ(B)</div>',"TUẤT":'<div class="line black size2 bol">Thái Âm(M)</div>',"HỢI":'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Tham Lang(H)</div>'}
                elif dia_chi == 'THÂN':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div><div class="line organ size2 bol">Thiên Phủ(M)</div>','DẦN':'<div class="line gray size2 bol">Thất Sát(M)</div>','SỬU':'<div class="line green size2 bol">Thiên Lương(Đ)</div>','TÝ':'<div class="line black size2 bol">Thiên Tướng(V)</div><div class="line red size2 bol">Liêm Trinh(V)</div>',"THÌN":'<div class="line grey size2 bol">Vũ Khúc(M)</div>',"TỴ":'<div class="line red size2 bol">Thái Dương(M)</div>',"NGỌ":'<div class="line black size2 bol">Phá Quân(M)</div>',"Mùi":'<div class="line green size2 bol">Thiên Cơ(Đ)</div>',"DẬU":'<div class="line black size2 bol">Thái Âm(M)</div>',"TUẤT":'<div class="line black size2 bol">Tham Lang(V)</div>',"HỢI":'<div class="line black size2 bol">Cư Môn(Đ)</div>','MÃO':'<div class="line black size2 bol">Thiên Đồng(Đ)</div>'}
                elif dia_chi == 'DẬU':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div><div class="line black size2 bol">Tham Lang(H)</div>','SỬU':'<div class="line red size2 bol">Liêm Trinh(Đ)</div><div class="line grey size2 bol">Thất Sát(Đ)</div>','TÝ':'<div class="line green size2 bol">Thiên Lương(V)</div>',"THÌN":'<div class="line black size2 bol">Thiên Đồng(H)</div>',"TỴ":'<div class="line black size2 bol">Phá Quân(H)</div><div class="line grey size2 bol">Vũ Khúc(H)</div>',"NGỌ":'<div class="line red size2 bol">Thái Dương(M)</div>',"Mùi":'<div class="line organ size2 bol">Thiên Phủ(Đ)</div>',"THÂN":'<div class="line black size2 bol">Thiên Cơ(V)</div><div class="line green size2 bol">Thiên Cơ(V)</div>',"TUẤT":'<div class="line black size2 bol">Cư Môn(H)</div>',"HỢI":'<div class="line black size2 bol">Thiên Tướng(Đ)</div>','TUẤT':'<div class="line black size2 bol">Cự Môn(H)</div>'}
                elif dia_chi == 'TUẤT':
                    #đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(V)</div><div class="line black size2 bol">Thiên Tướng(V)</div>','DẦN':'<div class="line red size2 bol">Liêm Trinh(V)</div>','TÝ':'<div class="line grey size2 bol">Thất Sát(M)</div>',"THÌN":'<div class="line black size2 bol">Phá Quân(Đ)</div>',"TỴ":'<div class="line black size2 bol">Thiên Đồng(Đ)</div>',"NGỌ":'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line organ size2 bol">Thiên Phủ(M)</div>',"Mùi":'<div class="line red size2 bol">Thái Dương(Đ)</div><div class="line black size2 bol">Thái Âm(Đ)</div>',"THÂN":'<div class="line black size2 bol">Tham Lang(Đ)</div>',"DẬU":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line black size2 bol">Cư Môn(M)</div>',"HỢI":'<div class="line green size2 bol">Thiên Lương(H)</div>'}
                else:
                    #đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div><div class="line grey size2 bol">Thất Sát(V)</div>',"TỴ":'<div class="line organ size2 bol">Thiên Phủ(Đ)</div>',"NGỌ":'<div class="line black size2 bol">Thiên Đồng(H)</div><div class="line black size2 bol">Thái Âm(H)</div>',"Mùi":'<div class="line grey size2 bol">Vũ Khúc(M)</div><div class="line black size2 bol">Tham Lang(M)</div>',"THÂN":'<div class="line red size2 bol">Thái Dương(H)</div><div class="line black size2 bol">Cự Môn(Đ)</div>',"DẬU":'<div class="line black size2 bol">Thiên Tướng(H)</div>',"TUẤT":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line green size2 bol">Thiên Lương(M)</div>','MÃO':'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Phá Quân(H)</div>'}

                print("dia_chi % 2: ", dia_chi)
            else:
                index = int((saotuvi.index('DẦN') + thuongso) - x) - 1
                print("index: ",index)
                if index > 11:
                    index -= 12
                dia_chi = saotuvi[index]
                if dia_chi == 'TÝ':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div>','DẦN':'<div class="line black size2 bol">Phá Quân(H)</div>',"THÌN":'<div class="line red size2 bol">Liêm Trinh(M)</div><div class="line organ size2 bol">Thiên Phủ(V)</div>',"TỴ":'<div class="line black size2 bol">Thái Âm(H)</div>',"NGỌ":'<div class="line black size2 bol">Tham Lang(M)</div>',"Mùi":'<div class="line black size2 bol">Thiên Đồng(H)</div><div class="line black size2 bol">Cự Môn(H)</div>',"THÂN":'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line black size2 bol">Thiên Tướng(M)</div>',"DẬU":'<div class="line red size2 bol">Thái Dương(H)</div><div class="line green size2 bol">Thiên Lương(H)</div>',"TUẤT":'<div class="line grey size2 bol">Thất Sát(H)</div>',"HỢI":'<div class="line green size2 bol">Thiên Cơ(H)</div>'}
                elif dia_chi == 'SỬU':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(Đ)</div><div class="line black size2 bol">Phá Quân(V)</div>','MÃO':'<div class="line organ size2 bol">Thiên Phủ(B)</div>',"THÌN":'<div class="line black size2 bol">Thái Âm(H)</div>',"TỴ":'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Tham Lang(H)</div>',"NGỌ":'<div class="line black size2 bol">Cự Môn(V)</div>',"Mùi":'<div class="line black size2 bol">Thiên Tướng(Đ)</div>',"THÂN":'<div class="line black size2 bol">Thiên Đồng(M)</div><div class="line green size2 bol">Thiên Lương(V)</div>',"DẬU":'<div class="line grey size2 bol">Vũ Khúc(Đ)</div><div class="line grey size2 bol">Thất Sát(H)</div>',"TUẤT":'<div class="line grey size2 bol">Thái Dương(H)</div>'}
                elif dia_chi == 'DẦN':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div><div class="line black size2 bol">Thiên Phủ(M)</div>','SỬU':'<div class="line green size2 bol">Thiên Cơ(Đ)</div>','TÝ':'<div class="line black size2 bol">Phá Quân(M)</div>','MÃO':'<div class="line black size2 bol">Thái Âm(H)</div>',"THÌN":'<div class="line black size2 bol">Tham Lang(V)</div>',"TỴ":'<div class="line black size2 bol">Cự Môn(H)</div>',"NGỌ":'<div class="line red size2 bol">Liêm Trinh(V)</div><div class="line black size2 bol">Thiên Tướng(V)</div>',"Mùi":'<div class="line green size2 bol">Thiên Lương(Đ)</div>',"THÂN":'<div class="line grey size2 bol">Thất Sát(M)</div>',"DẬU":'<div class="line black size2 bol">Thiên Đồng(H)</div>',"TUẤT":'<div class="line grey size2 bol">Vũ Khúc(M)</div>',"HỢI":'<div class="line red size2 bol">Thái Dương(H)</div>'}
                elif dia_chi == 'MÃO':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div><div class="line black size2 bol">Tham Lang(H)</div>','DẦN':'<div class="line green size2 bol">Thiên Cơ(H)</div><div class="line black size2 bol">Thái Âm(H)</div>','SỬU':'<div class="line organ size2 bol">Thiên Phủ(B)</div>','TÝ':'<div class="line red size2 bol">Thái Dương(H)</div>',"THÌN":'<div class="line black size2 bol">Cự Môn(H)</div>',"TỴ":'<div class="line black size2 bol">Thiên Tướng(Đ)</div>',"NGỌ":'<div class="line green size2 bol">Thiên Lương(M)</div>',"Mùi":'<div class="line red size2 bol">Liêm Trinh(Đ)</div><div class="line grey size2 bol">Thất Sát(Đ)</div>',"TUẤT":'<div class="line black size2 bol">Thiên Đồng(H)</div>',"HỢI":'<div class="line green size2 bol">Vũ Khúc(H)</div><div class="line black size2 bol">Phá Quân(H)</div>'}
                elif dia_chi == 'THÌN':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(V)</div><div class="line black size2 bol">Thiên Tướng(V)</div>','DẦN':'<div class="line black size2 bol">Tham Lang(Đ)</div>','SỬU':'<div class="line red size2 bol">Thái Dương(Đ)</div><div class="line black size2 bol">Thái Âm(Đ)</div>','TÝ':'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line organ size2 bol">Thiên Phủ(V)</div>',"MÃO":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line black size2 bol">Cự Môn(M)</div>',"TỴ":'<div class="line green size2 bol">Thiên Lương(H)</div>',"NGỌ":'<div class="line grey size2 bol">Thất Sát(M)</div>',"THÂN":'<div class="line red size2 bol">Liêm Trinh(V)</div>',"TUẤT":'<div class="line black size2 bol">Phá Quân(Đ)</div>',"HỢI":'<div class="line black size2 bol">Thiên Đồng(Đ)</div>'}
                elif dia_chi == 'TỴ':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div><div class="line grey size2 bol">Thất Sát(V)</div>','DẦN':'<div class="line red size2 bol">Thái Dương(V)</div><div class="line black size2 bol">Cự Môn(V)</div>','SỬU':'<div class="line grey size2 bol">Vũ Khúc(M)</div><div class="line black size2 bol">Tham Lang(M)</div>','TÝ':'<div class="line black size2 bol">Thiên Đồng(V)</div><div class="line black size2 bol">Thái Âm(V)</div>','MÃO':'<div class="line black size2 bol">Thiên Tướng(H)</div>',"THÌN":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line green size2 bol">Thiên Lương(M)</div>',"DẬU":'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Phá Quân(H)</div>',"HỢI":'<div class="line organ size2 bol">Thiên Phủ(Đ)</div>'}
                elif dia_chi == 'NGỌ':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div>','DẦN':'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line black size2 bol">Thiên Tướng(M)</div>','SỬU':'<div class="line black size2 bol">Thiên Đồng(H)</div><div class="line black size2 bol">Cự Môn(H)</div>','TÝ':'<div class="line black size2 bol">Tham Lang(H)</div>','MÃO':'<div class="line red size2 bol">Thái Dương(V)</div><div class="line green size2 bol">Thiên Lương(V)</div>',"THÌN":'<div class="line green size2 bol">Thất Sát(H)</div>',"TỴ":'<div class="line green size2 bol">Thiên Cơ(V)</div>',"THÂN":'<div class="line black size2 bol">Phá Quân(H)</div>',"TUẤT":'<div class="line red size2 bol">Liêm Trinh(M)</div><div class="line organ size2 bol">Thiên Phủ(V)</div>',"HỢI":'<div class="line black size2 bol">Thái Âm(M)</div>'}
                elif dia_chi == 'MÙI':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(Đ)</div><div class="line black size2 bol">Phá Quân(V)</div>','DẦN':'<div class="line black size2 bol">Thiên Đồng(M)</div><div class="line green size2 bol">Thiên Lương(V)</div>','MÃO':'<div class="line grey size2 bol">Vũ Khúc(M)</div><div class="line gray size2 bol">Thất Sát(H)</div>','SỬU':'<div class="line black size2 bol">Thiên Tướng(Đ)</div>','TÝ':'<div class="line black size2 bol">Cự Môn(V)</div>',"THÌN":'<div class="line red size2 bol">Thái Dương(V)</div>',"NGỌ":'<div class="line green size2 bol">Thiên Cơ(Đ)</div>',"DẬU":'<div class="line organ size2 bol">Thiên Phủ(B)</div>',"TUẤT":'<div class="line black size2 bol">Thái Âm(M)</div>',"HỢI":'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Tham Lang(H)</div>'}
                elif dia_chi == 'THÂN':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(M)</div><div class="line organ size2 bol">Thiên Phủ(M)</div>','DẦN':'<div class="line gray size2 bol">Thất Sát(M)</div>','SỬU':'<div class="line green size2 bol">Thiên Lương(Đ)</div>','TÝ':'<div class="line black size2 bol">Thiên Tướng(V)</div><div class="line red size2 bol">Liêm Trinh(V)</div>',"THÌN":'<div class="line grey size2 bol">Vũ Khúc(M)</div>',"TỴ":'<div class="line red size2 bol">Thái Dương(M)</div>',"NGỌ":'<div class="line black size2 bol">Phá Quân(M)</div>',"Mùi":'<div class="line green size2 bol">Thiên Cơ(Đ)</div>',"DẬU":'<div class="line black size2 bol">Thái Âm(M)</div>',"TUẤT":'<div class="line black size2 bol">Tham Lang(V)</div>',"HỢI":'<div class="line black size2 bol">Cư Môn(Đ)</div>','MÃO':'<div class="line black size2 bol">Thiên Đồng(Đ)</div>'}
                elif dia_chi == 'DẬU':
                    # đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div><div class="line black size2 bol">Tham Lang(H)</div>','SỬU':'<div class="line red size2 bol">Liêm Trinh(Đ)</div><div class="line grey size2 bol">Thất Sát(Đ)</div>','TÝ':'<div class="line green size2 bol">Thiên Lương(V)</div>',"THÌN":'<div class="line black size2 bol">Thiên Đồng(H)</div>',"TỴ":'<div class="line black size2 bol">Phá Quân(H)</div><div class="line grey size2 bol">Vũ Khúc(H)</div>',"NGỌ":'<div class="line red size2 bol">Thái Dương(M)</div>',"Mùi":'<div class="line organ size2 bol">Thiên Phủ(Đ)</div>',"THÂN":'<div class="line black size2 bol">Thiên Cơ(V)</div><div class="line green size2 bol">Thiên Cơ(V)</div>',"TUẤT":'<div class="line black size2 bol">Cư Môn(H)</div>',"HỢI":'<div class="line black size2 bol">Thiên Tướng(Đ)</div>','TUẤT':'<div class="line black size2 bol">Cự Môn(H)</div>'}
                elif dia_chi == 'TUẤT':
                    #đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(V)</div><div class="line black size2 bol">Thiên Tướng(V)</div>','DẦN':'<div class="line red size2 bol">Liêm Trinh(V)</div>','TÝ':'<div class="line grey size2 bol">Thất Sát(M)</div>',"THÌN":'<div class="line black size2 bol">Phá Quân(Đ)</div>',"TỴ":'<div class="line black size2 bol">Thiên Đồng(Đ)</div>',"NGỌ":'<div class="line grey size2 bol">Vũ Khúc(V)</div><div class="line organ size2 bol">Thiên Phủ(M)</div>',"Mùi":'<div class="line red size2 bol">Thái Dương(Đ)</div><div class="line black size2 bol">Thái Âm(Đ)</div>',"THÂN":'<div class="line black size2 bol">Tham Lang(Đ)</div>',"DẬU":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line black size2 bol">Cư Môn(M)</div>',"HỢI":'<div class="line green size2 bol">Thiên Lương(H)</div>'}
                else:
                    #đã xong
                    ansaochutinh ={dia_chi: '<div class="line organ size2 bol">Tử Vi(B)</div><div class="line grey size2 bol">Thất Sát(V)</div>',"TỴ":'<div class="line organ size2 bol">Thiên Phủ(Đ)</div>',"NGỌ":'<div class="line black size2 bol">Thiên Đồng(H)</div><div class="line black size2 bol">Thái Âm(H)</div>',"Mùi":'<div class="line grey size2 bol">Vũ Khúc(M)</div><div class="line black size2 bol">Tham Lang(M)</div>',"THÂN":'<div class="line red size2 bol">Thái Dương(H)</div><div class="line black size2 bol">Cự Môn(Đ)</div>',"DẬU":'<div class="line black size2 bol">Thiên Tướng(H)</div>',"TUẤT":'<div class="line green size2 bol">Thiên Cơ(M)</div><div class="line green size2 bol">Thiên Lương(M)</div>','MÃO':'<div class="line red size2 bol">Liêm Trinh(H)</div><div class="line black size2 bol">Phá Quân(H)</div>'}

                print("dia_chi : ", dia_chi)
            return ansaochutinh
    return ''

# Kim Tứ Cục khởi Trường Sinh tại Tỵ

# Mộc Tam Cục khởi Trường sinh tại Hợi

# Hỏa Lục Cục khởi Trường sinh tại Dần

# Thủy nhị Cục và Thổ Ngũ Cục khởi Trường Sinh tại Thân
def vongtruongsinhtuvi(*truongsinh):
    chi_gio = truongsinh[0]
    thang_am = truongsinh[1]
    can_nam = truongsinh[2]
    chi_nam = truongsinh[3]
    option = truongsinh[4]
    cuc_nguhanh = cucnguhanh(chi_gio,thang_am,can_nam,chi_nam)
    vongtruongsinh = {}
    if option == 'Nam':
        if chi_nam in chi_duong:
            if cuc_nguhanh == 'KIM TỨ CỤC':
                vongtruongsinh = {'TỴ':"Trường Sinh",
                                  'NGỌ':"Mộc Dục",
                                  'MÙI':"Quan Đới",
                                  'THÂN':"Lâm Quan",
                                  'DẬU':"Đế Vượng",
                                  'TUẤT':"Suy",
                                  'HỢI':"Bệnh",
                                  'TÝ':"Tử",
                                  'SỬU':"Mộ",
                                  'DẦN':"Tuyệt",
                                  'MÃO':"Thai",
                                  'THÌN':"Dưỡng"}
            elif cuc_nguhanh == 'THỦY NHỊ CỤC' or cuc_nguhanh == 'THỔ NGỦ CỤC':
                vongtruongsinh = {'THÂN':"Trường Sinh",
                                  'DẬU':"Mộc Dục",
                                  'TUẤT':"Quan Đới",
                                  'HỢI':"Lâm Quan",
                                  'TÝ':"Đế Vượng",
                                  'SỬU':"Suy",
                                  'DẦN':"Bệnh",
                                  'MÃO':"Tử",
                                  'THÌN':"Mộ",
                                  'TỴ':"Tuyệt",
                                  'NGỌ':"Thai",
                                  'MÙI':"Dưỡng"}
            elif cuc_nguhanh == 'MỘC TAM CỤC':
                vongtruongsinh = {'HỢI':"Trường Sinh",
                                  'TÝ':"Mộc Dục",
                                  'SỬU':"Quan Đới",
                                  'DẦN':"Lâm Quan",
                                  'MÃO':"Đế Vượng",
                                  'THÌN':"Suy",
                                  'TỴ':"Bệnh",
                                  'NGỌ':"Tử",
                                  'MÙI':"Mộ",
                                  'THÂN':"Tuyệt",
                                  'DẬU':"Thai",
                                  'TUẤT':"Dưỡng"}
            else:
                vongtruongsinh = {'DẦN':"Trường Sinh",
                                  'MÃO':"Mộc Dục",
                                  'THÌN':"Quan Đới",
                                  'TỴ':"Lâm Quan",
                                  'NGỌ':"Đế Vượng",
                                  'MÙI':"Suy",
                                  'THÂN':"Bệnh",
                                  'DẬU':"Tử",
                                  'TUẤT':"Mộ",
                                  'HỢI':"Tuyệt",
                                  'TÝ':"Thai",
                                  'SỬU':"Dưỡng"}
        else:
            if cuc_nguhanh == 'KIM TỨ CỤC':
                vongtruongsinh = {'TỴ':"Trường Sinh",
                                  'THÌN':"Mộc Dục",
                                  'MÃO':"Quan Đới",
                                  'DẦN':"Lâm Quan",
                                  'SỬU':"Đế Vượng",
                                  'TÝ':"Suy",
                                  'HỢI':"Bệnh",
                                  'TUẤT':"Tử",
                                  'DẬU':"Mộ",
                                  'THÂN':"Tuyệt",
                                  'MÙI':"Thai",
                                  'NGỌ':"Dưỡng"}
            elif cuc_nguhanh == 'THỦY NHỊ CỤC' or cuc_nguhanh == 'THỔ NGỦ CỤC':
                vongtruongsinh = {'THÂN':"Trường Sinh",
                                  'MÙI':"Mộc Dục",
                                  'NGỌ':"Quan Đới",
                                  'TỴ':"Lâm Quan",
                                  'THÌN':"Đế Vượng",
                                  'MÃO':"Suy",
                                  'DẦN':"Bệnh",
                                  'SỬU':"Tử",
                                  'TÝ':"Mộ",
                                  'HỢI':"Tuyệt",
                                  'TUẤT':"Thai",
                                  'DẬU':"Dưỡng"}
            elif cuc_nguhanh == 'MỘC TAM CỤC':
                vongtruongsinh = {'HỢI':"Trường Sinh",
                                  'TUẤT':"Mộc Dục",
                                  'DẬU':"Quan Đới",
                                  'THÂN':"Lâm Quan",
                                  'MÙI':"Đế Vượng",
                                  'NGỌ':"Suy",
                                  'TỴ':"Bệnh",
                                  'THÌN':"Tử",
                                  'MÃO':"Mộ",
                                  'DẦN':"Tuyệt",
                                  'SỬU':"Thai",
                                  'TÝ':"Dưỡng"}
            else:
                vongtruongsinh = {'DẦN':"Trường Sinh",
                                  'SỬU':"Mộc Dục",
                                  'TÝ':"Quan Đới",
                                  'HỢI':"Lâm Quan",
                                  'TUẤT':"Đế Vượng",
                                  'DẬU':"Suy",
                                  'THÂN':"Bệnh",
                                  'MÙI':"Tử",
                                  'NGỌ':"Mộ",
                                  'TỴ':"Tuyệt",
                                  'THÌN':"Thai",
                                  'MÃO':"Dưỡng"}
    else:
        if chi_nam in chi_am:
            if cuc_nguhanh == 'KIM TỨ CỤC':
                vongtruongsinh = {'TỴ':"Trường Sinh",
                                  'NGỌ':"Mộc Dục",
                                  'MÙI':"Quan Đới",
                                  'THÂN':"Lâm Quan",
                                  'DẬU':"Đế Vượng",
                                  'TUẤT':"Suy",
                                  'HỢI':"Bệnh",
                                  'TÝ':"Tử",
                                  'SỬU':"Mộ",
                                  'DẦN':"Tuyệt",
                                  'MÃO':"Thai",
                                  'THÌN':"Dưỡng"}
            elif cuc_nguhanh == 'THỦY NHỊ CỤC' or cuc_nguhanh == 'THỔ NGỦ CỤC':
                vongtruongsinh = {'THÂN':"Trường Sinh",
                                  'DẬU':"Mộc Dục",
                                  'TUẤT':"Quan Đới",
                                  'HỢI':"Lâm Quan",
                                  'TÝ':"Đế Vượng",
                                  'SỬU':"Suy",
                                  'DẦN':"Bệnh",
                                  'MÃO':"Tử",
                                  'THÌN':"Mộ",
                                  'TỴ':"Tuyệt",
                                  'NGỌ':"Thai",
                                  'MÙI':"Dưỡng"}
            elif cuc_nguhanh == 'MỘC TAM CỤC':
                vongtruongsinh = {'HỢI':"Trường Sinh",
                                  'TÝ':"Mộc Dục",
                                  'SỬU':"Quan Đới",
                                  'DẦN':"Lâm Quan",
                                  'MÃO':"Đế Vượng",
                                  'THÌN':"Suy",
                                  'TỴ':"Bệnh",
                                  'NGỌ':"Tử",
                                  'MÙI':"Mộ",
                                  'THÂN':"Tuyệt",
                                  'DẬU':"Thai",
                                  'TUẤT':"Dưỡng"}
            else:
                vongtruongsinh = {'DẦN':"Trường Sinh",
                                  'MÃO':"Mộc Dục",
                                  'THÌN':"Quan Đới",
                                  'TỴ':"Lâm Quan",
                                  'NGỌ':"Đế Vượng",
                                  'MÙI':"Suy",
                                  'THÂN':"Bệnh",
                                  'DẬU':"Tử",
                                  'TUẤT':"Mộ",
                                  'HỢI':"Tuyệt",
                                  'TÝ':"Thai",
                                  'SỬU':"Dưỡng"}
        else:
            if cuc_nguhanh == 'KIM TỨ CỤC':
                vongtruongsinh = {'TỴ':"Trường Sinh",
                                  'THÌN':"Mộc Dục",
                                  'MÃO':"Quan Đới",
                                  'DẦN':"Lâm Quan",
                                  'SỬU':"Đế Vượng",
                                  'TÝ':"Suy",
                                  'HỢI':"Bệnh",
                                  'TUẤT':"Tử",
                                  'DẬU':"Mộ",
                                  'THÂN':"Tuyệt",
                                  'MÙI':"Thai",
                                  'NGỌ':"Dưỡng"}
            elif cuc_nguhanh == 'THỦY NHỊ CỤC' or cuc_nguhanh == 'THỔ NGỦ CỤC':
                vongtruongsinh = {'THÂN':"Trường Sinh",
                                  'MÙI':"Mộc Dục",
                                  'NGỌ':"Quan Đới",
                                  'TỴ':"Lâm Quan",
                                  'THÌN':"Đế Vượng",
                                  'MÃO':"Suy",
                                  'DẦN':"Bệnh",
                                  'SỬU':"Tử",
                                  'TÝ':"Mộ",
                                  'HỢI':"Tuyệt",
                                  'TUẤT':"Thai",
                                  'DẬU':"Dưỡng"}
            elif cuc_nguhanh == 'MỘC TAM CỤC':
                vongtruongsinh = {'HỢI':"Trường Sinh",
                                  'TUẤT':"Mộc Dục",
                                  'DẬU':"Quan Đới",
                                  'THÂN':"Lâm Quan",
                                  'MÙI':"Đế Vượng",
                                  'NGỌ':"Suy",
                                  'TỴ':"Bệnh",
                                  'THÌN':"Tử",
                                  'MÃO':"Mộ",
                                  'DẦN':"Tuyệt",
                                  'SỬU':"Thai",
                                  'TÝ':"Dưỡng"}
            else:
                vongtruongsinh = {'DẦN':"Trường Sinh",
                                  'SỬU':"Mộc Dục",
                                  'TÝ':"Quan Đới",
                                  'HỢI':"Lâm Quan",
                                  'TUẤT':"Đế Vượng",
                                  'DẬU':"Suy",
                                  'THÂN':"Bệnh",
                                  'MÙI':"Tử",
                                  'NGỌ':"Mộ",
                                  'TỴ':"Tuyệt",
                                  'THÌN':"Thai",
                                  'MÃO':"Dưỡng"}



    return vongtruongsinh

def vonglocton(can_nam,chi_nam,option):
    locton = {}
    if option == 'Nam':
        if chi_nam in chi_am:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line green size2">Lộc Tồn</div>',
                'SỬU':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'TÝ':'<div class="line black size2">Thanh Long</div>',
                'HỢI XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TUẤT':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'DẬU':'<div class="line grey size2">Tấu Thư</div>',
                'THÂN':'<div class="line red size2">Phi Liêm</div>',
                'MÙI':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'NGỌ XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TỴ XẤU':'<div class="line red size2">Đại Hao</div>',
                'THÌN XẤU':'<div class="line red size2">Phục Binh</div>',
                'MÃO':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line green size2">Lộc Tồn</div>',
                'DẦN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'SỬU':'<div class="line black size2">Thanh Long</div>',
                'TÝ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'HỢI':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'TUẤT':'<div class="line grey size2">Tấu Thư</div>',
                'DẬU':'<div class="line red size2">Phi Liêm</div>',
                'THÂN':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'MÙI XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'NGỌ XẤU':'<div class="line red size2">Đại Hao</div>',
                'TỴ XẤU':'<div class="line red size2">Phục Binh</div>',
                'THÌN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line green size2">Lộc Tồn</div>',
                'THÌN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'MÃO':'<div class="line black size2">Thanh Long</div>',
                'DẦN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'SỬU':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'TÝ':'<div class="line grey size2">Tấu Thư</div>',
                'HỢI':'<div class="line red size2">Phi Liêm</div>',
                'TUẤT':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'DẬU XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'THÂN XẤU':'<div class="line red size2">Đại Hao</div>',
                'MÙI XẤU':'<div class="line red size2">Phục Binh</div>',
                'NGỌ':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line green size2">Lộc Tồn</div>',
                'TỴ':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'THÌN':'<div class="line black size2">Thanh Long</div>',
                'MÃO XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'DẦN':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'SỬU':'<div class="line grey size2">Tấu Thư</div>',
                'TÝ':'<div class="line red size2">Phi Liêm</div>',
                'HỢI':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'TUẤT XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'DẬU XẤU':'<div class="line red size2">Đại Hao</div>',
                'THÂN XẤU':'<div class="line red size2">Phục Binh</div>',
                'MÙI':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line green size2">Lộc Tồn</div>',
                'MÙI':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'NGỌ':'<div class="line black size2">Thanh Long</div>',
                'TỴ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'THÌN':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'MÃO':'<div class="line grey size2">Tấu Thư</div>',
                'DẦN':'<div class="line red size2">Phi Liêm</div>',
                'SỬU':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'TÝ XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'HỢI XẤU':'<div class="line red size2">Đại Hao</div>',
                'TUẤT XẤU':'<div class="line red size2">Phục Binh</div>',
                'DẬU':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line green size2">Lộc Tồn</div>',
                'THÂN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'MÙI':'<div class="line black size2">Thanh Long</div>',
                'NGỌ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TỴ':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'THÌN':'<div class="line grey size2">Tấu Thư</div>',
                'MÃO':'<div class="line red size2">Phi Liêm</div>',
                'DẦN':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'SỬU XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TÝ XẤU':'<div class="line red size2">Đại Hao</div>',
                'HỢI XẤU':'<div class="line red size2">Phục Binh</div>',
                'TUẤT':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line green size2">Lộc Tồn</div>',
                'TUẤT':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'DẬU':'<div class="line black size2">Thanh Long</div>',
                'THÂN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'MÙI':'<div class="line green size2">Tướng Quân</div>',
                'NGỌ':'<div class="line grey size2">Tấu Thư</div><div class="line organ size2">Quốc Ấn</div>',
                'TỴ':'<div class="line red size2">Phi Liêm</div>',
                'THÌN':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'MÃO XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'DẦN XẤU':'<div class="line red size2">Đại Hao</div>',
                'SỬU XẤU':'<div class="line red size2">Phục Binh</div>',
                'TÝ':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            else:
                locton = {'TÝ':'<div class="line green size2">Lộc Tồn</div>',
                'HỢI':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'TUẤT':'<div class="line black size2">Thanh Long</div>',
                'DẬU XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'THÂN':'<div class="line green size2">Tướng Quân</div>',
                'MÙI':'<div class="line grey size2">Tấu Thư</div><div class="line organ size2">Quốc Ấn</div>',
                'NGỌ':'<div class="line red size2">Phi Liêm</div>',
                'TỴ':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'THÌN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'MÃO XẤU':'<div class="line red size2">Đại Hao</div>',
                'DẦN XẤU':'<div class="line red size2">Phục Binh</div>',
                'SỬU':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}

        else:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line green size2">Lộc Tồn</div>',
                'MÃO':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'THÌN':'<div class="line black size2">Thanh Long</div>',
                'TỴ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'NGỌ':'<div class="line green size2">Tướng Quân</div>',
                'MÙI':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'THÂN':'<div class="line red size2">Phi Liêm</div>',
                'DẬU':'<div class="line green size2">Hỉ Thần</div>',
                'TUẤT XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TUẤT':'<div class="line organ size2">Quốc Ấn</div>',
                'HỢI XẤU':'<div class="line red size2">Đại Hao</div>',
                'TÝ XẤU':'<div class="line red size2">Phục Binh</div>',
                'SỬU':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line green size2">Lộc Tồn</div>',
                'THÌN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'TỴ':'<div class="line black size2">Thanh Long</div>',
                'NGỌ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'MÙI':'<div class="line green size2">Tướng Quân</div>',
                'THÂN':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'DẬU':'<div class="line red size2">Phi Liêm</div>',
                'TUẤT':'<div class="line green size2">Hỉ Thần</div>',
                'HỢI XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'HỢI':'<div class="line organ size2">Quốc Ấn</div>',
                'TÝ XẤU':'<div class="line red size2">Đại Hao</div>',
                'SỬU XẤU':'<div class="line red size2">Phục Binh</div>',
                'DẦN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line green size2">Lộc Tồn</div>',
                'NGỌ':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'MÙI':'<div class="line black size2">Thanh Long</div>',
                'THÂN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'DẬU':'<div class="line green size2">Tướng Quân</div>',
                'TUẤT':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'HỢI':'<div class="line red size2">Phi Liêm</div>',
                'TÝ':'<div class="line green size2">Hỉ Thần</div>',
                'SỬU XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'SỬU':'<div class="line organ size2">Quốc Ấn</div>',
                'DẦN XẤU':'<div class="line red size2">Đại Hao</div>',
                'MÃO XẤU':'<div class="line red size2">Phục Binh</div>',
                'THÌN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line green size2">Lộc Tồn</div>',
                'MÙI':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'THÂN':'<div class="line black size2">Thanh Long</div>',
                'DẬU XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TUẤT':'<div class="line green size2">Tướng Quân</div>',
                'HỢI':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'TÝ':'<div class="line red size2">Phi Liêm</div>',
                'SỬU':'<div class="line green size2">Hỉ Thần</div>',
                'DẦN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'DẦN':'<div class="line organ size2">Quốc Ấn</div>',
                'MÃO XẤU':'<div class="line red size2">Đại Hao</div>',
                'THÌN XẤU':'<div class="line red size2">Phục Binh</div>',
                'TỴ':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line green size2">Lộc Tồn</div>',
                'DẬU':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'TUẤT':'<div class="line black size2">Thanh Long</div>',
                'HỢI XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TÝ':'<div class="line green size2">Tướng Quân</div>',
                'SỬU':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'DẦN':'<div class="line red size2">Phi Liêm</div>',
                'MÃO':'<div class="line green size2">Hỉ Thần</div>',
                'THÌN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'THÌN':'<div class="line organ size2">Quốc Ấn</div>',
                'TỴ XẤU':'<div class="line red size2">Đại Hao</div>',
                'NGỌ XẤU':'<div class="line red size2">Phục Binh</div>',
                'MÙI':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line green size2">Lộc Tồn</div>',
                'TUẤT':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'HỢI':'<div class="line black size2">Thanh Long</div>',
                'TÝ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'SỬU':'<div class="line green size2">Tướng Quân</div>',
                'DẦN':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'MÃO':'<div class="line red size2">Phi Liêm</div>',
                'THÌN':'<div class="line green size2">Hỉ Thần</div>',
                'TỴ XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TỴ':'<div class="line organ size2">Quốc Ấn</div>',
                'NGỌ XẤU':'<div class="line red size2">Đại Hao</div>',
                'MÙI XẤU':'<div class="line red size2">Phục Binh</div>',
                'THÂN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line green size2">Lộc Tồn</div>',
                'TÝ':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'SỬU':'<div class="line black size2">Thanh Long</div>',
                'DẦN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'MÃO':'<div class="line green size2">Tướng Quân</div>',
                'THÌN':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'TỴ':'<div class="line red size2">Phi Liêm</div>',
                'NGỌ':'<div class="line green size2">Hỉ Thần</div>',
                'MÙI XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'MÙI':'<div class="line organ size2">Quốc Ấn</div>',
                'THÂN XẤU':'<div class="line red size2">Đại Hao</div>',
                'DẬU XẤU':'<div class="line red size2">Phục Binh</div>',
                'TUẤT':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            else:
                locton = {'TÝ':'<div class="line green size2">Lộc Tồn</div>',
                'SỬU':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'DẦN':'<div class="line black size2">Thanh Long</div>',
                'MÃO XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'THÌN':'<div class="line green size2">Tướng Quân</div>',
                'TỴ':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'NGỌ':'<div class="line red size2">Phi Liêm</div>',
                'MÙI':'<div class="line green size2">Hỉ Thần</div>',
                'THÂN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'THÂN':'<div class="line organ size2">Quốc Ấn</div>',
                'DẬU XẤU':'<div class="line red size2">Đại Hao</div>',
                'TUẤT XẤU':'<div class="line red size2">Phục Binh</div>',
                'HỢI':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}

    else:
        if chi_nam in chi_am:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line green size2">Lộc Tồn</div>',
                'MÃO':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'THÌN':'<div class="line black size2">Thanh Long</div>',
                'TỴ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'NGỌ':'<div class="line green size2">Tướng Quân</div>',
                'MÙI':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'THÂN':'<div class="line red size2">Phi Liêm</div>',
                'DẬU':'<div class="line green size2">Hỉ Thần</div>',
                'TUẤT XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TUẤT':'<div class="line organ size2">Quốc Ấn</div>',
                'HỢI XẤU':'<div class="line red size2">Đại Hao</div>',
                'TÝ XẤU':'<div class="line red size2">Phục Binh</div>',
                'SỬU':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line green size2">Lộc Tồn</div>',
                'THÌN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'TỴ':'<div class="line black size2">Thanh Long</div>',
                'NGỌ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'MÙI':'<div class="line green size2">Tướng Quân</div>',
                'THÂN':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'DẬU':'<div class="line red size2">Phi Liêm</div>',
                'TUẤT':'<div class="line green size2">Hỉ Thần</div>',
                'HỢI XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'HỢI':'<div class="line organ size2">Quốc Ấn</div>',
                'TÝ XẤU':'<div class="line red size2">Đại Hao</div>',
                'SỬU XẤU':'<div class="line red size2">Phục Binh</div>',
                'DẦN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line green size2">Lộc Tồn</div>',
                'NGỌ':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'MÙI':'<div class="line black size2">Thanh Long</div>',
                'THÂN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'DẬU':'<div class="line green size2">Tướng Quân</div>',
                'TUẤT':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'HỢI':'<div class="line red size2">Phi Liêm</div>',
                'TÝ':'<div class="line green size2">Hỉ Thần</div>',
                'SỬU XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'SỬU':'<div class="line organ size2">Quốc Ấn</div>',
                'DẦN XẤU':'<div class="line red size2">Đại Hao</div>',
                'MÃO XẤU':'<div class="line red size2">Phục Binh</div>',
                'THÌN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line green size2">Lộc Tồn</div>',
                'MÙI':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'THÂN':'<div class="line black size2">Thanh Long</div>',
                'DẬU XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TUẤT':'<div class="line green size2">Tướng Quân</div>',
                'HỢI':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'TÝ':'<div class="line red size2">Phi Liêm</div>',
                'SỬU':'<div class="line green size2">Hỉ Thần</div>',
                'DẦN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'DẦN':'<div class="line organ size2">Quốc Ấn</div>',
                'MÃO XẤU':'<div class="line red size2">Đại Hao</div>',
                'THÌN XẤU':'<div class="line red size2">Phục Binh</div>',
                'TỴ':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line green size2">Lộc Tồn</div>',
                'DẬU':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'TUẤT':'<div class="line black size2">Thanh Long</div>',
                'HỢI XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TÝ':'<div class="line green size2">Tướng Quân</div>',
                'SỬU':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'DẦN':'<div class="line red size2">Phi Liêm</div>',
                'MÃO':'<div class="line green size2">Hỉ Thần</div>',
                'THÌN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'THÌN':'<div class="line organ size2">Quốc Ấn</div>',
                'TỴ XẤU':'<div class="line red size2">Đại Hao</div>',
                'NGỌ XẤU':'<div class="line red size2">Phục Binh</div>',
                'MÙI':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line green size2">Lộc Tồn</div>',
                'TUẤT':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'HỢI':'<div class="line black size2">Thanh Long</div>',
                'TÝ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'SỬU':'<div class="line green size2">Tướng Quân</div>',
                'DẦN':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'MÃO':'<div class="line red size2">Phi Liêm</div>',
                'THÌN':'<div class="line green size2">Hỉ Thần</div>',
                'TỴ XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TỴ':'<div class="line organ size2">Quốc Ấn</div>',
                'NGỌ XẤU':'<div class="line red size2">Đại Hao</div>',
                'MÙI XẤU':'<div class="line red size2">Phục Binh</div>',
                'THÂN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line green size2">Lộc Tồn</div>',
                'TÝ':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(H)</div>',
                'SỬU':'<div class="line black size2">Thanh Long</div>',
                'DẦN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'MÃO':'<div class="line green size2">Tướng Quân</div>',
                'THÌN':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'TỴ':'<div class="line red size2">Phi Liêm</div>',
                'NGỌ':'<div class="line green size2">Hỉ Thần</div>',
                'MÙI XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'MÙI':'<div class="line organ size2">Quốc Ấn</div>',
                'THÂN XẤU':'<div class="line red size2">Đại Hao</div>',
                'DẬU XẤU':'<div class="line red size2">Phục Binh</div>',
                'TUẤT':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(Đ)</div>'}
            else:
                locton = {'TÝ':'<div class="line green size2">Lộc Tồn</div>',
                'SỬU':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Kình Dương(Đ)</div>',
                'DẦN':'<div class="line black size2">Thanh Long</div>',
                'MÃO XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'THÌN':'<div class="line green size2">Tướng Quân</div>',
                'TỴ':'<div class="line grey size2">Tấu Thư</div><div class="line green size2">Đường Phù</div>',
                'NGỌ':'<div class="line red size2">Phi Liêm</div>',
                'MÙI':'<div class="line green size2">Hỉ Thần</div>',
                'THÂN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'THÂN':'<div class="line organ size2">Quốc Ấn</div>',
                'DẬU XẤU':'<div class="line red size2">Đại Hao</div>',
                'TUẤT XẤU':'<div class="line red size2">Phục Binh</div>',
                'HỢI':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Đà La(H)</div>'}

        else:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line green size2">Lộc Tồn</div>',
                'SỬU':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'TÝ':'<div class="line black size2">Thanh Long</div>',
                'HỢI XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TUẤT':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'DẬU':'<div class="line grey size2">Tấu Thư</div>',
                'THÂN':'<div class="line red size2">Phi Liêm</div>',
                'MÙI':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'NGỌ XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TỴ XẤU':'<div class="line red size2">Đại Hao</div>',
                'THÌN XẤU':'<div class="line red size2">Phục Binh</div>',
                'MÃO':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line green size2">Lộc Tồn</div>',
                'DẦN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'SỬU':'<div class="line black size2">Thanh Long</div>',
                'TÝ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'HỢI':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'TUẤT':'<div class="line grey size2">Tấu Thư</div>',
                'DẬU':'<div class="line red size2">Phi Liêm</div>',
                'THÂN':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'MÙI XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'NGỌ XẤU':'<div class="line red size2">Đại Hao</div>',
                'TỴ XẤU':'<div class="line red size2">Phục Binh</div>',
                'THÌN':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line green size2">Lộc Tồn</div>',
                'THÌN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'MÃO':'<div class="line black size2">Thanh Long</div>',
                'DẦN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'SỬU':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'TÝ':'<div class="line grey size2">Tấu Thư</div>',
                'HỢI':'<div class="line red size2">Phi Liêm</div>',
                'TUẤT':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'DẬU XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'THÂN XẤU':'<div class="line red size2">Đại Hao</div>',
                'MÙI XẤU':'<div class="line red size2">Phục Binh</div>',
                'NGỌ':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line green size2">Lộc Tồn</div>',
                'TỴ':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'THÌN':'<div class="line black size2">Thanh Long</div>',
                'MÃO XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'DẦN':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'SỬU':'<div class="line grey size2">Tấu Thư</div>',
                'TÝ':'<div class="line red size2">Phi Liêm</div>',
                'HỢI':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'TUẤT XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'DẬU XẤU':'<div class="line red size2">Đại Hao</div>',
                'THÂN XẤU':'<div class="line red size2">Phục Binh</div>',
                'MÙI':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line green size2">Lộc Tồn</div>',
                'MÙI':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'NGỌ':'<div class="line black size2">Thanh Long</div>',
                'TỴ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'THÌN':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'MÃO':'<div class="line grey size2">Tấu Thư</div>',
                'DẦN':'<div class="line red size2">Phi Liêm</div>',
                'SỬU':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'TÝ XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'HỢI XẤU':'<div class="line red size2">Đại Hao</div>',
                'TUẤT XẤU':'<div class="line red size2">Phục Binh</div>',
                'DẬU':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line green size2">Lộc Tồn</div>',
                'THÂN':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'MÙI':'<div class="line black size2">Thanh Long</div>',
                'NGỌ XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'TỴ':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'THÌN':'<div class="line grey size2">Tấu Thư</div>',
                'MÃO':'<div class="line red size2">Phi Liêm</div>',
                'DẦN':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'SỬU XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'TÝ XẤU':'<div class="line red size2">Đại Hao</div>',
                'HỢI XẤU':'<div class="line red size2">Phục Binh</div>',
                'TUẤT':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line green size2">Lộc Tồn</div>',
                'TUẤT':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(Đ)</div>',
                'DẬU':'<div class="line black size2">Thanh Long</div>',
                'THÂN XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'MÙI':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'NGỌ':'<div class="line grey size2">Tấu Thư</div>',
                'TỴ':'<div class="line red size2">Phi Liêm</div>',
                'THÌN':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'MÃO XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'DẦN XẤU':'<div class="line red size2">Đại Hao</div>',
                'SỬU XẤU':'<div class="line red size2">Phục Binh</div>',
                'TÝ':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(H)</div>'}
            else:
                locton = {'TÝ':'<div class="line green size2">Lộc Tồn</div>',
                'HỢI':'<div class="line red size2">Lực Sĩ</div><div class="line grey size2">Đà La(H)</div>',
                'TUẤT':'<div class="line black size2">Thanh Long</div>',
                'DẬU XẤU':'<div class="line red size2">Tiểu Hao</div>',
                'THÂN':'<div class="line green size2">Tướng Quân</div><div class="line organ size2">Quốc Ấn</div>',
                'MÙI':'<div class="line grey size2">Tấu Thư</div>',
                'NGỌ':'<div class="line red size2">Phi Liêm</div>',
                'TỴ':'<div class="line green size2">Hỉ Thần</div><div class="line green size2">Đường Phù</div>',
                'THÌN XẤU':'<div class="line red size2">Bệnh Phù</div>',
                'MÃO XẤU':'<div class="line red size2">Đại Hao</div>',
                'DẦN XẤU':'<div class="line red size2">Phục Binh</div>',
                'SỬU':'<div class="line red size2">Quan Phủ</div><div class="line grey size2">Kình Dương(Đ)</div>'}

    return locton


def luuvonglocton(can_nam,chi_nam,option):
    locton = {}
    if option == 'Nam':
        if chi_nam in chi_am:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'SỬU':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'TÝ':'<div class="line grey size2">L.Thanh Long</div>',
                'HỢI':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'DẬU':'<div class="line grey size2">L.Tấu Thư</div>',
                'THÂN':'<div class="line grey size2">L.Phi Liêm</div>',
                'MÙI':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'NGỌ':'<div class="line grey size2">L.Bệnh Phù</div>',
                'TỴ':'<div class="line grey size2">L.Đại Hao</div>',
                'THÌN':'<div class="line grey size2">L.Phục Binh</div>',
                'MÃO':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line grey size2">L.Lộc Tồn</div>',
                'DẦN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'SỬU':'<div class="line grey size2">L.Thanh Long</div>',
                'TÝ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'HỢI':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TUẤT':'<div class="line grey size2">L.Tấu Thư</div>',
                'DẬU':'<div class="line grey size2">L.Phi Liêm</div>',
                'THÂN':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'MÙI':'<div class="line grey size2">L.Bệnh Phù</div>',
                'NGỌ':'<div class="line grey size2">L.Đại Hao</div>',
                'TỴ':'<div class="line grey size2">L.Phục Binh</div>',
                'THÌN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'THÌN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'MÃO':'<div class="line grey size2">L.Thanh Long</div>',
                'DẦN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'SỬU':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TÝ':'<div class="line grey size2">L.Tấu Thư</div>',
                'HỢI':'<div class="line grey size2">L.Phi Liêm</div>',
                'TUẤT':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'DẬU':'<div class="line grey size2">L.Bệnh Phù</div>',
                'THÂN':'<div class="line grey size2">L.Đại Hao</div>',
                'MÙI':'<div class="line grey size2">L.Phục Binh</div>',
                'NGỌ':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TỴ':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'THÌN':'<div class="line grey size2">L.Thanh Long</div>',
                'MÃO':'<div class="line grey size2">L.Tiểu Hao</div>',
                'DẦN':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'SỬU':'<div class="line grey size2">L.Tấu Thư</div>',
                'TÝ':'<div class="line grey size2">L.Phi Liêm</div>',
                'HỢI':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'TUẤT':'<div class="line grey size2">L.Bệnh Phù</div>',
                'DẬU':'<div class="line grey size2">L.Đại Hao</div>',
                'THÂN':'<div class="line grey size2">L.Phục Binh</div>',
                'MÙI':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'MÙI':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'NGỌ':'<div class="line grey size2">L.Thanh Long</div>',
                'TỴ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'THÌN':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'MÃO':'<div class="line grey size2">L.Tấu Thư</div>',
                'DẦN':'<div class="line grey size2">L.Phi Liêm</div>',
                'SỬU':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'TÝ':'<div class="line grey size2">L.Bệnh Phù</div>',
                'HỢI':'<div class="line grey size2">L.Đại Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Phục Binh</div>',
                'DẬU':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line grey size2">L.Lộc Tồn</div>',
                'THÂN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'MÙI':'<div class="line grey size2">L.Thanh Long</div>',
                'NGỌ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TỴ':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'THÌN':'<div class="line grey size2">L.Tấu Thư</div>',
                'MÃO':'<div class="line grey size2">L.Phi Liêm</div>',
                'DẦN':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'SỬU':'<div class="line grey size2">L.Bệnh Phù</div>',
                'TÝ':'<div class="line grey size2">L.Đại Hao</div>',
                'HỢI':'<div class="line grey size2">L.Phục Binh</div>',
                'TUẤT':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TUẤT':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'DẬU':'<div class="line grey size2">L.Thanh Long</div>',
                'THÂN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'MÙI':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'NGỌ':'<div class="line grey size2">L.Tấu Thư</div>',
                'TỴ':'<div class="line grey size2">L.Phi Liêm</div>',
                'THÌN':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'MÃO':'<div class="line grey size2">L.Bệnh Phù</div>',
                'DẦN':'<div class="line grey size2">L.Đại Hao</div>',
                'SỬU':'<div class="line grey size2">L.Phục Binh</div>',
                'TÝ':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            else:
                locton = {'TÝ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'HỢI':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'TUẤT':'<div class="line grey size2">L.Thanh Long</div>',
                'DẬU':'<div class="line grey size2">L.Tiểu Hao</div>',
                'THÂN':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'MÙI':'<div class="line grey size2">L.Tấu Thư</div>',
                'NGỌ':'<div class="line grey size2">L.Phi Liêm</div>',
                'TỴ':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'THÌN':'<div class="line grey size2">L.Bệnh Phù</div>',
                'MÃO':'<div class="line grey size2">L.Đại Hao</div>',
                'DẦN':'<div class="line grey size2">L.Phục Binh</div>',
                'SỬU':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}

        else:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'MÃO':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'THÌN':'<div class="line grey size2">L.Thanh Long</div>',
                'TỴ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'NGỌ':'<div class="line grey size2">L.Tướng Quân</div>',
                'MÙI':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'THÂN':'<div class="line grey size2">L.Phi Liêm</div>',
                'DẬU':'<div class="line grey size2">L.Hỉ Thần</div>',
                'TUẤT':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'HỢI':'<div class="line grey size2">L.Đại Hao</div>',
                'TÝ':'<div class="line grey size2">L.Phục Binh</div>',
                'SỬU':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line grey size2">L.Lộc Tồn</div>',
                'THÌN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'TỴ':'<div class="line grey size2">L.Thanh Long</div>',
                'NGỌ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'MÙI':'<div class="line grey size2">L.Tướng Quân</div>',
                'THÂN':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'DẬU':'<div class="line grey size2">L.Phi Liêm</div>',
                'TUẤT':'<div class="line grey size2">L.Hỉ Thần</div>',
                'HỢI':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TÝ':'<div class="line grey size2">L.Đại Hao</div>',
                'SỬU':'<div class="line grey size2">L.Phục Binh</div>',
                'DẦN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'NGỌ':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'MÙI':'<div class="line grey size2">L.Thanh Long</div>',
                'THÂN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'DẬU':'<div class="line grey size2">L.Tướng Quân</div>',
                'TUẤT':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'HỢI':'<div class="line grey size2">L.Phi Liêm</div>',
                'TÝ':'<div class="line grey size2">L.Hỉ Thần</div>',
                'SỬU':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'DẦN':'<div class="line grey size2">L.Đại Hao</div>',
                'MÃO':'<div class="line grey size2">L.Phục Binh</div>',
                'THÌN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'MÙI':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'THÂN':'<div class="line grey size2">L.Thanh Long</div>',
                'DẬU':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Tướng Quân</div>',
                'HỢI':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'TÝ':'<div class="line grey size2">L.Phi Liêm</div>',
                'SỬU':'<div class="line grey size2">L.Hỉ Thần</div>',
                'DẦN':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'MÃO':'<div class="line grey size2">L.Đại Hao</div>',
                'THÌN':'<div class="line grey size2">L.Phục Binh</div>',
                'TỴ':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'DẬU':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'TUẤT':'<div class="line grey size2">L.Thanh Long</div>',
                'HỢI':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TÝ':'<div class="line grey size2">L.Tướng Quân</div>',
                'SỬU':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'DẦN':'<div class="line grey size2">L.Phi Liêm</div>',
                'MÃO':'<div class="line grey size2">L.Hỉ Thần</div>',
                'THÌN':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TỴ':'<div class="line grey size2">L.Đại Hao</div>',
                'NGỌ':'<div class="line grey size2">L.Phục Binh</div>',
                'MÙI':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TUẤT':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'HỢI':'<div class="line grey size2">L.Thanh Long</div>',
                'TÝ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'SỬU':'<div class="line grey size2">L.Tướng Quân</div>',
                'DẦN':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'MÃO':'<div class="line grey size2">L.Phi Liêm</div>',
                'THÌN':'<div class="line grey size2">L.Hỉ Thần</div>',
                'TỴ':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'NGỌ':'<div class="line grey size2">L.Đại Hao</div>',
                'MÙI':'<div class="line grey size2">L.Phục Binh</div>',
                'THÂN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TÝ':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'SỬU':'<div class="line grey size2">L.Thanh Long</div>',
                'DẦN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'MÃO':'<div class="line grey size2">L.Tướng Quân</div>',
                'THÌN':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'TỴ':'<div class="line grey size2">L.Phi Liêm</div>',
                'NGỌ':'<div class="line grey size2">L.Hỉ Thần</div>',
                'MÙI':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'THÂN':'<div class="line grey size2">L.Đại Hao</div>',
                'DẬU':'<div class="line grey size2">L.Phục Binh</div>',
                'TUẤT':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            else:
                locton = {'TÝ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'SỬU':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'DẦN':'<div class="line grey size2">L.Thanh Long</div>',
                'MÃO':'<div class="line grey size2">L.Tiểu Hao</div>',
                'THÌN':'<div class="line grey size2">L.Tướng Quân</div>',
                'TỴ':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'NGỌ':'<div class="line grey size2">L.Phi Liêm</div>',
                'MÙI':'<div class="line grey size2">L.Hỉ Thần</div>',
                'THÂN':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'DẬU':'<div class="line grey size2">L.Đại Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Phục Binh</div>',
                'HỢI':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}

    else:
        if chi_nam in chi_am:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'MÃO':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'THÌN':'<div class="line grey size2">L.Thanh Long</div>',
                'TỴ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'NGỌ':'<div class="line grey size2">L.Tướng Quân</div>',
                'MÙI':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'THÂN':'<div class="line grey size2">L.Phi Liêm</div>',
                'DẬU':'<div class="line grey size2">L.Hỉ Thần</div>',
                'TUẤT':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'HỢI':'<div class="line grey size2">L.Đại Hao</div>',
                'TÝ':'<div class="line grey size2">L.Phục Binh</div>',
                'SỬU':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line grey size2">L.Lộc Tồn</div>',
                'THÌN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'TỴ':'<div class="line grey size2">L.Thanh Long</div>',
                'NGỌ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'MÙI':'<div class="line grey size2">L.Tướng Quân</div>',
                'THÂN':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'DẬU':'<div class="line grey size2">L.Phi Liêm</div>',
                'TUẤT':'<div class="line grey size2">L.Hỉ Thần</div>',
                'HỢI':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TÝ':'<div class="line grey size2">L.Đại Hao</div>',
                'SỬU':'<div class="line grey size2">L.Phục Binh</div>',
                'DẦN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'NGỌ':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'MÙI':'<div class="line grey size2">L.Thanh Long</div>',
                'THÂN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'DẬU':'<div class="line grey size2">L.Tướng Quân</div>',
                'TUẤT':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'HỢI':'<div class="line grey size2">L.Phi Liêm</div>',
                'TÝ':'<div class="line grey size2">L.Hỉ Thần</div>',
                'SỬU':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'DẦN':'<div class="line grey size2">L.Đại Hao</div>',
                'MÃO':'<div class="line grey size2">L.Phục Binh</div>',
                'THÌN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'MÙI':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'THÂN':'<div class="line grey size2">L.Thanh Long</div>',
                'DẬU':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Tướng Quân</div>',
                'HỢI':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'TÝ':'<div class="line grey size2">L.Phi Liêm</div>',
                'SỬU':'<div class="line grey size2">L.Hỉ Thần</div>',
                'DẦN':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'MÃO':'<div class="line grey size2">L.Đại Hao</div>',
                'THÌN':'<div class="line grey size2">L.Phục Binh</div>',
                'TỴ':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'DẬU':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'TUẤT':'<div class="line grey size2">L.Thanh Long</div>',
                'HỢI':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TÝ':'<div class="line grey size2">L.Tướng Quân</div>',
                'SỬU':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'DẦN':'<div class="line grey size2">L.Phi Liêm</div>',
                'MÃO':'<div class="line grey size2">L.Hỉ Thần</div>',
                'THÌN':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TỴ':'<div class="line grey size2">L.Đại Hao</div>',
                'NGỌ':'<div class="line grey size2">L.Phục Binh</div>',
                'MÙI':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TUẤT':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'HỢI':'<div class="line grey size2">L.Thanh Long</div>',
                'TÝ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'SỬU':'<div class="line grey size2">L.Tướng Quân</div>',
                'DẦN':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'MÃO':'<div class="line grey size2">L.Phi Liêm</div>',
                'THÌN':'<div class="line grey size2">L.Hỉ Thần</div>',
                'TỴ':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'NGỌ':'<div class="line grey size2">L.Đại Hao</div>',
                'MÙI':'<div class="line grey size2">L.Phục Binh</div>',
                'THÂN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TÝ':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(H)</div>',
                'SỬU':'<div class="line grey size2">L.Thanh Long</div>',
                'DẦN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'MÃO':'<div class="line grey size2">L.Tướng Quân</div>',
                'THÌN':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'TỴ':'<div class="line grey size2">L.Phi Liêm</div>',
                'NGỌ':'<div class="line grey size2">L.Hỉ Thần</div>',
                'MÙI':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'THÂN':'<div class="line grey size2">L.Đại Hao</div>',
                'DẬU':'<div class="line grey size2">L.Phục Binh</div>',
                'TUẤT':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(Đ)</div>'}
            else:
                locton = {'TÝ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'SỬU':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Kình Dương(Đ)</div>',
                'DẦN':'<div class="line grey size2">L.Thanh Long</div>',
                'MÃO':'<div class="line grey size2">L.Tiểu Hao</div>',
                'THÌN':'<div class="line grey size2">L.Tướng Quân</div>',
                'TỴ':'<div class="line grey size2">L.Tấu Thư</div><div class="line grey size2">L.Đường Phù</div>',
                'NGỌ':'<div class="line grey size2">L.Phi Liêm</div>',
                'MÙI':'<div class="line grey size2">L.Hỉ Thần</div>',
                'THÂN':'<div class="line grey size2">L.Bệnh Phù</div><div class="line grey size2">L.Quốc Ấn</div>',
                'DẬU':'<div class="line grey size2">L.Đại Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Phục Binh</div>',
                'HỢI':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Đà La(H)</div>'}

        else:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'SỬU':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'TÝ':'<div class="line grey size2">L.Thanh Long</div>',
                'HỢI':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'DẬU':'<div class="line grey size2">L.Tấu Thư</div>',
                'THÂN':'<div class="line grey size2">L.Phi Liêm</div>',
                'MÙI':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'NGỌ':'<div class="line grey size2">L.Bệnh Phù</div>',
                'TỴ':'<div class="line grey size2">L.Đại Hao</div>',
                'THÌN':'<div class="line grey size2">L.Phục Binh</div>',
                'MÃO':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'<div class="line grey size2">L.Lộc Tồn</div>',
                'DẦN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'SỬU':'<div class="line grey size2">L.Thanh Long</div>',
                'TÝ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'HỢI':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TUẤT':'<div class="line grey size2">L.Tấu Thư</div>',
                'DẬU':'<div class="line grey size2">L.Phi Liêm</div>',
                'THÂN':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'MÙI':'<div class="line grey size2">L.Bệnh Phù</div>',
                'NGỌ':'<div class="line grey size2">L.Đại Hao</div>',
                'TỴ':'<div class="line grey size2">L.Phục Binh</div>',
                'THÌN':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'THÌN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'MÃO':'<div class="line grey size2">L.Thanh Long</div>',
                'DẦN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'SỬU':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'TÝ':'<div class="line grey size2">L.Tấu Thư</div>',
                'HỢI':'<div class="line grey size2">L.Phi Liêm</div>',
                'TUẤT':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'DẬU':'<div class="line grey size2">L.Bệnh Phù</div>',
                'THÂN':'<div class="line grey size2">L.Đại Hao</div>',
                'MÙI':'<div class="line grey size2">L.Phục Binh</div>',
                'NGỌ':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TỴ':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'THÌN':'<div class="line grey size2">L.Thanh Long</div>',
                'MÃO':'<div class="line grey size2">L.Tiểu Hao</div>',
                'DẦN':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'SỬU':'<div class="line grey size2">L.Tấu Thư</div>',
                'TÝ':'<div class="line grey size2">L.Phi Liêm</div>',
                'HỢI':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'TUẤT':'<div class="line grey size2">L.Bệnh Phù</div>',
                'DẬU':'<div class="line grey size2">L.Đại Hao</div>',
                'THÂN':'<div class="line grey size2">L.Phục Binh</div>',
                'MÙI':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'<div class="line grey size2">L.Lộc Tồn</div>',
                'MÙI':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'NGỌ':'<div class="line grey size2">L.Thanh Long</div>',
                'TỴ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'THÌN':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'MÃO':'<div class="line grey size2">L.Tấu Thư</div>',
                'DẦN':'<div class="line grey size2">L.Phi Liêm</div>',
                'SỬU':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'TÝ':'<div class="line grey size2">L.Bệnh Phù</div>',
                'HỢI':'<div class="line grey size2">L.Đại Hao</div>',
                'TUẤT':'<div class="line grey size2">L.Phục Binh</div>',
                'DẬU':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'<div class="line grey size2">L.Lộc Tồn</div>',
                'THÂN':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'MÙI':'<div class="line grey size2">L.Thanh Long</div>',
                'NGỌ':'<div class="line grey size2">L.Tiểu Hao</div>',
                'TỴ':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'THÌN':'<div class="line grey size2">L.Tấu Thư</div>',
                'MÃO':'<div class="line grey size2">L.Phi Liêm</div>',
                'DẦN':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'SỬU':'<div class="line grey size2">L.Bệnh Phù</div>',
                'TÝ':'<div class="line grey size2">L.Đại Hao</div>',
                'HỢI':'<div class="line grey size2">L.Phục Binh</div>',
                'TUẤT':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'<div class="line grey size2">L.Lộc Tồn</div>',
                'TUẤT':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(Đ)</div>',
                'DẬU':'<div class="line grey size2">L.Thanh Long</div>',
                'THÂN':'<div class="line grey size2">L.Tiểu Hao</div>',
                'MÙI':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'NGỌ':'<div class="line grey size2">L.Tấu Thư</div>',
                'TỴ':'<div class="line grey size2">L.Phi Liêm</div>',
                'THÌN':'<div class="line grey size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'MÃO':'<div class="line grey size2">L.Bệnh Phù</div>',
                'DẦN':'<div class="line grey size2">L.Đại Hao</div>',
                'SỬU':'<div class="line grey size2">L.Phục Binh</div>',
                'TÝ':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(H)</div>'}
            else:
                locton = {'TÝ':'<div class="line grey size2">L.Lộc Tồn</div>',
                'HỢI':'<div class="line grey size2">L.Lực Sĩ</div><div class="line grey size2">L.Đà La(H)</div>',
                'TUẤT':'<div class="line grey size2">L.Thanh Long</div>',
                'DẬU':'<div class="line grey size2">L.Tiểu Hao</div>',
                'THÂN':'<div class="line grey size2">L.Tướng Quân</div><div class="line grey size2">L.Quốc Ấn</div>',
                'MÙI':'<div class="line grey size2">L.Tấu Thư</div>',
                'NGỌ':'<div class="line grey size2">L.Phi Liêm</div>',
                'TỴ':'<div class="line green size2">L.Hỉ Thần</div><div class="line grey size2">L.Đường Phù</div>',
                'THÌN':'<div class="line grey size2">L.Bệnh Phù</div>',
                'MÃO':'<div class="line grey size2">L.Đại Hao</div>',
                'DẦN':'<div class="line grey size2">L.Phục Binh</div>',
                'SỬU':'<div class="line grey size2">L.Quan Phủ</div><div class="line grey size2">L.Kình Dương(Đ)</div>'}

    return locton

def thienkhothienviet(can_nam):
    khoiviet={}
    if can_nam=='GIÁP' or can_nam=='MẬU':
        khoiviet={'SỬU':'<div class="line red size2">Thiên Khôi</div>',
        'MÙI':'<div class="line red size2">Thiên Việt</div>'}
    elif can_nam=='ẤT' or can_nam=='KỶ':
        khoiviet={'TÝ':'<div class="line red size2">Thiên Khôi</div>',
        'THÂN':'<div class="line red size2">Thiên Việt</div>'}
    elif can_nam=='CANH' or can_nam=='TÂN':
        khoiviet={'DẦN':'<div class="line red size2">Thiên Khôi</div>',
        'NGỌ':'<div class="line red size2">Thiên Việt</div>'}
    elif can_nam=='BÍNH' or can_nam=='ĐINH':
        khoiviet={'HỢI':'<div class="line red size2">Thiên Khôi</div>',
        'DẬU':'<div class="line red size2">Thiên Việt</div>'}
    else:
        khoiviet={'MÃO':'<div class="line red size2">Thiên Khôi</div>',
        'TỴ':'<div class="line red size2">Thiên Việt</div>'}
    return khoiviet

def antuhoa(*tuhoa):
    chi_gio = tuhoa[0]
    thang_am = tuhoa[1]
    can_nam = tuhoa[2]
    chi_nam = tuhoa[3]
    ngay_am = tuhoa[4]
    option = tuhoa[5]
    tuvi = ansaotuvi(chi_gio,int(thang_am),can_nam,chi_nam,int(ngay_am))
    ansao_theothang = ansaotheothang(thang_am)
    ansao_theogio = ansaotheogio(chi_gio,ngay_am,chi_nam,option)
    ansaotuhoa = {}
    for key, value in tuvi.items():
        if can_nam == 'GIÁP':
            if 'Liêm Trinh' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Phá Quân' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Vũ Khúc' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Thái Dương' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'ẤT':
            if 'Thiên Cơ' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Thiên Lương' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Tử Vi' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Thái Âm' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'BÍNH':
            if 'Thiên Đồng' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Thiên Cơ' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Tử Vi' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Liêm Trinh' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'ĐINH':
            if 'Thái Âm' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Thiên Đồng' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Thiên Cơ' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Cự Môn' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'MẬU':
            if 'Tham Lang' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Thái Âm' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Thiên Cơ' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'KỶ':
            if 'Vũ Khúc' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Tham Lang' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Thiên Lương' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'

        elif can_nam == 'CANH':
            if 'Thái Dương' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Vũ Khúc' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Thái Âm' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Thiên Đồng' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'TÂN':
            if 'Cự Môn' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Thái Dương' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Vũ Khúc' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
        elif can_nam == 'NHÂM':
            if 'Thiên Lương' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Tử Vi' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Thiên Phủ' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Vũ Khúc' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'QUÝ':
            if 'Phá Quân' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Lộc</div>'
            if 'Cự Môn' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Quyền</div>'
            if 'Thái Âm' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
            if 'Tham Lang' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
    for key, value in ansao_theothang.items():
        if can_nam == 'MẬU':
            if 'Hữu Bật' in value:
                ansaotuhoa[key]='<div class="line green size2">Hóa Khoa</div>'
    for key, value in ansao_theogio.items():
        if can_nam == 'KỶ':
            if 'Văn Khúc' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
        elif can_nam == 'TÂN':
            if 'Văn Xương' in value:
                ansaotuhoa[key]='<div class="line black size2">Hóa Kỵ</div>'
    return ansaotuhoa

def thienquanthienphuc(can_nam):
    quanphuc = {}
    if can_nam == 'GIÁP':
        quanphuc={'MÙI':'<div class="line red size2">Thiên Quan</div>',
        'DẬU':'<div class="line organ size2">Thiên Phúc</div>',
        'TỴ':'<div class="line organ size2">Thiên Trù</div><div class="line gray size2">LN Văn Tinh</div>',
        'DẬU XẤU':'<div class="line black size2">Lưu Hà</div>'}
    elif can_nam == 'ẤT':
        quanphuc={'THÌN':'<div class="line red size2">Thiên Quan</div>',
        'THÂN':'<div class="line organ size2">Thiên Phúc</div>',
        'NGỌ':'<div class="line organ size2">Thiên Trù</div><div class="line gray size2">LN Văn Tinh</div>',
        'TUẤT XẤU':'<div class="line black size2">Lưu Hà</div>'}
    elif can_nam == 'BÍNH':
        quanphuc={'TỴ':'<div class="line red size2">Thiên Quan</div>',
        'TÝ':'<div class="line organ size2">Thiên Phúc</div><div class="line organ size2">Thiên Trù</div>',
        'MÙI XẤU':'<div class="line black size2">Lưu Hà</div>',
        'THÂN':'<div class="line gray size2">LN Văn Tinh</div>'}
    elif can_nam == 'ĐINH':
        quanphuc={'DẦN':'<div class="line red size2">Thiên Quan</div>',
        'HỢI':'<div class="line organ size2">Thiên Phúc</div>',
        'TỴ':'<div class="line organ size2">Thiên Trù</div>',
        'THÌN XẤU':'<div class="line black size2">Lưu Hà</div>',
        'DẬU':'<div class="line gray size2">LN Văn Tinh</div>'}
    elif can_nam == 'MẬU':
        quanphuc={'MÃO':'<div class="line red size2">Thiên Quan</div><div class="line organ size2">Thiên Phúc</div>',
        'NGỌ':'<div class="line organ size2">Thiên Trù</div>',
        'TỴ XẤU':'<div class="line black size2">Lưu Hà</div>',
        'THÂN':'<div class="line gray size2">LN Văn Tinh</div>'}
    elif can_nam == 'KỶ':
        quanphuc={'DẬU':'<div class="line red size2">Thiên Quan</div>',
        'DẦN':'<div class="line organ size2">Thiên Phúc</div>',
        'THÂN':'<div class="line organ size2">Thiên Trù</div>',
        'NGỌ XẤU':'<div class="line black size2">Lưu Hà</div>',
        'DẬU':'<div class="line gray size2">LN Văn Tinh</div>'}
    elif can_nam == 'CANH':
        quanphuc={'HỢI':'<div class="line red size2">Thiên Quan</div><div class="line gray size2">LN Văn Tinh</div>',
        'NGỌ':'<div class="line organ size2">Thiên Phúc</div>',
        'DẦN':'<div class="line organ size2">Thiên Trù</div>',
        'THÂN XẤU':'<div class="line black size2">Lưu Hà</div>'}
    elif can_nam == 'TÂN':
        quanphuc={'DẬU':'<div class="line red size2">Thiên Quan</div>',
        'TỴ':'<div class="line organ size2">Thiên Phúc</div>',
        'NGỌ':'<div class="line organ size2">Thiên Trù</div>',
        'MÃO XẤU':'<div class="line black size2">Lưu Hà</div>',
        'TÝ':'<div class="line gray size2">LN Văn Tinh</div>'}
    elif can_nam == 'NHÂM':
        quanphuc={'TUẤT':'<div class="line red size2">Thiên Quan</div>',
        'NGỌ':'<div class="line organ size2">Thiên Phúc</div>',
        'DẬU':'<div class="line organ size2">Thiên Trù</div>',
        'HỢI XẤU':'<div class="line black size2">Lưu Hà</div>',
        'DẦN':'<div class="line gray size2">LN Văn Tinh</div>'}
    else:
        quanphuc={'NGỌ':'<div class="line red size2">Thiên Quan</div>',
        'TỴ':'<div class="line organ size2">Thiên Phúc</div>',
        'TUẤT':'<div class="line organ size2">Thiên Trù</div>',
        'DẦN XẤU':'<div class="line black size2">Lưu Hà</div>',
        'MÃO':'<div class="line gray size2">LN Văn Tinh</div>'}

    return quanphuc

def ansaotheochi(chi_nam):
    dic_theochi = {}
    if chi_nam == 'TÝ':
        dic_theochi ={'TÝ XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'SỬU':'<div class="line red size2">Thiếu Dương(H)</div>',
                      'DẦN XẤU':'<div class="line red size2">Thiên Mã(Đ)</div><div class="line green size2">Tang Môn(Đ)</div><div class="line organ size2">Cô Thần</div>',
                      'MÃO':'<div class="line black size2">Thiếu Âm(H)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'THÌN XẤU':'<div class="line red size2">Quan Phù</div>',
                      'THÌN':'<div class="line black size2">Long Trì</div><div class="line gray size2">Hoa Cái</div>',
                      'TỴ XẤU':'<div class="line red size2">Phá Toái</div><div class="line gray size2">Tử Phù</div><div class="line red size2">Kiếp Sát</div>',
                      'TỴ':'<div class="line red size2">Nguyệt Đức</div>',
                      'NGỌ XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Khốc(Đ)</div><div class="line black size2">Thiên Hư(Đ)</div>',
                      'MÙI':'<div class="line black size2">Long Đức</div>',
                      'THÂN':'<div class="line gray size2">Bạch Hỗ</div>',
                      'DẬU':'<div class="line green size2">Đào Hoa</div><div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'TUẤT XẤU':'<div class="line red size2">Điếu Khách</div><div class="line organ size2">Quả Tú</div>',
                      'TUẤT':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'HỢI XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'SỬU':
        dic_theochi ={'SỬU XẤU':'<div class="line red size2">Phá Toái</div><div class="line red size2">Thái Tuế</div>',
                      'SỬU':'<div class="line gray size2">Hoa Cái</div>',
                      'DẦN':'<div class="line red size2">Thiếu Dương(Đ)</div>',
                      'DẦN XẤU':'<div class="line red size2">Kiếp Sát</div><div class="line organ size2">Cô Thần</div>',
                      'MÃO XẤU':'<div class="line green size2">Tang Môn(Đ)</div>',
                      'THÌN':'<div class="line black size2">Thiếu Âm(H)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'TỴ XẤU':'<div class="line red size2">Quan Phù</div><div class="line black size2">Thiên Khốc(H)</div>',
                      'TỴ':'<div class="line black size2">Long Trì</div><div class="line green size2">Đào Hoa</div>',
                      'NGỌ XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'NGỌ':'<div class="line red size2">Nguyệt Đức</div>',
                      'MÙI XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(H)</div>',
                      'THÂN':'<div class="line black size2">Long Đức</div>',
                      'DẬU':'<div class="line gray size2">Bạch Hỗ(v)</div><div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'TUẤT':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'TUẤT XẤU':'<div class="line organ size2">Quả Tú</div>',
                      'HỢI XẤU':'<div class="line red size2">Điếu Khách</div><div class="line red size2">Thiên Mã</div>',
                      'TÝ XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'DẦN':
        dic_theochi ={'DẦN XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'MÃO':'<div class="line red size2">Thiếu Dương(Đ)</div><div class="line green size2">Đào Hoa</div>',
                      'THÌN XẤU':'<div class="line green size2">Tang Môn(Đ)</div><div class="line black size2">Thiên Khốc(H)</div>',
                      'TỴ':'<div class="line black size2">Thiếu Âm(H)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'TỴ XẤU':'<div class="line organ size2">Cô Thần</div>',
                      'NGỌ XẤU':'<div class="line red size2">Quan Phù</div>',
                      'NGỌ':'<div class="line black size2">Long Trì</div>',
                      'MÙI XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'MÙI':'<div class="line red size2">Nguyệt Đức</div>',
                      'THÂN XẤU':'<div class="line red size2">Thiên Mã</div><div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(H)</div>',
                      'THÂN':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'DẬU':'<div class="line black size2">Long Đức</div>',
                      'DẬU XẤU':'<div class="line red size2">Phá Toái</div>',
                      'TUẤT':'<div class="line gray size2">Hoa Cái</div><div class="line gray size2">Bạch Hỗ(v)</div>',
                      'HỢI':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'HỢI XẤU':'<div class="line red size2">Kiếp Sát</div>',
                      'TÝ XẤU':'<div class="line red size2">Điếu Khách</div>',
                      'SỬU XẤU':'<div class="line gray size2">Trực Phù</div><div class="line organ size2">Quả Tú</div>',
        }
    elif chi_nam == 'MÃO':
        dic_theochi ={'MÃO XẤU':'<div class="line red size2">Thái Tuế</div><div class="line black size2">Thiên Khốc(Đ)</div>',
                      'THÌN':'<div class="line red size2">Thiếu Dương(Đ)</div>',
                      'TỴ XẤU':'<div class="line red size2">Phá Toái</div><div class="line red size2">Thiên Mã(Đ)</div><div class="line green size2">Tang Môn(H)</div><div class="line organ size2">Cô Thần</div>',
                      'NGỌ':'<div class="line black size2">Thiếu Âm(H)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'MÙI XẤU':'<div class="line red size2">Quan Phù</div>',
                      'MÙI':'<div class="line gray size2">Hoa Cái</div><div class="line black size2">Long Trì</div><div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'THÂN XẤU':'<div class="line red size2">Kiếp Sát</div><div class="line gray size2">Tử Phù</div>',
                      'THÂN':'<div class="line red size2">Nguyệt Đức</div>',
                      'DẬU XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(Đ)</div>',
                      'TUẤT':'<div class="line black size2">Long Đức</div>',
                      'HỢI':'<div class="line gray size2">Bạch Hỗ</div>',
                      'TÝ':'<div class="line green size2">Đào Hoa</div><div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'SỬU XẤU':'<div class="line red size2">Điếu Khách</div><div class="line organ size2">Quả Tú</div>',
                      'DẦN XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'THÌN':
        dic_theochi ={'THÌN XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'THÌN':'<div class="line gray size2">Hoa Cái</div>',
                      'TỴ':'<div class="line red size2">Thiếu Dương(Đ)</div>',
                      'TỴ XẤU':'<div class="line organ size2">Cô Thần</div><div class="line red size2">Kiếp Sát</div>',
                      'NGỌ XẤU':'<div class="line green size2">Tang Môn(H)</div>',
                      'NGỌ':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'MÙI':'<div class="line black size2">Thiếu Âm(Đ)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'THÂN XẤU':'<div class="line red size2">Quan Phù</div>',
                      'THÂN':'<div class="line black size2">Long Trì</div>',
                      'DẬU XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'DẬU':'<div class="line red size2">Nguyệt Đức</div><div class="line green size2">Đào Hoa</div>',
                      'TUẤT XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(H)</div>',
                      'HỢI':'<div class="line black size2">Long Đức</div>',
                      'TÝ':'<div class="line gray size2">Bạch Hỗ(Đ)</div>',
                      'SỬU':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'SỬU XẤU':'<div class="line red size2">Phá Toái</div><div class="line organ size2">Quả Tú</div>',
                      'DẦN XẤU':'<div class="line red size2">Thiên Mã(Đ)</div><div class="line red size2">Điếu Khách</div><div class="line black size2">Thiên Khốc(H)</div>',
                      'MÃO XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'TỴ':
        dic_theochi ={'TỴ XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'TỴ':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'NGỌ':'<div class="line red size2">Thiếu Dương(Đ)</div><div class="line green size2">Đào Hoa</div>',
                      'MÙI XẤU':'<div class="line green size2">Tang Môn(H)</div>',
                      'THÂN':'<div class="line black size2">Thiếu Âm(Đ)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'THÂN XẤU':'<div class="line organ size2">Cô Thần</div>',
                      'DẬU XẤU':'<div class="line red size2">Quan Phù</div><div class="line red size2">Phá Toái</div>',
                      'DẬU':'<div class="line black size2">Long Trì</div>',
                      'TUẤT XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'TUẤT':'<div class="line red size2">Nguyệt Đức</div>',
                      'HỢI XẤU':'<div class="line red size2">Thiên Mã</div><div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(H)</div>',
                      'TÝ':'<div class="line black size2">Long Đức</div>',
                      'SỬU':'<div class="line gray size2">Hoa Cái</div><div class="line gray size2">Bạch Hỗ</div>',
                      'SỬU XẤU':'<div class="line black size2">Thiên Khốc(Đ)</div>',
                      'DẦN':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'DẦN XẤU':'<div class="line red size2">Kiếp Sát</div>',
                      'MÃO XẤU':'<div class="line red size2">Điếu Khách</div>',
                      'THÌN XẤU':'<div class="line gray size2">Trực Phù</div><div class="line organ size2">Quả Tú</div>',
        }
    elif chi_nam == 'NGỌ':
        dic_theochi ={'NGỌ XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'MÙI':'<div class="line red size2">Thiếu Dương</div>',
                      'THÂN XẤU':'<div class="line red size2">Thiên Mã</div><div class="line green size2">Tang Môn(Đ)</div><div class="line organ size2">Cô Thần</div>',
                      'DẬU':'<div class="line black size2">Thiếu Âm(Đ)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'TUẤT XẤU':'<div class="line red size2">Quan Phù</div>',
                      'TUẤT':'<div class="line gray size2">Hoa Cái</div><div class="line black size2">Long Trì</div>',
                      'HỢI XẤU':'<div class="line red size2">Kiếp Sát</div><div class="line gray size2">Tử Phù</div>',
                      'HỢI':'<div class="line red size2">Nguyệt Đức</div>',
                      'TÝ XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Khốc(Đ)</div><div class="line black size2">Thiên Hư(Đ)</div>',
                      'SỬU':'<div class="line black size2">Long Đức</div>',
                      'DẦN':'<div class="line gray size2">Bạch Hỗ(V)</div>',
                      'MÃO':'<div class="line green size2">Đào Hoa</div><div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'THÌN XẤU':'<div class="line red size2">Điếu Khách</div><div class="line organ size2">Quả Tú</div>',
                      'THÌN':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'TỴ XẤU':'<div class="line red size2">Phá Toái</div><div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'MÙI':
        dic_theochi ={'MÙI XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'MÙI':'<div class="line gray size2">Hoa Cái</div>',
                      'THÂN':'<div class="line red size2">Thiếu Dương(H)</div>',
                      'THÂN XẤU':'<div class="line red size2">Kiếp Sát</div><div class="line organ size2">Cô Thần</div>',
                      'DẬU XẤU':'<div class="line green size2">Tang Môn(Đ)</div>',
                      'TUẤT':'<div class="line black size2">Thiếu Âm(Đ)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'HỢI XẤU':'<div class="line red size2">Quan Phù(H)</div><div class="line black size2">Thiên Khốc(H)</div>',
                      'HỢI':'<div class="line black size2">Long Trì</div>',
                      'TÝ XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'TÝ':'<div class="line red size2">Nguyệt Đức</div><div class="line green size2">Đào Hoa</div>',
                      'SỬU XẤU':'<div class="line red size2">Phá Toái</div><div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(Đ)</div>',
                      'DẦN':'<div class="line black size2">Long Đức</div>',
                      'MÃO':'<div class="line gray size2">Bạch Hỗ</div><div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'THÌN':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'THÌN XẤU':'<div class="line organ size2">Quả Tú</div>',
                      'TỴ XẤU':'<div class="line red size2">Điếu Khách</div><div class="line red size2">Thiên Mã(Đ)</div>',
                      'NGỌ XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'THÂN':
        dic_theochi ={'THÂN XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'DẬU':'<div class="line red size2">Thiếu Dương(H)</div><div class="line green size2">Đào Hoa</div>',
                      'DẬU XẤU':'<div class="line red size2">Phá Toái</div>',
                      'TUẤT XẤU':'<div class="line green size2">Tang Môn(H)</div><div class="line black size2">Thiên Khốc(H)</div>',
                      'HỢI':'<div class="line black size2">Thiếu Âm(Đ)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'HỢI XẤU':'<div class="line organ size2">Cô Thần</div>',
                      'TÝ XẤU':'<div class="line red size2">Quan Phù(H)</div>',
                      'TÝ':'<div class="line black size2">Long Trì</div>',
                      'SỬU XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'SỬU':'<div class="line red size2">Nguyệt Đức</div>',
                      'DẦN XẤU':'<div class="line red size2">Thiên Mã(Đ)</div><div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(H)</div>',
                      'DẦN':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'MÃO':'<div class="line black size2">Long Đức</div>',
                      'THÌN':'<div class="line gray size2">Bạch Hỗ</div><div class="line gray size2">Hoa Cái</div>',
                      'TỴ':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'TỴ XẤU':'<div class="line red size2">Kiếp Sát</div>',
                      'NGỌ XẤU':'<div class="line red size2">Điếu Khách</div>',
                      'MÙI XẤU':'<div class="line gray size2">Trực Phù</div><div class="line organ size2">Quả Tú</div>',
        }
    elif chi_nam == 'DẬU':
        dic_theochi ={'DẬU XẤU':'<div class="line red size2">Thái Tuế</div><div class="line black size2">Thiên Khốc(Đ)</div>',
                      'TUẤT':'<div class="line red size2">Thiếu Dương(H)</div>',
                      'HỢI XẤU':'<div class="line red size2">Thiên Mã</div><div class="line green size2">Tang Môn(H)</div><div class="line organ size2">Cô Thần</div>',
                      'TÝ':'<div class="line black size2">Thiếu Âm(Đ)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'SỬU XẤU':'<div class="line red size2">Quan Phù</div>',
                      'SỬU':'<div class="line gray size2">Hoa Cái</div><div class="line black size2">Long Trì</div><div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'DẦN XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'DẦN':'<div class="line red size2">Nguyệt Đức</div>',
                      'MÃO XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(Đ)</div>',
                      'THÌN':'<div class="line black size2">Long Đức</div>',
                      'TỴ':'<div class="line gray size2">Bạch Hỗ</div>',
                      'TỴ XẤU':'<div class="line red size2">Phá Toái</div>',
                      'NGỌ':'<div class="line green size2">Đào Hoa</div><div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'MÙI XẤU':'<div class="line red size2">Điếu Khách</div><div class="line organ size2">Quả Tú</div>',
                      'THÂN XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    elif chi_nam == 'TUẤT':
        dic_theochi ={'TUẤT XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'TUẤT':'<div class="line gray size2">Hoa Cái</div>',
                      'HỢI':'<div class="line red size2">Thiếu Dương(H)</div>',
                      'HỢI XẤU':'<div class="line red size2">Kiếp Sát</div><div class="line organ size2">Cô Thần</div>',
                      'TÝ XẤU':'<div class="line green size2">Tang Môn(H)</div>',
                      'TÝ':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'SỬU':'<div class="line black size2">Thiếu Âm</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'SỬU XẤU':'<div class="line red size2">Phá Toái</div>',
                      'DẦN XẤU':'<div class="line red size2">Quan Phù</div>',
                      'DẦN':'<div class="line black size2">Long Trì</div>',
                      'MÃO XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'MÃO':'<div class="line red size2">Nguyệt Đức</div><div class="line green size2">Đào Hoa</div>',
                      'THÌN XẤU':'<div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(Đ)</div>',
                      'TỴ':'<div class="line black size2">Long Đức</div>',
                      'NGỌ':'<div class="line gray size2">Bạch Hỗ(Đ)</div>',
                      'MÙI':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'MÙI XẤU':'<div class="line organ size2">Quả Tú</div>',
                      'THÂN XẤU':'<div class="line red size2">Thiên Mã</div><div class="line red size2">Điếu Khách</div><div class="line black size2">Thiên Khốc(H)</div>',
                      'DẬU XẤU':'<div class="line gray size2">Trực Phù</div>',
        }
    else:
        dic_theochi ={'HỢI XẤU':'<div class="line red size2">Thái Tuế</div>',
                      'HỢI':'<div class="line green size2">Phượng Các</div><div class="line green size2">Giải Thần</div>',
                      'TÝ':'<div class="line red size2">Thiếu Dương(H)</div><div class="line green size2">Đào Hoa</div>',
                      'SỬU XẤU':'<div class="line green size2">Tang Môn(H)</div>',
                      'DẦN':'<div class="line black size2">Thiếu Âm(H)</div><div class="line black size2">Hồng Loan</div><div class="line black size2">Thiên Hỷ</div>',
                      'DẦN XẤU':'<div class="line organ size2">Cô Thần</div>',
                      'MÃO XẤU':'<div class="line red size2">Quan Phù</div>',
                      'MÃO':'<div class="line black size2">Long Trì</div>',
                      'THÌN XẤU':'<div class="line gray size2">Tử Phù</div>',
                      'THÌN':'<div class="line red size2">Nguyệt Đức</div>',
                      'TỴ XẤU':'<div class="line red size2">Thiên Mã(Đ)</div><div class="line red size2">Tuế Phá</div><div class="line black size2">Thiên Hư(H)</div>',
                      'NGỌ':'<div class="line black size2">Long Đức</div>',
                      'MÙI':'<div class="line gray size2">Bạch Hỗ(Đ)</div><div class="line gray size2">Hoa Cái</div>',
                      'MÙI XẤU':'<div class="line black size2">Thiên Khốc(Đ)</div>',
                      'THÂN':'<div class="line organ size2">Phúc Đức</div><div class="line red size2">Thiên Đức</div>',
                      'THÂN XẤU':'<div class="line red size2">Kiếp Sát</div>',
                      'DẬU XẤU':'<div class="line red size2">Điếu Khách</div><div class="line red size2">Phá Toái</div>',
                      'TUẤT XẤU':'<div class="line gray size2">Trực Phù</div><div class="line organ size2">Quả Tú</div>',
        }
    return dic_theochi

def thientaithientho(chi_gio,thang_am,chi_nam):
    dic_thietaithientho={}
    dic_thietai={}
    dic_thientho={}
    dic_cungmenhthan = cungmenhthan(chi_gio,thang_am)
    for key, value in dic_cungmenhthan.items():
        if 'MỆNH' in value:
            cungmenh = chieuthuan2diachi(key,chi_nam)
            dic_thietai[cungmenh] = '<div class="line organ size2">Thiên Tài</div>'
        if 'THÂN' in value:
            cungthan = chieuthuan2diachi(key,chi_nam)
            dic_thientho[cungthan] = '<div class="line organ size2">Thiên Thọ</div>'
    dic_thietaithientho = custom_merge(dic_thietai,dic_thientho)
    return dic_thietaithientho


def ansaotheothang(thang_am):
    dic_theothang={}
    taphu=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
    huubat=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
    thienhinh=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
    thienrieu=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
    thiengiai=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
    diagiai=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
    key_taphu = taphu[thang_am-1]
    dic_taphu = {}
    key_huubat = huubat[thang_am-1]
    dic_huubat = {}
    key_thienhinh = thienhinh[thang_am-1]
    dic_thienhinh = {}
    key_thienrieu = thienrieu[thang_am-1]
    dic_thienrieu = {}
    key_thiengiai = thiengiai[thang_am-1]
    dic_thiengiai = {}
    key_diagiai = diagiai[thang_am-1]
    dic_diagiai = {}
    if key_taphu == 'TÝ':
        dic_taphu ={'TÝ':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'SỬU':
        dic_taphu ={'SỬU':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'DẦN':
        dic_taphu ={'DẦN':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'MÃO':
        dic_taphu ={'MÃO':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'THÌN':
        dic_taphu ={'THÌN':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'TỴ':
        dic_taphu ={'TỴ':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'NGỌ':
        dic_taphu ={'NGỌ':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'MÙI':
        dic_taphu ={'MÙI':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'THÂN':
        dic_taphu ={'THÂN':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'DẬU':
        dic_taphu ={'DẬU XẤU':'<div class="line organ size2">Tả Phù</div>'
        }
    elif key_taphu == 'TUẤT':
        dic_taphu ={'TUẤT':'<div class="line organ size2">Tả Phù</div>'
        }
    else:
        dic_taphu ={'HỢI':'<div class="line organ size2">Tả Phù</div>'
        }

    if key_huubat == 'TÝ':
        dic_huubat ={'TÝ':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'SỬU':
        dic_huubat ={'SỬU':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'DẦN':
        dic_huubat ={'DẦN':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'MÃO':
        dic_huubat ={'MÃO':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'THÌN':
        dic_huubat ={'THÌN':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'TỴ':
        dic_huubat ={'TỴ':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'NGỌ':
        dic_huubat ={'NGỌ':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'MÙI':
        dic_huubat ={'MÙI':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'THÂN':
        dic_huubat ={'THÂN':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'DẬU':
        dic_huubat ={'DẬU XẤU':'<div class="line black size2">Hữu Bật</div>'
        }
    elif key_huubat == 'TUẤT':
        dic_huubat ={'TUẤT':'<div class="line black size2">Hữu Bật</div>'
        }
    else:
        dic_huubat ={'HỢI':'<div class="line black size2">Hữu Bật</div>'
        }

    if key_thienhinh == 'TÝ':
        dic_thienhinh ={'TÝ':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    elif key_thienhinh == 'SỬU':
        dic_thienhinh ={'SỬU':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    elif key_thienhinh == 'DẦN':
        dic_thienhinh ={'DẦN':'<div class="line red size2">Thiên Hình(Đ)</div>'
        }
    elif key_thienhinh == 'MÃO':
        dic_thienhinh ={'MÃO':'<div class="line red size2">Thiên Hình(Đ)</div>'
        }
    elif key_thienhinh == 'THÌN':
        dic_thienhinh ={'THÌN':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    elif key_thienhinh == 'TỴ':
        dic_thienhinh ={'TỴ':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    elif key_thienhinh == 'NGỌ':
        dic_thienhinh ={'NGỌ':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    elif key_thienhinh == 'MÙI':
        dic_thienhinh ={'MÙI':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    elif key_thienhinh == 'THÂN':
        dic_thienhinh ={'THÂN':'<div class="line red size2">Thiên Hình(Đ)</div>'
        }
    elif key_thienhinh == 'DẬU':
        dic_thienhinh ={'DẬU XẤU':'<div class="line red size2">Thiên Hình(Đ)</div>'
        }
    elif key_thienhinh == 'TUẤT':
        dic_thienhinh ={'TUẤT':'<div class="line red size2">Thiên Hình(H)</div>'
        }
    else:
        dic_thienhinh ={'HỢI':'<div class="line red size2">Thiên Hình(H)</div>'
        }

    if key_thienrieu == 'TÝ':
        dic_thienrieu ={'TÝ XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'TÝ':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'SỬU':
        dic_thienrieu ={'SỬU XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'SỬU':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'DẦN':
        dic_thienrieu ={'DẦN XẤU':'<div class="line black size2">Thiên Riêu(Đ)</div>',
                        'DẦN':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'MÃO':
        dic_thienrieu ={'MÃO XẤU':'<div class="line black size2">Thiên Riêu(Đ)</div>',
                        'MÃO':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'THÌN':
        dic_thienrieu ={'THÌN XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'THÌN':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'TỴ':
        dic_thienrieu ={'TỴ XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'TỴ':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'NGỌ':
        dic_thienrieu ={'NGỌ XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'NGỌ':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'MÙI':
        dic_thienrieu ={'MÙI XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'MÙI':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'THÂN':
        dic_thienrieu ={'THÂN XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'THÂN':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'DẬU':
        dic_thienrieu ={'DẬU XẤU':'<div class="line black size2">Thiên Riêu(Đ)</div>',
                        'DẬU':'<div class="line black size2">Thiên Y</div>'
        }
    elif key_thienrieu == 'TUẤT':
        dic_thienrieu ={'TUẤT XẤU':'<div class="line black size2">Thiên Riêu(Đ)</div>',
                        'TUẤT':'<div class="line black size2">Thiên Y</div>'
        }
    else:
        dic_thienrieu ={'HỢI XẤU':'<div class="line black size2">Thiên Riêu(H)</div>',
                        'HỢI':'<div class="line black size2">Thiên Y</div>'
        }

    if key_thiengiai == 'TÝ':
        dic_thiengiai ={'TÝ':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'SỬU':
        dic_thiengiai ={'SỬU':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'DẦN':
        dic_thiengiai ={'DẦN':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'MÃO':
        dic_thiengiai ={'MÃO':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'THÌN':
        dic_thiengiai ={'THÌN':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'TỴ':
        dic_thiengiai ={'TỴ':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'NGỌ':
        dic_thiengiai ={'NGỌ':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'MÙI':
        dic_thiengiai ={'MÙI':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'THÂN':
        dic_thiengiai ={'THÂN':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'DẬU':
        dic_thiengiai ={'DẬU XẤU':'<div class="line red size2">Thiên Giải</div>'
        }
    elif key_thiengiai == 'TUẤT':
        dic_thiengiai ={'TUẤT':'<div class="line red size2">Thiên Giải</div>'
        }
    else:
        dic_thiengiai ={'HỢI':'<div class="line red size2">Thiên Giải</div>'
        }

    if key_diagiai == 'TÝ':
        dic_diagiai ={'TÝ':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'SỬU':
        dic_diagiai ={'SỬU':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'DẦN':
        dic_diagiai ={'DẦN':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'MÃO':
        dic_diagiai ={'MÃO':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'THÌN':
        dic_diagiai ={'THÌN':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'TỴ':
        dic_diagiai ={'TỴ':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'NGỌ':
        dic_diagiai ={'NGỌ':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'MÙI':
        dic_diagiai ={'MÙI':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'THÂN':
        dic_diagiai ={'THÂN':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'DẬU':
        dic_diagiai ={'DẬU XẤU':'<div class="line red size2">Địa Giải</div>'
        }
    elif key_diagiai == 'TUẤT':
        dic_diagiai ={'TUẤT':'<div class="line red size2">Địa Giải</div>'
        }
    else:
        dic_diagiai ={'HỢI':'<div class="line red size2">Địa Giải</div>'
        }

    dic_theothang = {**dic_taphu,**dic_huubat,**dic_thienhinh,**dic_thienrieu,**dic_thiengiai,**dic_diagiai}
    return dic_theothang

def ansaotheongay(thang_am,ngay_am):
    taphu=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
    huubat=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
    key_taphu = taphu[thang_am-1]
    dic_tamthai = {}
    dic_battoa = {}
    key_huubat = huubat[thang_am-1]
    dic_huubat = {}
    if ngay_am > 12:
        ngay_am = ngay_am%12

    if key_taphu == 'TÝ':
        tamthai=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'SỬU':
        tamthai=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'DẦN':
        tamthai=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'MÃO':
        tamthai=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'THÌN':
        tamthai=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'TỴ':
        tamthai=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'NGỌ':
        tamthai=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'MÙI':
        tamthai=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'THÂN':
        tamthai=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'DẬU':
        tamthai=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    elif key_taphu == 'TUẤT':
        tamthai=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }
    else:
        tamthai=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'<div class="line black size2">Tam Thai</div>'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU XẤU':'<div class="line black size2">Tam Thai</div>'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'<div class="line black size2">Tam Thai</div>'
            }
        else:
            dic_tamthai ={'HỢI':'<div class="line black size2">Tam Thai</div>'
            }


    if key_huubat == 'TÝ':
        battoa=('TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'SỬU':
        battoa=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'DẦN':
        battoa=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'MÃO':
        battoa=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'THÌN':
        battoa=('THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'TỴ':
        battoa=('TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'NGỌ':
        battoa=('NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'MÙI':
        battoa=('MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'THÂN':
        battoa=('THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'DẬU':
        battoa=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    elif key_huubat == 'TUẤT':
        battoa=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }
    else:
        battoa=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'<div class="line green size2">Bát Tọa</div>'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU XẤU':'<div class="line green size2">Bát Tọa</div>'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'<div class="line green size2">Bát Tọa</div>'
            }
        else:
            dic_battoa ={'HỢI':'<div class="line green size2">Bát Tọa</div>'
            }


    merge = custom_merge(dic_tamthai,dic_battoa)

    return merge

def custom_merge(unit1, unit2):
   # Merge dictionaries and add values of same keys
   out = {**unit1, **unit2}
   for key, value in out.items():
       if key in unit1 and key in unit2:
               out[key] = value +''+ unit1[key]
   return out

def ansaotheogio(chi_gio,ngay_am,chi_nam,option):
    diakiep=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
    diakhong=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
    vanxuong=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
    vankhuc=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
    dic_diakiep={}
    if ngay_am > 12:
        ngay_am = ngay_am%12
    if chi_gio == 'TÝ':
        saoanquang=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'HỢI XẤU':'<div class="line red size2">Địa Kiếp(Đ)</div><div class="line red size2">Địa Không(Đ)</div>',
                      'TUẤT':'<div class="line grey size2">Văn Xương(Đ)</div>',
                      'THÌN':'<div class="line black size2">Văn Khúc(Đ)</div>',
                      'TỴ':'<div class="line grey size2">Thai Phụ</div>',
                      'MÃO':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'SỬU':
        saoanquang=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'TÝ XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'TUẤT XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'HỢI':'<div class="line grey size2">Văn Xương(Đ)</div>',
                      'TỴ':'<div class="line black size2">Văn Khúc(Đ)</div>',
                      'NGỌ':'<div class="line grey size2">Thai Phụ</div>',
                      'THÌN':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'DẦN':
        saoanquang=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'SỬU XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'DẬU XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'TÝ':'<div class="line grey size2">Văn Xương(H)</div>',
                      'NGỌ':'<div class="line black size2">Văn Khúc(Đ)</div>',
                      'MÙI':'<div class="line grey size2">Thai Phụ</div>',
                      'TỴ':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'MÃO':
        saoanquang=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'DẦN XẤU':'<div class="line red size2">Địa Kiếp(Đ)</div>',
                      'THÂN XẤU':'<div class="line red size2">Địa Không(Đ)</div>',
                      'SỬU':'<div class="line grey size2">Văn Xương(Đ)</div>',
                      'MÙI':'<div class="line black size2">Văn Khúc(Đ)</div>',
                      'THÂN':'<div class="line grey size2">Thai Phụ</div>',
                      'NGỌ':'<div class="line organ size2">Phong Cáo</div>'

        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'THÌN':
        saoanquang=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'MÃO XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'MÙI XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'DẦN':'<div class="line grey size2">Văn Xương(H)</div>',
                      'THÂN':'<div class="line black size2">Văn Khúc(H)</div>',
                      'DẬU':'<div class="line grey size2">Thai Phụ</div>',
                      'MÙI':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'TỴ':
        saoanquang=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'THÌN XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'NGỌ XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'MÃO':'<div class="line grey size2">Văn Xương(H)</div>',
                      'DẬU':'<div class="line black size2">Văn Khúc(H)</div>',
                      'TUẤT':'<div class="line grey size2">Thai Phụ</div>',
                      'THÂN':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'NGỌ':
        saoanquang=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'TỴ XẤU':'<div class="line red size2">Địa Kiếp(Đ)</div><div class="line red size2">Địa Không(Đ)</div>',
                      'THÌN':'<div class="line grey size2">Văn Xương(Đ)</div>',
                      'TUẤT':'<div class="line black size2">Văn Khúc(H)</div>',
                      'DẬU':'<div class="line grey size2">Thai Phụ</div>',
                      'HỢI':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'MÙI':
        saoanquang=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'NGỌ XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'THÌN XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'TỴ':'<div class="line grey size2">Văn Xương(Đ)</div>',
                      'HỢI':'<div class="line black size2">Văn Khúc(H)</div>',
                      'TUẤT':'<div class="line grey size2">Thai Phụ</div>',
                      'TÝ':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'THÂN':
        saoanquang=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'MÙI XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'MÃO XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'NGỌ':'<div class="line grey size2">Văn Xương(H)</div>',
                      'TÝ':'<div class="line black size2">Văn Khúc(H)</div>',
                      'HỢI':'<div class="line grey size2">Thai Phụ</div>',
                      'SỬU':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'DẬU':
        saoanquang=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'THÂN XẤU':'<div class="line red size2">Địa Kiếp(Đ)</div>',
                      'DẦN XẤU':'<div class="line red size2">Địa Không(Đ)</div>',
                      'MÙI':'<div class="line grey size2">Văn Xương(Đ)</div>',
                      'SỬU':'<div class="line black size2">Văn Khúc(H)</div>',
                      'TÝ':'<div class="line grey size2">Thai Phụ</div>',
                      'DẦN':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    elif chi_gio == 'TUẤT':
        saoanquang=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'DẬU XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'SỬU XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'THÂN':'<div class="line grey size2">Văn Xương(H)</div>',
                      'DẦN':'<div class="line black size2">Văn Khúc(H)</div>',
                      'MÃO':'<div class="line grey size2">Thai Phụ</div>',
                      'SỬU':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    else:
        saoanquang=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
        key_anquan = saoanquang[ngay_am-2]
        saothienquy=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
        key_thienquy = saothienquy[ngay_am-2]
        dic_anquan={key_anquan:'<div class="line green size2">Ân Quang</div>'}
        dic_thienquy={key_thienquy:'<div class="line organ size2">Thiên Quý</div>'}
        dic_quanquy = custom_merge(dic_anquan,dic_thienquy)
        dic_diakiep ={'TUẤT XẤU':'<div class="line red size2">Địa Kiếp(H)</div>',
                      'TÝ XẤU':'<div class="line red size2">Địa Không(H)</div>',
                      'DẬU':'<div class="line grey size2">Văn Xương(H)</div>',
                      'MÃO':'<div class="line black size2">Văn Khúc(H)</div>',
                      'THÌN':'<div class="line grey size2">Thai Phụ</div>',
                      'DẦN':'<div class="line organ size2">Phong Cáo</div>'
        }
        dic_theogio = custom_merge(dic_quanquy,dic_diakiep)
    dic_hoalinh = hoatinhlinhtinh(option,chi_nam,chi_gio)
    dic_kethophoalinh={}
    if dic_hoalinh:
        dic_kethophoalinh = custom_merge(dic_theogio,dic_hoalinh)


    return dic_kethophoalinh

def hoatinhlinhtinh(option,chi_nam,chi_gio):
    dic_hoalinhtinh={}
    if option == 'Nam':
        if chi_nam in chi_duong:
            if chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
                hoalinh=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
                hoalinh=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(h)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
                hoalinh=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
                linhtinh=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)Linh</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Linh Tinh(h)</div>',
                    'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
            else:
                hoalinh=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
        else:
            if chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
                hoalinh=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
                hoalinh=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(h)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
                hoalinh=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
                linhtinh=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)Linh</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Linh Tinh(h)</div>',
                    'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
            else:
                hoalinh=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
    else:
        if chi_nam in chi_am:
            if chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
                hoalinh=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
                hoalinh=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(h)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
                hoalinh=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
                linhtinh=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)Linh</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Linh Tinh(h)</div>',
                    'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>',
                    'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>'}
            else:
                hoalinh=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
                linhtinh=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
        else:
            if chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
                hoalinh=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
                linhtinh=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
                hoalinh=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
                linhtinh=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
            elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
                hoalinh=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
                linhtinh=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
            else:
                hoalinh=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
                linhtinh=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
                if chi_gio == 'TÝ':
                    dic_hoalinhtinh={'DẬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TUẤT XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'SỬU':
                    dic_hoalinhtinh={'THÂN XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'DẦN':
                    dic_hoalinhtinh={'MÙI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'THÂN XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'MÃO':
                    dic_hoalinhtinh={'NGỌ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'MÙI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'THÌN':
                    dic_hoalinhtinh={'TỴ XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'NGỌ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'TỴ':
                    dic_hoalinhtinh={'THÌN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'TỴ XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'NGỌ':
                    dic_hoalinhtinh={'MÃO XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'THÌN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'MÙI':
                    dic_hoalinhtinh={'DẦN XẤU':'<div class="line red size2">Hỏa Tinh(Đ)</div>',
                    'MÃO XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'THÂN':
                    dic_hoalinhtinh={'SỬU XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'DẦN XẤU':'<div class="line red size2">Linh Tinh(Đ)</div>'}
                elif chi_gio == 'DẬU':
                    dic_hoalinhtinh={'TÝ XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'SỬU XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'TUẤT':
                    dic_hoalinhtinh={'HỢI XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'TÝ XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
                elif chi_gio == 'HỢI':
                    dic_hoalinhtinh={'TUẤT XẤU':'<div class="line red size2">Hỏa Tinh(H)</div>',
                    'HỢI XẤU':'<div class="line red size2">Linh Tinh(H)</div>'}
    return dic_hoalinhtinh

def cacbosaokhac(chi_gio,thang_am,can_nam,chi_nam,ngay_am,option):
    dic_thienladiavong = thienladiavong()
    dic_thienluongthiensu = thienluongthiensu(chi_gio,thang_am)
    dic_lavongluongsu = custom_merge(dic_thienladiavong,dic_thienluongthiensu)
    dic_ansaobacsi = ansaobacsi(can_nam,chi_nam,option)
    dic_lavongluongsusi = custom_merge(dic_lavongluongsu,dic_ansaobacsi)
    dic_ansaodauquan_thienkhong = ansaodauquan_thienkhong(chi_nam,thang_am,chi_gio)
    dic_lavongluongsusiquankhong = custom_merge(dic_lavongluongsusi,dic_ansaodauquan_thienkhong)
    dic_antuhoa = antuhoa(chi_gio,thang_am,can_nam,chi_nam,ngay_am,option)
    dic_dic_lavongluongsusiquankhongtuhoa = custom_merge(dic_lavongluongsusiquankhong,dic_antuhoa)
    dic_thientaithientho = thientaithientho(chi_gio,thang_am,chi_nam)
    dic_dic_lavongluongsusiquankhongtuhoataitho = custom_merge(dic_dic_lavongluongsusiquankhongtuhoa,dic_thientaithientho)
    return dic_dic_lavongluongsusiquankhongtuhoataitho

def thienladiavong():
    dic_thienladiavong = {}
    dic_thienladiavong={'THÌN XẤU':'<div class="line red size2">Thiên La</div>',
                    'TUẤT XẤU':'<div class="line red size2">Địa Võng</div>'}

    return dic_thienladiavong

def thienluongthiensu(chi_gio,thang_am):
    dic_thienluongthiensu={}
    dic_cungmenhthan = cungmenhthan(chi_gio,thang_am)
    for key, value in dic_cungmenhthan.items():
        if 'NÔ BỘC' in value:
            key1= key + ' XẤU'
            dic_thienluong={key1:'<div class="line green size2">Thiên Thương</div>'}
        if 'TẬT ÁCH' in value:
            key2=key + ' XẤU'
            dic_thiensu={key2:'<div class="line black size2">Thiên Sứ</div>'}
    dic_thienluongthiensu={**dic_thienluong,**dic_thiensu}
    return dic_thienluongthiensu

def ansaobacsi(can_nam,chi_nam,option):
    dic_ansaobacsi={}
    dic_vonglocton =  vonglocton(can_nam,chi_nam,option)
    for key, value in dic_vonglocton.items():
        if 'Lộc Tồn' in value:
            dic_ansaobacsi={key:'<div class="line green size2">Bác Sĩ</div>'}
    return dic_ansaobacsi

def ansaodauquan_thienkhong(chi_nam,thang_am,chi_gio):
    dic_ansaotheochi = ansaotheochi(chi_nam)
    for key, value in dic_ansaotheochi.items():
        if 'Thái Tuế' in value:
            key = key.split()[0]
            dauquandemnghich = chieunghichdiachi(thang_am,key)
            key_dauquan = chieuthuan2diachi(dauquandemnghich,chi_gio)
            key_dauquan = key_dauquan + ' XẤU'
            dic_dauquan={key_dauquan:'<div class="line red size2">Đẩu Quân</div>'}
            if key == 'TÝ':
                dic_thienkhong={'SỬU XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'SỬU':
                dic_thienkhong={'DẦN XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'DẦN':
                dic_thienkhong={'MÃO XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'MÃO':
                dic_thienkhong={'THÌN XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'THÌN':
                dic_thienkhong={'TỴ XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'TỴ':
                dic_thienkhong={'NGỌ XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'NGỌ':
                dic_thienkhong={'MÙI XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'MÙI':
                dic_thienkhong={'THÂN XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'THÂN':
                dic_thienkhong={'DẬU XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'DẬU':
                dic_thienkhong={'TUẤT XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'TUẤT':
                dic_thienkhong={'HỢI XẤU':'<div class="line red size2">Thiên Không</div>'}
            elif key == 'HỢI':
                dic_thienkhong={'TÝ XẤU':'<div class="line red size2">Thiên Không</div>'}
    dic_ansaodauquan_thienkhong = custom_merge(dic_dauquan,dic_thienkhong)

    return dic_ansaodauquan_thienkhong

def chieunghichdiachi(number,dia_chi):
    if dia_chi == 'TÝ':
        chieunghich=('TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'SỬU':
        chieunghich=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'DẦN':
        chieunghich=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'MÃO':
        chieunghich=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'THÌN':
        chieunghich=('THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'TỴ':
        chieunghich=('TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'NGỌ':
        chieunghich=('NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'MÙI':
        chieunghich=('MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'THÂN':
        chieunghich=('THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'DẬU':
        chieunghich=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
        key_chieunghich = chieunghich[number-1]

    elif dia_chi == 'TUẤT':
        chieunghich=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
        key_chieunghich = chieunghich[number-1]

    else:
        chieunghich=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
        key_chieunghich = chieunghich[number-1]
    return key_chieunghich


def chieuthuandiachi(number,dia_chi):
    if dia_chi == 'TÝ':
        chieuthuan=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'SỬU':
        chieuthuan=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'DẦN':
        chieuthuan=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'MÃO':
        chieuthuan=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'THÌN':
        chieuthuan=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'TỴ':
        chieuthuan=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'NGỌ':
        chieuthuan=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'MÙI':
        chieuthuan=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'THÂN':
        chieuthuan=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'DẬU':
        chieuthuan=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
        key_chieuthuan = chieuthuan[number-1]
    elif dia_chi == 'TUẤT':
        chieuthuan=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
        key_chieuthuan = chieuthuan[number-1]
    else:
        chieuthuan=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
        key_chieuthuan = chieuthuan[number-1]
    return key_chieuthuan

def chieuthuan2diachi(dia_chi1,dia_chi2):
    if dia_chi1 == 'TÝ':
        chieuthuan=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
        number = int(chieuthuan.index(dia_chi2))
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'SỬU':
        chieuthuan=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
        number = int(chieuthuan.index(dia_chi2))
        number = number+1
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'DẦN':
        chieuthuan=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
        number = int(chieuthuan.index(dia_chi2))
        number = number+2
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'MÃO':
        chieuthuan=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
        number = int(chieuthuan.index(dia_chi2))
        number = number+3
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'THÌN':
        chieuthuan=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
        number = int(chieuthuan.index(dia_chi2))
        number = number+4
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'TỴ':
        chieuthuan=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
        number = int(chieuthuan.index(dia_chi2))
        number = number+5
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'NGỌ':
        chieuthuan=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
        number = int(chieuthuan.index(dia_chi2))
        number = number+6
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'MÙI':
        chieuthuan=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
        number = int(chieuthuan.index(dia_chi2))
        number = number+7
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'THÂN':
        chieuthuan=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
        number = int(chieuthuan.index(dia_chi2))
        number = number+8
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'DẬU':
        chieuthuan=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
        number = int(chieuthuan.index(dia_chi2))
        number = number+9
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'TUẤT':
        chieuthuan=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
        number = int(chieuthuan.index(dia_chi2))
        number = number+10
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    elif dia_chi1 == 'HỢI':
        chieuthuan=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
        number = int(chieuthuan.index(dia_chi2))
        number = number+11
        if number > 11:
            number = number%11
        key_chieuthuan = chieuthuan[number]
    return key_chieuthuan

def tuankhong(can_nam,chi_nam):
    dic_khong = {}
    dic_tuankhong = can_nam + ' ' + chi_nam
    print("dic_tuankhong : ",dic_tuankhong)
    tuathoi = ("GIÁP TÝ","ẤT SỬU","BÍNH DẦN","ĐINH MÃO","MẬU THÌN","KỶ TỴ","CANH NGỌ","TÂN MÙI","NHÂM THÂN","QUÝ DẬU")
    thandau = ("GIÁP TUẤT","ẤT HỢI","BÍNH TÝ","ĐINH SỬU","MẬU DẦN","KỶ MÃO","CANH THÌN","TÂN TỴ","NHÂM NGỌ","QUÝ MÙI")
    ngomui = ("GIÁP THÂN","ẤT DẬU","BÍNH TUẤT","ĐINH HỢI","MẬU TÝ","KỶ SỬU","CANH DẦN","TÂN MÃO","NHÂM THÌN","QUÝ TỴ")
    thinty = ("GIÁP NGỌ","ẤT MÙI","BÍNH THÂN","ĐINH DẬU","MẬU TUẤT","KỶ HỢI","CANH TÝ","TÂN SỬU","NHÂM DẦN","QUÝ MÃO")
    danmao = ("GIÁP THÌN","ẤT TỴ","BÍNH NGỌ","ĐINH MÙI","MẬU THÂN","KỶ DẬU","CANH TUẤT","TÂN HỢI","NHÂM TÝ","QUÝ SỬU")
    tysuu = ("GIÁP DẦN","ẤT MÃO","BÍNH THÌN","ĐINH TỴ","MẬU NGỌ","KỶ MÙI","CANH THÂN","TÂN DẬU","NHÂM TUẤT","QUÝ HỢI")
    if dic_tuankhong in tuathoi:
        dic_khong={'tuathoi':'<div class="ttitem ttbotright bgorgan">Tuần</div>'}
        return dic_khong
    elif dic_tuankhong in thandau:
        dic_khong={'thandau':'<div class="ttitem ttbotright bgorgan">Tuần</div>'}
        return dic_khong
    elif dic_tuankhong in ngomui:
        dic_khong={'ngomui':'<div class="ttitem tttopcen bgorgan">Tuần</div>'}
        return dic_khong
    elif dic_tuankhong in thinty:
        dic_khong={'thinty':'<div class="ttitem ttbotright bgorgan">Tuần</div>'}
        return dic_khong
    elif dic_tuankhong in danmao:
        dic_khong={'danmao':'<div class="ttitem ttbotright bgorgan">Tuần</div>'}
        return dic_khong
    elif dic_tuankhong in tysuu:
        dic_khong={'tysuu':'<div class="ttitem ttbotcen2 bgorgan">Tuần</div>'}
        return dic_khong
    return ''

def tuantriet(can_nam):
    dic_khong = {}
    if can_nam == 'GIÁP' or can_nam == 'KỶ':
        dic_khong={'thandau':'<div class="ttitem ttbotleft bgblue2">Triệt</div>'}
        return dic_khong
    elif can_nam == 'ẤT' or can_nam == 'CANH':
        dic_khong={'ngomui':'<div class="ttitem tttopcen bgblue2">Triệt</div>'}
        return dic_khong
    elif can_nam == 'BÍNH' or can_nam == 'TÂN':
        dic_khong={'thinty':'<div class="ttitem ttbotleft bgblue2">Triệt</div>'}
        return dic_khong
    elif can_nam == 'ĐINH' or can_nam == 'NHÂM':
        dic_khong={'danmao':'<div class="ttitem ttbotleft bgblue2">Triệt</div>'}
        return dic_khong
    elif can_nam == 'MẬU' or can_nam == 'QUÝ':
        dic_khong={'tysuu':'<div class="ttitem ttbotcen2 bgblue2">Triệt</div>'}
        return dic_khong
    return ''

def khongtuantriet(can_nam,chi_nam):
    tuan_khong = tuankhong(can_nam,chi_nam)
    tuan_triet = tuantriet(can_nam)
    print("tuan_khong : ",tuan_khong)
    print("tuan_triet : ",tuan_triet)
    dic_khongtuantriet = custom_merge(tuan_khong,tuan_triet)
    if len(dic_khongtuantriet) == 1:
        dic_tuantriet={}
        for key in dic_khongtuantriet.keys():
            if key=='thandau':
                dic_tuantriet ={key:'<div class="ttitem ttbotleft bggreen">Tuần - Triệt</div>'}
            elif key=='ngomui':
                dic_tuantriet ={key:'<div class="ttitem tttopcen bggreen">Tuần - Triệt</div>'}
            elif key=='thinty':
                dic_tuantriet ={key:'<div class="ttitem ttbotleft bggreen">Tuần - Triệt</div>'}
            elif key=='danmao':
                dic_tuantriet ={key:'<div class="ttitem ttbotleft bggreen">Tuần - Triệt</div>'}
            else:
                dic_tuantriet ={key:'<div class="ttitem ttbotcen2 bggreen">Tuần - Triệt</div>'}
        return dic_tuantriet
    return dic_khongtuantriet

def daivantuvi(option,chi_gio,chi_nam,can_ngay,chi_ngay,ngay_am,thang_am,nam_am,gio,phut):
    namdaivan = namvaodaivan(chi_nam,option,gio,phut,ngay_am,thang_am,nam_am)
    cung_menhthan = cungmenhthan(chi_gio,thang_am)
    key_menh = ''
    for key, value in cung_menhthan.items():
        if 'MỆNH' in value:
            key_menh = key
    dic_daivan = {}
    if option == 'Nam':
        if chi_nam in chi_duong:
            if key_menh == 'TÝ':
                tuple_tuvi=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'SỬU':
                tuple_tuvi=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẦN':
                tuple_tuvi=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÃO':
                tuple_tuvi=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÌN':
                tuple_tuvi=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TỴ':
                tuple_tuvi=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'NGỌ':
                tuple_tuvi=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÙI':
                tuple_tuvi=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÂN':
                tuple_tuvi=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẬU':
                tuple_tuvi=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TUẤT':
                tuple_tuvi=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            else:
                tuple_tuvi=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
        else:
            if key_menh == 'TÝ':
                tuple_tuvi=('TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'SỬU':
                tuple_tuvi=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẦN':
                tuple_tuvi=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÃO':
                tuple_tuvi=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÌN':
                tuple_tuvi=('THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TỴ':
                tuple_tuvi=('TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'NGỌ':
                tuple_tuvi=('NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÙI':
                tuple_tuvi=('MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÂN':
                tuple_tuvi=('THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẬU':
                tuple_tuvi=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TUẤT':
                tuple_tuvi=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            else:
                tuple_tuvi=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
    else:
        if chi_nam in chi_am:
            if key_menh == 'TÝ':
                tuple_tuvi=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'SỬU':
                tuple_tuvi=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẦN':
                tuple_tuvi=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÃO':
                tuple_tuvi=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÌN':
                tuple_tuvi=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TỴ':
                tuple_tuvi=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'NGỌ':
                tuple_tuvi=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÙI':
                tuple_tuvi=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÂN':
                tuple_tuvi=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẬU':
                tuple_tuvi=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TUẤT':
                tuple_tuvi=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            else:
                tuple_tuvi=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
        else:
            if key_menh == 'TÝ':
                tuple_tuvi=('TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'SỬU':
                tuple_tuvi=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẦN':
                tuple_tuvi=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÃO':
                tuple_tuvi=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÌN':
                tuple_tuvi=('THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TỴ':
                tuple_tuvi=('TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'NGỌ':
                tuple_tuvi=('NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'MÙI':
                tuple_tuvi=('MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'THÂN':
                tuple_tuvi=('THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'DẬU':
                tuple_tuvi=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            elif key_menh == 'TUẤT':
                tuple_tuvi=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
            else:
                tuple_tuvi=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
                for key_nam in tuple_tuvi:
                    dic_daivan[key_nam] = namdaivan
                    namdaivan += 10
    return dic_daivan

def tuoituvi(option,can_nam,chi_nam,thang_now,nam_now,nam_birthday):
    tuoi = (nam_now - nam_birthday) + 1
    if option == 'Nam':
        if chi_nam in chi_duong:
            return f'Dương {option}-{tuoi} tuổi (tháng {thang_now} năm {nam_now}-{can_nam} {chi_nam})'
        else:
            return f'Âm {option}-{tuoi} tuổi (tháng {thang_now} năm {nam_now}-{can_nam} {chi_nam})'
    else:
        if chi_nam in chi_am:
            return f'Âm {option}-{tuoi} tuổi (tháng {thang_now} năm {nam_now}-{can_nam} {chi_nam})'
        else:
            return f'Dương {option}-{tuoi} tuổi (tháng {thang_now} năm {nam_now}-{can_nam} {chi_nam})'
    return ''

def tieuvantungnamtuvi(option,chi_gio,chi_nam,can_ngay,chi_ngay,ngay_am,thang_am,nam_am,gio,phut,nam_now):
    daivan = daivantuvi(option,chi_gio,chi_nam,can_ngay,chi_ngay,ngay_am,thang_am,nam_am,gio,phut)
    tieuvan = {}
    tieuvan_tungnam= {}
    daivan_tungnam={}
    dic_daitieuvan={}
    dic_tieuvan = {}
    for key, value in daivan.items():
        if value >= 1:
            tongdaivan = nam_am + (value-1)
            tieuvan[key] = tongdaivan
        else:
            tongdaivan = nam_am
            value = value + 1
            tieuvan[key] = tongdaivan
    for key, value in tieuvan.items():
        result = []
        for i in range(0,10):
            result.append(value+i)
        tieuvan_tungnam[key] = result
    for key, value in daivan.items():
        result = []
        for i in range(0,10):
            result.append(value+i)
        daivan_tungnam[key] = result
    for i, j in tieuvan_tungnam.items():
        for x, y in daivan_tungnam.items():
            if i == x:
                dic_daitieuvan[i]=(j+y)
    for key, value in dic_daitieuvan.items():
        if nam_now in value:
            if key == 'TÝ':
                dic_tieuvan={'TÝ':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'SỬU':
                dic_tieuvan={'SỬU':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'DẦN':
                dic_tieuvan={'DẦN':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'MÃO':
                dic_tieuvan={'MÃO':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'THÌN':
                dic_tieuvan={'THÌN':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'TỴ':
                dic_tieuvan={'TỴ':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'NGỌ':
                dic_tieuvan={'NGỌ':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'HỢI':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'MÙI':
                dic_tieuvan={'MÙI':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'TÝ':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'THÂN':
                dic_tieuvan={'THÂN':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'SỬU':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'DẬU':
                dic_tieuvan={'DẬU':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'DẦN':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            elif key == 'TUẤT':
                dic_tieuvan={'TUẤT':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'MÃO':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
            else:
                dic_tieuvan={'HỢI':f'<div class="line grey size4">{value[10]}-{value[19]}</div><div class="line grey size5">{value[0]}-{value[9]}</div>',
                            'TỴ':f'<div class="line grey size4">{value[11]}-{value[13]}</div><div class="line grey size5">{value[1]}-{value[3]}</div>',
                            'THÌN':f'<div class="line grey size4">{value[12]}</div><div class="line grey size5">{value[2]}</div>',
                            'NGỌ':f'<div class="line grey size4">{value[14]}</div><div class="line grey size5">{value[4]}</div>',
                            'MÙI':f'<div class="line grey size4">{value[15]}</div><div class="line grey size5">{value[5]}</div>',
                            'THÂN':f'<div class="line grey size4">{value[16]}</div><div class="line grey size5">{value[6]}</div>',
                            'DẬU':f'<div class="line grey size4">{value[17]}</div><div class="line grey size5">{value[7]}</div>',
                            'TUẤT':f'<div class="line grey size4">{value[18]}</div><div class="line grey size5">{value[8]}</div>'}
    return dic_tieuvan


def custom_merge_luunien(unit1, unit2):
   # Merge dictionaries and add values of same keys
   out = {**unit1, **unit2}
   for key, value in out.items():
       if key in unit1 and key in unit2:
               out[key] = value +', '+ unit1[key]
   return out

def luuvonglocton(can_nam,chi_nam,option):
    locton = {}
    if option == 'Nam':
        if chi_nam in chi_am:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'LY.Lộc Tồn',
                'SỬU':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'TÝ':'LY.Thanh Long',
                'HỢI':'LY.Tiểu Hao',
                'TUẤT':'LY.Tướng Quân, LY.Quốc Ấn',
                'DẬU':'LY.Tấu Thư',
                'THÂN':'LY.Phi Liêm',
                'MÙI':'LY.Hỉ Thần, LY.Đường Phù',
                'NGỌ':'LY.Bệnh Phù',
                'TỴ':'LY.Đại Hao',
                'THÌN':'LY.Phục Binh',
                'MÃO':'LY.Quan Phủ, LY.Kình Dương(H)'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'LY.Lộc Tồn',
                'DẦN':'LY.Lực Sĩ, LY.Đà La(H)',
                'SỬU':'LY.Thanh Long',
                'TÝ':'LY.Tiểu Hao',
                'HỢI':'LY.Tướng Quân, LY.Quốc Ấn',
                'TUẤT':'LY.Tấu Thư',
                'DẬU':'LY.Phi Liêm',
                'THÂN':'LY.Hỉ Thần, LY.Đường Phù',
                'MÙI':'LY.Bệnh Phù',
                'NGỌ':'LY.Đại Hao',
                'TỴ':'LY.Phục Binh',
                'THÌN':'LY.Quan Phủ, LY.Kình Dương(Đ)'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'LY.Lộc Tồn',
                'THÌN':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'MÃO':'LY.Thanh Long',
                'DẦN':'LY.Tiểu Hao',
                'SỬU':'LY.Tướng Quân, LY.Quốc Ấn',
                'TÝ':'LY.Tấu Thư',
                'HỢI':'LY.Phi Liêm',
                'TUẤT':'LY.Hỉ Thần, LY.Đường Phù',
                'DẬU':'LY.Bệnh Phù',
                'THÂN':'LY.Đại Hao',
                'MÙI':'LY.Phục Binh',
                'NGỌ':'LY.Quan Phủ, LY.Kình Dương(H)'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'LY.Lộc Tồn',
                'TỴ':'LY.Lực Sĩ, LY.Đà La(H)',
                'THÌN':'LY.Thanh Long',
                'MÃO':'LY.Tiểu Hao',
                'DẦN':'LY.Tướng Quân, LY.Quốc Ấn',
                'SỬU':'LY.Tấu Thư',
                'TÝ':'LY.Phi Liêm',
                'HỢI':'LY.Hỉ Thần, LY.Đường Phù',
                'TUẤT':'LY.Bệnh Phù',
                'DẬU':'LY.Đại Hao',
                'THÂN':'LY.Phục Binh',
                'MÙI':'LY.Quan Phủ, LY.Kình Dương(Đ)'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'LY.Lộc Tồn',
                'MÙI':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'NGỌ':'LY.Thanh Long',
                'TỴ':'LY.Tiểu Hao',
                'THÌN':'LY.Tướng Quân, LY.Quốc Ấn',
                'MÃO':'LY.Tấu Thư',
                'DẦN':'LY.Phi Liêm',
                'SỬU':'LY.Hỉ Thần, LY.Đường Phù',
                'TÝ':'LY.Bệnh Phù',
                'HỢI':'LY.Đại Hao',
                'TUẤT':'LY.Phục Binh',
                'DẬU':'LY.Quan Phủ, LY.Kình Dương(H)'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'LY.Lộc Tồn',
                'THÂN':'LY.Lực Sĩ, LY.Đà La(H)',
                'MÙI':'LY.Thanh Long',
                'NGỌ':'LY.Tiểu Hao',
                'TỴ':'LY.Tướng Quân, LY.Quốc Ấn',
                'THÌN':'LY.Tấu Thư',
                'MÃO':'LY.Phi Liêm',
                'DẦN':'LY.Hỉ Thần, LY.Đường Phù',
                'SỬU':'LY.Bệnh Phù',
                'TÝ':'LY.Đại Hao',
                'HỢI':'LY.Phục Binh',
                'TUẤT':'LY.Quan Phủ, LY.Kình Dương(Đ)'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'LY.Lộc Tồn',
                'TUẤT':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'DẬU':'LY.Thanh Long',
                'THÂN':'LY.Tiểu Hao',
                'MÙI':'LY.Tướng Quân, LY.Quốc Ấn',
                'NGỌ':'LY.Tấu Thư',
                'TỴ':'LY.Phi Liêm',
                'THÌN':'LY.Hỉ Thần, LY.Đường Phù',
                'MÃO':'LY.Bệnh Phù',
                'DẦN':'LY.Đại Hao',
                'SỬU':'LY.Phục Binh',
                'TÝ':'LY.Quan Phủ, LY.Kình Dương(H)'}
            else:
                locton = {'TÝ':'LY.Lộc Tồn',
                'HỢI':'LY.Lực Sĩ, LY.Đà La(H)',
                'TUẤT':'LY.Thanh Long',
                'DẬU':'LY.Tiểu Hao',
                'THÂN':'LY.Tướng Quân, LY.Quốc Ấn',
                'MÙI':'LY.Tấu Thư',
                'NGỌ':'LY.Phi Liêm',
                'TỴ':'LY.Hỉ Thần, LY.Đường Phù',
                'THÌN':'LY.Bệnh Phù',
                'MÃO':'LY.Đại Hao',
                'DẦN':'LY.Phục Binh',
                'SỬU':'LY.Quan Phủ, LY.Kình Dương(Đ)'}

        else:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'LY.Lộc Tồn',
                'MÃO':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'THÌN':'LY.Thanh Long',
                'TỴ':'LY.Tiểu Hao',
                'NGỌ':'LY.Tướng Quân',
                'MÙI':'LY.Tấu Thư, LY.Đường Phù',
                'THÂN':'LY.Phi Liêm',
                'DẬU':'LY.Hỉ Thần',
                'TUẤT':'LY.Bệnh Phù, LY.Quốc Ấn',
                'HỢI':'LY.Đại Hao',
                'TÝ':'LY.Phục Binh',
                'SỬU':'LY.Quan Phủ, LY.Đà La(Đ)'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'LY.Lộc Tồn',
                'THÌN':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'TỴ':'LY.Thanh Long',
                'NGỌ':'LY.Tiểu Hao',
                'MÙI':'LY.Tướng Quân',
                'THÂN':'LY.Tấu Thư, LY.Đường Phù',
                'DẬU':'LY.Phi Liêm',
                'TUẤT':'LY.Hỉ Thần',
                'HỢI':'LY.Bệnh Phù, LY.Quốc Ấn',
                'TÝ':'LY.Đại Hao',
                'SỬU':'LY.Phục Binh',
                'DẦN':'LY.Quan Phủ, LY.Đà La(H)'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'LY.Lộc Tồn',
                'NGỌ':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'MÙI':'LY.Thanh Long',
                'THÂN':'LY.Tiểu Hao',
                'DẬU':'LY.Tướng Quân',
                'TUẤT':'LY.Tấu Thư, LY.Đường Phù',
                'HỢI':'LY.Phi Liêm',
                'TÝ':'LY.Hỉ Thần',
                'SỬU':'LY.Bệnh Phù, LY.Quốc Ấn',
                'DẦN':'LY.Đại Hao',
                'MÃO':'LY.Phục Binh',
                'THÌN':'LY.Quan Phủ, LY.Đà La(Đ)'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'LY.Lộc Tồn',
                'MÙI':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'THÂN':'LY.Thanh Long',
                'DẬU':'LY.Tiểu Hao',
                'TUẤT':'LY.Tướng Quân',
                'HỢI':'LY.Tấu Thư, LY.Đường Phù',
                'TÝ':'LY.Phi Liêm',
                'SỬU':'LY.Hỉ Thần',
                'DẦN':'LY.Bệnh Phù, LY.Quốc Ấn',
                'MÃO':'LY.Đại Hao',
                'THÌN':'LY.Phục Binh',
                'TỴ':'LY.Quan Phủ, LY.Đà La(H)'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'LY.Lộc Tồn',
                'DẬU':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'TUẤT':'LY.Thanh Long',
                'HỢI':'LY.Tiểu Hao',
                'TÝ':'LY.Tướng Quân',
                'SỬU':'LY.Tấu Thư, LY.Đường Phù',
                'DẦN':'LY.Phi Liêm',
                'MÃO':'LY.Hỉ Thần',
                'THÌN':'LY.Bệnh Phù, LY.Quốc Ấn',
                'TỴ':'LY.Đại Hao',
                'NGỌ':'LY.Phục Binh',
                'MÙI':'LY.Quan Phủ, LY.Đà La(Đ)'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'LY.Lộc Tồn',
                'TUẤT':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'HỢI':'LY.Thanh Long',
                'TÝ':'LY.Tiểu Hao',
                'SỬU':'LY.Tướng Quân',
                'DẦN':'LY.Tấu Thư, LY.Đường Phù',
                'MÃO':'LY.Phi Liêm',
                'THÌN':'LY.Hỉ Thần',
                'TỴ':'LY.Bệnh Phù, LY.Quốc Ấn',
                'NGỌ':'LY.Đại Hao',
                'MÙI':'LY.Phục Binh',
                'THÂN':'LY.Quan Phủ, LY.Đà La(H)'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'LY.Lộc Tồn',
                'TÝ':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'SỬU':'LY.Thanh Long',
                'DẦN':'LY.Tiểu Hao',
                'MÃO':'LY.Tướng Quân',
                'THÌN':'LY.Tấu Thư, LY.Đường Phù',
                'TỴ':'LY.Phi Liêm',
                'NGỌ':'LY.Hỉ Thần',
                'MÙI':'LY.Bệnh Phù, LY.Quốc Ấn',
                'THÂN':'LY.Đại Hao',
                'DẬU':'LY.Phục Binh',
                'TUẤT':'LY.Quan Phủ, LY.Đà La(Đ)'}
            else:
                locton = {'TÝ':'LY.Lộc Tồn',
                'SỬU':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'DẦN':'LY.Thanh Long',
                'MÃO':'LY.Tiểu Hao',
                'THÌN':'LY.Tướng Quân',
                'TỴ':'LY.Tấu Thư, LY.Đường Phù',
                'NGỌ':'LY.Phi Liêm',
                'MÙI':'LY.Hỉ Thần',
                'THÂN':'LY.Bệnh Phù, LY.Quốc Ấn',
                'DẬU':'LY.Đại Hao',
                'TUẤT':'LY.Phục Binh',
                'HỢI':'LY.Quan Phủ, LY.Đà La(H)'}

    else:
        if chi_nam in chi_am:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'LY.Lộc Tồn',
                'MÃO':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'THÌN':'LY.Thanh Long',
                'TỴ':'LY.Tiểu Hao',
                'NGỌ':'LY.Tướng Quân',
                'MÙI':'LY.Tấu Thư, LY.Đường Phù',
                'THÂN':'LY.Phi Liêm',
                'DẬU':'LY.Hỉ Thần',
                'TUẤT':'LY.Bệnh Phù, LY.Quốc Ấn',
                'HỢI':'LY.Đại Hao',
                'TÝ':'LY.Phục Binh',
                'SỬU':'LY.Quan Phủ, LY.Đà La(Đ)'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'LY.Lộc Tồn',
                'THÌN':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'TỴ':'LY.Thanh Long',
                'NGỌ':'LY.Tiểu Hao',
                'MÙI':'LY.Tướng Quân',
                'THÂN':'LY.Tấu Thư, LY.Đường Phù',
                'DẬU':'LY.Phi Liêm',
                'TUẤT':'LY.Hỉ Thần',
                'HỢI':'LY.Bệnh Phù, LY.Quốc Ấn',
                'TÝ':'LY.Đại Hao',
                'SỬU':'LY.Phục Binh',
                'DẦN':'LY.Quan Phủ, LY.Đà La(H)'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'LY.Lộc Tồn',
                'NGỌ':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'MÙI':'LY.Thanh Long',
                'THÂN':'LY.Tiểu Hao',
                'DẬU':'LY.Tướng Quân',
                'TUẤT':'LY.Tấu Thư, LY.Đường Phù',
                'HỢI':'LY.Phi Liêm',
                'TÝ':'LY.Hỉ Thần',
                'SỬU':'LY.Bệnh Phù, LY.Quốc Ấn',
                'DẦN':'LY.Đại Hao',
                'MÃO':'LY.Phục Binh',
                'THÌN':'LY.Quan Phủ, LY.Đà La(Đ)'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'LY.Lộc Tồn',
                'MÙI':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'THÂN':'LY.Thanh Long',
                'DẬU':'LY.Tiểu Hao',
                'TUẤT':'LY.Tướng Quân',
                'HỢI':'LY.Tấu Thư, LY.Đường Phù',
                'TÝ':'LY.Phi Liêm',
                'SỬU':'LY.Hỉ Thần',
                'DẦN':'LY.Bệnh Phù, LY.Quốc Ấn',
                'MÃO':'LY.Đại Hao',
                'THÌN':'LY.Phục Binh',
                'TỴ':'LY.Quan Phủ, LY.Đà La(H)'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'LY.Lộc Tồn',
                'DẬU':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'TUẤT':'LY.Thanh Long',
                'HỢI':'LY.Tiểu Hao',
                'TÝ':'LY.Tướng Quân',
                'SỬU':'LY.Tấu Thư, LY.Đường Phù',
                'DẦN':'LY.Phi Liêm',
                'MÃO':'LY.Hỉ Thần',
                'THÌN':'LY.Bệnh Phù, LY.Quốc Ấn',
                'TỴ':'LY.Đại Hao',
                'NGỌ':'LY.Phục Binh',
                'MÙI':'LY.Quan Phủ, LY.Đà La(Đ)'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'LY.Lộc Tồn',
                'TUẤT':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'HỢI':'LY.Thanh Long',
                'TÝ':'LY.Tiểu Hao',
                'SỬU':'LY.Tướng Quân',
                'DẦN':'LY.Tấu Thư, LY.Đường Phù',
                'MÃO':'LY.Phi Liêm',
                'THÌN':'LY.Hỉ Thần',
                'TỴ':'LY.Bệnh Phù, LY.Quốc Ấn',
                'NGỌ':'LY.Đại Hao',
                'MÙI':'LY.Phục Binh',
                'THÂN':'LY.Quan Phủ, LY.Đà La(H)'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'LY.Lộc Tồn',
                'TÝ':'LY.Lực Sĩ, LY.Kình Dương(H)',
                'SỬU':'LY.Thanh Long',
                'DẦN':'LY.Tiểu Hao',
                'MÃO':'LY.Tướng Quân',
                'THÌN':'LY.Tấu Thư, LY.Đường Phù',
                'TỴ':'LY.Phi Liêm',
                'NGỌ':'LY.Hỉ Thần',
                'MÙI':'LY.Bệnh Phù, LY.Quốc Ấn',
                'THÂN':'LY.Đại Hao',
                'DẬU':'LY.Phục Binh',
                'TUẤT':'LY.Quan Phủ, LY.Đà La(Đ)'}
            else:
                locton = {'TÝ':'LY.Lộc Tồn',
                'SỬU':'LY.Lực Sĩ, LY.Kình Dương(Đ)',
                'DẦN':'LY.Thanh Long',
                'MÃO':'LY.Tiểu Hao',
                'THÌN':'LY.Tướng Quân',
                'TỴ':'LY.Tấu Thư, LY.Đường Phù',
                'NGỌ':'LY.Phi Liêm',
                'MÙI':'LY.Hỉ Thần',
                'THÂN':'LY.Bệnh Phù, LY.Quốc Ấn',
                'DẬU':'LY.Đại Hao',
                'TUẤT':'LY.Phục Binh',
                'HỢI':'LY.Quan Phủ, LY.Đà La(H)'}

        else:
            if can_nam == 'GIÁP':
                locton = {'DẦN':'LY.Lộc Tồn',
                'SỬU':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'TÝ':'LY.Thanh Long',
                'HỢI':'LY.Tiểu Hao',
                'TUẤT':'LY.Tướng Quân, LY.Quốc Ấn',
                'DẬU':'LY.Tấu Thư',
                'THÂN':'LY.Phi Liêm',
                'MÙI':'LY.Hỉ Thần, LY.Đường Phù',
                'NGỌ':'LY.Bệnh Phù',
                'TỴ':'LY.Đại Hao',
                'THÌN':'LY.Phục Binh',
                'MÃO':'LY.Quan Phủ, LY.Kình Dương(H)'}
            elif can_nam == 'ẤT':
                locton = {'MÃO':'LY.Lộc Tồn',
                'DẦN':'LY.Lực Sĩ, LY.Đà La(H)',
                'SỬU':'LY.Thanh Long',
                'TÝ':'LY.Tiểu Hao',
                'HỢI':'LY.Tướng Quân, LY.Quốc Ấn',
                'TUẤT':'LY.Tấu Thư',
                'DẬU':'LY.Phi Liêm',
                'THÂN':'LY.Hỉ Thần, LY.Đường Phù',
                'MÙI':'LY.Bệnh Phù',
                'NGỌ':'LY.Đại Hao',
                'TỴ':'LY.Phục Binh',
                'THÌN':'LY.Quan Phủ, LY.Kình Dương(Đ)'}
            elif can_nam == 'BÍNH' or can_nam == 'MẬU':
                locton = {'TỴ':'LY.Lộc Tồn',
                'THÌN':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'MÃO':'LY.Thanh Long',
                'DẦN':'LY.Tiểu Hao',
                'SỬU':'LY.Tướng Quân, LY.Quốc Ấn',
                'TÝ':'LY.Tấu Thư',
                'HỢI':'LY.Phi Liêm',
                'TUẤT':'LY.Hỉ Thần, LY.Đường Phù',
                'DẬU':'LY.Bệnh Phù',
                'THÂN':'LY.Đại Hao',
                'MÙI':'LY.Phục Binh',
                'NGỌ':'LY.Quan Phủ, LY.Kình Dương(H)'}
            elif can_nam == 'ĐINH' or can_nam == 'KỶ':
                locton = {'NGỌ':'LY.Lộc Tồn',
                'TỴ':'LY.Lực Sĩ, LY.Đà La(H)',
                'THÌN':'LY.Thanh Long',
                'MÃO':'LY.Tiểu Hao',
                'DẦN':'LY.Tướng Quân, LY.Quốc Ấn',
                'SỬU':'LY.Tấu Thư',
                'TÝ':'LY.Phi Liêm',
                'HỢI':'LY.Hỉ Thần, LY.Đường Phù',
                'TUẤT':'LY.Bệnh Phù',
                'DẬU':'LY.Đại Hao',
                'THÂN':'LY.Phục Binh',
                'MÙI':'LY.Quan Phủ, LY.Kình Dương(Đ)'}
            elif can_nam == 'CANH':
                locton = {'THÂN':'LY.Lộc Tồn',
                'MÙI':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'NGỌ':'LY.Thanh Long',
                'TỴ':'LY.Tiểu Hao',
                'THÌN':'LY.Tướng Quân, LY.Quốc Ấn',
                'MÃO':'LY.Tấu Thư',
                'DẦN':'LY.Phi Liêm',
                'SỬU':'LY.Hỉ Thần, LY.Đường Phù',
                'TÝ':'LY.Bệnh Phù',
                'HỢI':'LY.Đại Hao',
                'TUẤT':'LY.Phục Binh',
                'DẬU':'LY.Quan Phủ, LY.Kình Dương(H)'}
            elif can_nam == 'TÂN':
                locton = {'DẬU':'LY.Lộc Tồn',
                'THÂN':'LY.Lực Sĩ, LY.Đà La(H)',
                'MÙI':'LY.Thanh Long',
                'NGỌ':'LY.Tiểu Hao',
                'TỴ':'LY.Tướng Quân, LY.Quốc Ấn',
                'THÌN':'LY.Tấu Thư',
                'MÃO':'LY.Phi Liêm',
                'DẦN':'LY.Hỉ Thần, LY.Đường Phù',
                'SỬU':'LY.Bệnh Phù',
                'TÝ':'LY.Đại Hao',
                'HỢI':'LY.Phục Binh',
                'TUẤT':'LY.Quan Phủ, LY.Kình Dương(Đ)'}
            elif can_nam == 'NHÂM':
                locton = {'HỢI':'LY.Lộc Tồn',
                'TUẤT':'LY.Lực Sĩ, LY.Đà La(Đ)',
                'DẬU':'LY.Thanh Long',
                'THÂN':'LY.Tiểu Hao',
                'MÙI':'LY.Tướng Quân, LY.Quốc Ấn',
                'NGỌ':'LY.Tấu Thư',
                'TỴ':'LY.Phi Liêm',
                'THÌN':'LY.Hỉ Thần, LY.Đường Phù',
                'MÃO':'LY.Bệnh Phù',
                'DẦN':'LY.Đại Hao',
                'SỬU':'LY.Phục Binh',
                'TÝ':'LY.Quan Phủ, LY.Kình Dương(H)'}
            else:
                locton = {'TÝ':'LY.Lộc Tồn',
                'HỢI':'LY.Lực Sĩ, LY.Đà La(H)',
                'TUẤT':'LY.Thanh Long',
                'DẬU':'LY.Tiểu Hao',
                'THÂN':'LY.Tướng Quân, LY.Quốc Ấn',
                'MÙI':'LY.Tấu Thư',
                'NGỌ':'LY.Phi Liêm',
                'TỴ':'LY.Hỉ Thần, LY.Đường Phù',
                'THÌN':'LY.Bệnh Phù',
                'MÃO':'LY.Đại Hao',
                'DẦN':'LY.Phục Binh',
                'SỬU':'LY.Quan Phủ, LY.Kình Dương(Đ)'}

    return locton

def ansaoluutheothang(thang_am):
    dic_theothang={}
    taphu=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
    huubat=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
    thienhinh=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
    thienrieu=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
    thiengiai=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
    diagiai=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
    key_taphu = taphu[thang_am-1]
    dic_taphu = {}
    key_huubat = huubat[thang_am-1]
    dic_huubat = {}
    key_thienhinh = thienhinh[thang_am-1]
    dic_thienhinh = {}
    key_thienrieu = thienrieu[thang_am-1]
    dic_thienrieu = {}
    key_thiengiai = thiengiai[thang_am-1]
    dic_thiengiai = {}
    key_diagiai = diagiai[thang_am-1]
    dic_diagiai = {}
    if key_taphu == 'TÝ':
        dic_taphu ={'TÝ':'LM.Tả Phù'
        }
    elif key_taphu == 'SỬU':
        dic_taphu ={'SỬU':'LM.Tả Phù'
        }
    elif key_taphu == 'DẦN':
        dic_taphu ={'DẦN':'LM.Tả Phù'
        }
    elif key_taphu == 'MÃO':
        dic_taphu ={'MÃO':'LM.Tả Phù'
        }
    elif key_taphu == 'THÌN':
        dic_taphu ={'THÌN':'LM.Tả Phù'
        }
    elif key_taphu == 'TỴ':
        dic_taphu ={'TỴ':'LM.Tả Phù'
        }
    elif key_taphu == 'NGỌ':
        dic_taphu ={'NGỌ':'LM.Tả Phù'
        }
    elif key_taphu == 'MÙI':
        dic_taphu ={'MÙI':'LM.Tả Phù'
        }
    elif key_taphu == 'THÂN':
        dic_taphu ={'THÂN':'LM.Tả Phù'
        }
    elif key_taphu == 'DẬU':
        dic_taphu ={'DẬU XẤU':'LM.Tả Phù'
        }
    elif key_taphu == 'TUẤT':
        dic_taphu ={'TUẤT':'LM.Tả Phù'
        }
    else:
        dic_taphu ={'HỢI':'LM.Tả Phù'
        }

    if key_huubat == 'TÝ':
        dic_huubat ={'TÝ':'LM.Hữu Bật'
        }
    elif key_huubat == 'SỬU':
        dic_huubat ={'SỬU':'LM.Hữu Bật'
        }
    elif key_huubat == 'DẦN':
        dic_huubat ={'DẦN':'LM.Hữu Bật'
        }
    elif key_huubat == 'MÃO':
        dic_huubat ={'MÃO':'LM.Hữu Bật'
        }
    elif key_huubat == 'THÌN':
        dic_huubat ={'THÌN':'LM.Hữu Bật'
        }
    elif key_huubat == 'TỴ':
        dic_huubat ={'TỴ':'LM.Hữu Bật'
        }
    elif key_huubat == 'NGỌ':
        dic_huubat ={'NGỌ':'LM.Hữu Bật'
        }
    elif key_huubat == 'MÙI':
        dic_huubat ={'MÙI':'LM.Hữu Bật'
        }
    elif key_huubat == 'THÂN':
        dic_huubat ={'THÂN':'LM.Hữu Bật'
        }
    elif key_huubat == 'DẬU':
        dic_huubat ={'DẬU XẤU':'LM.Hữu Bật'
        }
    elif key_huubat == 'TUẤT':
        dic_huubat ={'TUẤT':'LM.Hữu Bật'
        }
    else:
        dic_huubat ={'HỢI':'LM.Hữu Bật'
        }

    if key_thienhinh == 'TÝ':
        dic_thienhinh ={'TÝ':'LM.Thiên Hình(H)'
        }
    elif key_thienhinh == 'SỬU':
        dic_thienhinh ={'SỬU':'LM.Thiên Hình(H)'
        }
    elif key_thienhinh == 'DẦN':
        dic_thienhinh ={'DẦN':'LM.Thiên Hình(Đ)'
        }
    elif key_thienhinh == 'MÃO':
        dic_thienhinh ={'MÃO':'LM.Thiên Hình(Đ)'
        }
    elif key_thienhinh == 'THÌN':
        dic_thienhinh ={'THÌN':'LM.Thiên Hình(H)'
        }
    elif key_thienhinh == 'TỴ':
        dic_thienhinh ={'TỴ':'LM.Thiên Hình(H)'
        }
    elif key_thienhinh == 'NGỌ':
        dic_thienhinh ={'NGỌ':'LM.Thiên Hình(H)'
        }
    elif key_thienhinh == 'MÙI':
        dic_thienhinh ={'MÙI':'LM.Thiên Hình(H)'
        }
    elif key_thienhinh == 'THÂN':
        dic_thienhinh ={'THÂN':'LM.Thiên Hình(Đ)'
        }
    elif key_thienhinh == 'DẬU':
        dic_thienhinh ={'DẬU XẤU':'LM.Thiên Hình(Đ)'
        }
    elif key_thienhinh == 'TUẤT':
        dic_thienhinh ={'TUẤT':'LM.Thiên Hình(H)'
        }
    else:
        dic_thienhinh ={'HỢI':'LM.Thiên Hình(H)'
        }

    if key_thienrieu == 'TÝ':
        dic_thienrieu ={'TÝ':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'SỬU':
        dic_thienrieu ={'SỬU':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'DẦN':
        dic_thienrieu ={'DẦN':'LM.Thiên Riêu(Đ),LM.Thiên Y'
        }
    elif key_thienrieu == 'MÃO':
        dic_thienrieu ={'MÃO':'LM.Thiên Riêu(Đ),LM.Thiên Y'
        }
    elif key_thienrieu == 'THÌN':
        dic_thienrieu ={'THÌN':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'TỴ':
        dic_thienrieu ={'TỴ':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'NGỌ':
        dic_thienrieu ={'NGỌ':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'MÙI':
        dic_thienrieu ={'MÙI':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'THÂN':
        dic_thienrieu ={'THÂN':'LM.Thiên Riêu(H), LM.Thiên Y'
        }
    elif key_thienrieu == 'DẬU':
        dic_thienrieu ={'DẬU':'LM.Thiên Riêu(Đ),LM.Thiên Y'
        }
    elif key_thienrieu == 'TUẤT':
        dic_thienrieu ={'TUẤT':'LM.Thiên Riêu(Đ),LM.Thiên Y'
        }
    else:
        dic_thienrieu ={'HỢI':'LM.Thiên Riêu(H), LM.Thiên Y'
        }

    if key_thiengiai == 'TÝ':
        dic_thiengiai ={'TÝ':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'SỬU':
        dic_thiengiai ={'SỬU':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'DẦN':
        dic_thiengiai ={'DẦN':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'MÃO':
        dic_thiengiai ={'MÃO':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'THÌN':
        dic_thiengiai ={'THÌN':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'TỴ':
        dic_thiengiai ={'TỴ':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'NGỌ':
        dic_thiengiai ={'NGỌ':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'MÙI':
        dic_thiengiai ={'MÙI':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'THÂN':
        dic_thiengiai ={'THÂN':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'DẬU':
        dic_thiengiai ={'DẬU XẤU':'LM.Thiên Giải'
        }
    elif key_thiengiai == 'TUẤT':
        dic_thiengiai ={'TUẤT':'LM.Thiên Giải'
        }
    else:
        dic_thiengiai ={'HỢI':'LM.Thiên Giải'
        }

    if key_diagiai == 'TÝ':
        dic_diagiai ={'TÝ':'LM.Địa Giải'
        }
    elif key_diagiai == 'SỬU':
        dic_diagiai ={'SỬU':'LM.Địa Giải'
        }
    elif key_diagiai == 'DẦN':
        dic_diagiai ={'DẦN':'LM.Địa Giải'
        }
    elif key_diagiai == 'MÃO':
        dic_diagiai ={'MÃO':'LM.Địa Giải'
        }
    elif key_diagiai == 'THÌN':
        dic_diagiai ={'THÌN':'LM.Địa Giải'
        }
    elif key_diagiai == 'TỴ':
        dic_diagiai ={'TỴ':'LM.Địa Giải'
        }
    elif key_diagiai == 'NGỌ':
        dic_diagiai ={'NGỌ':'LM.Địa Giải'
        }
    elif key_diagiai == 'MÙI':
        dic_diagiai ={'MÙI':'LM.Địa Giải'
        }
    elif key_diagiai == 'THÂN':
        dic_diagiai ={'THÂN':'LM.Địa Giải'
        }
    elif key_diagiai == 'DẬU':
        dic_diagiai ={'DẬU XẤU':'LM.Địa Giải'
        }
    elif key_diagiai == 'TUẤT':
        dic_diagiai ={'TUẤT':'LM.Địa Giải'
        }
    else:
        dic_diagiai ={'HỢI':'LM.Địa Giải'
        }

    dic_theothang = {**dic_taphu,**dic_huubat,**dic_thienhinh,**dic_thienrieu,**dic_thiengiai,**dic_diagiai}
    taphu_huubat = custom_merge_luunien(dic_taphu,dic_huubat)
    thienhinh_thienrieu = custom_merge_luunien(dic_thienhinh,dic_thienrieu)
    thiengiai_diagiai = custom_merge_luunien(dic_thiengiai,dic_diagiai)
    dic_thang = custom_merge_luunien(taphu_huubat,thienhinh_thienrieu)
    dic_theothang = custom_merge_luunien(dic_thang,thiengiai_diagiai)
    return dic_theothang

def ansaoluutheongay(thang_am,ngay_am):
    taphu=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
    huubat=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
    key_taphu = taphu[thang_am-1]
    dic_tamthai = {}
    dic_battoa = {}
    key_huubat = huubat[thang_am-1]
    dic_huubat = {}
    if ngay_am > 12:
        ngay_am = ngay_am%12

    if key_taphu == 'TÝ':
        tamthai=('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'SỬU':
        tamthai=('SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'DẦN':
        tamthai=('DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'MÃO':
        tamthai=('MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'THÌN':
        tamthai=('THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'TỴ':
        tamthai=('TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'NGỌ':
        tamthai=('NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'MÙI':
        tamthai=('MÙI','THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'THÂN':
        tamthai=('THÂN','DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'DẬU':
        tamthai=('DẬU','TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    elif key_taphu == 'TUẤT':
        tamthai=('TUẤT','HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }
    else:
        tamthai=('HỢI','TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT')
        key_tamthai = tamthai[ngay_am-1]
        if key_tamthai == 'TÝ':
            dic_tamthai ={'TÝ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'SỬU':
            dic_tamthai ={'SỬU':'LĐ.Tam Thai'
        }
        elif key_tamthai == 'DẦN':
            dic_tamthai ={'DẦN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÃO':
            dic_tamthai ={'MÃO':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÌN':
            dic_tamthai ={'THÌN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TỴ':
            dic_tamthai ={'TỴ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'NGỌ':
            dic_tamthai ={'NGỌ':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'MÙI':
            dic_tamthai ={'MÙI':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'THÂN':
            dic_tamthai ={'THÂN':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'DẬU':
            dic_tamthai ={'DẬU':'LĐ.Tam Thai'
            }
        elif key_tamthai == 'TUẤT':
            dic_tamthai ={'TUẤT':'LĐ.Tam Thai'
            }
        else:
            dic_tamthai ={'HỢI':'LĐ.Tam Thai'
            }


    if key_huubat == 'TÝ':
        battoa=('TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'SỬU':
        battoa=('SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'DẦN':
        battoa=('DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'MÃO':
        battoa=('MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'THÌN':
        battoa=('THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'TỴ':
        battoa=('TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'NGỌ':
        battoa=('NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN','MÙI')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'MÙI':
        battoa=('MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU','THÂN')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'THÂN':
        battoa=('THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT','DẬU')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'DẬU':
        battoa=('DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI','TUẤT')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    elif key_huubat == 'TUẤT':
        battoa=('TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ','HỢI')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }
    else:
        battoa=('HỢI','TUẤT','DẬU','THÂN','MÙI','NGỌ','TỴ','THÌN','MÃO','DẦN','SỬU','TÝ')
        key_battoa = battoa[ngay_am-1]
        if key_battoa == 'TÝ':
            dic_battoa ={'TÝ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'SỬU':
            dic_battoa ={'SỬU':'LĐ.Bát Tọa'
        }
        elif key_battoa == 'DẦN':
            dic_battoa ={'DẦN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÃO':
            dic_battoa ={'MÃO':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÌN':
            dic_battoa ={'THÌN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TỴ':
            dic_battoa ={'TỴ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'NGỌ':
            dic_battoa ={'NGỌ':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'MÙI':
            dic_battoa ={'MÙI':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'THÂN':
            dic_battoa ={'THÂN':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'DẬU':
            dic_battoa ={'DẬU':'LĐ.Bát Tọa'
            }
        elif key_battoa == 'TUẤT':
            dic_battoa ={'TUẤT':'LĐ.Bát Tọa'
            }
        else:
            dic_battoa ={'HỢI':'LĐ.Bát Tọa'
            }


    merge = custom_merge_luunien(dic_tamthai,dic_battoa)

    return merge

def ansaoluunien(can_nam,chi_nam,option,thang_am,ngay_am):
    dic_ansaoluunien = {}
    luuniennam = luuvonglocton(can_nam,chi_nam,option)
    luuthang = ansaoluutheothang(thang_am)
    luutheongay = ansaoluutheongay(thang_am,ngay_am)
    print("luutheongay : ",luutheongay)
    luuniennamthang = custom_merge_luunien(luuniennam,luuthang)
    dic_ansaoluunien =  custom_merge_luunien(luuniennamthang,luutheongay)
    return dic_ansaoluunien
