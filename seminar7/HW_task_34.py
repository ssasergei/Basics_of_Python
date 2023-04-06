'''
	Задача 34:
	Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
	разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
	стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
	гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
	слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
	от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
	напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
	в порядке
	'''
vowels = ['а', 'я', 'о', 'ё', 'э', 'е', 'ы', 'и', 'у', 'ю']
good_chant = 'па-ра-ра рам-пам-па ра-па-дам ра-рам-па'
bad_chant = 'па-ра-рам пам-ра-рам па-пам па-ра-па-дам'
	

def check(chant):
    counts = list(map(lambda x: len(list(filter(lambda i: i in vowels, x))), chant.split()))
    return all(i == counts[0] for i in counts)


print(f'{good_chant} -> {check(good_chant)}')
print(f'{bad_chant} -> {check(bad_chant)}')