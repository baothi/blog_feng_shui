'''
(http://www.informatik.uni-leipzig.de/~duc/amlich/calrules.html)
http://www.informatik.uni-leipzig.de/~duc/amlich/
http://www.informatik.uni-leipzig.de/~duc/amlich/AL.py
https://www.informatik.uni-leipzig.de/~duc/amlich/tietkhi.html
(c) 2006 Ho Ngoc Duc.
Astronomical algorithms
from the book "Astronomical Algorithms" by Jean Meeus, 1998

Thuật toán chuyển đổi giữa ngày dương và âm
Trong tính toán thiên văn người ta lấy ngày 1/1/4713 trước công nguyên của lịch Julius (tức ngày 24/11/4714 trước 
CN theo lịch Gregorius) làm điểm gốc. Số ngày tính từ điểm gốc này gọi là số ngày Julius (Julian day number) 
của một thời điểm. Ví dụ, số ngày Julius của 1/1/2000 là 24515455.
Dùng các công thức sau ta có thể chuyển đổi giữa ngày/tháng/năm và số ngày Julius. Phép chia ở 2 công thức sau được 
hiểu là chia số nguyên, bỏ phần dư: 23/4=5.
'''

import math
color = (
        ("GIÁP","green"),
        ("ẤT","green"),
        ("BÍNH","red"),
        ("ĐINH","red"),
        ("MẬU","organ"),
        ("KỶ","organ"),
        ("CANH","grey"),
        ("TÂN","grey"),
        ("NHÂM","blue"),
        ("QUÝ","blue"),
        ("TÝ","blue"),
        ("SỬU","organ"),
        ("DẦN","green"),
        ("MÃO","green"),
        ("THÌN","organ"),
        ("TỴ","red"),
        ("NGỌ","red"),
        ("MÙI","organ"),
        ("THÂN","grey"),
        ("DẬU","grey"),
        ("TUẤT","organ"),
        ("HỢI","blue"),
    )

def jdFromDate(dd, mm, yy):
    '''def jdFromDate(dd, mm, yy): 
    Compute the (integral) Julian day number of day dd/mm/yyyy, i.e., 
    the number of days between 1/1/4713 BC (Julian calendar) 
    and dd/mm/yyyy.'''
    a = int((14 - mm) / 12.)
    y = yy + 4800 - a
    m = mm + 12*a - 3
    jd = dd + int((153*m + 2) / 5.) + 365*y + int(y/4.) - int(y/100.) + int(y/400.) - 32045
    if (jd < 2299161):
        jd = dd + int((153*m + 2)/5.) + 365*y + int(y/4.) - 32083
    return jd

def jdToDate(jd):
    '''def jdToDate(jd): Convert a Julian day number to day/month/year. jd is an integer.'''
    if (jd > 2299160):
        ## After 5/10/1582, Gregorian calendar
        a = jd + 32044
        b = int((4*a + 3) / 146097.)
        c = a - int((b*146097) / 4.)
    else:
        b = 0
        c = jd + 32082
    d = int((4*c + 3) / 1461.)
    e = c - int((1461*d) / 4.)
    m = int((5*e + 2) / 153.)
    day = e - int((153*m + 2) / 5.) + 1
    month = m + 3 - 12*int(m / 10.)
    year = b*100 + d - 4800 + int(m / 10.)
    return [day, month, year]

