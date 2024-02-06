#print('\a')

# Chuỗi trần thêm r trước ~ @ trong C#
print(r'Haizz, \neu mot ngay nao do')


strA = "Prism9x.com\n"
strB = "Demo String"
# Cộng trong chuỗi (+)
strC = strA +"\n"+ strB

# Toán tử nhân (*)
strD = strA*5

print(strC)

print(strD)

# toán tử "in" kiểm tra chuỗi có nằm trong chuỗi đó hay không

e = "Prism9x@gmail.com"
d = "x"

rs = d in e
print(rs)

#index chuỗi
# Đi xuôi chuỗi
print(e[1])
# Đi ngược chuỗi
print(e[-2])

# hàm len lấy ra độ dài chuỗi kí tự
f = "xin cho toi mot cai ten"
strLen = f[len(f) - 1]

print(strLen)

# cắt chuỗi [vị trí đầu : vị trí cuối]
print("Cắt chuỗi")
strTrim = f[0:10]
strTrim1 = f[None:5:-1]
print(strTrim)
print(strTrim1)


# Ép kiểu

strAA = int("69") + 5
strBB = str(69) + "5"

print(strAA)
print(strBB)