import random
angka = random.randint(0,100)

nama = "Radin Mundingwangi Nurangga Prabasakti"
TTL = " Sukoharjo, 27 Desember 1999 "

NamaSingkat = nama [ 0 : 13 ]
userName= nama [0] + nama [6:13] + " _ " + TTL [11:14]
pasword = nama[0:5] + str(angka)
