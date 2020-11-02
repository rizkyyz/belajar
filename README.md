# Tugas Ini Untuk Melengkapi Pertemuan 6 <br>
## Dan Menjelaskan Project <br>

**NAMA : Muhammad Rizky Abdillah** <br>
**NIM : 312010049** <br>
**KELAS : TI.20.A.2** <br>
**TUGAS : BAHASA PEMOGRAMAN** <br>

## DAFTAR ISI <br>

| NO | Description | Link |
| ----- | ----- | ---- |
| 1. | Pertemuan 5 | [click here](#pertemuan-5---latihan) |
| 1. | Pertemuan 6 lab 1 | [click here](#pertemuan-6---lab-1) |
### Pertemuan 5 - Latihan

Pada pertemuan 5 bahasa pemograman, saya diberi soal untuk latihan oleh Dosen untuk membuat Aplikasi Biodata dengan python (Seperti gambar di bawah ini:)
![latihan pertemuan 5]

![foto 1](https://user-images.githubusercontent.com/66506609/97837657-3d002000-1d11-11eb-80d0-7332a6b8a92c.png)


Saat ini saya akan menjelaskan hasil dari tugas tersebut. <br>
Berikut *source code* nya atau klik berikut ([latihan 5](tugas5.py)): <br>

``` python
print "  ====================================" 
print "       Latihan 1 Biodata Rizky        "
print "  ===================================="

#variabel

nama= raw_input ("Masukan Nama Lengkap Anda: ")
panggilan= raw_input ("Masukan Nama Panggilan: ")
nim= raw_input ("Masukan Nim Anda: ")
ttl= raw_input ("Masukan Tempat Lahir Anda`: ")
tl= input ("Masukan Tanggal lahir  Anda: ")
alamat= raw_input ("Masukan Alamat Anda: ")
telpone= raw_input ("Masukan No Telpon Anda: ")

#hasil inputan dari variable
print "Assalamu'alaikum Wr.Wb"
print "Let me introduce my self My name is",nama,"but you can call me",panggilan,"my NPM is",nim,"I was born in",ttl,"and I am",tl,"years old. I am very glad if you want to invite my house in",alamat,".So, don't forget to call me before with the number",telpone,
```

* Berikut penjelasan :<br>
``` python
print("masukan nama lengkap anda : ")
```

source code fiatas berfungsi untuk mencetak hasil / output berupa " **masukan nama lengkap anda :** ". <br>
 Untuk menampilkan output string, saya menggunakan *tanda petik dua* didalam fungsi print(), sedangkan jika saya ingin menampilkan output / hasil berupa angka / interger saya tidak perlu menggunakan *tanda petik dua*. Contohnya:
 
``` python
print("nama lengkap saya adalah ...")
print(696969)
```
* Seperti gambar berikut ini 

![image](https://user-images.githubusercontent.com/66506609/97841431-640e2000-1d18-11eb-84bf-f955715c3642.png)

* Untuk source code berikutnya adalah inputan atau membuat variable. Seperti syntax dibawah ini:

``` python
nama=raw_input()
```
Keterangan : <br>
1. Variable adalah sebuah wadah penyimpanan data pada program yang akan digunakan selama program itu berjalan. Yang berfungsi sebagai variable dalam source code diatas adalah **NAMA** . <br>

2. Fungsi **input()** adalah untuk memasukan nilai dar layar console di command prompt, lalu kemudian mengembalikan nilai saat kita menekan tombol enter *(newline)*

![image](https://user-images.githubusercontent.com/66506609/97842495-45108d80-1d1a-11eb-900f-768f750724bf.png)


Pada gambar diatas, hasil dari inputan tersebut berwarna *putih* <br>
* Untuk memasukan printah lain seperti *Nama, NIM, Tempat lahir, Tanggal Lahir, Nomor Telphone,* mengikuti perintah yang sama seperti memasukan *NAMA* <br>

* Untuk menghitung rumus umur saya menggunakan variable *DOB* yaitu 2020 (Tahun sekarang) dikurangi dengan Year of bircth, pada source code berikut : <br>
``` python
dob=2020-year
```
Pada syntax / source code diatas, saya menggunakan variable *dob* dimana untuk menghitung umur (variable **age** pada output), yaitu dengan rumus pada variable *dob=2020-year* <br>

* Langkah kali ini saya akan menampilkan output yang diminta oleh Dosen. <br>
Output pertama yang di minta Dosen adalah menampilkan salam, yaitu dengan mengetikkan syntax / source code berikut : 
``` python
print("\n Asalammu'alaikum Wr.Wb. ")
```
Keterangan :
1. Fungsi **\n** pada source code diatas adalah untuk memberi baris baru / enter / *newline*
2. Fungsi print() seperti dijelaskan pada point **Output** diatas
Hasil source code diatas adalah seperti gambar dibawah ini : <br>

![image](https://user-images.githubusercontent.com/66506609/97844863-578cc600-1d1e-11eb-82a3-fff14807d002.png)

* Langkah terakhir menampilkan semua hasil dari inputan diatas. Dengan mengetikan source code berikut : <br>
``` python
print(f"Let me introduce my self. My name is {fullname}, but you can call me {nickname}. My NPM {npm}. I was born in {pob} and Iam {dob} years old. I am very glad if you want to invite my house in {address}. So don't forget to call me before with the number {phone}. \n Thank You ")
```
Keterangan : <br>
* Fungsi huruf **f** pada perintah *print(f"....")* adalah fungsi print atau bisa memudahkan program dalam mencetak statement dalam suatu baris dibandingkan dengan metode yang lama yaitu memisahkan string dan variable dengan symbol koma ( , ) atau plus ( + ) <br>
* Sedangkan fungsi {} pada output tersebut menampilkan hasil variable <br>
Hasil dari output tersebut seperti berikut : <br>

![image](https://user-images.githubusercontent.com/66506609/97845181-d97cef00-1d1e-11eb-9d80-abd18be3e518.png)


### Pertemuan 6 - lab 1

Pada halaman ini (Tugas pertemuan 6 - lab 1) Saya di berikan tugas oleh Dosen yaitu mempelajari Operator Aritmatika menggunakan bahasa pemograman python. Berikut source yang di berikan oleh Dosen [source lab 1](lab1.py)
![Pertemmuan 6 - lab 1]

<img width="158" alt="fot0 6" src="https://user-images.githubusercontent.com/66506609/97900144-de688f80-1d6c-11eb-84ec-5ad80103d26e.png">

``` python
#Penggunaan End
print("A", end="")
print("B", end="")
print("C", end="")

print()
print("X")
print("Y")
print("Z")

#Penggunaan Separator
w,x,y,z=10,15,20,25
print(w,x,y,z)
print(w,x,y,z,sep=",")
print(w,x,y,z,sep="")
print(w,x,y,z,sep=":")
print(w,x,y,z,sep="-----")
```
Oke, kali ini saya menjelaskan materi yang dijelaskan oleh Dosen. <br><br>

* Penggunaan END
Penggunaan end digunakan untuk menambahkan kata yang dicetak di akhir baris

``` python
print("A", end="")
print("B", end="")
print("C", end="")
```

> Penggunaan print() digunakan untuk mencetak output, seperti syntax dibawah ini : <br>
``` python 
print()
```
> Syntax dibawah ini digunakan untuk menampilkan output berupa string
``` python
print("X")
print("Y")
print("Z")
```
Hasil dari source code terseut seperti gambar di bawah ini: 

![Screenshot (78)](https://user-images.githubusercontent.com/66506609/97899963-98abc700-1d6c-11eb-8b66-db069d427d3b.png)

* Pengertian separaktor
Sepaktor adalah pemisah yang berfungsi sebagai tanda pemisah antar objek yang dicetak. Defaultnya adalah tanda sepasi <br><br>
> Pendeklarasian beberapa variable berserta nilainya
``` python
w,x,y,z=10,15,20,25
```
> Menampilkan hasil setiap variable tiap-tiap variable
``` python
print(w,x,y,z)
```
> Menampilkan hasil variable dari tiap-tiap variable menggunakan pemisah , (koma)
``` python
print(w,x,y,z,sep=",")
```
> Menampilkan hasil variable dari tiap-tiap variable tanpa menggunakan pemisah
``` python
print(w,x,y,z,sep="")
```
> Menampilkan hasil variable dari tiap-tiap variable dengan menggunakan pemisah : (titik dua)
``` python
print(w,x,y,z,sep=":")
```
> Menampilkan hasil variable dari tiap-tiap variable dengan menggunakan pemisah ----
``` python
print(w,x,y,z,sep="-----")
```

Hasil dari syntax / source code diatas adalah seperti berikut iniL: <br>
![Output Separator](praktikum/10.png)
<br>
<br>
<br>
### Pertemuan 6 - lab 1-2 
* String format <br>
String formatting atau pemformatan string memungkinkan kita menyuntikkan item kedalam string daripada kita mencoba menggabungkan string menggunakan koma atau string concatenation.<br>

Penggunaan pada source yang di berikan Dosen sebagai berikut : <br>
![Lab 1-2](praktikum/lab1-2.png) <br> 
``` python
# string format 1
print(0, 10 ** 0)
print(1, 10 ** 1)
print(2, 10 ** 2)
print(3, 10 ** 3)
print(4, 10 ** 4)
print(5, 10 ** 5)
print(6, 10 ** 6)
print(7, 10 ** 7)
print(8, 10 ** 8)
print(9, 10 ** 9)
print(10, 10 ** 10)

# string format 2
print('{0:>3}{1:>16})'.format(0, 10 ** 0))
print('{0:>3}{1:>16})'.format(1, 10 ** 1))
print('{0:>3}{1:>16})'.format(2, 10 ** 2))
print('{0:>3}{1:>16})'.format(3, 10 ** 3))
print('{0:>3}{1:>16})'.format(4, 10 ** 4))
print('{0:>3}{1:>16})'.format(5, 10 ** 5))
print('{0:>3}{1:>16})'.format(6, 10 ** 6))
print('{0:>3}{1:>16})'.format(7, 10 ** 7))
print('{0:>3}{1:>16})'.format(8, 10 ** 8))
print('{0:>3}{1:>16})'.format(9, 10 ** 9))
print('{0:>3}{1:>16})'.format(10, 10 ** 10))
```
<br>
Saat ini saya akan menjelaskan satu persatu dari syntax yang diberikan oleh Dosen <br>
1. **String format 1** <br>
Pada syntax / source code string format 1 akan menampilkan output berupa 2 outputan. <br>
Yang pertama (sebelah kiri) akan menampilkan angka urut dari angka 0 hingga 10, sedangkan sebelah kanan akan menampilkan Oprasi Aritmatika Pangkat. <br>
Dengan ketentuan sebagau berikut, oprasi pangkat dengan angka kiri sebagai pokok (Rumus : ** [Bintang dua]) <br>
Hasil dari syntax tersebut adalah 10 pangkat 0, hingga 10 pangkat 10. Dengan output sebagai berikut : <br>

![Operasi Aritmatika pangkat **](praktikum/pangkat.png)<br><br>

2. **String Format 2** <br><br>
Pada syntax / source code string format 2 akan menampilkan output berupa 2 output'an juga (Seoerti string format 1, yaitu kanan dan kiri) <br>
Dengan ketentuan sebagai berikut : <br>
> > Alignment, padding, dan precesion dengan **.format()** dalam kurung kurawal kita dapat menetapkan panjang bidang, rata kanan/kiri, parameter pembulatan dan banyak lagi. Contoh lain seperti berikut :
``` python
print('{0:8} | {1:9}'.format('sepatu','Jumlah'))
print('{0:8} | {1:9}'.format('dalas', 3.))
print('{0:8} | {1:9}'.format('NB',10))
```
Hasil dari source code contoh di atas akan seperti berikut : <br>
![OutPut Aligmnent contoh](praktikum/nb.png)<br><br>
> Secara default, **.format()** menggunakan rata text kiri, angka ke kanan. <,^, atau > untuk perataan kiri, tengah , atau kanan. Contoh lain dari penggunaan **.format()** sebagai berikut : <br>
``` python
print('{:<30}{:^30}{:>30}'.format('Kiri','Tengah','Kanan'))
print('{:<30}{:^30}{:>30}'.format(12,34,56))
```
Hasil dari source code contohdiatas akan muncul seperti ini : <br>
![Output Alignment](praktikum/rata.png)
<br>
<br>
Hasil string format 2 adalah : <br>
![Output Alignment contoh 2](praktikum/ratakanan.png)
<br>
<br>

### Pertemuan 6 - Lab 2

* Konversi Nilai Variable
Untuk pembahasan terakhir, kali ini akan myenyelesaikan tugas Lab 2 dari Dosen, yaitu Konversi Nilai Variable <br>
Tugas yang di berikan oleh Dosen adalah seperti gambar dibawah ini atau bisa di temukan dengan link berikut : ([temukan](lab%202.py))
``` python
a=int(input("Masukkan Nilai A : "))
b=int(input("Masukkan Nilai B : "))
print("Variable A : ",a)
print("Variable B : ",b)
print("Hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#Konversi nilai variable
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
```
<br>
Hasil dari source / code diatas : <br>

![Output source diatas](praktikum/code.png)
<br>
<br>
