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



