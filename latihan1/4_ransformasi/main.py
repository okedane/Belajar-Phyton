print("======================")
# Mengubah Huruf Besar/Kecil


# "upper()" mengubah huruf kecil ke Besar
kata = "dicoding"
kata = kata.upper()
print(kata)

#lower() mengubah huruf besar ke kecil
kata = "diCodinG"
kata = kata.lower()
print(kata)

#rstrip() menghapus whitespace pada sebelah kenan atau akhir string
print("Dicoding             a")
print("Dicodinga".rstrip())
#lstrip()  menghapus whitespace pada sebelah kanan atau akhir string
print("         Dicoding".lstrip())
#strip awal dan akhir
print("         Dicoding        ".strip()),

#menghilangkan value yang sama
kata = 'CodeCodecodingCode'
print(kata.strip("Code"))

#menemukan kata pada awal string
print('Dicoding Indonesia'.startswith('Dicoding'))

#menemukan kata pada awal string
print('Dicoding Indonesia'.endswith('Dicoding'))

#Join() Menggabungkan String
print(''.join(['Dicoding', 'Indonesia', '!']))

#split() Memisahkan data
print('Dicoding Indonesia !'.split())

print("""
Halo semuanya,
perkenalkan nama ku dani,
dari Sumenep
""".split('\n'))


# Mengganti Elemen String
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemprograman"))

#isuppwe() Mengembalikan falue true jika semunya KAPITAL
kata = 'DICODING'
print(kata.isupper())

#isLower() mengecek apakah semunya kecil maka true
kata = 'dicoding'
print(kata.islower())

#isalpha() mengembalikan value true jika semua karakter alfabert
kata = 'dicoding'
kataNo = 'dicoding123'
print(kata.isalpha())

#isalnum() AlsaFumnerik = true
print(kataNo.isalnum())

#isdecimal(), numerik == true
print('123'.isdecimal())

#isspace mengecek apakah hanya berisi spasi, tab, newline, withspace lainya = true
print('    '.isspace())

#istitle() mengembalikan nilai true jika string berisis huruf kapital setiap kata

print('Dicoding Indonesia'.istitle())

print("======================")

#zfill() menambahkan nilai 0 tujuan membantu untuk memastikan sebauah value meiliki panjnag tetap
teks = 'Code'
tambah_number = teks.zfill(6)
print(tambah_number)

print("======================")

#rjust() untuk menjadi rata kanan sesuai value
print('Dicoding'.rjust(20))
print('Dicoding'.rjust(10))
print('Dicoding'.rjust(20, '!'))
print("======================")

#ijust() menambajan rata kiri sesuai value
print('Dicoding'.ljust(20, '!'))

#center() rata kanan kiri
print('Dicoding'.center(10, "-"))


# agar bisa tanda petik di string

st1 = "Jum\'at"
print(st1)


print('sekarang hari \nsenin dan hari jum\'at')

#raw string menampilkan sesuai value
print('Dicoding\tindonesia')
print(r'Dicoding\ttahioalan')
print('Dicoding\indonesia')
