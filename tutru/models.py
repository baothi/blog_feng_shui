from django.db import models
from django.db.models import Model
from blog_feng_shui.AmLich import *
import datetime

# Create your models here.
chi_duong = ('TÝ','DẦN','THÌN','NGỌ','THÂN','TUẤT')
chi_am = ('SỬU','MÃO','TỴ','MÙI','DẬU','HỢI')
dia_chi = ('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
thien_can = ('GIÁP','ẤT','BÍNH','ĐINH','MẬU','KỶ','CANH','TÂN','NHÂM','QUÝ')
chi_cungmenh = {'TÝ': 11,'SỬU': 12,'DẦN': 1,'MÃO': 2,'THÌN': 3,'TỴ': 4,'NGỌ': 5,'MÙI': 6,'THÂN': 7,'DẬU': 8,'TUẤT': 9,'HỢI': 10}
class LichTietKhi(models.Model):
    tietkhi = models.CharField(max_length=255)
    daytiekhi = models.CharField(max_length=255)
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)

    def __str__(self):
        return self.tietkhi

def thapthan(can_ngay,can_thapthan):
    if can_ngay == 'GIÁP':
        if can_thapthan == 'GIÁP':
            can_thap = 'T Kiên'
        elif can_thapthan == 'ẤT':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'BÍNH':
            can_thap = 'T Thần'
        elif can_thapthan == 'ĐINH':
            can_thap = 'T Quan'
        elif can_thapthan == 'MẬU':
            can_thap = 'T Tài'
        elif can_thapthan == 'KỶ':
            can_thap = 'C Tài'
        elif can_thapthan == 'CANH':
            can_thap = 'Thất sát'
        elif can_thapthan == 'TÂN':
            can_thap = 'C Quan'
        elif can_thapthan == 'NHÂM':
            can_thap = 'Kiêu'
        else:
            can_thap = 'C Ấn'
    elif can_ngay == 'ẤT':
        if can_thapthan == 'GIÁP':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'ẤT':
            can_thap = 'T Kiên'
        elif can_thapthan == 'BÍNH':
            can_thap = 'T Quan'
        elif can_thapthan == 'ĐINH':
            can_thap = 'T Thần'
        elif can_thapthan == 'MẬU':
            can_thap = 'C Tài'
        elif can_thapthan == 'KỶ':
            can_thap = 'T Tài'
        elif can_thapthan == 'CANH':
            can_thap = 'C Quan'
        elif can_thapthan == 'TÂN':
            can_thap = 'Thất sát'
        elif can_thapthan == 'NHÂM':
            can_thap = 'C Ấn'
        else:
            can_thap = 'Kiêu'
    elif can_ngay == 'BÍNH':
        if can_thapthan == 'GIÁP':
            can_thap = 'Kiêu'
        elif can_thapthan == 'ẤT':
            can_thap = 'C Ấn'
        elif can_thapthan == 'BÍNH':
            can_thap = 'T Kiên'
        elif can_thapthan == 'ĐINH':
            can_thap = 'K Tài'
        elif can_thapthan == 'MẬU':
            can_thap = 'T Thần'
        elif can_thapthan == 'KỶ':
            can_thap = 'T Quan'
        elif can_thapthan == 'CANH':
            can_thap = 'T Tài'
        elif can_thapthan == 'TÂN':
            can_thap = 'C Tài'
        elif can_thapthan == 'NHÂM':
            can_thap = 'Thất sát'
        else:
            can_thap = 'C Quan'
    elif can_ngay == 'ĐINH':
        if can_thapthan == 'GIÁP':
            can_thap = 'C Ấn'
        elif can_thapthan == 'ẤT':
            can_thap = 'Kiêu'
        elif can_thapthan == 'BÍNH':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'ĐINH':
            can_thap = 'T Kiên'
        elif can_thapthan == 'MẬU':
            can_thap = 'T Quan'
        elif can_thapthan == 'KỶ':
            can_thap = 'T Thần'
        elif can_thapthan == 'CANH':
            can_thap = 'C Tài'
        elif can_thapthan == 'TÂN':
            can_thap = 'T Tài'
        elif can_thapthan == 'NHÂM':
            can_thap = 'C Quan'
        else:
            can_thap = 'Thất sát'
    elif can_ngay == 'MẬU':
        if can_thapthan == 'GIÁP':
            can_thap = 'Thất sát'
        elif can_thapthan == 'ẤT':
            can_thap = 'C Quan'
        elif can_thapthan == 'BÍNH':
            can_thap = 'Kiêu'
        elif can_thapthan == 'ĐINH':
            can_thap = 'C Ấn'
        elif can_thapthan == 'MẬU':
            can_thap = 'T Kiên'
        elif can_thapthan == 'KỶ':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'CANH':
            can_thap = 'T Thần'
        elif can_thapthan == 'TÂN':
            can_thap = 'T Quan'
        elif can_thapthan == 'NHÂM':
            can_thap = 'T Tài'
        else:
            can_thap = 'C Tài'
    elif can_ngay == 'KỶ':
        if can_thapthan == 'GIÁP':
            can_thap = 'C Quan'
        elif can_thapthan == 'ẤT':
            can_thap = 'Thất sát'
        elif can_thapthan == 'BÍNH':
            can_thap = 'C Ấn'
        elif can_thapthan == 'ĐINH':
            can_thap = 'Kiêu'
        elif can_thapthan == 'MẬU':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'KỶ':
            can_thap = 'T Kiên'
        elif can_thapthan == 'CANH':
            can_thap = 'T Quan'
        elif can_thapthan == 'TÂN':
            can_thap = 'T Thần'
        elif can_thapthan == 'NHÂM':
            can_thap = 'C Tài'
        else:
            can_thap = 'T Tài'
    elif can_ngay == 'CANH':
        if can_thapthan == 'GIÁP':
            can_thap = 'T Tài'
        elif can_thapthan == 'ẤT':
            can_thap = 'C Tài'
        elif can_thapthan == 'BÍNH':
            can_thap = 'Thất sát'
        elif can_thapthan == 'ĐINH':
            can_thap = 'C Quan'
        elif can_thapthan == 'MẬU':
            can_thap = 'Kiêu'
        elif can_thapthan == 'KỶ':
            can_thap = 'C Ấn'
        elif can_thapthan == 'CANH':
            can_thap = 'T Kiên'
        elif can_thapthan == 'TÂN':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'NHÂM':
            can_thap = 'T Thần'
        else:
            can_thap = 'T Quan'
    elif can_ngay == 'TÂN':
        if can_thapthan == 'GIÁP':
            can_thap = 'C Tài'
        elif can_thapthan == 'ẤT':
            can_thap = 'T Tài'
        elif can_thapthan == 'BÍNH':
            can_thap = 'C Quan'
        elif can_thapthan == 'ĐINH':
            can_thap = 'Thất sát'
        elif can_thapthan == 'MẬU':
            can_thap = 'C Ấn'
        elif can_thapthan == 'KỶ':
            can_thap = 'Kiêu'
        elif can_thapthan == 'CANH':
            can_thap = 'Kiếp Tài'
        elif can_thapthan == 'TÂN':
            can_thap = 'T Kiên'
        elif can_thapthan == 'NHÂM':
            can_thap = 'T Quan'
        else:
            can_thap = 'T Thần'
    elif can_ngay == 'NHÂM':
        if can_thapthan == 'GIÁP':
            can_thap = 'T Thần'
        elif can_thapthan == 'ẤT':
            can_thap = 'T Quan'
        elif can_thapthan == 'BÍNH':
            can_thap = 'T Tài'
        elif can_thapthan == 'ĐINH':
            can_thap = 'C Tài'
        elif can_thapthan == 'MẬU':
            can_thap = 'Thất sát'
        elif can_thapthan == 'KỶ':
            can_thap = 'C Quan'
        elif can_thapthan == 'CANH':
            can_thap = 'Kiêu'
        elif can_thapthan == 'TÂN':
            can_thap = 'C Ấn'
        elif can_thapthan == 'NHÂM':
            can_thap = 'T Kiên'
        else:
            can_thap = 'Kiếp Tài'
    else:
        if can_thapthan == 'GIÁP':
            can_thap = 'T Quan'
        elif can_thapthan == 'ẤT':
            can_thap = 'T Thần'
        elif can_thapthan == 'BÍNH':
            can_thap = 'C Tài'
        elif can_thapthan == 'ĐINH':
            can_thap = 'T Tài'
        elif can_thapthan == 'MẬU':
            can_thap = 'C Quan'
        elif can_thapthan == 'KỶ':
            can_thap = 'Thất sát'
        elif can_thapthan == 'CANH':
            can_thap = 'C Ấn'
        elif can_thapthan == 'TÂN':
            can_thap = 'Kiêu'
        elif can_thapthan == 'NHÂM':
            can_thap = 'Kiếp Tài'
        else:
            can_thap = 'T Kiên'
    return can_thap

