import time

'''
%a – abbreviated day of week
%A – full day of week
%b – abbreviated name of month
%B – full name of month
%c – preferred date and time representation
%C – century number (the year divided by 100; range 00 to 99)
%d – day of month (1 to 31)
%D – the same as %m/%d/%y
%e – day of month (1 to 31)
%g – like %G, but without the century
%G – 4-digit year corresponding to the ISO week number (ref. %V).
%h – same as %b
%H – hour; using a 24-hr clock (0 to 23)
%I – hour; using a 12-hr clock (1 to 12)
%j – day of year (1 to 366)
%m – month (1 to 12)
%M – minute
%n – newline character
%p – AM/PM according to given time value
%r – time in AM/PM representation
%R – time in 24-hr representation
%S – second
%t – tab
%T – current time; equal to %H:%M:%S
%u – day of week as a number (1 to 7); Monday=1
%U – week of year, beginning with the first Sunday as the first day of the first week
%V – The ISO 8601 week of year (1 to 53); week 1 is the first with at least 4 days in the current year, and with Monday as the first day of the week
%W – week of year; beginning with the first Monday as the first day of the first week
%w – day of week as a decimal; Sunday=0
%x – the preferred date representation without the time
%X – the preferred time representation without the date
%y – year without century (00 to 99)
%Y – year including century
%Z or %z – time zone/name/abbreviation
%% – a % character

'''

# Time intervals are floating point numbers in units of seconds.Particular instants in time are
# expressed in seconds since 12:00am,january 1,1970

tick = time.time()
print("no.of ticks since 12:am,January 1,1970", tick)

# Getting calendar for the month
#month() returns a calendar for a certain month of a certain year.
# These are two of the arguments.
# There are two other optional arguments- one for width of characters in name of day, and
#  another one for the number of lines for each week.

import calendar
cal = calendar.month(2018,7)
print("Here is the calendar:")
print(cal)
print(calendar.month(2018,8,3,2))

#strftime() method returns a string from a format (and optionally, a tuple)
print(time.strftime("%b",time.localtime()))

#his method takes a time tuple and returns the equivalent in ticks since the epoch, in floating point.
print(calendar.timegm(time.localtime()))