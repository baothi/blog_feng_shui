from django.db import models
from django.db.models import Model
from blog_feng_shui.AmLich import *
from tutru.models import *
import datetime
# Create your models
class KINHDICH(models.Model):
  dic_batque = {
      '1': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
            '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
            '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',

      '2': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
           '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',

      '3': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',

      '4': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',

      '5': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
           '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>',

      '6': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>',

      '7': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>',

      '8': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'
           '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>',
  }

  # xac dinh 0 la hào âm , 1 là hào dương
  dic_quedich = {'1': ['1', '1', '1'],'2': ['0', '1', '1'],'3': ['1', '0', '1'],'4': ['0', '0', '1'],'5': ['1', '1', '0'],'6': ['0', '1', '0'],'7': ['1', '0', '0'],'8': ['0', '0', '0']}
  dic_amduong = {'1' : '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>', '0': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'}
  dic_dia_chi = {'TÝ': 1,'SỬU': 2,'DẦN': 3,'MÃO': 4,'THÌN': 5,'TỴ': 6,'NGỌ': 7,'MÙI': 8,'THÂN': 9,'DẬU': 10,'TUẤT': 11,'HỢI': 12}
  dic_chi_nguhanh = {'TÝ': "Thủy",'SỬU': "Thổ",'DẦN': "Mộc",'MÃO': "Mộc",'THÌN': "Thổ",'TỴ': "Hỏa",'NGỌ': "Hỏa",'MÙI': "Thổ",'THÂN': "Kim",'DẬU': "Kim",'TUẤT': "Thổ",'HỢI': "Thủy"}
  dic_haodong = {'1': '<td colspan="2" class="bgred">&nbsp;</td>', '0': '<td class="bgred">&nbsp;</td><td class="bgred">&nbsp;</td>'}
  dic_tenque = {
    "['1', '1', '1', '1', '1', '1']": ['BÁT THUẦN CÀN','Họ Càn (Lục Xung)','KHỐN LONG ĐẮC THỦY','Kim',{'6':'Thế'},{'3':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']}],
    "['1', '1', '1', '1', '1', '0']": ['THIÊN PHONG CẤU','Họ Càn','THA HƯƠNG NGỘ HỮU','Kim',{'1':'Thế'},{'4':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'2':['Dần','Mộc']}],
    "['1', '1', '1', '1', '0', '0']": ['THIÊN SƠN ĐỘN','Họ Càn','NÙNG VÂN TẾ NHẬT','Kim',{'2':'Thế'},{'5':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'1':['Tý','Thủy'],'2':['Dần','Mộc']}],
    "['1', '1', '1', '0', '0', '0']": ['THIÊN ĐỊA BĨ','Họ Càn','HỖ LẠC HÃM KHANH','Kim',{'3':'Thế'},{'6':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'1':['Tý','Thủy']}],
    "['1', '1', '0', '0', '0', '0']": ['PHONG ĐỊA QUÁN','Họ Càn','HẠN BỒNG PHÙNG HÀ','Kim',{'4':'Thế'},{'1':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'1':['Tý','Thủy'],'5':['Thân','Kim']}],
    "['1', '0', '0', '0', '0', '0']": ['SƠN ĐỊA BÁC','Họ Càn','ƯNG THƯỚC ĐỒNG LÂM','Kim',{'5':'Thế'},{'2':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'5':['Thân','Kim']}],
    "['1', '0', '1', '0', '0', '0']": ['HỎA ĐỊA TẤN','Họ Càn(Du Hồn)','SỬ ĐỊA ĐẮC KIM','Kim',{'4':'Thế'},{'1':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']},{'1':['Tý','Thủy']}],
    "['1', '0', '1', '1', '1', '1']": ['HỎA THIÊN ĐẠI HỮU','Họ Càn(Quy Hồn)','TRẢM THỤ MÔ TƯỚC','Kim',{'3':'Thế'},{'6':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']}],
    "['0', '1', '1', '0', '1', '1']": ['BÁT THUẦN ĐOÀI','Họ Đoài(Lục Xung)','CHẨN THỦY HÒA NÊ','Kim',{'6':'Thế'},{'3':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']}],
    "['0', '1', '1', '0', '1', '0']": ['TRẠCH THỦY KHỐN','Họ Đoài','THOÁT LÃNG TRỪU ĐÊ','Kim',{'1':'Thế'},{'4':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']}],
    "['0', '1', '1', '0', '0', '0']": ['TRẠCH ĐỊA TỤY','Họ Đoài','LÝ NGƯ HỎA LONG','Kim',{'2':'Thế'},{'5':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']}],
    "['0', '1', '1', '1', '0', '0']": ['TRẠCH SƠN HÀM','Họ Đoài','MANH NHA XUẤT THỔ','Kim',{'3':'Thế'},{'6':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']},{'2':['Mão','Mộc']}],
    "['0', '1', '0', '1', '0', '0']": ['THỦY SƠN KIỂN','Họ Đoài','VŨ TUYẾT TẢI ĐỒ','Kim',{'4':'Thế'},{'1':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Thân','kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']},{'2':['Mão','Mộc']}],
    "['0', '0', '0', '1', '0', '0']": ['ĐỊA SƠN KHIÊM','Họ Đoài','NHỊ NHÂN PHÂN KIM','Kim',{'5':'Thế'},{'2':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']},{'2':['Mão','Mộc']}],
    "['0', '0', '1', '1', '0', '0']": ['LÔI SƠN TIỂU QUÁ','Họ Đoài(Du Hồn)','CẤP QUÁ ĐỘC KIỀU','Kim',{'4':'Thế'},{'1':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'2':['Mão','Mộc'],'4':['Hợi','Thủy']}],
    "['0', '0', '1', '0', '1', '1']": ['LÔI TRẠCH QUY MUỘI','Họ Đoài(Quy Hồn)','DUYÊN MỘC CẦU NGƯ','Kim',{'3':'Thế'},{'6':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'4':['Hợi','Thủy']}],
    "['1', '0', '1', '1', '0', '1']": ['BÁT THUẦN LY','Họ Ly(Lục Xung)','THIÊN QUAN TỨ PHÚC','Hỏa',{'6':'Thế'},{'3':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']}],
    "['1', '0', '1', '1', '0', '0']": ['HỎA SƠN LỮ','Họ Ly','TÚC ĐIỂU PHẦN SÀO','Hỏa',{'1':'Thế'},{'4':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']},{'1':['Mão','Mộc']}],
    "['1', '0', '1', '1', '1', '0']": ['HỎA PHONG ĐỈNH','Họ Ly','NGƯ NHÂN ĐẮC LỢI','Hỏa',{'2':'Thế'},{'5':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']},{'1':['Mão','Mộc']}],
    "['1', '0', '1', '0', '1', '0']": ['HỎA THỦY VỊ TẾ','Họ Ly','TIỂU NHÂN HÃM HẠI','Hỏa',{'3':'Thế'},{'6':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']},{'4':['Hợi','Thủy']}],
    "['1', '0', '0', '0', '1', '0']": ['SƠN THỦY MÔNG','Họ Ly','TIỂU QUỶ THÂU TIỀN','Hỏa',{'4':'Thế'},{'1':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'4':['Dậu','Kim']}],
    "['1', '1', '0', '0', '1', '0']": ['PHONG THỦY HOÁN','Họ Ly','CÁCH HÀ VỌNG KIM','Hỏa',{'5':'Thế'},{'2':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'3':['Hợi','Thủy'],'4':['Dậu','Kim']}],
    "['1', '1', '1', '0', '1', '0']": ['THIÊN THỦY TỤNG','Họ Ly(Du Hồn)','NHỊ NHÂN TRANH LỘ','Hỏa',{'4':'Thế'},{'1':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'3':['Hợi','Thủy']}],
    "['1', '1', '1', '1', '0', '1']": ['THIÊN HỎA ĐỒNG NHÂN','Họ Ly (Quy Hồn)','TIÊN NHÂN CHỈ LỘ','Hỏa',{'3':'Thế'},{'6':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']}],
    "['0', '0', '1', '0', '0', '1']": ['BÁT THUẦN CHẤN','Họ Chấn(Lục Xung)','KIM CHUNG DẠ TRÀNG','Mộc',{'6':'Thế'},{'3':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']}],
    "['0', '0', '1', '0', '0', '0']": ['LÔI ĐỊA DỰ','Họ Chấn','THANH LONG ĐẮC VỊ','Mộc',{'1':'Thế'},{'4':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'1':['Tý','Thủy']}],
    "['0', '0', '1', '0', '1', '0']": ['LÔI THỦY GIẢI','Họ Chấn','NGŨ QUAN THOÁT NẠN','Mộc',{'2':'Thế'},{'5':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'1':['Tý','Thủy']}],
    "['0', '0', '1', '1', '1', '0']": ['LÔI PHONG HẰNG','Họ Chấn','NGƯ LAI TRÀNG VÕNG','Mộc',{'3':'Thế'},{'6':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'2':['Dần','Mộc']}],
    "['0', '0', '0', '1', '1', '0']": ['ĐỊA PHONG THĂNG','Họ Chấn','CHỈ NHẬT CAO THĂNG','Mộc',{'4':'Thế'},{'1':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']},{'2':['Dần','Mộc'],'4':['Ngọ','Hỏa']}],
    "['0', '1', '0', '1', '1', '0']": ['THỦY PHONG TĨNH','Họ Chấn','KHÔ TINH SINH TUYỀN','Mộc',{'5':'Thế'},{'2':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']},{'2':['Dần','Mộc'],'4':['Ngọ','Hỏa']}],
    "['0', '1', '1', '1', '1', '0']": ['TRẠCH PHONG ĐẠI QUÁ','Họ Chấn(Du Hồn)','DẠ MỘNG KIM NGÂN','Mộc',{'4':'Thế'},{'1':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']},{'2':['Dần','Mộc'],'4':['Ngọ','Hỏa']}],
    "['0', '1', '1', '0', '0', '1']": ['TRẠCH LÔI TÙY','Họ Chấn(Quy Hồn)','BỘ BỘ ĐĂNG CAO','Mộc',{'3':'Thế'},{'6':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']},{'4':['Ngọ','Hỏa']}],
    "['1', '1', '0', '1', '1', '0']": ['BÁT THUẦN TỐN','Họ Tốn(Lục Xung)','CHÂU ĐẮC THUẬN PHONG','Mộc',{'6':'Thế'},{'3':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']}],
    "['1', '1', '0', '1', '1', '1']": ['PHONG THIÊN TIỂU SÚC','Họ Tốn','MẬT VÂN BẤT VŨ','Mộc',{'1':'Thế'},{'4':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'3':['Dậu','Kim']}],
    "['1', '1', '0', '1', '0', '1']": ['PHONG HỎA GIAI NHÂN','Họ Tốn','CẢNH LÝ QUAN HOA','Mộc',{'2':'Thế'},{'5':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'3':['Dậu','Kim']}],
    "['1', '1', '0', '0', '0', '1']": ['PHONG LÔI ÍCH','Họ Tốn','KHÔ MỘC KHAI HOA','Mộc',{'3':'Thế'},{'6':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'3':['Dậu','Kim']}],
    "['1', '1', '1', '0', '0', '1']": ['THIÊN LÔI VÔ VỌNG','Họ Tốn(Lục Xung)','ĐIỂU BỊ LAO XUNG','Mộc',{'4':'Thế'},{'1':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']}],
    "['1', '0', '1', '0', '0', '1']": ['HỎA LÔI PHỆ HẠP','Họ Tốn','CƠ NHÂN NGỘ THỰC','Mộc',{'5':'Thế'},{'2':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']}],
    "['1', '0', '0', '0', '0', '1']": ['SƠN LÔI DI','Họ Tốn(Du Hồn)','VỊ THỦY PHỎNG HIỀN','Mộc',{'4':'Thế'},{'1':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'3':['Dậu','Kim']}],
    "['1', '0', '0', '1', '1', '0']": ['SƠN PHONG CỔ','Họ Tốn(Quy Hồn)','THÔI MA PHẦN ĐẠO','Mộc',{'3':'Thế'},{'6':'Ứng'},{'1':['Sửu','Thổ'],'2':['Hợi','Thủy'],'3':['Dậu','Kim'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'5':['Tị','Hỏa']}],
    "['0', '1', '0', '0', '1', '0']": ['BÁT THUẦN KHẢM','Họ Khảm(Lục Xung)','THỦY ĐẾ LAO NGUYỆT','Thủy',{'6':'Thế'},{'3':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']}],
    "['0', '1', '0', '0', '1', '1']": ['THỦY TRẠCH TIẾT','Họ Khảm','TRẢM TƯỚNG PHONG THẦN','Thủy',{'1':'Thế'},{'4':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']}],
    "['0', '1', '0', '0', '0', '1']": ['THỦY LÔI TRUÂN','Họ Khảm','LOẠN TI VÔ ĐẦU','Thủy',{'2':'Thế'},{'5':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']},{'3':['Ngọ','Hỏa']}],
    "['0', '1', '0', '1', '0', '1']": ['THỦY HỎA KÝ TẾ','Họ Khảm','KIM BẢNG ĐỀ DANH','Thủy',{'3':'Thế'},{'6':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']},{'3':['Ngọ','Hỏa']}],
    "['0', '1', '1', '1', '0', '1']": ['TRẠCH HỎA CÁCH','Họ Khảm','HẠN MIÊU ĐẮC VŨ','Thủy',{'4':'Thế'},{'1':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']},{'3':['Ngọ','Hỏa']}],
    "['0', '0', '1', '1', '0', '1']": ['LÔI HỎA PHONG','Họ Khảm','CỐ KÍNH TRÙNG MINH','Thủy',{'5':'Thế'},{'2':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']}],
    "['0', '0', '0', '1', '0', '1']": ['ĐỊA HỎA MINH DI','Họ Khảm(Du Hồn)','QUÁ GIANG CHIẾT KIỀU','Thủy',{'4':'Thế'},{'1':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']},{'3':['Ngọ','Hỏa']}],
    "['0', '0', '0', '0', '1', '0']": ['ĐỊA THỦY SƯ','Họ Khảm(Quy Hồn)','MÃ ĐÁO THÀNH CÔNG','Thủy',{'3':'Thế'},{'6':'Ứng'},{'1':['Dần','Mộc'],'2':['Thìn','Thổ'],'3':['Ngọ','Hỏa'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']}],
    "['1', '0', '0', '1', '0', '0']": ['BÁT THUẦN CẤN','Họ Cấn(Lục Xung)','NHÂN ĐOẢN TÁO CAO','Thổ',{'6':'Thế'},{'3':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']}],
    "['1', '0', '0', '1', '0', '1']": ['SƠN HỎA BÍ','Họ Cấn','HỈ KHÍ DOANH MÔN','Thổ',{'1':'Thế'},{'4':'Ứng'},{'1':['Mão','Mộc'],'2':['Sửu','Thổ'],'3':['Hợi','Thủy'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'2':['Ngọ','Hỏa'],'3':['Thân','Kim']}],
    "['1', '0', '0', '1', '1', '1']": ['SƠN THIÊN ĐẠI SÚC','Họ Cấn','TRẬN THẾ ĐẮC KHAI','Thổ',{'2':'Thế'},{'5':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'2':['Ngọ','Hỏa'],'3':['Thân','Kim']}],
    "['1', '0', '0', '0', '1', '1']": ['SƠN TRẠCH TỔN','Họ Cấn','THÔI XA PHÍ LỰC','Thổ',{'3':'Thế'},{'6':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Tuất','Thổ'],'5':['Tý','Thủy'],'6':['Dần','Mộc']},{'3':['Thân','Kim']}],
    "['1', '0', '1', '0', '1', '1']": ['HỎA TRẠCH KHUÊ','Họ Cấn','PHẢN MAI TRƯ DƯƠNG','Thổ',{'4':'Thế'},{'1':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Dậu','Kim'],'5':['Mùi','Thổ'],'6':['Tị','Hỏa']},{'5':['Tý','Thủy']}],
    "['1', '1', '1', '0', '1', '1']": ['THIÊN TRẠCH LÝ','Họ Cấn','PHỤNG MINH KỲ SƠN','Thổ',{'5':'Thế'},{'2':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']},{'5':['Tý','Thủy']}],
    "['1', '1', '0', '0', '1', '1']": ['PHONG TRẠCH TRUNG PHU','Họ Cấn(Du Hồn)','HÀNH TẨU BẠC BĂNG','Thổ',{'4':'Thế'},{'1':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'3':['Thân','Kim'],'5':['Tý','Thủy']}],
    "['1', '1', '0', '1', '0', '0']": ['PHONG SƠN TIỆM','Họ Cấn(Quy Hồn)','TUẤN MÃ XUẤT LUNG','Thổ',{'3':'Thế'},{'6':'Ứng'},{'1':['Thìn','Thổ'],'2':['Ngọ','Hỏa'],'3':['Thân','Kim'],'4':['Mùi','Thổ'],'5':['Tị','Hỏa'],'6':['Mão','Mộc']},{'5':['Tý','Thủy']}],
    "['0', '0', '0', '0', '0', '0']": ['BÁT THUẦN KHÔN','Họ Khôn(Lục Xung)','NGẠ HỔ ĐẮC THỰC','Thổ',{'6':'Thế'},{'3':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']}],
    "['0', '0', '0', '0', '0', '1']": ['ĐỊA LÔI PHỤC','Họ Khôn','PHU THÊ PHẢN MỤC','Thổ',{'1':'Thế'},{'4':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']},{'2':['Tị','Hỏa']}],
    "['0', '0', '0', '0', '1', '1']": ['ĐỊA TRẠCH LÂM','Họ Khôn','PHÁT CHÍNH THI NHÂN','Thổ',{'2':'Thế'},{'5':'Ứng'},{'1':['Tị','Hỏa'],'2':['Mão','Mộc'],'3':['Sửu','Thổ'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']}],
    "['0', '0', '0', '1', '1', '1']": ['ĐỊA THIÊN THÁI','Họ Khôn(Lục Hợp)','HỈ BÁO TAM NGUYÊN','Thổ',{'3':'Thế'},{'6':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Sửu','Thổ'],'5':['Hợi','Thủy'],'6':['Dậu','Kim']},{'2':['Tị','Hỏa']}],
    "['0', '0', '1', '1', '1', '1']": ['LÔI THIÊN ĐẠI TRÁNG','Họ Khôn(Lục Xung)','CÔNG SƯ ĐẮC MỘC','Thổ',{'4':'Thế'},{'1':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Ngọ','Hỏa'],'5':['Thân','Kim'],'6':['Tuất','Thổ']}],
    "['0', '1', '1', '1', '1', '1']": ['TRẠCH THIÊN QUẢI','Họ Khôn','DU PHONG THOÁT VÕNG','Thổ',{'5':'Thế'},{'2':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Hợi','Thủy'],'5':['Dậu','Kim'],'6':['Mùi','Thổ']},{'2':['Tị','Hỏa']}],
    "['0', '1', '0', '1', '1', '1']": ['THỦY THIÊN NHU','Họ Khôn(Du Hồn)','MINH CHÂU XUẤT THỔ','Thổ',{'4':'Thế'},{'1':'Ứng'},{'1':['Tý','Thủy'],'2':['Dần','Mộc'],'3':['Thìn','Thổ'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']},{'2':['Tị','Hỏa']}],
    "['0', '1', '0', '0', '0', '0']": ['THỦY ĐỊA TỶ','Họ Khôn(Quy Hồn)','THUẬN PHONG HÀNH THUYỀN','Thổ',{'3':'Thế'},{'6':'Ứng'},{'1':['Mùi','Thổ'],'2':['Tị','Hỏa'],'3':['Mão','Mộc'],'4':['Thân','Kim'],'5':['Tuất','Thổ'],'6':['Tý','Thủy']}]
  }
  dia_chi = ('TÝ','SỬU','DẦN','MÃO','THÌN','TỴ','NGỌ','MÙI','THÂN','DẬU','TUẤT','HỢI')
  thien_can = ('GIÁP','ẤT','BÍNH','ĐINH','MẬU','KỶ','CANH','TÂN','NHÂM','QUÝ')
  dic_cannapgiap = {
    "['1', '1', '1', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất'},
    "['1', '1', '1', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất','quai_than':{'4':'Ngọ'}},
    "['1', '1', '1', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Giáp Ngọ','5':'Giáp Thân','6':'Giáp Tuất'},
    "['1', '1', '1', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất','quai_than':{'5':'Thân'}},
    "['1', '1', '0', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão'},
    "['1', '0', '0', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần','quai_than':{'4':'Tuất'}},
    "['1', '0', '1', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị','quai_than':{'3':'Mão'}},
    "['1', '0', '1', '1', '1', '1']": {'1':'Ất Tý','2':'Ất Dần','3':'Ất Thìn','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị','quai_than':{'2':'Dần'}},
    "['0', '1', '1', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi','quai_than':{'4':'Hợi'}},
    "['0', '1', '1', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi','quai_than':{'3':'Ngọ'}},
    "['0', '1', '1', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi','quai_than':{'1':'Mùi','6':'Mùi'}},
    "['0', '1', '1', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi'},
    "['0', '1', '0', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý'},
    "['0', '0', '0', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu'},
    "['0', '0', '1', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất','quai_than':{'2':'Mão'}},
    "['0', '0', '1', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất','quai_than':{'5':'Thân'}},
    "['1', '0', '1', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị','quai_than':{'6':'Tị'}},
    "['1', '0', '1', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị','quai_than':{'2':'Ngọ'}},
    "['1', '0', '1', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị','quai_than':{'1':'Sửu'}},
    "['1', '0', '1', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị'},
    "['1', '0', '0', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần','quai_than':{'5':'Dậu'}},
    "['1', '1', '0', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão','quai_than':{'2':'Thìn'}},
    "['1', '1', '1', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất'},
    "['1', '1', '1', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất'},
    "['0', '0', '1', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất'},
    "['0', '0', '1', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất','quai_than':{'4':'Ngọ'}},
    "['0', '0', '1', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất'},
    "['0', '0', '1', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất','quai_than':{'2':'Dần'}},
    "['0', '0', '0', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu','quai_than':{'3':'Dậu','6':'Dậu'}},
    "['0', '1', '0', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý'},
    "['0', '1', '1', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi'},
    "['0', '1', '1', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi'},
    "['1', '1', '0', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão','quai_than':{'5':'Tị'}},
    "['1', '1', '0', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão','quai_than':{'1':'Tý'}},
    "['1', '1', '0', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão','quai_than':{'4':'Mùi'}},
    "['1', '1', '0', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão'},
    "['1', '1', '1', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất'},
    "['1', '0', '1', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị'},
    "['1', '0', '0', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần','quai_than':{'3':'Dậu'}},
    "['1', '0', '0', '1', '1', '0']": {'1':'Tân Sửu','2':'Tân Hợi','3':'Tân Dậu','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần','quai_than':{'6':'Dần'}},
    "['0', '1', '0', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý'},
    "['0', '1', '0', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý','quai_than':{'6':'Tý'}},
    "['0', '1', '0', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý'},
    "['0', '1', '0', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý'},
    "['0', '1', '1', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi','quai_than':{'1':'Mão'}},
    "['0', '0', '1', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất','quai_than':{'6':'Tuất'}},
    "['0', '0', '0', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu','quai_than':{'6':'Dậu'}},
    "['0', '0', '0', '0', '1', '0']": {'1':'Mậu Dần','2':'Mậu Thìn','3':'Mậu Ngọ','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu'},
    "['1', '0', '0', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần'},
    "['1', '0', '0', '1', '0', '1']": {'1':'Kỷ Mão','2':'Kỷ Sửu','3':'Kỷ Hợi','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần','quai_than':{'5':'Tý'}},
    "['1', '0', '0', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần'},
    "['1', '0', '0', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Bính Tuất','5':'Bính Tý','6':'Bính Dần'},
    "['1', '0', '1', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Kỷ Dậu','5':'Kỷ Mùi','6':'Kỷ Tị'},
    "['1', '1', '1', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Nhâm Ngọ','5':'Nhâm Thân','6':'Nhâm Tuất'},
    "['1', '1', '0', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão','quai_than':{'2':'Mão','6':'Mão'}},
    "['1', '1', '0', '1', '0', '0']": {'1':'Bính Thìn','2':'Bính Ngọ','3':'Bính Thân','4':'Tân Mùi','5':'Tân Tị','6':'Tân Mão'},
    "['0', '0', '0', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu','quai_than':{'5':'Hợi'}},
    "['0', '0', '0', '0', '0', '1']": {'1':'Canh Tý','2':'Canh Dần','3':'Canh Thìn','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu','quai_than':{'1':'Tý'}},
    "['0', '0', '0', '0', '1', '1']": {'1':'Đinh Tị','2':'Đinh Mão','3':'Đinh Sửu','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu','quai_than':{'3':'Sửu'}},
    "['0', '0', '0', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Quý Sửu','5':'Quý Hợi','6':'Quý Dậu','quai_than':{'2':'Dần'}},
    "['0', '0', '1', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Canh Ngọ','5':'Canh Thân','6':'Canh Tuất'},
    "['0', '1', '1', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Đinh Hợi','5':'Đinh Dậu','6':'Đinh Mùi','quai_than':{'3':'Thìn'}},
    "['0', '1', '0', '1', '1', '1']": {'1':'Giáp Tý','2':'Giáp Dần','3':'Giáp Thìn','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý'},
    "['0', '1', '0', '0', '0', '0']": {'1':'Ất Mùi','2':'Ất Tị','3':'Ất Mão','4':'Mậu Thân','5':'Mậu Tuất','6':'Mậu Tý','quai_than':{'4':'Thân'}},
  }

  lich_tiet_khi={'DẦN':['Lập xuân','Vũ thủy'],'MÃO':['Kinh trập','Xuân phân'],'THÌN':['Thanh minh','Cốc vũ'],
  'TỴ':['Lập hạ','Tiểu mãn'],'NGỌ':['Mang chủng','Hạ chí'],'MÙI':['Tiểu thử','Đại thử'],
  'THÂN':['Lập thu','Xử thử'],'DẬU':['Bạch lộ','Thu phân'],'TUẤT':['Hàn lộ','Sương giáng'],'HỢI':['Lập đông','Tiểu tuyết'],'TÝ':['Đại tuyết','Đông chí'],'SỬU':['Tiểu hàn','Đại hàn']}

  def xacdinhnguhanh(chi):
    nguhanh = KINHDICH.dic_chi_nguhanh[chi]
    chi = chi.capitalize()
    ngu_hanh = f'{chi} {nguhanh}'
    return ngu_hanh

  # @classmethod
  def lapque(chi_gio,ngay,thang,chi_nam):
    que_dich = {}
    thuongquai = (ngay + thang + KINHDICH.dic_dia_chi[chi_nam])%8
    if thuongquai == 0:
      thuongquai = 8
    que_dich['thuongquai'] = thuongquai
    haquai = (KINHDICH.dic_dia_chi[chi_gio] + ngay + thang + KINHDICH.dic_dia_chi[chi_nam])%8
    if haquai == 0:
      haquai = 8
    que_dich['haquai'] = haquai
    haodong = (KINHDICH.dic_dia_chi[chi_gio] + ngay + thang + KINHDICH.dic_dia_chi[chi_nam])%6
    if haodong == 0:
      haodong = 6
    que_dich['haodong'] = haodong
    return que_dich

  def tongquetren(chi_gio,ngay,thang,chi_nam):
    lap_que = KINHDICH.lapque(chi_gio,ngay,thang,chi_nam)
    thuongquai = str(lap_que['thuongquai'])
    haquai = str(lap_que['haquai'])
    haodong = str(lap_que['haodong'])
    haoquedich = {}
    array_thuongquai =  KINHDICH.dic_quedich[thuongquai]
    array_haquai =  KINHDICH.dic_quedich[haquai]
    array_thuonghaquai = enumerate(array_thuongquai + array_haquai)
    for idx, val in array_thuonghaquai:
      if val == 1:
        hao = KINHDICH.dic_amduong[val]
      else:
        hao = KINHDICH.dic_amduong[val]
      if idx == 0:
        haoquedich['6'] = hao
      elif idx == 1:
        haoquedich['5'] = hao
      elif idx == 2:
        haoquedich['4'] = hao
      elif idx == 3:
        haoquedich['3'] = hao
      elif idx == 4:
        haoquedich['2'] = hao
      elif idx == 5:
        haoquedich['1'] = hao
     # {'6': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',
     # '5': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',
     # '4': '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>',
     # '3': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>',
     # '2': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>',
     # '1': '<tr><td class="bgblue">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgblue">&nbsp;</td></tr>'}
    return haoquedich

  def tongquehaodong(chi_gio,ngay,thang,chi_nam):
    lap_que = KINHDICH.lapque(chi_gio,ngay,thang,chi_nam)
    haodong = str(lap_que['haodong'])
    tong_quetren = KINHDICH.tongquetren(chi_gio,ngay,thang,chi_nam)
    haoquedich = {}
    for key, val in tong_quetren.items():
      if key == haodong:
        if val == '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>':
          val = '<tr><td colspan="3" class="bgred">&nbsp;</td></tr>'
        else:
          val = '<tr><td class="bgred">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgred">&nbsp;</td></tr>'
      haoquedich[key] = val
    return haoquedich

  def tongquehaohotro(chi_gio,ngay,thang,chi_nam):
    tong_quetren = KINHDICH.tongquetren(chi_gio,ngay,thang,chi_nam)
    haoquedich = {}
    for key, val in tong_quetren.items():
      if key == '2':
        haoquedich['1'] = val
      elif key == '3':
        haoquedich['2'] = val
        haoquedich['4'] = val
      elif key == '4':
        haoquedich['3'] = val
        haoquedich['5'] = val
      elif key == '5':
        haoquedich['6'] = val
    return haoquedich

  def tongquehaoketqua(chi_gio,ngay,thang,chi_nam):
    lap_que = KINHDICH.lapque(chi_gio,ngay,thang,chi_nam)
    haodong = str(lap_que['haodong'])
    tong_quetren = KINHDICH.tongquetren(chi_gio,ngay,thang,chi_nam)
    haoquedich = {}
    for key, val in tong_quetren.items():
      if key == haodong:
        if val == '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>':
          val = '<tr><td class="bgred">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgred">&nbsp;</td></tr>'
        else:
          val = '<tr><td colspan="3" class="bgred">&nbsp;</td></tr>'
      haoquedich[key] = val
    return haoquedich

  def tenque(chi_gio,ngay,thang,chi_nam,can_ngay,chi_ngay):
    chi_ngay = chi_ngay.capitalize()
    ten_que = {}
    lap_que = KINHDICH.lapque(chi_gio,ngay,thang,chi_nam)
    haodong = str(lap_que['haodong'])
    # xác định quẻ chính
    quechinh = KINHDICH.tongquetren(chi_gio,ngay,thang,chi_nam)
    que_chinh = []
    for key, val in quechinh.items():
      if key == haodong:
        ten_que['haodong'] = key
      if val == '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>':
        num = '1'
      else:
        num = '0'
      que_chinh.append(num)
    que_chinh = str(que_chinh)
    ten_que['quechinh'] = KINHDICH.dic_tenque[que_chinh]
    ten_que['thien_can_que_chinh'] = KINHDICH.dic_cannapgiap[que_chinh]
    nguhanh = ten_que['quechinh']
    nguhanh_quegoc = nguhanh[3] # lấy ngũ hành quẻ gốc ra để so sánh
    tong_nguhanhque_chinh = nguhanh[6]
    ngu_hanh = {}
    ngu_hanh_an = {}
    ngu_hanh_khongvong = {}
    quy_nhan_que_chinh = {}
    loc_que_chinh = {}
    dichma_que_chinh = {}
    daohoa_que_chinh = {}
    for key,val in tong_nguhanhque_chinh.items():
      luc_than = KINHDICH.lucthan(nguhanh_quegoc, val[1])
      ngu_hanh[key] = luc_than
      quy_nhan_que_chinh[key] = KINHDICH.quynhan(can_ngay,val[0])
      loc_que_chinh[key] = KINHDICH.loc(can_ngay,val[0])
      dichma_que_chinh[key] = KINHDICH.dichma(chi_ngay,val[0])
      daohoa_que_chinh[key] = KINHDICH.daohoa(chi_ngay,val[0])

    ten_que['lucthan_quechinh'] = ngu_hanh
    ten_que['quynhan_que_chinh'] = quy_nhan_que_chinh
    ten_que['loc_que_chinh'] = loc_que_chinh
    ten_que['dichma_que_chinh'] = dichma_que_chinh
    ten_que['daohoa_que_chinh'] = daohoa_que_chinh
    if len(nguhanh) == 8:
      tong_nguhanhque_chinh_an = nguhanh[7]
      for key,val in tong_nguhanhque_chinh_an.items():
        luc_than = KINHDICH.lucthan_haophuc(nguhanh_quegoc, val[1])
        luc_than = luc_than + '-' + val[0]
        ngu_hanh_an[key] = luc_than
    ten_que['lucthan_quean'] = ngu_hanh_an

    # xác định quẻ hỗ trợ
    queho = KINHDICH.tongquehaohotro(chi_gio,ngay,thang,chi_nam)
    queho = dict( sorted(queho.items(),key=lambda item: item[0],reverse=True))
    que_ho = []
    for key, val in queho.items():
      if val == '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>':
        num = '1'
      else:
        num = '0'
      que_ho.append(num)
    que_ho = str(que_ho)
    ten_que['queho'] = KINHDICH.dic_tenque[que_ho]

    # xác định quẻ kết quả
    quekq = KINHDICH.tongquehaoketqua(chi_gio,ngay,thang,chi_nam)
    quekq = dict( sorted(quekq.items(),key=lambda item: item[0],reverse=True))
    que_kq = []
    for key, val in quekq.items():
      if val == '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>' or val == '<tr><td colspan="3" class="bgred">&nbsp;</td></tr>':
        num = '1'
      else:
        num = '0'
      que_kq.append(num)
    que_kq = str(que_kq)
    ten_que['thien_can_que_kq'] = KINHDICH.dic_cannapgiap[que_kq]
    ten_que['quekq'] = KINHDICH.dic_tenque[que_kq]
    nguhanh_kq = ten_que['quekq']
    tong_nguhanhque_kq = nguhanh_kq[6]
    ngu_hanh_kq = {}
    quy_nhan_que_kq = {}
    loc_que_kq = {}
    dichma_que_kq = {}
    daohoa_que_kq = {}
    for key,val in tong_nguhanhque_kq.items():
      luc_than = KINHDICH.lucthan(nguhanh_quegoc, val[1])
      ngu_hanh_kq[key] = luc_than
      quy_nhan_que_kq[key] = KINHDICH.quynhan(can_ngay,val[0])
      loc_que_kq[key] = KINHDICH.loc(can_ngay,val[0])
      dichma_que_kq[key] = KINHDICH.dichma(chi_ngay,val[0])
      daohoa_que_kq[key] = KINHDICH.daohoa(chi_ngay,val[0])
    ten_que['lucthan_kq'] = ngu_hanh_kq
    ten_que['quy_nhan_que_kq'] = quy_nhan_que_kq
    ten_que['loc_que_kq'] = loc_que_kq
    ten_que['dichma_que_kq'] = dichma_que_kq
    ten_que['daohoa_que_kq'] = daohoa_que_kq

    return ten_que

  def lucthan(nguhanh_quegoc, nguhanh_hao):
    if nguhanh_quegoc == 'Kim':
      if nguhanh_hao == 'Thủy':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Kim':
        nguhanh = 'Huynh Đệ'
      elif nguhanh_hao == 'Mộc':
        nguhanh = 'Thê Tài'
      elif nguhanh_hao == 'Hỏa':
        nguhanh = 'Quan Quỷ'
      else:
        nguhanh = 'Phụ Mẫu'
    elif nguhanh_quegoc == 'Mộc':
      if nguhanh_hao == 'Hỏa':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Mộc':
        nguhanh = 'Huynh Đệ'
      elif nguhanh_hao == 'Thổ':
        nguhanh = 'Thê Tài'
      elif nguhanh_hao == 'Kim':
        nguhanh = 'Quan Quỷ'
      else:
        nguhanh = 'Phụ Mẫu'
    elif nguhanh_quegoc == 'Thủy':
      if nguhanh_hao == 'Kim':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Thủy':
        nguhanh = 'Huynh Đệ'
      elif nguhanh_hao == 'Hỏa':
        nguhanh = 'Thê Tài'
      elif nguhanh_hao == 'Thổ':
        nguhanh = 'Quan Quỷ'
      else:
        nguhanh = 'Phụ Mẫu'
    elif nguhanh_quegoc == 'Hỏa':
      if nguhanh_hao == 'Thổ':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Hỏa':
        nguhanh = 'Huynh Đệ'
      elif nguhanh_hao == 'Kim':
        nguhanh = 'Thê Tài'
      elif nguhanh_hao == 'Thủy':
        nguhanh = 'Quan Quỷ'
      else:
        nguhanh = 'Phụ Mẫu'
    elif nguhanh_quegoc == 'Thổ':
      if nguhanh_hao == 'Kim':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Thổ':
        nguhanh = 'Huynh Đệ'
      elif nguhanh_hao == 'Thủy':
        nguhanh = 'Thê Tài'
      elif nguhanh_hao == 'Mộc':
        nguhanh = 'Quan Quỷ'
      else:
        nguhanh = 'Phụ Mẫu'
    return nguhanh

  # xác định lục thân bị ẩn
  def lucthan_haophuc(nguhanh_quegoc, nguhanh_hao):
    if nguhanh_quegoc == 'Kim':
      if nguhanh_hao == 'Thủy':
        nguhanh = 'Tử'
      elif nguhanh_hao == 'Kim':
        nguhanh = 'Huynh'
      elif nguhanh_hao == 'Mộc':
        nguhanh = 'Thê'
      elif nguhanh_hao == 'Hỏa':
        nguhanh = 'Quan'
      else:
        nguhanh = 'Phụ'
    elif nguhanh_quegoc == 'Mộc':
      if nguhanh_hao == 'Hỏa':
        nguhanh = 'Tử '
      elif nguhanh_hao == 'Mộc':
        nguhanh = 'Huynh'
      elif nguhanh_hao == 'Thổ':
        nguhanh = 'Thê'
      elif nguhanh_hao == 'Kim':
        nguhanh = 'Quan'
      else:
        nguhanh = 'Phụ'
    elif nguhanh_quegoc == 'Thủy':
      if nguhanh_hao == 'Kim':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Thủy':
        nguhanh = 'Huynh'
      elif nguhanh_hao == 'Hỏa':
        nguhanh = 'Thê'
      elif nguhanh_hao == 'Thổ':
        nguhanh = 'Quan'
      else:
        nguhanh = 'Phụ'
    elif nguhanh_quegoc == 'Hỏa':
      if nguhanh_hao == 'Thổ':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Hỏa':
        nguhanh = 'Huynh'
      elif nguhanh_hao == 'Kim':
        nguhanh = 'Thê'
      elif nguhanh_hao == 'Thủy':
        nguhanh = 'Quan'
      else:
        nguhanh = 'Phụ'
    elif nguhanh_quegoc == 'Thổ':
      if nguhanh_hao == 'Kim':
        nguhanh = 'Tử Tôn'
      elif nguhanh_hao == 'Thổ':
        nguhanh = 'Huynh'
      elif nguhanh_hao == 'Thủy':
        nguhanh = 'Thê'
      elif nguhanh_hao == 'Mộc':
        nguhanh = 'Quan'
      else:
        nguhanh = 'Phụ'
    return nguhanh

  # xác định lục thú
  def lucthu(can_ngay):
    can_ngay = can_ngay.capitalize()
    if can_ngay == 'Giáp' or can_ngay == 'Ất':
      luc_thu = {'1':"Thanh Long",'2':"Chu Tước",'3':"Câu Trần",'4':"Đằng Xà",'5':"Bạch Hổ",'6':"Huyền Vũ"}
    elif can_ngay == 'Bính' or can_ngay == 'Đinh':
      luc_thu = {'6':"Thanh Long",'1':"Chu Tước",'2':"Câu Trần",'3':"Đằng Xà",'4':"Bạch Hổ",'5':"Huyền Vũ"}
    elif can_ngay == 'Mậu':
      luc_thu = {'5':"Thanh Long",'6':"Chu Tước",'1':"Câu Trần",'2':"Đằng Xà",'3':"Bạch Hổ",'4':"Huyền Vũ"}
    elif can_ngay == 'Kỷ':
      luc_thu = {'4':"Thanh Long",'5':"Chu Tước",'6':"Câu Trần",'1':"Đằng Xà",'2':"Bạch Hổ",'3':"Huyền Vũ"}
    elif can_ngay == 'Canh' or can_ngay == 'Tân':
      luc_thu = {'3':"Thanh Long",'4':"Chu Tước",'5':"Câu Trần",'6':"Đằng Xà",'1':"Bạch Hổ",'2':"Huyền Vũ"}
    elif can_ngay == 'Nhâm' or can_ngay == 'Quý':
      luc_thu = {'2':"Thanh Long",'3':"Chu Tước",'4':"Câu Trần",'5':"Đằng Xà",'6':"Bạch Hổ",'1':"Huyền Vũ"}
    return luc_thu

  def khongvong(can,chi,chi_khac):
    print()
    chican_kv = []
    index = KINHDICH.thien_can.index(can)
    index_m = KINHDICH.dia_chi.index(chi)
    chi_dau = int(index_m-index) -1
    chican_kv.append(dia_chi[chi_dau])
    chi_sau = chi_dau - 1
    chican_kv.append(dia_chi[chi_sau])
    # print('The index of e:', chican_kv)
    if chi_khac in chican_kv:
        return 'KV'
    return ''

  def quynhan(can_ngay,val):
    quy_nhan = ''
    if can_ngay == 'GIÁP' or can_ngay == 'MẬU':
        if val == 'Sửu':
          quy_nhan = 'Sửu'
        elif val == 'Mùi':
          quy_nhan = 'Mùi'
        else:
          quy_nhan = ''
    elif can_ngay == 'ẤT' or can_ngay == 'KỶ':
      if val == 'Tý':
        quy_nhan = 'Tý'
      elif val == 'Thân':
        quy_nhan = 'Thân'
      else:
        quy_nhan = ''
    elif can_ngay == 'BÍNH' or can_ngay == 'ĐINH':
      if val == 'Dậu':
        quy_nhan = 'Dậu'
      elif val == 'Hợi':
        quy_nhan = 'Hợi'
      else:
        quy_nhan = ''
    elif can_ngay == 'NHÂM' or can_ngay == 'QUÝ':
      if val == 'Mão':
        quy_nhan = 'Mão'
      elif val == 'Tị':
        quy_nhan = 'Tị'
      else:
        quy_nhan = ''
    elif can_ngay == 'CANH' or can_ngay == 'TÂN':
      if val == 'Ngọ':
        quy_nhan = 'Ngọ'
      elif val == 'Dần':
        quy_nhan = 'Dần'
      else:
        quy_nhan = ''
    return quy_nhan

  def loc(can_ngay,val):
    quy_nhan = ''
    if can_ngay == 'GIÁP':
        if val == 'Dần':
          quy_nhan = 'Dần'
        else:
          quy_nhan = ''
    elif can_ngay == 'ẤT':
      if val == 'Mão':
        quy_nhan = 'Mão'
      else:
        quy_nhan = ''
    elif can_ngay == 'BÍNH' or can_ngay == 'MẬU':
      if val == 'Tị':
        quy_nhan = 'Tị'
      else:
        quy_nhan = ''
    elif can_ngay == 'ĐINH' or can_ngay == 'KỶ':
      if val == 'Ngọ':
        quy_nhan = 'Ngọ'
      else:
        quy_nhan = ''
    elif can_ngay == 'CANH':
      if val == 'Thân':
        quy_nhan = 'Thân'
      else:
        quy_nhan = ''
    elif can_ngay == 'TÂN':
      if val == 'Dậu':
        quy_nhan = 'Dậu'
      else:
        quy_nhan = ''
    elif can_ngay == 'NHÂM':
      if val == 'Hợi':
        quy_nhan = 'Hợi'
      else:
        quy_nhan = ''
    elif can_ngay == 'QUÝ':
      if val == 'Tý':
        quy_nhan = 'Tý'
      else:
        quy_nhan = ''

    return quy_nhan

  def dichma(chi_ngay,val):
    quy_nhan = ''
    if chi_ngay == 'Thân' or chi_ngay == 'Tý' or chi_ngay == 'Thìn':
      if val == 'Dần':
        quy_nhan = 'Dần'
      else:
        quy_nhan = ''
    elif chi_ngay == 'Tỵ' or chi_ngay == 'Dậu' or chi_ngay == 'Sửu':
      if val == 'Hợi':
        quy_nhan = 'Hợi'
      else:
        quy_nhan = ''
    elif chi_ngay == 'Dần' or chi_ngay == 'Ngọ' or chi_ngay == 'Tuất':
      if val == 'Thân':
        quy_nhan = 'Thân'
      else:
        quy_nhan = ''
    elif chi_ngay == 'Hợi' or chi_ngay == 'Mão' or chi_ngay == 'Mùi':
      if val == 'Tị':
        quy_nhan = 'Tị'
      else:
        quy_nhan = ''

    return quy_nhan

  def daohoa(chi_ngay,val):
    quy_nhan = ''
    if chi_ngay == 'Thân' or chi_ngay == 'Tý' or chi_ngay == 'Thìn':
      if val == 'Dậu':
        quy_nhan = 'Dậu'
      else:
        quy_nhan = ''
    elif chi_ngay == 'Tỵ' or chi_ngay == 'Dậu' or chi_ngay == 'Sửu':
      if val == 'Ngọ':
        quy_nhan = 'Ngọ'
      else:
        quy_nhan = ''
    elif chi_ngay == 'Dần' or chi_ngay == 'Ngọ' or chi_ngay == 'Tuất':
      if val == 'Mão':
        quy_nhan = 'Mão'
      else:
        quy_nhan = ''
    elif chi_ngay == 'Hợi' or chi_ngay == 'Mão' or chi_ngay == 'Mùi':
      if val == 'Tý':
        quy_nhan = 'Tý'
      else:
        quy_nhan = ''

    return quy_nhan

  def lucxung(chi_1,chi_2):
    chi_1 = chi_1.capitalize()
    chi_2 = chi_2.capitalize()
    luc_xung = False
    if chi_1 == 'Dần' and chi_2 == 'Thân' or chi_2 == 'Dần' and chi_1 == 'Thân':
      luc_xung = True
    elif chi_1 == 'Tỵ' and chi_2 == 'Hợi' or chi_2 == 'Tỵ' and chi_1 == 'Hợi':
      luc_xung = True
    elif chi_1 == 'Tý' and chi_2 == 'Ngọ' or chi_2 == 'Tý' and chi_1 == 'Ngọ':
      luc_xung = True
    elif chi_1 == 'Mão' and chi_2 == 'Dậu' or chi_2 == 'Mão' and chi_1 == 'Dậu':
      luc_xung = True
    elif chi_1 == 'Thìn' and chi_2 == 'Tuất' or chi_2 == 'Thìn' and chi_1 == 'Tuất':
      luc_xung = True
    elif chi_1 == 'Sửu' and chi_2 == 'Mùi' or chi_2 == 'Sửu' and chi_1 == 'Mùi':
      luc_xung = True
    return luc_xung

  def luckhac(chi_1,chi_2):
    chi_1 = chi_1.capitalize()
    chi_2 = chi_2.capitalize()
    luc_khac = False
    if chi_1 == 'Thân' and chi_2 == 'Mão' or chi_1 == 'Dậu' and chi_2 == 'Dần':
      luc_khac = True
    elif chi_1 == 'Tý' and chi_2 == 'Tỵ' or chi_1 == 'Hợi' and chi_2 == 'Ngọ':
      luc_khac = True
    elif chi_1 == 'Tỵ' and chi_2 == 'Dậu' or chi_1 == 'Ngọ' and chi_2 == 'Thân' or chi_1 == 'Ngọ' and chi_2 == 'Dậu':
      luc_khac = True
    elif chi_1 == 'Sửu' and chi_2 == 'Tý' or chi_1 == 'Sửu' and chi_2 == 'Hợi':
      luc_khac = True
    elif chi_1 == 'Thìn' and chi_2 == 'Tý' or chi_1 == 'Thìn' and chi_2 == 'Hợi':
      luc_khac = True
    elif chi_1 == 'Mùi' and chi_2 == 'Tý' or chi_1 == 'Mùi' and chi_2 == 'Hợi':
      luc_khac = True
    elif chi_1 == 'Tuất' and chi_2 == 'Tý' or chi_1 == 'Tuất' and chi_2 == 'Hợi':
      luc_khac = True
    elif chi_1 == 'Dần' and chi_2 == 'Sửu' or chi_1 == 'Mão' and chi_2 == 'Sửu':
      luc_khac = True
    elif chi_1 == 'Dần' and chi_2 == 'Thìn' or chi_1 == 'Mão' and chi_2 == 'Thìn':
      luc_khac = True
    elif chi_1 == 'Dần' and chi_2 == 'Mùi' or chi_1 == 'Mão' and chi_2 == 'Mùi':
      luc_khac = True
    elif chi_1 == 'Dần' and chi_2 == 'Tuất' or chi_1 == 'Mão' and chi_2 == 'Tuất':
      luc_khac = True
    return luc_khac

  def tuongsinh(chi_1,chi_2):
    chi_1 = chi_1.capitalize()
    chi_2 = chi_2.capitalize()
    tuong_sinh = False
    luc_hop = KINHDICH.luchop(chi_1,chi_2)
    if luc_hop == True:
      tuong_sinh = True
    if chi_1 == 'Tý' and (chi_2 == 'Tý' or chi_2 == 'Mão'):
      tuong_sinh = True
    elif chi_1 == 'Hợi' and (chi_2 == 'Hợi' or chi_2 == 'Mão'):
      tuong_sinh = True
    elif chi_1 == 'Dần' and (chi_2 == 'Dần' or chi_2 == 'Tỵ' or chi_2 == 'Ngọ'):
      tuong_sinh = True
    elif chi_1 == 'Mão' and (chi_2 == 'Mão' or chi_2 == 'Tỵ' or chi_2 == 'Ngọ'):
      tuong_sinh = True
    elif chi_1 == 'Tỵ' and (chi_2 == 'Tỵ' or chi_2 == 'Sửu' or chi_2 == 'Thìn' or chi_2 == 'Mùi' or chi_2 == 'Tuất'):
      tuong_sinh = True
    elif chi_1 == 'Ngọ' and (chi_2 == 'Ngọ' or chi_2 == 'Sửu' or chi_2 == 'Thìn' or chi_2 == 'Mùi' or chi_2 == 'Tuất'):
      tuong_sinh = True
    elif chi_1 == 'Sửu' and (chi_2 == 'Sửu' or chi_2 == 'Thân' or chi_2 == 'Dậu'):
      tuong_sinh = True
    elif chi_1 == 'Thìn' and (chi_2 == 'Thìn' or chi_2 == 'Thân' or chi_2 == 'Dậu'):
      tuong_sinh = True
    elif chi_1 == 'Mùi' and (chi_2 == 'Mùi' or chi_2 == 'Thân' or chi_2 == 'Dậu'):
      tuong_sinh = True
    elif chi_1 == 'Tuất' and (chi_2 == 'Tuất' or chi_2 == 'Thân' or chi_2 == 'Dậu'):
      tuong_sinh = True
    elif chi_1 == 'Thân' and (chi_2 == 'Thân' or chi_2 == 'Hợi' or chi_2 == 'Tý'):
      tuong_sinh = True
    elif chi_1 == 'Dậu' and (chi_2 == 'Dậu' or chi_2 == 'Hợi' or chi_2 == 'Tý'):
      tuong_sinh = True
    return tuong_sinh

  def amdonghaodong(chi_gio,ngay,thang,chi_nam,can_ngay,chi_ngay,chi_thang):
    ten_que = KINHDICH.tenque(chi_gio,ngay,thang,chi_nam,can_ngay,chi_ngay)
    haodong = ten_que['haodong']
    que_chinh = KINHDICH.tongquehaodong(chi_gio,ngay,thang,chi_nam)
    amdong = {}
    num_kv = []
    for key,val in ten_que['quechinh'][6].items():
      chi_khac = (val[0]).upper()
      khong_vong = KINHDICH.khongvong(can_ngay,chi_ngay,chi_khac)
      if khong_vong == 'KV':
        luc_xung = KINHDICH.lucxung(chi_ngay,val[0])
        if luc_xung == True:
          num_kv.append(key)
      chithang = KINHDICH.tuongsinh(chi_thang,val[0])
      chingay = KINHDICH.lucxung(chi_ngay,val[0])
      if chithang == True and chingay == True:
        num_kv.append(key)

    num_kv = list(dict.fromkeys(num_kv))
    if len(num_kv) > 0:
      for num in num_kv:
        if num != haodong:
          for key,val in que_chinh.items():
            if key == num:
              if val == '<tr><td colspan="3" class="bgblue">&nbsp;</td></tr>':
                val = '<tr><td colspan="3" class="bgyellow">&nbsp;</td></tr>'
              else:
                val = '<tr><td class="bgyellow">&nbsp;</td><td class="widthkdsmall">&nbsp;</td><td class="bgyellow">&nbsp;</td></tr>'
            amdong[key] = val
    else:
      for key,val in que_chinh.items():
        amdong[key] = val
    return amdong

  def quaithan(chi_gio,ngay,thang,chi_nam,can_ngay,chi_ngay):
    quai_than = {}
    ten_que = KINHDICH.tenque(chi_gio,ngay,thang,chi_nam,can_ngay,chi_ngay)
    for key in ten_que['quechinh'][4]:
      the = key
      for key,val in ten_que['quechinh'][6].items():
        if the == key:
          if val[0] == 'Tý':
            quai_than['1'] = val[0]
          elif val[0] == 'Ngọ':
            quai_than['1'] = val[0]
          elif val[0] == 'Sửu':
            quai_than['2'] = val[0]
          elif val[0] == 'Mùi':
            quai_than['2'] = val[0]
          elif val[0] == 'Dần':
            quai_than['3'] = val[0]
          elif val[0] == 'Thân':
            quai_than['3'] = val[0]
          elif val[0] == 'Mão':
            quai_than['4'] = val[0]
          elif val[0] == 'Dậu':
            quai_than['4'] = val[0]
          elif val[0] == 'Thìn':
            quai_than['5'] = val[0]
          elif val[0] == 'Tuất':
            quai_than['5'] = val[0]
          elif val[0] == 'Tỵ':
            quai_than['6'] = val[0]
          elif val[0] == 'Mùi':
            quai_than['Hợi'] = val[0]
    return quai_than

  def luchop(chi_1,chi_2):
    chi_1 = chi_1.capitalize()
    chi_2 = chi_2.capitalize()
    luc_hop = False
    if chi_1 == 'Tý' and chi_2 == 'Sửu' or chi_2 == 'Tý' and chi_1 == 'Sửu':
      luc_hop = True
    elif chi_1 == 'Hợi' and chi_2 == 'Dần' or chi_1 == 'Dần' and chi_2 == 'Hợi':
      luc_hop = True
    elif chi_1 == 'Mão' and chi_2 == 'Tuất' or chi_1 == 'Tuất' and chi_2 == 'Mão':
      luc_hop = True
    elif chi_1 == 'Thìn' and chi_2 == 'Dậu' or chi_1 == 'Dậu' and chi_2 == 'Thìn':
      luc_hop = True
    elif chi_1 == 'Tỵ' and chi_2 == 'Thân' or chi_1 == 'Thân' and chi_2 == 'Tỵ':
      luc_hop = True
    elif chi_1 == 'Ngọ' and chi_2 == 'Mùi' or chi_2 == 'Ngọ' and chi_1 == 'Mùi':
      luc_hop = True
    return luc_hop

  def lichtietkhi(hours,minute,day,month,year):
    tiet_khi = {}

    if month == 12:
      before_month = month - 1
      last_month = 1
      last_tietkhi = LichTietKhi.objects.filter(year=year+1,month=last_month).values('daytiekhi')
      print("last_tietkhi : ",last_tietkhi)
      before_tietkhi = LichTietKhi.objects.filter(year=year,month__in=[before_month,month]).values('daytiekhi')
      print("before_tietkhi : ",before_tietkhi)
      # before_tietkhi :  <QuerySet [{'daytiekhi': '7/11/2021 11:57 AM'}, {'daytiekhi': '22/11/2021 9:32 AM'},
      # {'daytiekhi': '7/12/2021 4:55 AM'}, {'daytiekhi': '21/12/2021 10:58 PM'}]>
      # last_tietkhi :  <QuerySet [{'daytiekhi': '5/1/2022 4:12 PM'}, {'daytiekhi': '20/1/2022 9:37 AM'}]>
      year_tietkhi_1 = before_tietkhi[1]['daytiekhi']
      year_tietkhi_2 = before_tietkhi[2]['daytiekhi']
      year_tietkhi_3 = before_tietkhi[3]['daytiekhi']
      year_tietkhi_4 = last_tietkhi[1]['daytiekhi']
    elif month == 1:
      before_month = 12
      last_month = month + 1
      before_tietkhi = LichTietKhi.objects.filter(year=year-1,month=before_month).values('daytiekhi')
      print("before_tietkhi : ",before_tietkhi)
      last_tietkhi = LichTietKhi.objects.filter(year=year,month__in=[month,last_month]).values('daytiekhi')
      print("last_tietkhi : ",last_tietkhi)

      # before_tietkhi :  <QuerySet [{'daytiekhi': '6/12/2020 11:08 PM'}, {'daytiekhi': '21/12/2020 5:01 PM'}]>
      # last_tietkhi :  <QuerySet [{'daytiekhi': '5/1/2021 10:22 AM'}, {'daytiekhi': '20/1/2021 3:38 AM'},
      # {'daytiekhi': '3/2/2021 9:57 PM'}, {'daytiekhi': '18/2/2021 5:42 PM'}]>

      year_tietkhi_1 = before_tietkhi[1]['daytiekhi']
      year_tietkhi_2 = last_tietkhi[0]['daytiekhi']
      year_tietkhi_3 = last_tietkhi[1]['daytiekhi']
      year_tietkhi_4 = last_tietkhi[2]['daytiekhi']
    else:
      before_month = month - 1
      last_month = month + 1
      year_tietkhi = LichTietKhi.objects.filter(year=year,month__in=[before_month,month,last_month]).values('daytiekhi')
      print(year_tietkhi)
      # <QuerySet [{'daytiekhi': '5/3/2021 3:52 PM'}, {'daytiekhi': '20/3/2021 4:36 PM'},
      # {'daytiekhi': '4/4/2021 8:33 PM'}, {'daytiekhi': '20/4/2021 3:32 AM'},
      # {'daytiekhi': '5/5/2021 1:46 PM'}, {'daytiekhi': '21/5/2021 2:35 AM'}]>
      year_tietkhi_1 = year_tietkhi[1]['daytiekhi']
      year_tietkhi_2 = year_tietkhi[2]['daytiekhi']
      year_tietkhi_3 = year_tietkhi[3]['daytiekhi']
      year_tietkhi_4 = year_tietkhi[4]['daytiekhi']
    day_tiekhi_1 =  datetime.datetime.strptime(year_tietkhi_1, "%d/%m/%Y %I:%M %p")
    day_tiekhi_2 =  datetime.datetime.strptime(year_tietkhi_2, "%d/%m/%Y %I:%M %p")
    day_tiekhi_3 =  datetime.datetime.strptime(year_tietkhi_3, "%d/%m/%Y %I:%M %p")
    day_tiekhi_4 =  datetime.datetime.strptime(year_tietkhi_4, "%d/%m/%Y %I:%M %p")
    day_now = datetime.datetime(year, month, day, hours, minute, 59)
    if day_tiekhi_2 <= day_now < day_tiekhi_4:
      if day_tiekhi_2 <= day_now < day_tiekhi_3:
        tietkhi = LichTietKhi.objects.filter(daytiekhi=year_tietkhi_2).values('tietkhi')
      elif day_tiekhi_3 <= day_now < day_tiekhi_4:
        tietkhi = LichTietKhi.objects.filter(daytiekhi=year_tietkhi_3).values('tietkhi')
    else:
        if day_tiekhi_2 > day_now:
          tietkhi = LichTietKhi.objects.filter(daytiekhi=year_tietkhi_1).values('tietkhi')
        elif  day_now > day_tiekhi_3:
          print("day_now > day_tiekhi_2")
    print("111111111111111  ",tietkhi)
    for key,val in KINHDICH.lich_tiet_khi.items():
      if tietkhi[0]['tietkhi'] in val:
        tiet_khi['TietKhi'] = tietkhi[0]['tietkhi']
        nguhanh = f'{key} {KINHDICH.dic_chi_nguhanh[key]}'
        tiet_khi['nguhanh'] = nguhanh.capitalize()
    return tiet_khi
# class History(models.Model):
#     @classmethod
#     def insert_history(cls, field1, field2, field3):
#         # Here be code


# from app.models import History
# History.insert_history(field1, field2, field3)