def tangcang(chi):
    mydict = {}
    can_an = []
    if chi == 'TÝ':
        can = 'QUÝ'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'SỬU':
        can = 'KỶ'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'QUÝ'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'TÂN'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'DẦN':
        can = 'GIÁP'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'MẬU'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'BÍNH'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'MÃO':
        can = 'ẤT'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'THÌN':
        can = 'MẬU'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'ẤT'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'QUÝ'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'TỴ':
        can = 'BÍNH'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'MẬU'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'CANH'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'NGỌ':
        can = 'ĐINH'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'KỶ'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'MÙI':
        can = 'KỶ'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'ĐINH'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'ẤT'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'THÂN':
        can = 'CANH'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'MẬU'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'NHÂM'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'DẬU':
        can = 'TÂN'
        color_can = color_canchi(can)
        mydict[color_can] = can
    elif chi == 'TUẤT':
        can = 'MẬU'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'TÂN'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'ĐINH'
        color_can = color_canchi(can)
        mydict[color_can] = can
    else:
        can = 'NHÂM'
        color_can = color_canchi(can)
        mydict[color_can] = can
        can = 'GIÁP'
        color_can = color_canchi(can)
        mydict[color_can] = can
    return mydict

def truongsinh(can,chi):
    if chi == 'TÝ':
        if can == 'GIÁP':
            TSinh = 'M Dục'
        elif can == 'ẤT':
            TSinh = 'Bệnh'
        elif can == 'BÍNH':
            TSinh = 'Thai'
        elif can == 'ĐINH':
            TSinh = 'Bệnh'
        elif can == 'MẬU':
            TSinh = 'Thai'
        elif can == 'KỶ':
            TSinh = 'Tuyệt'
        elif can == 'CANH':
            TSinh = 'Tử'
        elif can == 'TÂN':
            TSinh = 'T Sinh'
        elif can == 'NHÂM':
            TSinh = 'Đ Vượng'
        else:
            TSinh = 'L Quan'
    elif chi == 'SỬU':
        if can == 'GIÁP':
            TSinh = 'Q Đới'
        elif can == 'ẤT':
            TSinh = 'Suy'
        elif can == 'BÍNH':
            TSinh = 'Dưỡng'
        elif can == 'ĐINH':
            TSinh = 'Mộ'
        elif can == 'MẬU':
            TSinh = 'Dưỡng'
        elif can == 'KỶ':
            TSinh = 'Mộ'
        elif can == 'CANH':
            TSinh = 'Mộ'
        elif can == 'TÂN':
            TSinh = 'Dưỡng'
        elif can == 'NHÂM':
            TSinh = 'Suy'
        else:
            TSinh = 'Q Đới'
    elif chi == 'DẦN':
        if can == 'GIÁP':
            TSinh = 'L Quan'
        elif can == 'ẤT':
            TSinh = 'Đ Vượng'
        elif can == 'BÍNH':
            TSinh = 'T Sinh'
        elif can == 'ĐINH':
            TSinh = 'Tử'
        elif can == 'MẬU':
            TSinh = 'T Sinh'
        elif can == 'KỶ':
            TSinh = 'Tử'
        elif can == 'CANH':
            TSinh = 'Tuyệt'
        elif can == 'TÂN':
            TSinh = 'Thai'
        elif can == 'NHÂM':
            TSinh = 'Bệnh'
        else:
            TSinh = 'M Dục'
    elif chi == 'MÃO':
        if can == 'GIÁP':
            TSinh = 'Đ Vượng'
        elif can == 'ẤT':
            TSinh = 'L Quan'
        elif can == 'BÍNH':
            TSinh = 'M Dục'
        elif can == 'ĐINH':
            TSinh = 'Bệnh'
        elif can == 'MẬU':
            TSinh = 'M Dục'
        elif can == 'KỶ':
            TSinh = 'Bệnh'
        elif can == 'CANH':
            TSinh = 'Thai'
        elif can == 'TÂN':
            TSinh = 'Tuyệt'
        elif can == 'NHÂM':
            TSinh = 'Tử'
        else:
            TSinh = 'T Sinh'
    elif chi == 'THÌN':
        if can == 'GIÁP':
            TSinh = 'Suy'
        elif can == 'ẤT':
            TSinh = 'Q Đới'
        elif can == 'BÍNH':
            TSinh = 'Q Đới'
        elif can == 'ĐINH':
            TSinh = 'Suy'
        elif can == 'MẬU':
            TSinh = 'Q Đới'
        elif can == 'KỶ':
            TSinh = 'Suy'
        elif can == 'CANH':
            TSinh = 'Dưỡng'
        elif can == 'TÂN':
            TSinh = 'Mộ'
        elif can == 'NHÂM':
            TSinh = 'Mộ'
        else:
            TSinh = 'Dưỡng'
    elif chi == 'TỴ':
        if can == 'GIÁP':
            TSinh = 'Bệnh'
        elif can == 'ẤT':
            TSinh = 'M Dục'
        elif can == 'BÍNH':
            TSinh = 'L Quan'
        elif can == 'ĐINH':
            TSinh = 'Đ Vượng'
        elif can == 'MẬU':
            TSinh = 'L Quan'
        elif can == 'KỶ':
            TSinh = 'Đ Vượng'
        elif can == 'CANH':
            TSinh = 'T Sinh'
        elif can == 'TÂN':
            TSinh = 'Tử'
        elif can == 'NHÂM':
            TSinh = 'Tuyệt'
        else:
            TSinh = 'Thai'
    elif chi == 'NGỌ':
        if can == 'GIÁP':
            TSinh = 'Tử'
        elif can == 'ẤT':
            TSinh = 'T Sinh'
        elif can == 'BÍNH':
            TSinh = 'Đ Vượng'
        elif can == 'ĐINH':
            TSinh = 'L Quan'
        elif can == 'MẬU':
            TSinh = 'Đ Vượng'
        elif can == 'KỶ':
            TSinh = 'L Quan'
        elif can == 'CANH':
            TSinh = 'M Dục'
        elif can == 'TÂN':
            TSinh = 'Bệnh'
        elif can == 'NHÂM':
            TSinh = 'Thai'
        else:
            TSinh = 'Tuyệt'
    elif chi == 'MÙI':
        if can == 'GIÁP':
            TSinh = 'Mộ'
        elif can == 'ẤT':
            TSinh = 'Dưỡng'
        elif can == 'BÍNH':
            TSinh = 'Suy'
        elif can == 'ĐINH':
            TSinh = 'Q Đới'
        elif can == 'MẬU':
            TSinh = 'Suy'
        elif can == 'KỶ':
            TSinh = 'Q Đới'
        elif can == 'CANH':
            TSinh = 'Q Đới'
        elif can == 'TÂN':
            TSinh = 'Suy'
        elif can == 'NHÂM':
            TSinh = 'Dưỡng'
        else:
            TSinh = 'Mộ'
    elif chi == 'THÂN':
        if can == 'GIÁP':
            TSinh = 'Tuyệt'
        elif can == 'ẤT':
            TSinh = 'Thai'
        elif can == 'BÍNH':
            TSinh = 'Bệnh'
        elif can == 'ĐINH':
            TSinh = 'M Dục'
        elif can == 'MẬU':
            TSinh = 'Bệnh'
        elif can == 'KỶ':
            TSinh = 'M Dục'
        elif can == 'CANH':
            TSinh = 'L Quan'
        elif can == 'TÂN':
            TSinh = 'Đ Vượng'
        elif can == 'NHÂM':
            TSinh = 'T Sinh'
        else:
            TSinh = 'Tử'
    elif chi == 'DẬU':
        if can == 'GIÁP':
            TSinh = 'Thai'
        elif can == 'ẤT':
            TSinh = 'Tuyệt'
        elif can == 'BÍNH':
            TSinh = 'Tử'
        elif can == 'ĐINH':
            TSinh = 'T Sinh'
        elif can == 'MẬU':
            TSinh = 'Tử'
        elif can == 'KỶ':
            TSinh = 'T Sinh'
        elif can == 'CANH':
            TSinh = 'Đ Vượng'
        elif can == 'TÂN':
            TSinh = 'L Quan'
        elif can == 'NHÂM':
            TSinh = 'M Dục'
        else:
            TSinh = 'Bệnh'

    elif chi == 'TUẤT':
        if can == 'GIÁP':
            TSinh = 'Dưỡng'
        elif can == 'ẤT':
            TSinh = 'Mộ'
        elif can == 'BÍNH':
            TSinh = 'Mộ'
        elif can == 'ĐINH':
            TSinh = 'Dưỡng'
        elif can == 'MẬU':
            TSinh = 'Mộ'
        elif can == 'KỶ':
            TSinh = 'Dưỡng'
        elif can == 'CANH':
            TSinh = 'Suy'
        elif can == 'TÂN':
            TSinh = 'Q Đới'
        elif can == 'NHÂM':
            TSinh = 'Q Đới'
        else:
            TSinh = 'Suy'
    else:
        if can == 'GIÁP':
            TSinh = 'T Sinh'
        elif can == 'ẤT':
            TSinh = 'Tử'
        elif can == 'BÍNH':
            TSinh = 'Tuyệt'
        elif can == 'ĐINH':
            TSinh = 'Thai'
        elif can == 'MẬU':
            TSinh = 'Tuyệt'
        elif can == 'KỶ':
            TSinh = 'Thai'
        elif can == 'CANH':
            TSinh = 'Bệnh'
        elif can == 'TÂN':
            TSinh = 'M Dục'
        elif can == 'NHÂM':
            TSinh = 'L Quan'
        else:
            TSinh = 'Đ Vượng'
    return TSinh

