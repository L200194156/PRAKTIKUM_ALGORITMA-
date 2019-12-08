import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50002))
s.listen(5)
print"Program Informatika Tentang Data Diri"
data= ""
kamus = {"nama" : "Radin Mundingwangi Nurangga Prabasakti",
         "NIM" : "L200194156",
         "angkatan" : "2019",
         "keluar" : "siap"}
while data.lower() != "keluar":
    komm,addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print"Perintah:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, perintah Anda tidak dimengerti")
