print("<!DOCTYPE html>\n")
print("""<html>
<head><title>Akses dengan SimpleHTTPRequestHadler</title></head>
<body><h3>Bangun Geometri</h3>""")
panjang = 10
lebar = 5
tinggi = 2
luas = panjang*tinggi
print ("""<table><tr><td>Nama Bangunan</td><td>:</td>Jajar genjang</td></tr>
                 <tr><td>Dimensi</td><td>:</td><td>3D</td></tr>
                 <tr><td>Rumus luas</td><td>:</td><td>panjang*tinggi</td></tr>""")
print("""<tr><td>Parameter 1</td><td>:</td><td>(0)</td></tr>""".format(panjang))
print("""<tr><td>Parameter 3</td><td>:</td><td>(0)</td></tr>""".format(tinggi))
print("""<tr><td>Luas</td><td>:</td><td>(0)</td></tr></table>""".format(luas))
print("""<script>var c = document.grtElementById("myCanvas")</script></body></html>"""))