def daivan(option,can,chi,chi_nam,can_ngay,chi_ngay):
    if option == 'Nam':
        if chi_nam in chi_am:
            diachi = tuple(reversed(dia_chi))
            thiencan = tuple(reversed(thien_can))
        else:
            diachi = dia_chi
            thiencan = thien_can
    else:
        if chi_nam in chi_duong:
            diachi = tuple(reversed(dia_chi))
            thiencan = tuple(reversed(thien_can))
        else:
            diachi = dia_chi
            thiencan = thien_can
    can_index = next((i for i in range(len(thiencan)) if thiencan[i].upper() == can.upper()), -1)
    chi_index = next((i for i in range(len(diachi)) if diachi[i].upper() == chi.upper()), -1)
    if can_index >= 0 and chi_index >= 0:
        result = []
        for i in range(10):
            can = thiencan[(i+can_index)%10]
            thap_than = thapthan(can_ngay,can)
            chi = diachi[(i+chi_index)%12]
            kv = khongvong(can_ngay,chi_ngay,chi)
            result.append(f'{can} {chi} -{thap_than} {kv}')
        return result
    return []

def khongvong(can,chi,chi_khac):
    chican_kv = []
    index = thien_can.index(can)
    index_m = dia_chi.index(chi)
    chi_dau = int(index_m-index) -1
    chican_kv.append(dia_chi[chi_dau])
    chi_sau = chi_dau - 1
    chican_kv.append(dia_chi[chi_sau])
    # print('The index of e:', chican_kv)
    if chi_khac in chican_kv:
        return 'KV'
    return ''

def niennhatkhongvong(can,chi):
    # chican_kv = []
    index = thien_can.index(can)
    index_m = dia_chi.index(chi)
    chi_dau = int(index_m-index) -1
    dia_chi_dau = dia_chi[chi_dau]
    chi_sau = chi_dau - 1
    dia_chi_sau = dia_chi[chi_sau]
    # print('The index of e:', chican_kv)
    return f'{dia_chi_sau}-{dia_chi_dau}'

def namvaodaivan(chi_nam,options,hours,minute,day,month,year):
    if options == 'Nam':
        if chi_nam in chi_am:
            year_tietkhi = LichTietKhi.objects.filter(year=year,month=month).values('daytiekhi')
            year_tietkhi = year_tietkhi[0]
            year_tietkhi = year_tietkhi['daytiekhi']
            day_tiekhi =  datetime.datetime.strptime(year_tietkhi, "%d/%m/%Y %I:%M %p")
            day_birthday = datetime.datetime(year, month, day, hours, minute, 59)
            day_number = int(round((((day_birthday-day_tiekhi).total_seconds())/60/60/24)/3))
        else:
            if month == 12:
                year_tietkhi = LichTietKhi.objects.filter(year=year+1,month=1).values('daytiekhi')
            else:
                year_tietkhi = LichTietKhi.objects.filter(year=year,month=(month+1)).values('daytiekhi')
            year_tietkhi = year_tietkhi[0]
            year_tietkhi = year_tietkhi['daytiekhi']
            day_tiekhi =  datetime.datetime.strptime(year_tietkhi, "%d/%m/%Y %I:%M %p")
            day_birthday = datetime.datetime(year, month, day, hours, minute, 59)
            day_number = int(round((((day_tiekhi-day_birthday).total_seconds())/60/60/24)/3))
    else:
        if chi_nam in chi_duong:
            year_tietkhi = LichTietKhi.objects.filter(year=year,month=month).values('daytiekhi')
            year_tietkhi = year_tietkhi[0]
            year_tietkhi = year_tietkhi['daytiekhi']
            day_tiekhi =  datetime.datetime.strptime(year_tietkhi, "%d/%m/%Y %I:%M %p")
            day_birthday = datetime.datetime(year, month, day, hours, minute, 59)
            day_number = int(round((((day_birthday-day_tiekhi).total_seconds())/60/60/24)/3))
        else:
            if month == 12:
                year_tietkhi = LichTietKhi.objects.filter(year=year+1,month=1).values('daytiekhi')
            else:
                year_tietkhi = LichTietKhi.objects.filter(year=year,month=(month+1)).values('daytiekhi')
            year_tietkhi = year_tietkhi[0]
            year_tietkhi = year_tietkhi['daytiekhi']
            day_tiekhi =  datetime.datetime.strptime(year_tietkhi, "%d/%m/%Y %I:%M %p")
            day_birthday = datetime.datetime(year, month, day, hours, minute, 59)
            day_number = int(round((((day_tiekhi-day_birthday).total_seconds())/60/60/24)/3))

    return day_number

def tieuvantungnam(namdaivan,year,options,can_ngay,chi_ngay):
    if namdaivan >= 1:
        tongdaivan = year + (namdaivan-1)
    else:
        tongdaivan = year
        namdaivan = namdaivan + 1
    result = []
    for i in range(tongdaivan,tongdaivan+11):
        thap_than = thapthan(can_ngay,year_can(i))
        chi_nam = year_chi(i)
        khong_vong = khongvong(can_ngay,chi_ngay,chi_nam)
        khong_vong = "<span class='red'>"+khong_vong+"</span>"
        result.append(f'{i}-{year_can(i)} {year_chi(i)}-{thap_than} {khong_vong}')
    return result

