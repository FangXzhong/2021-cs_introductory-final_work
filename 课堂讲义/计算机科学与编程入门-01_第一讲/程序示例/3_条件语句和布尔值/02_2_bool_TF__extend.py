"""
Date: 2021.01.26
Author: Justin

要点说明：
直接写布尔值，虽然不常用，但有时很方便
"""

year = 2100
check = False

if year % 4 == 0:
    check = True
    
if year % 100 == 0:
    check = False

if year % 400 == 0:
    check = True

print(str(year) + '年是否闰年：' + str(check))