def NewMoon(k):
    '''def NewMoon(k): Compute the time of the k-th new moon after the new moon 
    of 1/1/1900 13:52 UCT (measured as the number of days since 1/1/4713 BC noon UCT, 
    e.g., 2451545.125 is 1/1/2000 15:00 UTC. Returns a floating number, e.g., 2415079.9758617813 
    for k=2 or 2414961.935157746 for k=-2.'''
    ## Time in Julian centuries from 1900 January 0.5
    T = k / 1236.85
    T2 = T * T
    T3 = T2 * T
    dr = math.pi / 180.
    Jd1 = 2415020.75933 + 29.53058868*k + 0.0001178*T2 - 0.000000155*T3
    Jd1 = Jd1 + 0.00033*math.sin((166.56 + 132.87*T - 0.009173*T2)*dr)
    ## Mean new moon
    M = 359.2242 + 29.10535608*k - 0.0000333*T2 - 0.00000347*T3
    ## Sun's mean anomaly
    Mpr = 306.0253 + 385.81691806*k + 0.0107306*T2 + 0.00001236*T3
    ## Moon's mean anomaly
    F = 21.2964 + 390.67050646*k - 0.0016528*T2 - 0.00000239*T3
    ## Moon's argument of latitude
    C1 = (0.1734 - 0.000393*T)*math.sin(M*dr) + 0.0021*math.sin(2*dr*M)
    C1 = C1 - 0.4068*math.sin(Mpr*dr) + 0.0161*math.sin(dr*2*Mpr)
    C1 = C1 - 0.0004*math.sin(dr*3*Mpr)
    C1 = C1 + 0.0104*math.sin(dr*2*F) - 0.0051*math.sin(dr*(M + Mpr))
    C1 = C1 - 0.0074*math.sin(dr*(M - Mpr)) + 0.0004*math.sin(dr*(2*F + M))
    C1 = C1 - 0.0004*math.sin(dr*(2*F - M)) - 0.0006*math.sin(dr*(2*F + Mpr))
    C1 = C1 + 0.0010*math.sin(dr*(2*F - Mpr)) + 0.0005*math.sin(dr*(2*Mpr + M))
    if (T < -11):
        deltat= 0.001 + 0.000839*T + 0.0002261*T2 - 0.00000845*T3 - 0.000000081*T*T3
    else:
        deltat= -0.000278 + 0.000265*T + 0.000262*T2
    JdNew = Jd1 + C1 - deltat
    return JdNew

def SunLongitude(jdn):
    '''def SunLongitude(jdn): Compute the longitude of the sun at any time. 
    Parameter: floating number jdn, the number of days since 1/1/4713 BC noon.'''
    T = (jdn - 2451545.0 ) / 36525.
    ## Time in Julian centuries
    ## from 2000-01-01 12:00:00 GMT
    T2 = T * T
    dr = math.pi / 180.  ## degree to radian
    M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T*T2
    ## mean anomaly, degree
    L0 = 280.46645 + 36000.76983*T + 0.0003032*T2
    ## mean longitude, degree
    DL = (1.914600 - 0.004817*T - 0.000014*T2) * math.sin(dr*M)
    DL += (0.019993 - 0.000101*T) *math.sin(dr*2*M) + 0.000290*math.sin(dr*3*M)
    L = L0 + DL  ## true longitude, degree
    L = L * dr
    L = L - math.pi*2*(int(L / (math.pi*2)))
    #### Normalize to (0, 2*math.pi)
    return L

def getSunLongitude(dayNumber, timeZone):
    '''def getSunLongitude(dayNumber, timeZone):  Compute sun position at 
    midnight of the day with the given Julian day number. 
    The time zone if the time difference between local time and UTC: 7.0 for UTC+7:00. 
    The function returns a number between 0 and 11.  
    From the day after March equinox and the 1st major term after March equinox, 0 is returned. 
    After that, return 1, 2, 3 ...'''
    return int( SunLongitude(dayNumber - 0.5 - timeZone/24.) / math.pi*6)

def getNewMoonDay(k, timeZone):
    '''def getNewMoonDay(k, timeZone): Compute the day of the k-th 
    new moon in the given time zone. The time zone if the time difference 
    between local time and UTC: 7.0 for UTC+7:00.'''
    return int(NewMoon(k) + 0.5 + timeZone / 24.)