def thienatquynhan(can_nam,can_ngay,chi_ngay,chi_thang,chi_nam,chi_gio):
    dic_thienat = {}
    if can_nam == 'GIÁP' or can_nam == 'MẬU':
        if chi_gio == 'MÙI' or chi_gio == 'SỬU':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'MÙI' or chi_ngay == 'SỬU':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'MÙI' or chi_thang == 'SỬU':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'MÙI' or chi_nam == 'SỬU':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_ngay == 'GIÁP' or can_ngay == 'MẬU':
        if chi_gio == 'MÙI' or chi_gio == 'SỬU':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'MÙI' or chi_ngay == 'SỬU':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'MÙI' or chi_thang == 'SỬU':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'MÙI' or chi_nam == 'SỬU':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_nam == 'ẤT' or can_nam == 'KỶ':
        if chi_gio == 'THÂN' or chi_gio =='TÝ':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'THÂN' or chi_ngay == 'TÝ':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'THÂN' or chi_thang == 'TÝ':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'THÂN' or chi_nam == 'TÝ':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_ngay == 'ẤT' or can_ngay == 'KỶ':
        if chi_gio == 'THÂN' or chi_gio == 'TÝ':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'THÂN' or chi_ngay == 'TÝ':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'THÂN' or chi_thang == 'TÝ':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'THÂN' or chi_nam == 'TÝ':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_nam == 'BÍNH' or can_nam == 'ĐINH':
        if chi_gio == 'DẬU' or chi_gio =='HỢI':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'DẬU' or chi_ngay == 'HỢI':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'DẬU' or chi_thang == 'HỢI':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'DẬU' or chi_nam == 'HỢI':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_ngay == 'BÍNH' or can_ngay == 'ĐINH':
        if chi_gio == 'DẬU' or chi_gio == 'HỢI':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'DẬU' or chi_ngay == 'HỢI':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'DẬU' or chi_thang == 'HỢI':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'DẬU' or chi_nam == 'HỢI':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_nam == 'CANH' or can_nam == 'TÂN':
        if chi_gio == 'DẦN' or chi_gio =='NGỌ':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'DẦN' or chi_ngay == 'NGỌ':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'DẦN' or chi_thang == 'NGỌ':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'DẦN' or chi_nam == 'NGỌ':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_ngay == 'CANH' or can_ngay == 'TÂN':
        if chi_gio == 'DẦN' or chi_gio == 'NGỌ':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'DẦN' or chi_ngay == 'NGỌ':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'DẦN' or chi_thang == 'NGỌ':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'DẦN' or chi_nam == 'NGỌ':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_nam == 'NHÂM' or can_nam == 'QUÝ':
        if chi_gio == 'MÃO' or chi_gio =='TỴ':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'MÃO' or chi_ngay == 'TỴ':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'MÃO' or chi_thang == 'TỴ':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'MÃO' or chi_nam == 'TỴ':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    if can_ngay == 'NHÂM' or can_ngay == 'QUÝ':
        if chi_gio == 'MÃO' or chi_gio == 'TỴ':
            dic_thienat.update(gio = 'Thiên Ất Quý Nhân')
        if chi_ngay == 'MÃO' or chi_ngay == 'TỴ':
            dic_thienat.update(ngay = 'Thiên Ất Quý Nhân')
        if chi_thang == 'MÃO' or chi_thang == 'TỴ':
            dic_thienat.update(thang = 'Thiên Ất Quý Nhân')
        if chi_nam == 'MÃO' or chi_nam == 'TỴ':
            dic_thienat.update(nam = 'Thiên Ất Quý Nhân')
    return dic_thienat

def khoicanh(can_ngay,chi_ngay):
    khoi_canh = ''
    if can_ngay == 'NHÂM' and chi_ngay == 'THÌN':
        khoi_canh = 'Khôi Canh'
    elif  can_ngay == 'CANH' and chi_ngay == 'THÌN':
        khoi_canh = 'Khôi Canh'
    elif  can_ngay == 'MẬU' and chi_ngay == 'TUẤT':
        khoi_canh = 'Khôi Canh'
    elif  can_ngay == 'CANH' and chi_ngay == 'TUẤT':
        khoi_canh = 'Khôi Canh'
    else:
        khoi_canh = ''
    return khoi_canh

def thienloc(can_ngay, chi_ngay, chi_thang, chi_nam, chi_gio):
    dic_thienloc = {}
    if can_ngay == 'GIÁP':
        if chi_ngay == 'DẦN':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'DẦN':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'DẦN':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'DẦN':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'ẤT':
        if chi_ngay == 'MÃO':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'MÃO':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'MÃO':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'MÃO':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'BÍNH' or can_ngay == 'MẬU':
        if chi_ngay == 'TỴ':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'TỴ':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'TỴ':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'TỴ':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'ĐINH' or can_ngay == 'KỶ':
        if chi_ngay == 'NGỌ':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'NGỌ':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'NGỌ':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'NGỌ':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'CANH':
        if chi_ngay == 'THÂN':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'THÂN':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'THÂN':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'THÂN':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'TÂN':
        if chi_ngay == 'DẬU':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'DẬU':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'DẬU':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'DẬU':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'NHÂM':
        if chi_ngay == 'HỢI':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'HỢI':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'HỢI':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'HỢI':
            dic_thienloc.update(gio = 'Thiên Lộc')
    elif can_ngay == 'QUÝ':
        if chi_ngay == 'TÝ':
            dic_thienloc.update(ngay = 'Thiên Lộc')
        if chi_thang == 'TÝ':
            dic_thienloc.update(thang = 'Thiên Lộc')
        if chi_nam == 'TÝ':
            dic_thienloc.update(nam = 'Thiên Lộc')
        if chi_gio == 'TÝ':
            dic_thienloc.update(gio = 'Thiên Lộc')
    return dic_thienloc

def kinhduong(can_ngay, chi_ngay, chi_thang, chi_nam, chi_gio):
    dic_thienloc = {}
    if can_ngay == 'GIÁP':
        if chi_ngay == 'MÃO':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'MÃO':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'MÃO':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'MÃO':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'ẤT':
        if chi_ngay == 'DẦN':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'DẦN':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'DẦN':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'DẦN':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'BÍNH' or can_ngay == 'MẬU':
        if chi_ngay == 'NGỌ':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'NGỌ':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'NGỌ':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'NGỌ':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'ĐINH' or can_ngay == 'KỶ':
        if chi_ngay == 'TỴ':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'TỴ':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'TỴ':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'TỴ':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'CANH':
        if chi_ngay == 'DẬU':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'DẬU':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'DẬU':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'DẬU':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'TÂN':
        if chi_ngay == 'THÂN':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'THÂN':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'THÂN':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'THÂN':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'NHÂM':
        if chi_ngay == 'TÝ':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'TÝ':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'TÝ':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'TÝ':
            dic_thienloc.update(gio = 'Kình Dương')
    elif can_ngay == 'QUÝ':
        if chi_ngay == 'HỢI':
            dic_thienloc.update(ngay = 'Kình Dương')
        if chi_thang == 'HỢI':
            dic_thienloc.update(thang = 'Kình Dương')
        if chi_nam == 'HỢI':
            dic_thienloc.update(nam = 'Kình Dương')
        if chi_gio == 'HỢI':
            dic_thienloc.update(gio = 'Kình Dương')
    return dic_thienloc

def kimdu(can_ngay, chi_ngay, chi_thang, chi_nam, chi_gio):
    dic_kimdu = {}
    if can_ngay == 'GIÁP':
        if chi_ngay == 'THÌN':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'THÌN':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'THÌN':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'THÌN':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'ẤT':
        if chi_ngay == 'TỴ':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'TỴ':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'TỴ':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'TỴ':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'BÍNH':
        if chi_ngay == 'MÙI':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'MÙI':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'MÙI':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'MÙI':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'ĐINH':
        if chi_ngay == 'THÂN':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'THÂN':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'THÂN':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'THÂN':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'MẬU':
        if chi_ngay == 'MÙI':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'MÙI':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'MÙI':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'MÙI':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'KỶ':
        if chi_ngay == 'THÂN':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'THÂN':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'THÂN':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'THÂN':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'CANH':
        if chi_ngay == 'TUẤT':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'TUẤT':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'TUẤT':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'TUẤT':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'TÂN':
        if chi_ngay == 'HỢI':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'HỢI':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'HỢI':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'HỢI':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'NHÂM':
        if chi_ngay == 'SỬU':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'SỬU':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'SỬU':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'SỬU':
            dic_kimdu.update(gio = 'Kim Dư')
    elif can_ngay == 'QUÝ':
        if chi_ngay == 'DẦN':
            dic_kimdu.update(ngay = 'Kim Dư')
        if chi_thang == 'DẦN':
            dic_kimdu.update(thang = 'Kim Dư')
        if chi_nam == 'DẦN':
            dic_kimdu.update(nam = 'Kim Dư')
        if chi_gio == 'DẦN':
            dic_kimdu.update(gio = 'Kim Dư')
    return dic_kimdu

