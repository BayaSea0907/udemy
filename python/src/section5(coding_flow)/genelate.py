
def genelate():
	yield print('hello')
	yield print('world')
	yield print('!!')

func = genelate()

next(func)
next(func)
next(func)
next(func)



