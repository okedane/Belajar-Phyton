# Data Typing

print('Data Typing')
age = 17
salary = 500000.00
name = 'dani'
benar = True
variabel_list = [1, "Dicoding", True, 1.0]
print(type(age))
print(type(salary))
print(type(name))
print(type(benar))
print(type(variabel_list))
print(variabel_list)

print('=======================')
print('double quuoto')

multi_line = """Helloo
Kapan Terakhir Kita Bertemu ?
Kita Bertemu Hari Jummat
"""
print(multi_line)

print('=======================')
# untuk melihat urutan karakter

x = 'Dicoding'
print(x[0])
print(x[2:]) #melewatkan 2 karakter
print(x[:2]) # mengambil 2 karakter
print(variabel_list[2:]) # melewati 2 value

print('=======================')
#formatted String
name = 'dani'
print(f"Hello ,nama saya {name} semua" )
print("Hello, nama Saya %s" % (name))
print("Hello, nama saya {}".format(name))

print("======================")

# Mengubah list data dalam List
x = [1, 2, 3 , 4]
x[0] = 0
x[1] = 'dua'
print(x)

print("======================")

# indexing

x = [ "Laptop", "Minotor", "Mouse", "MousePad", "Keyboard", "webcam", "microphone"]
print(x[0])
print(x[3])
print(x[-3]) # menampilkan 3 value dari terakhir

#square[start:stop:step]
print(x[0:7:1])

print("======================")
#tuple  seperti sama dengan list

x = (1, "Dicoding", 1+3j)
print(type(x))
print(x[1])
print(x[1:3])

print("======================")
#set
x = {1,2,"dani", 2, "dani", 13, 3}
print(type(x))
print(x)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1.union(set2)
print("Union : ", union)

intersection = set1.intersection(set2)
print("Interaction", intersection)

print("======================")
print("Dict")
x = {'name': 'Perseus Evans', 'age':20, 'isMarried':False}
print(type(x))
#memanggil dict
print("nama saya", x['name'])
#Mengubah
x['Job'] = "Web Developer"
print(x)
#Menghapus
del x['isMarried']
print(x)

#memanggil dua value
print(f"Nama : {x['name']}, Pekerjaan : {x['Job']}")
print("Nama :", x['name'], "Pekerjaan : ", x['Job'])



