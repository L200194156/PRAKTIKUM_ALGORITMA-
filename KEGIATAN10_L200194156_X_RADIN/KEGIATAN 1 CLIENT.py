import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50002))
print"Program Komunikasi Tentang Data Diri"

while pesan.lower() != 'q':
    pesan = raw_input("Perintah: ")
    s.send(pesan)
    if pesan.lower() == "keluar":
        response = s.recv(1024)
        print "Jawab: ", response
        s.close()
        break
    elif pesan.lower() != "keluar" :
        response = s.recv(1024)
        print "Jawab: ", response
s.close()
