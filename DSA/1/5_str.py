str1 = input('Str1 : ')
str2 = input('Str2 : ')
str3 = input('Str3 : ')
i = 0
while i < len(str1) :
	if str1[i]==str2[0]:
		found = True
		for j in range(1, len(str2)):
			if not str1[i+j]==str2[j]:
				found = False
				break
		if found:
			str1 = str1[:i]+str3+str1[i+len(str2):]
			i = i + len(str3) - 1
	i = i + 1
print('str  : ' + str1)