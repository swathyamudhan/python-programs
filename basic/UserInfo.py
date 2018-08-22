''''
Format strings
The following directives can be embedded in the format string:

Directive	Meaning
%a	Weekday name.
%A	Full weekday name.
%b	Abbreviated month name.
%B	Full month name.
%c	Appropriate date and time representation.
%d	Day of the month as a decimal number [01,31].
%H	Hour (24-hour clock) as a decimal number [00,23].
%I	Hour (12-hour clock) as a decimal number [01,12].
%j	Day of the year as a decimal number [001,366].
%m	Month as a decimal number [01,12].
%M	Minute as a decimal number [00,59].
%p	Equivalent of either AM or PM.
%S	Second as a decimal number [00,61].
%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w	Weekday as a decimal number [0(Sunday),6].
%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x	Appropriate date representation.
%X	Apropriate time representation.
%y	Year without century as a decimal number [00,99].
%Y	Year with century as a decimal number.
%Z	Time zone name (no characters if no time zone exists).
%%	A literal ‘%’ character.
'''
#-------------------------------------------------------
'''
The locale module opens access to the POSIX locale database and functionality.
The POSIX locale mechanism allows programmers to deal with certain cultural issues in an application, 
without requiring the programmer to know all the specifics of each country where the software is executed.
'''

# To get the current date and time
import time
import socket
import locale
import os
from requests import get

# date and time representation
print(time.strftime("Current date and time is " + "%c"))
#IPaddress
print("My local IP address is " + socket.gethostbyname(socket.gethostname()))
ip= get('https://api.ipify.org').text
print('My Public IP address is '+ ip)

#Time zone
print(time.strftime("Current timezone is " + "%z"))
#Country
print("Currrent country is " + locale.setlocale(locale.LC_ALL,''))
#Currency
print("Current currency is " + locale.currency(0))
print(os.getenv('LANG'))

