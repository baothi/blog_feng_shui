from django import forms
from django.forms import ModelForm
from .models import *

class KinhDichForm(forms.Form):
    Timezone_CHOICES = (
        ("-12.0","(GMT-12:00)-International Date Line West"),
        ("-11.0","(GMT-11:00)-Midway Island, Samoa"),
        ("-10.0","(GMT-10:00)-Hawaii"),
        ("-9.0","(GMT-09:00)-Alaska"),
        ("-8.0","(GMT-08:00)-Pacific Time (US &amp; Canada); Tijuana"),
        ("-7.0","(GMT-07:00)-Arizona"),
        ("-7.0","(GMT-07:00)-Chihuahua, La Paz, Mazatlan"),
        ("-7.0","(GMT-07:00)-Mountain Time (US &amp; Canada)"),
        ("-6.0","(GMT-06:00)-Central America"),
        ("-6.0","(GMT-06:00)-Central Time (US &amp; Canada)"),
        ("-6.0","(GMT-06:00)-Guadalajara, Mexico City, Monterrey"),
        ("-6.0","(GMT-06:00)-Saskatchewan"),
        ("-5.0","(GMT-05:00)-Bogota, Lima, Quito"),
        ("-5.0","(GMT-05:00)-Eastern Time (US &amp; Canada)"),
        ("-5.0","(GMT-05:00)-Indiana (East)"),
        ("-4.0","(GMT-04:00)-Atlantic Time (Canada)"),
        ("-4.0","(GMT-04:00)-Caracas, La Paz"),
        ("-4.0","(GMT-04:00)-Santiago"),
        ("-3.5","(GMT-03:30)-Newfoundland"),
        ("-3.0","(GMT-03:00)-Brasilia"),
        ("-3.0","(GMT-03:00)-Buenos Aires, Georgetown"),
        ("-3.0","(GMT-03:00)-Greenland"),
        ("-2.0","(GMT-02:00)-Mid-Atlantic"),
        ("-1.0","(GMT-01:00)-Azores"),
        ("-1.0","(GMT-01:00)-Cape Verde Is."),
        ("0.0","(GMT)-Casablanca, Monrovia"),
        ("0.0","(GMT)-Greenwich Mean Time: Dublin, Edinburgh, Lisbon, London"),
        ("1.0","(GMT+01:00)-Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna"),
        ("1.0","(GMT+01:00)-Belgrade, Bratislava, Budapest, Ljubljana, Prague"),
        ("1.0","(GMT+01:00)-Brussels, Copenhagen, Madrid, Paris"),
        ("1.0","(GMT+01:00)-Sarajevo, Skopje, Warsaw, Zagreb"),
        ("1.0","(GMT+01:00)-West Central Africa"),
        ("2.0","(GMT+02:00)-Athens, Beirut, Istanbul, Minsk"),
        ("2.0","(GMT+02:00)-Bucharest"),
        ("2.0","(GMT+02:00)-Cairo"),
        ("2.0","(GMT+02:00)-Harare, Pretoria"),
        ("2.0","(GMT+02:00)-Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius"),
        ("2.0","(GMT+02:00)-Jerusalem"),
        ("3.0","(GMT+03:00)-Baghdad"),
        ("3.0","(GMT+03:00)-Kuwait, Riyadh"),
        ("3.0","(GMT+03:00)-Moscow, St. Petersburg, Volgograd"),
        ("3.0","(GMT+03:00)-Nairobi"),
        ("3.5","(GMT+03:30)-Tehran"),
        ("4.0","(GMT+04:00)-Abu Dhabi, Muscat"),
        ("4.0","(GMT+04:00)-Baku, Tbilisi, Yerevan"),
        ("4.5","(GMT+04:30)-Kabul"),
        ("5.0","(GMT+05:00)-Ekaterinburg"),
        ("5.0","(GMT+05:00)-Islamabad, Karachi, Tashkent"),
        ("5.5","(GMT+05:30)-Chennai, Kolkata, Mumbai, New Delhi"),
        ("5.75","(GMT+05:45)-Kathmandu"),
        ("6.0","(GMT+06:00)-Almaty, Novosibirsk"),
        ("6.0","(GMT+06:00)-Astana, Dhaka"),
        ("6.0","(GMT+06:00)-Sri Jayawardenepura"),
        ("6.5","(GMT+06:30)-Rangoon"),
        ("7.0","(GMT+07:00)-Bangkok, Hanoi, Jakarta"),
        ("7.0","(GMT+07:00)-Krasnoyarsk"),
        ("8.0","(GMT+08:00)-Beijing, Chongqing, Hong Kong, Urumqi"),
        ("8.0","(GMT+08:00)-Irkutsk, Ulaan Bataar"),
        ("8.0","(GMT+08:00)-Kuala Lumpur, Singapore"),
        ("8.0","(GMT+08:00)-Perth"),
        ("8.0","(GMT+08:00)-Taipei"),
        ("9.0","(GMT+09:00)-Osaka, Sapporo, Tokyo"),
        ("9.0","(GMT+09:00)-Seoul"),
        ("9.0","(GMT+09:00)-Vakutsk"),
        ("9.5","(GMT+09:30)-Adelaide"),
        ("9.5","(GMT+09:30)-Darwin"),
        ("10.0","(GMT+10:00)-Brisbane"),
        ("10.0","(GMT+10:00)-Canberra, Melbourne, Sydney"),
        ("10.0","(GMT+10:00)-Guam, Port Moresby"),
        ("10.0","(GMT+10:00)-Hobart"),
        ("10.0","(GMT+10:00)-Vladivostok"),
        ("11.0","(GMT+11:00)-Magadan, Solomon Is., New Caledonia"),
        ("12.0","(GMT+12:00)-Auckland, Wellington"),
        ("12.0","(GMT+12:00)-Fiji, Kamchatka, Marshall Is."),

    )
    vieccanhoi = forms.CharField(max_length=250, required=False,widget = forms.TextInput(attrs={'class': 'form-control','placeholder' : "Input Full Name"}))
    day = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control','text-align': 'center'}),
        choices=((str(x), x) for x in range(1,32)), initial='9', required = True,)
    month = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}),
        choices=((str(x), x) for x in range(1,13)), initial='1', required = True,)
    year = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}),
        choices=((str(x), str(x)) for x in range(1900,2044)), initial='1998', required = True,)
    hours = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}),
        choices=((str(x), x) for x in range(0,24)), initial='21', required = True,)
    minute = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}),
        choices=((str(x), x) for x in range(0,60)), initial='12', required = True,)
    options = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}),
                 choices = ([('Nam','Nam'), ('Nữ','Nữ'), ]), initial='Nam', required = True,)

    calendar = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}),
                 choices = ([('Dương Lịch','Dương Lịch')]), initial='Dương Lịch', required = True,)


    timezone = forms.ChoiceField(choices=Timezone_CHOICES,
        required=False, initial='7.0',
        widget=forms.Select(attrs={'style':"width:100%"}))
    check = forms.BooleanField(required=False)