def vanxuong(can_ngay, can_nam , chi_ngay, chi_thang, chi_nam, chi_gio):
    dic_vanxuong = {}
    if can_ngay == 'GIÁP' or can_nam == 'GIÁP':
        if chi_ngay == 'TỴ':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'TỴ':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'TỴ':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'TỴ':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'ẤT' or can_nam == 'ẤT':
        if chi_ngay == 'NGỌ':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'NGỌ':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'NGỌ':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'NGỌ':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'BÍNH' or can_nam == 'BÍNH':
        if chi_ngay == 'THÂN':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'THÂN':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'THÂN':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'THÂN':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'ĐINH' or can_nam == 'ĐINH':
        if chi_ngay == 'DẬU':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'DẬU':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'DẬU':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'DẬU':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'MẬU' or can_nam == 'MẬU':
        if chi_ngay == 'THÂN':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'THÂN':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'THÂN':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'THÂN':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'KỶ' or can_nam == 'KỶ':
        if chi_ngay == 'DẬU':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'DẬU':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'DẬU':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'DẬU':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'CANH' or can_nam == 'CANH':
        if chi_ngay == 'HỢI':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'HỢI':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'HỢI':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'HỢI':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'TÂN' or can_nam == 'TÂN':
        if chi_ngay == 'TÝ':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'TÝ':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'TÝ':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'TÝ':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'NHÂM' or can_nam == 'NHÂM':
        if chi_ngay == 'DẦN':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'DẦN':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'DẦN':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'DẦN':
            dic_vanxuong.update(gio = 'Văn Xương')
    elif can_ngay == 'QUÝ' or can_nam == 'QUÝ':
        if chi_ngay == 'MÃO':
            dic_vanxuong.update(ngay = 'Văn Xương')
        if chi_thang == 'MÃO':
            dic_vanxuong.update(thang = 'Văn Xương')
        if chi_nam == 'MÃO':
            dic_vanxuong.update(nam = 'Văn Xương')
        if chi_gio == 'MÃO':
            dic_vanxuong.update(gio = 'Văn Xương')
    return dic_vanxuong

def thieny(*thien_y):
    chi_ngay = thien_y[0]
    chi_thang = thien_y[1]
    chi_nam = thien_y[2]
    chi_gio = thien_y[3]
    dic_thieny = {}
    if chi_thang == 'DẦN':
        if chi_ngay == 'SỬU':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'SỬU':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'SỬU':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'MÃO':
        if chi_ngay == 'DẦN':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'DẦN':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'DẦN':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'THÌN':
        if chi_ngay == 'MÃO':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'MÃO':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'MÃO':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'TỴ':
        if chi_ngay == 'THÌN':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'THÌN':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'THÌN':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'NGỌ':
        if chi_ngay == 'TỴ':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'TỴ':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'TỴ':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'MÙI':
        if chi_ngay == 'NGỌ':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'NGỌ':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'NGỌ':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'THÂN':
        if chi_ngay == 'MÙI':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'MÙI':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'MÙI':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'DẬU':
        if chi_ngay == 'THÂN':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'THÂN':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'THÂN':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'TUẤT':
        if chi_ngay == 'DẬU':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'DẬU':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'DẬU':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'HỢI':
        if chi_ngay == 'TUẤT':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'TUẤT':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'TUẤT':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'TÝ':
        if chi_ngay == 'HỢI':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'HỢI':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'HỢI':
            dic_thieny.update(gio = 'Thiên Y')
    elif chi_thang == 'SỬU':
        if chi_ngay == 'TÝ':
            dic_thieny.update(ngay = 'Thiên Y')
        if chi_nam == 'TÝ':
            dic_thieny.update(nam = 'Thiên Y')
        if chi_gio == 'TÝ':
            dic_thieny.update(gio = 'Thiên Y')
    return dic_thieny

def dichma(*dich_ma):
    chi_ngay = dich_ma[0]
    chi_thang = dich_ma[1]
    chi_nam = dich_ma[2]
    chi_gio = dich_ma[3]
    dic_dicma = {}
    if chi_ngay == 'DẦN' or chi_ngay == 'NGỌ' or chi_ngay == 'TUẤT':
        if chi_nam == 'THÂN':
            dic_dicma.update(nam = 'Dịch Mã')
        if chi_thang == 'THÂN':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'THÂN':
            dic_dicma.update(gio = 'Dịch Mã')
    elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
        if chi_ngay == 'THÂN':
            dic_dicma.update(ngay = 'Dịch Mã')
        if chi_thang == 'THÂN':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'THÂN':
            dic_dicma.update(gio = 'Dịch Mã')
    if chi_ngay == 'THÂN' or chi_ngay == 'TÝ' or chi_ngay == 'THÌN':
        if chi_nam == 'DẦN':
            dic_dicma.update(nam = 'Dịch Mã')
        if chi_thang == 'DẦN':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'DẦN':
            dic_dicma.update(gio = 'Dịch Mã')
    elif chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
        if chi_ngay == 'DẦN':
            dic_dicma.update(ngay = 'Dịch Mã')
        if chi_thang == 'DẦN':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'DẦN':
            dic_dicma.update(gio = 'Dịch Mã')
    if chi_ngay == 'TỴ' or chi_ngay == 'DẬU' or chi_ngay == 'SỬU':
        if chi_nam == 'HỢI':
            dic_dicma.update(nam = 'Dịch Mã')
        if chi_thang == 'HỢI':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'HỢI':
            dic_dicma.update(gio = 'Dịch Mã')
    elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
        if chi_ngay == 'HỢI':
            dic_dicma.update(ngay = 'Dịch Mã')
        if chi_thang == 'HỢI':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'HỢI':
            dic_dicma.update(gio = 'Dịch Mã')
    if chi_ngay == 'HỢI' or chi_ngay == 'MÃO' or chi_ngay == 'MÙI':
        if chi_nam == 'TỴ':
            dic_dicma.update(nam = 'Dịch Mã')
        if chi_thang == 'TỴ':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'TỴ':
            dic_dicma.update(gio = 'Dịch Mã')
    elif chi_nam == 'HỢI' or chi_nam == 'MÃO' or chi_nam == 'MÙI':
        if chi_ngay == 'TỴ':
            dic_dicma.update(ngay = 'Dịch Mã')
        if chi_thang == 'TỴ':
            dic_dicma.update(thang = 'Dịch Mã')
        if chi_gio == 'TỴ':
            dic_dicma.update(gio = 'Dịch Mã')
    return dic_dicma

