#Сайт: https://pythobyte.com/python-hashmaps-52737/

phone_numbers={
'person1':909090909,
'person2':808080808,
'person3':707070707,
'person4':606060606,
'person5':505050505,
'person6':909090901,
'person7':808080802,
'person8':707070703,
'person9':606060604,
'person10':505050500
} #Хеш-мапа оформлюється як словник з парами ключ-значення. У даному випадку до кожної особи додано її телефон.

print(phone_numbers) #Виводимо існуючі значення на екран для демонстрації.

print(phone_numbers['person1']) #Знаходимо наявну інформацію по person1 за відповідним ключем 'person1'.

phone_numbers.pop('person1') #Видаляємо значення 'person1'
print(phone_numbers) #Демонструємо отриманий результат

phone_numbers.update({'person4':111111111}) #Оновлюємо номер телефона person1
print(phone_numbers) #Демонструємо отриманий результат