# Tìm ngày bắt đầu tháng 11 âm lịch
# Đông chí thường nằm vào khoảng 19/12-22/12, như vậy trước hết ta tìm ngày Sóc trước 
# ngày 31/12. Nếu tháng bắt đầu vào ngày đó không chứa Đông chí thì ta phải lùi lại 1 tháng nữa.
def getLunarMonth11(yy, timeZone):
    '''def getLunarMonth11(yy, timeZone):  Find the day that starts the 
    luner month 11of the given year for the given time zone.'''
    # off = jdFromDate(31, 12, yy) \
    #            - 2415021.076998695
    off = jdFromDate(31, 12, yy) - 2415021.
    k = int(off / 29.530588853)
    nm = getNewMoonDay(k, timeZone)
    sunLong = getSunLongitude(nm, timeZone)
    #### sun longitude at local midnight
    if (sunLong >= 9):
        nm = getNewMoonDay(k - 1, timeZone)
    return nm

# Xác định tháng nhuận
# Nếu giữa hai tháng 11 âm lịch (tức tháng có chứa Đông chí) có 13 tháng âm lịch thì năm âm lịch đó 
# có tháng nhuận. Để xác định tháng nhuận, ta sử dụng hàm getSunLongitude như đã nói ở trên. 
# Cho a11 là ngày bắt đầu tháng 11 âm lịch mà một trong 13 tháng sau đó là tháng nhuận. 
# Hàm sau cho biết tháng nhuận nằm ở vị trí nào sau tháng 11 này.
def getLeapMonthOffset(a11, timeZone):
    '''def getLeapMonthOffset(a11, timeZone): Find the index of the leap month after 
    the month starting on the day a11.
    Giả sử hàm getLeapMonthOffset trả lại giá trị 4, như thế tháng nhuận sẽ là tháng sau tháng 2 
    thường. (Tháng thứ 4 sau tháng 11 đáng ra là tháng 3, nhưng vì đó là tháng nhuận nên sẽ 
    lấy tên của tháng trước đó tức tháng 2, và tháng thứ 5 sau tháng 11 mới là tháng 3).'''

    k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
    last = 0
    i = 1  ## start with month following lunar month 11
    arc = getSunLongitude(getNewMoonDay(k + i, timeZone), timeZone)
    while True:
        last = arc
        i += 1
        arc = getSunLongitude(getNewMoonDay(k + i, timeZone), timeZone)
        if  not (arc != last and i < 14):
            break
    return i - 1

def S2L(dd, mm, yy, timeZone = 7):
    '''def S2L(dd, mm, yy, timeZone = 7): 
    Convert solar date dd/mm/yyyy to the corresponding lunar date.
    chuyển đổi lịch dương sang lịch âm '''
    dayNumber = jdFromDate(dd, mm, yy)
    k = int((dayNumber - 2415021.076998695) / 29.530588853)
    monthStart = getNewMoonDay(k + 1, timeZone)
    if (monthStart > dayNumber):
        monthStart = getNewMoonDay(k, timeZone)
    # alert(dayNumber + " -> " + monthStart)
    a11 = getLunarMonth11(yy, timeZone)
    b11 = a11
    if (a11 >= monthStart):
        lunarYear = yy
        a11 = getLunarMonth11(yy - 1, timeZone)
    else:
        lunarYear = yy + 1
        b11 = getLunarMonth11(yy + 1, timeZone)
    lunarDay = dayNumber - monthStart + 1
    diff = int((monthStart - a11) / 29.)
    lunarLeap = 0
    lunarMonth = diff + 11
    if (b11 - a11 > 365):
        leapMonthDiff = getLeapMonthOffset(a11, timeZone)
        if (diff >= leapMonthDiff):
            lunarMonth = diff + 10
            if (diff == leapMonthDiff):
                lunarLeap = 1
    if (lunarMonth > 12):
        lunarMonth = lunarMonth - 12
    if (lunarMonth >= 11 and diff < 4):
        lunarYear -= 1
    return [ lunarDay, lunarMonth, lunarYear, lunarLeap ]

