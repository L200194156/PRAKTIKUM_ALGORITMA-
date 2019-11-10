Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Radin Mundingwangi Nurangga Prabasakti"
>>> NIM = 156
>>> Tinggi = 1.55
>>> Berat = 46
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(aku)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(aku)
NameError: name 'aku' is not defined
>>> type(Aku)
<class 'tuple'>
>>> #because is used with parenthesis or "kurung buka, kurung tutup" the data can be strig, float, or anything else, with coma(,) sebagai pemisah
>>> Aku[0]
1999
>>> #because the list it start from 0 not 1, 0 = 1999
>>> a = NIM % 4 ; Aku [a]
1999
>>> #because the remaining result of 156 divide 4 is 0, so the result Aku[0] is 1999.
>>> type(Aku[a])
<class 'int'>
>>> #because the value of "TahunLahir" is 0, and 0 is integer data type
>>> aku [a:4]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    aku [a:4]
NameError: name 'aku' is not defined
>>> Aku[a:4]
(1999, 46, 1.55, 156)
>>> #because the first 4 object in the "Aku" data is "TahunLahir", "Berat", "Tinggi",and "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #because the function of string is to save the data like huruf/karakter, atau tanda baca with quotes one or quotes two
>>> Aku[0]= "aku"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Aku[0]= "aku"
TypeError: 'tuple' object does not support item assignment
>>> #because the type is tuple and it can't be changed the list,  but if that's list you can changed it.
>>> type(Data)
<class 'list'>
>>> #because list used square brackets
>>> type(Data[4])
<class 'str'>
>>> #because Data[4] is Nama and the stype is string data type
>>> Data[4][5]
' '
>>> #because in valeu "Data[4]"object tn the valeu start in 5, and this is "space"
>>> Data[4][a:6]
'Radin '
>>> #because in value"Data[4]" object in the valeu start from "a" until "5" is "Radin"
>>> Data[0]= "ok"; Data
['ok', 46, 1.55, 156, 'Radin Mundingwangi Nurangga Prabasakti']
>>> ##because the first obeject has changed by "ok" and after that it call all in "Data"
>>> Data[-1]
'Radin Mundingwangi Nurangga Prabasakti'
>>> #because it's call from rear list
>>> range(0,1)
range(0, 1)
>>> #because range of 1 is (0,1)
