# Pengembang - Tonumoy Mukherjee


impor kura-kura sebagai tu


roo = tu.Turtle() #objek Penyu
wn = tu.Layar() #Objek Layar
wn.bgcolor("hitam") #Layar Bg warna
wn.title("Pola Pohon Fraktal")
roo.left(90) #menggerakkan kura-kura 90 derajat ke kiri
roo.speed(20)#mengatur kecepatan kura-kura


def draw(l): #fungsi rekursif mengambil panjang 'l' sebagai argumen
    jika (l<10):
        kembali
    lain:

        roo.pensize(2) #Pengaturan Ukuran Pensize
        roo.pencolor("kuning") #Mengatur Pencolor sebagai kuning
        roo.forward(l) #moving turtle maju dengan 'l'
        roo.left(30) #menggerakkan kura-kura 30 derajat ke kiri
        draw(3*l/4) #menggambar fraktal di sebelah kiri objek kura-kura 'roo' dengan 3/4 panjangnya
        roo.right(60) #menggerakkan kura-kura 60 derajat ke kanan
        draw(3*l/4) #menggambar fraktal di sebelah kanan objek kura-kura 'roo' dengan 3/4 panjangnya
        roo.left(30) #menggerakkan kura-kura 30 derajat ke kiri
        roo.pensize(2)
        roo.backward(l) #mengembalikan kura-kura ke posisi semula

menggambar (20) # menggambar 20 kali 

roo.kanan(90)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(2)
        roo.pencolor("magenta") #magenta
        roo.maju(l)
        roo.kiri(30)
        menggambar (3*l/4)
        roo.kanan(60)
        menggambar (3*l/4)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)

menggambar (20)


roo.kiri(270)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(2)
        roo.pencolor("merah") #red
        roo.maju(l)
        roo.kiri(30)
        menggambar (3*l/4)
        roo.kanan(60)
        menggambar (3*l/4)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)

menggambar (20)

roo.kanan(90)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(2)
        roo.pencolor('#FFF8DC') #white
        roo.maju(l)
        roo.kiri(30)
        menggambar (3*l/4)
        roo.kanan(60)
        menggambar (3*l/4)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)

menggambar (20)
############################################################# ######

def menggambar (l):
    jika (l<10):
        kembali
    lain:

        roo.pensize(3)
        roo.pencolor("hijau muda") #hijau muda
        roo.maju(l)
        roo.kiri(30)
        menggambar (4*l/5)
        roo.kanan(60)
        menggambar (4*l/5)
        roo.kiri(30)
        roo.pensize(3)
        roo.backward(l)

menggambar (40)

roo.kanan(90)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(3)
        roo.pencolor("merah") #red
        roo.maju(l)
        roo.kiri(30)
        menggambar (4*l/5)
        roo.kanan(60)
        menggambar (4*l/5)
        roo.kiri(30)
        roo.pensize(3)
        roo.backward(l)

menggambar (40)


roo.kiri(270)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(3)
        roo.pencolor("kuning") #kuning
        roo.maju(l)
        roo.kiri(30)
        menggambar (4*l/5)
        roo.kanan(60)
        menggambar (4*l/5)
        roo.kiri(30)
        roo.pensize(3)
        roo.backward(l)

menggambar (40)

roo.kanan(90)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(3)
        roo.pencolor('#FFF8DC') #white
        roo.maju(l)
        roo.kiri(30)
        menggambar (4*l/5)
        roo.kanan(60)
        menggambar (4*l/5)
        roo.kiri(30)
        roo.pensize(3)
        roo.backward(l)

menggambar (40)

############################################################# ######
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        
        roo.pensize(2)
        roo.pencolor("cyan") #cyan
        roo.maju(l)
        roo.kiri(30)
        menggambar (6*l/7)
        roo.kanan(60)
        menggambar (6*l/7)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)
        
menggambar (60)

roo.kanan(90)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(2)
        roo.pencolor("kuning") #kuning
        roo.maju(l)
        roo.kiri(30)
        menggambar (6*l/7)
        roo.kanan(60)
        menggambar (6*l/7)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)
        
menggambar (60)


roo.kiri(270)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(2)
        roo.pencolor("magenta") #magenta
        roo.maju(l)
        roo.kiri(30)
        menggambar (6*l/7)
        roo.kanan(60)
        menggambar (6*l/7)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)
        
menggambar (60)

roo.kanan(90)
kecepatan.roo(2000)

#pengulangan
def menggambar (l):
    jika (l<10):
        kembali
    lain:
        roo.pensize(2)
        roo.pencolor('#FFF8DC') #white
        roo.maju(l)
        roo.kiri(30)
        menggambar (6*l/7)
        roo.kanan(60)
        menggambar (6*l/7)
        roo.kiri(30)
        roo.pensize(2)
        roo.backward(l)
menggambar(60)
wn.exitonclick()