def L2S(lunarD, lunarM, lunarY, lunarLeap, tZ = 7):
    '''def L2S(lunarD, lunarM, lunarY, lunarLeap, tZ = 7): 
    Convert a lunar date to the corresponding solar date.
    Chuyển đổi ngày âm lịch thành ngày dương lịch tương ứng'''
    if (lunarM < 11):
        a11 = getLunarMonth11(lunarY - 1, tZ)
        b11 = getLunarMonth11(lunarY, tZ)
    else:
        a11 = getLunarMonth11(lunarY, tZ)
        b11 = getLunarMonth11(lunarY + 1, tZ)
    k = int(0.5 + (a11 - 2415021.076998695) / 29.530588853)
    off = lunarM - 11
    if (off < 0):
        off += 12
    if (b11 - a11 > 365):
        leapOff = getLeapMonthOffset(a11, tZ)
        leapM = leapOff - 2
        if (leapM < 0):
            leapM += 12
        if (lunarLeap != 0 and lunarM != leapM):
            return [0, 0, 0]
        elif (lunarLeap != 0 or off >= leapOff):
            off += 1
    monthStart = getNewMoonDay(k + off, tZ)
    return jdToDate(monthStart + lunarD - 1)

def day_can(dd, mm, yy):
    calendar_Julius = jdFromDate(dd, mm, yy)
    thien_can = (calendar_Julius + 9)%10
    if thien_can == 0:
        can = 'GIÁP'
    elif thien_can == 1:
        can = 'ẤT'
    elif thien_can == 2:
        can = 'BÍNH'
    elif thien_can == 3:
        can = 'ĐINH'
    elif thien_can == 4:
        can = 'MẬU'
    elif thien_can == 5:
        can = 'KỶ'
    elif thien_can == 6:
        can = 'CANH'
    elif thien_can == 7:
        can = 'TÂN'
    elif thien_can == 8:
        can = 'NHÂM'
    else:
        can = 'QUÝ'
    return can

def day_chi(dd, mm, yy):
    calendar_Julius = jdFromDate(dd, mm, yy)
    thien_chi = (calendar_Julius + 1)%12
    if thien_chi == 0:
        chi = 'TÝ'
    elif thien_chi == 1:
        chi = 'SỬU'
    elif thien_chi == 2:
        chi = 'DẦN'
    elif thien_chi == 3:
        chi = 'MÃO'
    elif thien_chi == 4:
        chi = 'THÌN'
    elif thien_chi == 5:
        chi = 'TỴ'
    elif thien_chi == 6:
        chi = 'NGỌ'
    elif thien_chi == 7:
        chi = 'MÙI'
    elif thien_chi == 8:
        chi = 'THÂN'
    elif thien_chi == 9:
        chi = 'DẬU'
    elif thien_chi == 10:
        chi = 'TUẤT'
    else:
        chi = 'HỢI'

    return chi

def mont_can(mm, yy):
    thien_can = ( yy*12+mm+3)%10
    if thien_can == 0:
        can = 'GIÁP'
    elif thien_can == 1:
        can = 'ẤT'
    elif thien_can == 2:
        can = 'BÍNH'
    elif thien_can == 3:
        can = 'ĐINH'
    elif thien_can == 4:
        can = 'MẬU'
    elif thien_can == 5:
        can = 'KỶ'
    elif thien_can == 6:
        can = 'CANH'
    elif thien_can == 7:
        can = 'TÂN'
    elif thien_can == 8:
        can = 'NHÂM'
    else:
        can = 'QUÝ'
    return can

def mont_chi(mm):
    thien_chi = mm
    if thien_chi == 11:
        chi = 'TÝ'
    elif thien_chi == 12:
        chi = 'SỬU'
    elif thien_chi == 1:
        chi = 'DẦN'
    elif thien_chi == 2:
        chi = 'MÃO'
    elif thien_chi == 3:
        chi = 'THÌN'
    elif thien_chi == 4:
        chi = 'TỴ'
    elif thien_chi == 5:
        chi = 'NGỌ'
    elif thien_chi == 6:
        chi = 'MÙI'
    elif thien_chi == 7:
        chi = 'THÂN'
    elif thien_chi == 8:
        chi = 'DẬU'
    elif thien_chi == 9:
        chi = 'TUẤT'
    else:
        chi = 'HỢI'

    return chi

