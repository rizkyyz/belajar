"""
Aplikasi KHS dengan paradigma prosedural
"""

# Matakuliah 1
mk1_nama = 'kalkulus'
mk1_sks = 3
mk1_nilai = 77

# Matakuliah 2
mk2_nama = 'indonesia'
mk2_sks = 2
mk2_nilai = 81

# Matakuliah 3
mk3_nama = 'Algoritma dan Struktur Data'
mk3_sks = 3
mk3_nilai = 74

# Matakuliah 4
mk4_nama = 'pemrograman'
mk4_sks = 3
mk4_nilai = 74

# Matakuliah 5
mk5_nama = 'teknologi'
mk5_sks = 2
mk5_nilai = 100

# Matakuliah 6
mk6_nama = 'fisika'
mk6_sks = 4
mk6_nilai = 80

# Matakuliah 7
mk7_nama = 'pkn'
mk7_sks = 3
mk7_nilai = 91

# ---- PROSES ----
# Mengubah ke skala-4

mk1_skala_7 = mk1_nilai / 100 * 4
mk2_skala_7 = mk2_nilai / 100 * 4
mk3_skala_7 = mk3_nilai / 100 * 4
mk4_skala_7 = mk4_nilai / 100 * 4
mk5_skala_7 = mk5_nilai / 100 * 4
mk6_skala_7 = mk6_nilai / 100 * 4
mk7_skala_7 = mk7_nilai / 100 * 4


def get_nilai_huruf(nilai: float):
    if nilai >= 3.70:
        return 'A'
    elif 3.70 > nilai >= 3.0:
        return 'B'
    elif 3.0 > nilai >= 2.0:
        return 'C'
    elif 2.0 > nilai >= 1.0:
        return 'D'
    else:
        return 'E'

# Menentukan nilai huruf
mk1_nilai_huruf = get_nilai_huruf(mk1_skala_7)
mk2_nilai_huruf = get_nilai_huruf(mk2_skala_7)
mk3_nilai_huruf = get_nilai_huruf(mk3_skala_7)
mk4_nilai_huruf = get_nilai_huruf(mk4_skala_7)
mk5_nilai_huruf = get_nilai_huruf(mk5_skala_7)
mk6_nilai_huruf = get_nilai_huruf(mk6_skala_7)
mk7_nilai_huruf = get_nilai_huruf(mk7_skala_7)

# Menghitung total SKS
total_sks = mk1_sks + mk2_sks + mk3_sks + mk4_sks + mk5_sks + mk6_sks + mk7_sks

# Menghitung IPK
ipk = ((mk1_skala_7 * mk1_sks) + (mk2_skala_7 * mk2_sks) + (mk3_skala_7 * mk3_sks) + (mk4_skala_7 * mk4_sks) + (mk5_skala_7 * mk5_sks) + (mk6_skala_7 * mk6_sks) + (mk7_skala_7 * mk7_sks)) / total_sks

print("KARTU HASIL ")
print("--------------------------")
print("Mata Kuliah : {}".format(mk1_nama))
print("Nilai Angka : {}".format(mk1_skala_7))
print("Nilai Huruf : {}".format(mk1_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk2_nama))
print("Nilai Angka : {}".format(mk2_skala_7))
print("Nilai Huruf : {}".format(mk2_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk3_nama))
print("Nilai Angka : {}".format(mk3_skala_7))
print("Nilai Huruf : {}".format(mk3_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk4_nama))
print("Nilai Angka : {}".format(mk4_skala_7))
print("Nilai Huruf : {}".format(mk4_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk5_nama))
print("Nilai Angka : {}".format(mk5_skala_7))
print("Nilai Huruf : {}".format(mk5_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk6_nama))
print("Nilai Angka : {}".format(mk6_skala_7))
print("Nilai Huruf : {}".format(mk6_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk7_nama))
print("Nilai Angka : {}".format(mk7_skala_7))
print("Nilai Huruf : {}".format(mk7_nilai_huruf))
print("--------------------------")
print("Total SKS \t: {}".format(total_sks))
print("IPK \t\t: {}".format(ipk))
