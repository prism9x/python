demo = "haalo" 
aa = "zzz"
a = "My name is Tuong %s %s"%(demo,aa)
print(a)

d = '%d'%(3.5)
e = '%d'%(10/6)
print(d)
print(e)

print('%.3f'%(3.9999))


# chuoi f-string

name = 'Tuong'
address = 'Phu Xuyen - Ha Noi'
phone= '0963953870'
email= 'prism9x@gmail.com'

rs = f'Name: {name} , \naddress: {address}, \nphone {phone}, \nemail {email}'
print(rs)


print('a:{1}, b: {2}, c: {0}'.format('one','two','three'))