def year_can(year):
    thien_can = (year + 6)%10
    if thien_can == 0:
        can = 'GIÁP'
    elif thien_can == 1:
        can = 'ẤT'
    elif thien_can == 2:
        can = 'BÍNH'
    elif thien_can == 3:
        can = 'ĐINH'
    elif thien_can == 4:
        can = 'MẬU'
    elif thien_can == 5:
        can = 'KỶ'
    elif thien_can == 6:
        can = 'CANH'
    elif thien_can == 7:
        can = 'TÂN'
    elif thien_can == 8:
        can = 'NHÂM'
    else:
        can = 'QUÝ'
    return can

def year_chi(year):
    thien_chi = (year + 8)%12
    if thien_chi == 0:
        chi = 'TÝ'
    elif thien_chi == 1:
        chi = 'SỬU'
    elif thien_chi == 2:
        chi = 'DẦN'
    elif thien_chi == 3:
        chi = 'MÃO'
    elif thien_chi == 4:
        chi = 'THÌN'
    elif thien_chi == 5:
        chi = 'TỴ'
    elif thien_chi == 6:
        chi = 'NGỌ'
    elif thien_chi == 7:
        chi = 'MÙI'
    elif thien_chi == 8:
        chi = 'THÂN'
    elif thien_chi == 9:
        chi = 'DẬU'
    elif thien_chi == 10:
        chi = 'TUẤT'
    else:
        chi = 'HỢI'

    return chi

def hours_can(hours,can_ngay):
    hours = int(hours)
    if can_ngay == 'GIÁP' or can_ngay == 'KỶ':
        if hours == 23 or hours == 0 or hours == 19 or hours == 20:
            can_hours = 'GIÁP'
        elif hours == 1 or hours == 2 or hours == 21 or hours == 22:
            can_hours = 'ẤT'
        elif hours == 3 or hours == 4:
            can_hours = 'BÍNH'
        elif hours == 5 or hours == 6:
            can_hours = 'ĐINH'
        elif hours == 7 or hours == 8:
            can_hours = 'MẬU'
        elif hours == 9 or hours == 10:
            can_hours = 'KỶ'
        elif hours == 11 or hours == 12:
            can_hours = 'CANH'
        elif hours == 13 or hours == 14:
            can_hours = 'TÂN'
        elif hours == 15 or hours == 16:
            can_hours = 'NHÂM'
        else:
            can_hours = 'QUÝ'
    elif can_ngay == 'ẤT' or can_ngay == 'CANH':
        if hours == 23 or hours == 0 or hours == 19 or hours == 20:
            can_hours = 'BÍNH'
        elif hours == 1 or hours == 2 or hours == 21 or hours == 22:
            can_hours = 'ĐINH'
        elif hours == 3 or hours == 4:
            can_hours = 'MẬU'
        elif hours == 5 or hours == 6:
            can_hours = 'KỶ'
        elif hours == 7 or hours == 8:
            can_hours = 'CANH'
        elif hours == 9 or hours == 10:
            can_hours = 'TÂN'
        elif hours == 11 or hours == 12:
            can_hours = 'NHÂM'
        elif hours == 13 or hours == 14:
            can_hours = 'QUÝ'
        elif hours == 15 or hours == 16:
            can_hours = 'GIÁP'
        else:
            can_hours = 'ẤT'
    elif can_ngay == 'BÍNH' or can_ngay == 'TÂN':
        if hours == 23 or hours == 0 or hours == 19 or hours == 20:
            can_hours = 'MẬU'
        elif hours == 1 or hours == 2 or hours == 21 or hours == 22:
            can_hours = 'KỶ'
        elif hours == 3 or hours == 4:
            can_hours = 'CANH'
        elif hours == 5 or hours == 6:
            can_hours = 'TÂN'
        elif hours == 7 or hours == 8:
            can_hours = 'NHÂM'
        elif hours == 9 or hours == 10:
            can_hours = 'QUÝ'
        elif hours == 11 or hours == 12:
            can_hours = 'GIÁP'
        elif hours == 13 or hours == 14:
            can_hours = 'ẤT'
        elif hours == 15 or hours == 16:
            can_hours = 'BÍNH'
        else:
            can_hours = 'ĐINH'
    elif can_ngay == 'ĐINH' or can_ngay == 'NHÂM':
        if hours == 23 or hours == 0 or hours == 19 or hours == 20:
            can_hours = 'CANH'
        elif hours == 1 or hours == 2 or hours == 21 or hours == 22:
            can_hours = 'TÂN'
        elif hours == 3 or hours == 4:
            can_hours = 'NHÂM'
        elif hours == 5 or hours == 6:
            can_hours = 'QUÝ'
        elif hours == 7 or hours == 8:
            can_hours = 'GIÁP'
        elif hours == 9 or hours == 10:
            can_hours = 'ẤT'
        elif hours == 11 or hours == 12:
            can_hours = 'BÍNH'
        elif hours == 13 or hours == 14:
            can_hours = 'ĐINH'
        elif hours == 15 or hours == 16:
            can_hours = 'MẬU'
        else:
            can_hours = 'KỶ'
    else:
        if hours == 23 or hours == 0 or hours == 19 or hours == 20:
            can_hours = 'NHÂM'
        elif hours == 1 or hours == 2 or hours == 21 or hours == 22:
            can_hours = 'QUÝ'
        elif hours == 3 or hours == 4:
            can_hours = 'GIÁP'
        elif hours == 5 or hours == 6:
            can_hours = 'ẤT'
        elif hours == 7 or hours == 8:
            can_hours = 'BÍNH'
        elif hours == 9 or hours == 10:
            can_hours = 'ĐINH'
        elif hours == 11 or hours == 12:
            can_hours = 'MẬU'
        elif hours == 13 or hours == 14:
            can_hours = 'KỶ'
        elif hours == 15 or hours == 16:
            can_hours = 'CANH'
        else:
            can_hours = 'TÂN'
    return can_hours

