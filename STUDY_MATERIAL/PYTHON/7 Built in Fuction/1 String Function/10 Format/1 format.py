#empty placholders
str3 = 'Welcome to {} {}'.format('Sandip','M')
#numbered indexes
str2 = 'Welcome to {1} {0}'.format('Sandip','Makwana')

print(str3)
print(str2)

#name indexes
str1 = 'Welcome to {fnm} {lnm}'
print(str1.format(fnm='Sandip',lnm='Makwana'))