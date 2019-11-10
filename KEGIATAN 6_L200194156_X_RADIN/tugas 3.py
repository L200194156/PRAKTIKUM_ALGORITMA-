Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Radin Mundingwangi Nurangga Prabasakti"
>>> NIM ="L200194156"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> X
'1156'
>>> a
1156
>>> type(a)
<class 'int'>
>>> #because the type of X has changed from string to integer
>>> type(b)
<class 'int'>
>>> #because the "Nama" data has a "len" instruction
>>> b
38
>>> a/b
30.42105263157895
>>> #because the result of 1156 divided by 38 is 30.42105226....
>>> a//b
30
>>> #because the meaning of "//" is division with rounding down
>>> 10*(a-999)
1570
>>> #because a is 1156 and minus by 999 is 157 after that the result will be multiplied by 10 and the result is 1570
>>> b**2
1444
>>> #because "**" is call "pangkat" or "power of" b power of 2 is 38 multiplied 38 and the result is 1444
>>> a%b
16
>>> #charcters of"%" is call module that's mean is revenue share or sisa hasil bagi. and 1156 % 38 is 16
>>> c = 12.5
>>> c
12.5
>>> type(c)
<class 'float'>
>>> #because data c is decimal.
>>> a/c
92.48
>>> #because 1156 devided by 12.5 is 92.48
>>> a//c
92.0
>>> #the meaning of "//" is division with rounding down
>>> a%c
6.0
>>> #the revenue share od sisa hasil bagi is 6
>>> #the revenue share or sisa hasil bagi is 6
>>> c > b
False
>>> #because b is more bigger than c, 12.5 < 38
>>> type(c > b)
<class 'bool'>
>>> #becasue the answer is "True" or "False" is called boolean
>>> a > b and b > c
True
>>> #because this program included of type boolean, a = 1156, b = 38, and c = 12.5
>>> a > 1100 or b < 10
True
>>> #because if one program is correct it will still give the correct answer because it uses "or" not "and"