def hours_chi(hours):
    hours = int(hours)
    can_gio = ''
    if hours == 0 or hours == 23:
        can_gio = 'TÝ'
    elif hours == 1 or hours == 2:
        can_gio = 'SỬU'
    elif hours == 3 or hours == 4:
        can_gio = 'DẦN'
    elif hours == 5 or hours == 6:
        can_gio = 'MÃO'
    elif hours == 7 or hours == 8:
        can_gio = 'THÌN'
    elif hours == 9 or hours == 10:
        can_gio = 'TỴ'
    elif hours == 11 or hours == 12:
        can_gio = 'NGỌ'
    elif hours == 13 or hours == 14:
        can_gio = 'MÙI'
    elif hours == 15 or hours == 16:
        can_gio = 'THÂN'
    elif hours == 17 or hours == 18:
        can_gio = 'DẬU'
    elif hours == 19 or hours == 20:
        can_gio = 'TUẤT'
    else:
        can_gio = 'HỢI'

    return can_gio


def color_canchi(canchi):
    for val in color:
        val = list(val)
        if val[0] == canchi:
            chican = val[1]
            return chican

def nguhanhnapam(can, chi):
    if can == 'GIÁP' and chi == 'TÝ' or can == 'ẤT' and chi == 'SỬU':
        napam = 'Hải Trung Kim'
    elif can == 'BÍNH' and chi == 'DẦN' or can == 'ĐINH' and chi == 'MÃO':
        napam = 'Lô Trung Hỏa'
    elif can == 'MẬU' and chi == 'THÌN' or can == 'KỶ' and chi == 'TỴ':
        napam = 'Đại Lâm Mộc'
    elif can == 'CANH' and chi == 'NGỌ' or can == 'TÂN' and chi == 'MÙI':
        napam = 'Lộ Bàng Thổ'
    elif can == 'NHÂM' and chi == 'THÂN' or can == 'QUÝ' and chi == 'DẬU':
        napam = 'Kiếm Phong Kim'
    elif can == 'GIÁP' and chi == 'TUẤT' or can == 'ẤT' and chi == 'HỢI':
        napam = 'Sơn Đầu Hỏa'
    elif can == 'BÍNH' and chi == 'TÝ' or can == 'ĐINH' and chi == 'SỬU':
        napam = 'Giản Hạ Thủy'
    elif can == 'MẬU' and chi == 'DẦN' or can == 'KỶ' and chi == 'MÃO':
        napam = 'Thành Đầu Thổ'
    elif can == 'CANH' and chi == 'THÌN' or can == 'TÂN' and chi == 'TỴ':
        napam = 'Bạch Lạp Kim'
    elif can == 'NHÂM' and chi == 'NGỌ' or can == 'QUÝ' and chi == 'MÙI':
        napam = 'Dương Liễu Mộc'
    elif can == 'GIÁP' and chi == 'THÂN' or can == 'ẤT' and chi == 'DẬU':
        napam = 'Tinh Tuyền Thủy'
    elif can == 'BÍNH' and chi == 'TUẤT' or can == 'ĐINH' and chi == 'HỢI':
        napam = 'Ốc Thượng Thổ'
    elif can == 'MẬU' and chi == 'TÝ' or can == 'KỶ' and chi == 'SỬU':
        napam = 'Tích Lịch Hỏa'
    elif can == 'CANH' and chi == 'DẦN' or can == 'TÂN' and chi == 'MÃO':
        napam = 'Tùng Bách Mộc'
    elif can == 'NHÂM' and chi == 'THÌN' or can == 'QUÝ' and chi == 'TỴ':
        napam = 'Trường Lưu Thủy'
    elif can == 'GIÁP' and chi == 'NGỌ' or can == 'ẤT' and chi == 'MÙI':
        napam = 'Sa Trung Kim'
    elif can == 'BÍNH' and chi == 'THÂN' or can == 'ĐINH' and chi == 'DẬU':
        napam = 'Sơn Hạ Hỏa'
    elif can == 'MẬU' and chi == 'TUẤT' or can == 'KỶ' and chi == 'HỢI':
        napam = 'Bình Địa Mộc'
    elif can == 'CANH' and chi == 'TÝ' or can == 'TÂN' and chi == 'SỬU':
        napam = 'Bích Thượng Thổ'
    elif can == 'NHÂM' and chi == 'DẦN' or can == 'QUÝ' and chi == 'MÃO':
        napam = 'Kim Bạch Kim'
    elif can == 'GIÁP' and chi == 'THÌN' or can == 'ẤT' and chi == 'TỴ':
        napam = 'Phúc Đăng Hỏa'
    elif can == 'BÍNH' and chi == 'NGỌ' or can == 'ĐINH' and chi == 'MÙI':
        napam = 'Thiên Hà Thủy'
    elif can == 'MẬU' and chi == 'THÂN' or can == 'KỶ' and chi == 'DẬU':
        napam = 'Đại Dịch Thổ'
    elif can == 'CANH' and chi == 'TUẤT' or can == 'TÂN' and chi == 'HỢI':
        napam = 'Thoa Xuyến Kim'
    elif can == 'NHÂM' and chi == 'TÝ' or can == 'QUÝ' and chi == 'SỬU':
        napam = 'Tang Đố Mộc'
    elif can == 'GIÁP' and chi == 'DẦN' or can == 'ẤT' and chi == 'MÃO':
        napam = 'Đại Khuê Thủy'
    elif can == 'BÍNH' and chi == 'THÌN' or can == 'ĐINH' and chi == 'TỴ':
        napam = 'Sa Trung Thổ'
    elif can == 'MẬU' and chi == 'NGỌ' or can == 'KỶ' and chi == 'MÙI':
        napam = 'Thiên Thượng Hỏa'
    elif can == 'CANH' and chi == 'THÂN' or can == 'TÂN' and chi == 'DẬU':
        napam = 'Thạch Lựu Mộc'
    elif can == 'NHÂM' and chi == 'TUẤT' or can == 'QUÝ' and chi == 'HỢI':
        napam = 'Đại Hải Thủy'
    return napam
