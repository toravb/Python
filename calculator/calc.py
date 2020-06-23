#Функция считает согласно математическим правилас
def calc(array):
	i = 0
	while i < len(array):
		if array[i] == '*':
			array[i] = array[i-1] * array[i+1]
			del array[i-1]
			del array[i]
		else:
			i += 1
	i = 0
	while i < len(array):
		if array[i] == '/':
			array[i] = array[i-1] / array[i+1]
			del array[i-1]
			del array[i]
		else:
			i += 1
	i = 0
	while i < len(array):
		if array[i] == '+':
			array[i] = array[i-1] + array[i+1]
			del array[i-1]
			del array[i]
		else:
			i += 1
	i = 0
	while i < len(array):
		if array[i] == '-':
			array[i] = array[i-1] - array[i+1]
			del array[i-1]
			del array[i]
		else:
			i += 1
		
#Нужен если есть скобки
subValue = []

value = input()
text = value

#Заменяет введенный пользователем текст, для правильного разбиения в массив
if '+' in value:
	value = value.replace('+', ' + ')
if '-' in value:
	value = value.replace('-', ' - ')
if '*' in value:
	value = value.replace('*', ' * ')
if '/' in value:
	value = value.replace('/', ' / ')
if '(' in value:
	value = value.replace('(', ' ( ')
if ')' in value:
	value = value.replace(')', ' ) ')

value = value.split()

#Заменяет тип str на int или float где возможно
i = 0
while i < len(value):
	if value[i] == '-' and value[i+1] == '-' or value[i] == '+' and value[i+1] == '-' or value[i] == '(' and value[i+1] == '-':
		value[i+1] = value[i+1] + value[i+2]
		del value[i+2]
	else:
		i += 1

for i in range(len(value)):
	
	if value[i].isdigit():
		value[i] = int(value[i])
	else:
		try:
			value[i] = float(value[i])
		except ValueError:
			value[i] = value[i]

#Переносит значения в скобках в отдельный массив 
i = 0
while i < len(value):
	if value[i] == '(':
		del value[i]
		while i < len(value):
			if value[i] == ')':
				value[i] = '|'
				break
			else:
				subValue.append(value[i])
				del value[i]
	i += 1

calc(subValue)

#переносит посчитанные значения обратно в основной массив
l = 0
for i in range(len(value)):
	
	try:
		index = value.index('|')
		value.insert(index, subValue[l])
		l += 1
		del value[index + 1]
	except ValueError:
		pass
del subValue

calc(value)

print(text + ' = ' + str(value[0]))

del(value)