def hoacai(*hoa_cai):
    chi_ngay = hoa_cai[0]
    chi_thang = hoa_cai[1]
    chi_nam = hoa_cai[2]
    chi_gio = hoa_cai[3]
    dic_hoacai = {}
    if chi_ngay == 'DẦN' or chi_ngay == 'NGỌ' or chi_ngay == 'TUẤT':
        if chi_nam == 'TUẤT':
            dic_hoacai.update(nam = 'Hoa Cái')
        if chi_thang == 'TUẤT':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'TUẤT':
            dic_hoacai.update(gio = 'Hoa Cái')
    elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
        if chi_ngay == 'TUẤT':
            dic_hoacai.update(ngay = 'Hoa Cái')
        if chi_thang == 'TUẤT':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'TUẤT':
            dic_hoacai.update(gio = 'Hoa Cái')
    if chi_ngay == 'THÂN' or chi_ngay == 'TÝ' or chi_ngay == 'THÌN':
        if chi_nam == 'THÌN':
            dic_hoacai.update(nam = 'Hoa Cái')
        if chi_thang == 'THÌN':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'THÌN':
            dic_hoacai.update(gio = 'Hoa Cái')
    elif chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
        if chi_ngay == 'THÌN':
            dic_hoacai.update(nam = 'Hoa Cái')
        if chi_thang == 'THÌN':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'THÌN':
            dic_hoacai.update(gio = 'Hoa Cái')
    if chi_ngay == 'TỴ' or chi_ngay == 'DẬU' or chi_ngay == 'SỬU':
        if chi_nam == 'SỬU':
            dic_hoacai.update(nam = 'Hoa Cái')
        if chi_thang == 'SỬU':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'SỬU':
            dic_hoacai.update(gio = 'Hoa Cái')
    elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
        if chi_ngay == 'SỬU':
            dic_hoacai.update(ngay = 'Hoa Cái')
        if chi_thang == 'SỬU':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'SỬU':
            dic_hoacai.update(gio = 'Hoa Cái')
    if chi_ngay == 'HỢI' or chi_ngay == 'MÃO' or chi_ngay == 'MÙI':
        if chi_nam == 'MÙI':
            dic_hoacai.update(nam = 'Hoa Cái')
        if chi_thang == 'MÙI':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'MÙI':
            dic_hoacai.update(gio = 'Hoa Cái')
    elif chi_nam == 'HỢI' or chi_nam == 'MÃO' or chi_nam == 'MÙI':
        if chi_ngay == 'MÙI':
            dic_hoacai.update(ngay = 'Hoa Cái')
        if chi_thang == 'MÙI':
            dic_hoacai.update(thang = 'Hoa Cái')
        if chi_gio == 'MÙI':
            dic_hoacai.update(gio = 'Hoa Cái')
    return dic_hoacai

def tuongtinh(*tuong_tinh):
    chi_ngay = tuong_tinh[0]
    chi_thang = tuong_tinh[1]
    chi_nam = tuong_tinh[2]
    chi_gio = tuong_tinh[3]
    dic_tuongtinh = {}
    if chi_ngay == 'DẦN' or chi_ngay == 'NGỌ' or chi_ngay == 'TUẤT':
        if chi_nam == 'NGỌ':
            dic_tuongtinh.update(nam = 'Tướng Tinh')
        if chi_thang == 'NGỌ':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'NGỌ':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
        if chi_ngay == 'NGỌ':
            dic_tuongtinh.update(ngay = 'Tướng Tinh')
        if chi_thang == 'NGỌ':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'NGỌ':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    if chi_ngay == 'THÂN' or chi_ngay == 'TÝ' or chi_ngay == 'THÌN':
        if chi_nam == 'TÝ':
            dic_tuongtinh.update(nam = 'Tướng Tinh')
        if chi_thang == 'TÝ':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'TÝ':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    elif chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
        if chi_ngay == 'TÝ':
            dic_tuongtinh.update(nam = 'Tướng Tinh')
        if chi_thang == 'TÝ':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'TÝ':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    if chi_ngay == 'TỴ' or chi_ngay == 'DẬU' or chi_ngay == 'SỬU':
        if chi_nam == 'DẬU':
            dic_tuongtinh.update(nam = 'Tướng Tinh')
        if chi_thang == 'DẬU':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'DẬU':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
        if chi_ngay == 'DẬU':
            dic_tuongtinh.update(ngay = 'Tướng Tinh')
        if chi_thang == 'DẬU':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'DẬU':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    if chi_ngay == 'HỢI' or chi_ngay == 'MÃO' or chi_ngay == 'MÙI':
        if chi_nam == 'MÃO':
            dic_tuongtinh.update(nam = 'Tướng Tinh')
        if chi_thang == 'MÃO':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'MÃO':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    elif chi_nam == 'HỢI' or chi_nam == 'MÃO' or chi_nam == 'MÙI':
        if chi_ngay == 'MÃO':
            dic_tuongtinh.update(ngay = 'Tướng Tinh')
        if chi_thang == 'MÃO':
            dic_tuongtinh.update(thang = 'Tướng Tinh')
        if chi_gio == 'MÃO':
            dic_tuongtinh.update(gio = 'Tướng Tinh')
    return dic_tuongtinh

def daohoa(*dao_hoa):
    chi_ngay = dao_hoa[0]
    chi_thang = dao_hoa[1]
    chi_nam = dao_hoa[2]
    chi_gio = dao_hoa[3]
    dic_daohoa = {}
    if chi_ngay == 'DẦN' or chi_ngay == 'NGỌ' or chi_ngay == 'TUẤT':
        if chi_nam == 'MÃO':
            dic_daohoa.update(nam = 'Đào Hoa')
        if chi_thang == 'MÃO':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'MÃO':
            dic_daohoa.update(gio = 'Đào Hoa')
    elif chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
        if chi_ngay == 'MÃO':
            dic_daohoa.update(ngay = 'Đào Hoa')
        if chi_thang == 'MÃO':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'MÃO':
            dic_daohoa.update(gio = 'Đào Hoa')
    if chi_ngay == 'THÂN' or chi_ngay == 'TÝ' or chi_ngay == 'THÌN':
        if chi_nam == 'DẬU':
            dic_daohoa.update(nam = 'Đào Hoa')
        if chi_thang == 'DẬU':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'DẬU':
            dic_daohoa.update(gio = 'Đào Hoa')
    elif chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
        if chi_ngay == 'DẬU':
            dic_daohoa.update(nam = 'Đào Hoa')
        if chi_thang == 'DẬU':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'DẬU':
            dic_daohoa.update(gio = 'Đào Hoa')
    if chi_ngay == 'TỴ' or chi_ngay == 'DẬU' or chi_ngay == 'SỬU':
        if chi_nam == 'NGỌ':
            dic_daohoa.update(nam = 'Đào Hoa')
        if chi_thang == 'NGỌ':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'NGỌ':
            dic_daohoa.update(gio = 'Đào Hoa')
    elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
        if chi_ngay == 'NGỌ':
            dic_daohoa.update(ngay = 'Đào Hoa')
        if chi_thang == 'NGỌ':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'NGỌ':
            dic_daohoa.update(gio = 'Đào Hoa')
    if chi_ngay == 'HỢI' or chi_ngay == 'MÃO' or chi_ngay == 'MÙI':
        if chi_nam == 'TÝ':
            dic_daohoa.update(nam = 'Đào Hoa')
        if chi_thang == 'TÝ':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'TÝ':
            dic_daohoa.update(gio = 'Đào Hoa')
    elif chi_nam == 'HỢI' or chi_nam == 'MÃO' or chi_nam == 'MÙI':
        if chi_ngay == 'TÝ':
            dic_daohoa.update(ngay = 'Đào Hoa')
        if chi_thang == 'TÝ':
            dic_daohoa.update(thang = 'Đào Hoa')
        if chi_gio == 'TÝ':
            dic_daohoa.update(gio = 'Đào Hoa')
    return dic_daohoa

def daohoasat(*dao_hoa_sat):
    can_ngay = dao_hoa_sat[0]
    chi_ngay = dao_hoa_sat[1]
    chi_thang = dao_hoa_sat[2]
    chi_nam = dao_hoa_sat[3]
    chi_gio = dao_hoa_sat[4]
    dic_daohoasat = {}
    if can_ngay == 'GIÁP':
        if chi_ngay == 'TÝ':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'TÝ':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'TÝ':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'TÝ':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'ẤT':
        if chi_ngay == 'TỴ':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'TỴ':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'TỴ':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'TỴ':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'BÍNH':
        if chi_ngay == 'MÃO':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'MÃO':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'MÃO':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'MÃO':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'ĐINH':
        if chi_ngay == 'THÂN':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'THÂN':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'THÂN':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'THÂN':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'MẬU':
        if chi_ngay == 'MÃO':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'MÃO':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'MÃO':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'MÃO':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'KỶ':
        if chi_ngay == 'THÂN':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'THÂN':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'THÂN':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'THÂN':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'CANH':
        if chi_ngay == 'NGỌ':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'NGỌ':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'NGỌ':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'NGỌ':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'TÂN':
        if chi_ngay == 'HỢI':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'HỢI':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'HỢI':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'HỢI':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'NHÂM':
        if chi_ngay == 'DẬU':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'DẬU':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'DẬU':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'DẬU':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    elif can_ngay == 'QUÝ':
        if chi_ngay == 'DẦN':
            dic_daohoasat.update(ngay = 'Đào Hoa Sát')
        if chi_thang == 'DẦN':
            dic_daohoasat.update(thang = 'Đào Hoa Sát')
        if chi_nam == 'DẦN':
            dic_daohoasat.update(nam = 'Đào Hoa Sát')
        if chi_gio == 'DẦN':
            dic_daohoasat.update(gio = 'Đào Hoa Sát')
    return dic_daohoasat

