# Напишите функцию где дан список целых чисел. Заменить отрицательные на -1,
# положительные - на число 1, ноль оставить без изменений.
a=[1,-1,2,-2,3,-3,4,-4,0]
b=[]
for x in a:
	if x<0:
		b.append(-1)
	elif x>0:
		b.append(1)
	else:
		b.append(0)
print(a,b)
