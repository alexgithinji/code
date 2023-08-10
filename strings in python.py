name=("alex githinji")

first_name = name[0:2]
last_name = name[5:7]
funky_name = name[::3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])