def kiepsat(*kiep_sat):
    chi_ngay = kiep_sat[0]
    chi_thang = kiep_sat[1]
    chi_nam = kiep_sat[2]
    chi_gio = kiep_sat[3]
    dic_kiepsat = {}
    if chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
        if chi_ngay == 'HỢI':
            dic_kiepsat.update(ngay = 'Kiếp Sát')
        if chi_thang == 'HỢI':
            dic_kiepsat.update(thang = 'Kiếp Sát')
        if chi_gio == 'HỢI':
            dic_kiepsat.update(gio = 'Kiếp Sát')
    elif chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
        if chi_ngay == 'TỴ':
            dic_kiepsat.update(ngay = 'Kiếp Sát')
        if chi_thang == 'TỴ':
            dic_kiepsat.update(thang = 'Kiếp Sát')
        if chi_gio == 'TỴ':
            dic_kiepsat.update(gio = 'Kiếp Sát')
    elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
        if chi_ngay == 'DẦN':
            dic_kiepsat.update(ngay = 'Kiếp Sát')
        if chi_thang == 'DẦN':
            dic_kiepsat.update(thang = 'Kiếp Sát')
        if chi_gio == 'DẦN':
            dic_kiepsat.update(gio = 'Kiếp Sát')
    elif chi_nam == 'HỢI' or chi_nam == 'MÃO' or chi_nam == 'MÙI':
        if chi_ngay == 'THÂN':
            dic_kiepsat.update(ngay = 'Kiếp Sát')
        if chi_thang == 'THÂN':
            dic_kiepsat.update(thang = 'Kiếp Sát')
        if chi_gio == 'THÂN':
            dic_kiepsat.update(gio = 'Kiếp Sát')
    return dic_kiepsat


def thienxa(*thien_xa):
    chi_thang = thien_xa[0]
    can_ngay = thien_xa[1]
    chi_ngay = thien_xa[2]
    dic_thienxa = ''
    if chi_thang == 'DẦN' or chi_thang == 'MÃO' or chi_thang == 'THÌN':
        if can_ngay == 'MẬU' and chi_ngay == 'DẦN':
            dic_thienxa = 'Thiên Xá Nhật'
    elif chi_thang == 'TỴ' or chi_thang == 'NGỌ' or chi_thang == 'MÙI':
        if can_ngay == 'GIÁP' and chi_ngay == 'NGỌ':
            dic_thienxa = 'Thiên Xá Nhật'
    elif chi_thang == 'THÂN' or chi_thang == 'DẬU' or chi_thang == 'TUẤT':
        if can_ngay == 'MẬU' and chi_ngay == 'THÂN':
            dic_thienxa = 'Thiên Xá Nhật'
    elif chi_thang == 'HỢI' or chi_thang == 'TÝ' or chi_thang == 'SỬU':
        if can_ngay == 'GIÁP' and chi_ngay == 'TÝ':
            dic_thienxa = 'Thiên Xá Nhật'
    else:
        dic_thienxa = ''
    return dic_thienxa

def taisat(*tai_sat):
    chi_ngay = tai_sat[0]
    chi_thang = tai_sat[1]
    chi_nam = tai_sat[2]
    chi_gio = tai_sat[3]
    dic_taisat = {}
    if chi_nam == 'DẦN' or chi_nam == 'NGỌ' or chi_nam == 'TUẤT':
        if chi_ngay == 'TÝ':
            dic_taisat.update(ngay = 'Tai Sát')
        if chi_thang == 'TÝ':
            dic_taisat.update(thang = 'Tai Sát')
        if chi_gio == 'TÝ':
            dic_taisat.update(gio = 'Tai Sát')
    elif chi_nam == 'THÂN' or chi_nam == 'TÝ' or chi_nam == 'THÌN':
        if chi_ngay == 'NGỌ':
            dic_taisat.update(nam = 'Tai Sát')
        if chi_thang == 'NGỌ':
            dic_taisat.update(thang = 'Tai Sát')
        if chi_gio == 'NGỌ':
            dic_taisat.update(gio = 'Tai Sát')
    elif chi_nam == 'TỴ' or chi_nam == 'DẬU' or chi_nam == 'SỬU':
        if chi_ngay == 'MÃO':
            dic_taisat.update(ngay = 'Tai Sát')
        if chi_thang == 'MÃO':
            dic_taisat.update(thang = 'Tai Sát')
        if chi_gio == 'MÃO':
            dic_taisat.update(gio = 'Tai Sát')
    elif chi_nam == 'HỢI' or chi_nam == 'MÃO' or chi_nam == 'MÙI':
        if chi_ngay == 'DẬU':
            dic_taisat.update(ngay = 'Tai Sát')
        if chi_thang == 'DẬU':
            dic_taisat.update(thang = 'Tai Sát')
        if chi_gio == 'DẬU':
            dic_taisat.update(gio = 'Tai Sát')
    return dic_taisat

def quocanquynhan(*quocan_quynhan):
    can_ngay = quocan_quynhan[0]
    can_nam = quocan_quynhan[1]
    chi_ngay = quocan_quynhan[2]
    chi_thang = quocan_quynhan[3]
    chi_nam = quocan_quynhan[4]
    chi_gio = quocan_quynhan[5]
    dic_quocanquynhan = {}
    if can_ngay == 'GIÁP' or can_nam == 'GIÁP':
        if chi_ngay == 'TUẤT':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'TUẤT':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'TUẤT':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'TUẤT':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    if can_ngay == 'ẤT' or can_nam == 'ẤT':
        if chi_ngay == 'HỢI':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'HỢI':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'HỢI':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'HỢI':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    if can_ngay == 'BÍNH' or can_nam == 'BÍNH':
        if chi_ngay == 'SỬU':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'SỬU':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'SỬU':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'SỬU':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    elif can_ngay == 'MẬU' or can_nam == 'MẬU':
        if chi_ngay == 'SỬU':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'SỬU':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'SỬU':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'SỬU':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    if can_ngay == 'ĐINH' or can_nam == 'ĐINH':
        if chi_ngay == 'DẦN':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'DẦN':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'DẦN':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'DẦN':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    elif can_ngay == 'KỶ' or can_nam == 'KỶ':
        if chi_ngay == 'DẦN':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'DẦN':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'DẦN':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'DẦN':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    if can_ngay == 'CANH' or can_nam == 'CANH':
        if chi_ngay == 'THÌN':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'THÌN':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'THÌN':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'THÌN':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    if can_ngay == 'TÂN' or can_nam == 'TÂN':
        if chi_ngay == 'TỴ':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'TỴ':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'TỴ':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'TỴ':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    if can_ngay == 'NHÂM' or can_nam == 'NHÂM':
        if chi_ngay == 'MÙI':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'MÙI':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'MÙI':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'MÙI':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    elif can_ngay == 'QUÝ' or can_nam == 'QUÝ':
        if chi_ngay == 'THÂN':
            dic_quocanquynhan.update(ngay = 'Quốc Ấn Quý Nhân')
        if chi_thang == 'THÂN':
            dic_quocanquynhan.update(thang = 'Quốc Ấn Quý Nhân')
        if chi_nam == 'THÂN':
            dic_quocanquynhan.update(nam = 'Quốc Ấn Quý Nhân')
        if chi_gio == 'THÂN':
            dic_quocanquynhan.update(gio = 'Quốc Ấn Quý Nhân')
    return dic_quocanquynhan


def cothanquatu(*cothan_quatu):
    chi_ngay = cothan_quatu[0]
    chi_thang = cothan_quatu[1]
    chi_nam = cothan_quatu[2]
    chi_gio = cothan_quatu[3]
    dic_cothanquatu = {}
    if chi_nam == 'DẦN' or chi_nam == 'MÃO' or chi_nam == 'THÌN':
        if chi_ngay == 'TỴ':
            dic_cothanquatu.update(ngay = 'Cô Thần')
        elif chi_ngay == 'SỬU':
            dic_cothanquatu.update(ngay = 'Quả Tú')
        if chi_thang == 'TỴ':
            dic_cothanquatu.update(thang = 'Cô Thần')
        elif chi_thang == 'SỬU':
            dic_cothanquatu.update(thang = 'Quả Tú')
        if chi_gio == 'TỴ':
            dic_cothanquatu.update(gio = 'Cô Thần')
        elif chi_gio == 'SỬU':
            dic_cothanquatu.update(gio = 'Quả Tú')
    elif chi_nam == 'TỴ' or chi_nam == 'NGỌ' or chi_nam == 'MÙI':
        if chi_ngay == 'THÂN':
            dic_cothanquatu.update(ngay = 'Cô Thần')
        elif chi_ngay == 'THÌN':
            dic_cothanquatu.update(ngay = 'Quả Tú')
        if chi_thang == 'THÂN':
            dic_cothanquatu.update(thang = 'Cô Thần')
        elif chi_thang == 'THÌN':
            dic_cothanquatu.update(thang = 'Quả Tú')
        if chi_gio == 'THÂN':
            dic_cothanquatu.update(gio = 'Cô Thần')
        elif chi_gio == 'THÌN':
            dic_cothanquatu.update(gio = 'Quả Tú')
    elif chi_nam == 'THÂN' or chi_nam == 'DẬU' or chi_nam == 'TUẤT':
        if chi_ngay == 'HỢI':
            dic_cothanquatu.update(ngay = 'Cô Thần')
        elif chi_ngay == 'MÙI':
            dic_cothanquatu.update(ngay = 'Quả Tú')
        if chi_thang == 'HỢI':
            dic_cothanquatu.update(thang = 'Cô Thần')
        elif chi_thang == 'MÙI':
            dic_cothanquatu.update(thang = 'Quả Tú')
        if chi_gio == 'HỢI':
            dic_cothanquatu.update(gio = 'Cô Thần')
        elif chi_gio == 'MÙI':
            dic_cothanquatu.update(gio = 'Quả Tú')
    elif chi_nam == 'HỢI' or chi_nam == 'TÝ' or chi_nam == 'SỬU':
        if chi_ngay == 'DẦN':
            dic_cothanquatu.update(ngay = 'Cô Thần')
        elif chi_ngay == 'TUẤT':
            dic_cothanquatu.update(ngay = 'Quả Tú')
        if chi_thang == 'DẦN':
            dic_cothanquatu.update(thang = 'Cô Thần')
        elif chi_thang == 'TUẤT':
            dic_cothanquatu.update(thang = 'Quả Tú')
        if chi_gio == 'DẦN':
            dic_cothanquatu.update(gio = 'Cô Thần')
        elif chi_gio == 'TUẤT':
            dic_cothanquatu.update(gio = 'Quả Tú')
    else:
        dic_cothanquatu = ''
    return dic_cothanquatu


def thapacdaibai(*thapac_daibai):
    can_ngay = thapac_daibai[0]
    chi_ngay = thapac_daibai[1]
    dic_thapacdaibai = ''
    if can_ngay == 'GIÁP' and chi_ngay == 'THÌN':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'ẤT' and chi_ngay == 'TỴ':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'BÍNH' and chi_ngay == 'THÂN':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'ĐINH' and chi_ngay == 'HỢI':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'MẬU' and chi_ngay == 'TUẤT':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'KỶ' and chi_ngay == 'SỬU':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'CANH' and chi_ngay == 'THÌN':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'TÂN' and chi_ngay == 'TỴ':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'NHÂM' and chi_ngay == 'THÂN':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    elif  can_ngay == 'QUÝ' and chi_ngay == 'HỢI':
        dic_thapacdaibai = 'Thập Ác Đại Bại'
    else:
        dic_thapacdaibai = ''
    return dic_thapacdaibai

# dia_chi = ('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
# thien_can = ('GIÁP','ẤT','BÍNH','ĐINH','MẬU','KỶ','CANH','TÂN','NHÂM','QUÝ')
def tamkyquynhan(*tamky_quynhan):
    can_ngay = tamky_quynhan[0]
    can_thang = tamky_quynhan[1]
    can_nam = tamky_quynhan[2]
    can_gio = tamky_quynhan[3]
    chi_thang = tamky_quynhan[4]
    dic_tamkyquynhan = ''
    T_Sinh_Nam = truongsinh(can_nam,chi_thang)
    T_Sinh_Thang = truongsinh(can_thang,chi_thang)
    T_Sinh_Ngay = truongsinh(can_ngay,chi_thang)
    T_Sinh_Gio = truongsinh(can_gio,chi_thang)
    if T_Sinh_Nam != 'Tuyệt' and T_Sinh_Nam != 'Tử' or T_Sinh_Thang != 'Tuyệt' and T_Sinh_Thang != 'Tử' or T_Sinh_Ngay != 'Tuyệt' and T_Sinh_Ngay != 'Tử':
        if can_nam == 'GIÁP' and can_thang == 'MẬU' and can_ngay == 'CANH':
            dic_tamkyquynhan = 'Tam Kỳ Quý Nhân'
        if can_nam == 'ẤT' and can_thang == 'BÍNH' and can_ngay == 'ĐINH':
            dic_tamkyquynhan = 'Tam Kỳ Quý Nhân'
        if can_nam == 'NHÂM' and can_thang == 'QUÝ' and can_ngay == 'TÂN':
            dic_tamkyquynhan = 'Tam Kỳ Quý Nhân'
    if T_Sinh_Gio != 'Tuyệt' and T_Sinh_Gio != 'Tử' or T_Sinh_Thang != 'Tuyệt' and T_Sinh_Thang != 'Tử' or T_Sinh_Ngay != 'Tuyệt' and T_Sinh_Ngay != 'Tử':
        if can_thang == 'GIÁP' and can_nam == 'MẬU' and can_gio == 'CANH':
            dic_tamkyquynhan = 'Tam Kỳ Quý Nhân'
        if can_thang == 'ẤT' and can_nam == 'BÍNH' and can_gio == 'ĐINH':
            dic_tamkyquynhan = 'Tam Kỳ Quý Nhân'
        if can_thang == 'NHÂM' and can_nam == 'QUÝ' and can_gio == 'TÂN':
            dic_tamkyquynhan = 'Tam Kỳ Quý Nhân'
    return dic_tamkyquynhan

def cungmenh(chi_thang, chi_gio, can_nam):
    tongcung = chi_cungmenh[chi_thang] + chi_cungmenh[chi_gio]
    dic_cungmenh = []
    if tongcung < 14:
        tong_chi = 14 - tongcung
        for key, value in chi_cungmenh.items():
            if tong_chi == value:
                chi_menh = key
    else:
        tong_chi = 26 - tongcung
        for key, value in chi_cungmenh.items():
            if tong_chi == value:
                chi_menh = key
    index = int(thien_can.index(can_nam) -3)
    dic_cungmenh.append(f'{thien_can[index]} {chi_menh}')
    return dic_cungmenh

def thainguyen(can_thang,chi_thang):
    dic_thainguyen = []
    index_can = int(thien_can.index(can_thang) +1)
    if index_can > 9:
        index_can = index_can- 10
    index_chi = int(dia_chi.index(chi_thang) +3)
    if index_chi > 11:
        index_chi = index_chi - 12
    dic_thainguyen.append(f'{thien_can[index_can]} {dia_chi[index_chi]}')
    return dic_thainguyen

# import datetime
# dt = datetime.datetime.strptime("6/1/1900 6:03 PM", "%d/%m/%Y %I:%M %p")
# abs(a = -1)
# https://pypi.org/project/imgkit/
