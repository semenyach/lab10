import json
file='file.json'
a=''
def avail():
    if tov['available']== True:
        return 'В наличии'
    else:
        return 'Нет в наличии!'
with open(file, encoding='utf-8 ') as js:
    dict=json.load(js)
    name=input('Введите название')
    price=input('Введите Цену')
    weight=input('Введите вес')
    available=bool(input('В наличии?'))
    dict['products'].append({
        'name': name,
        'price': price,
        'weight': weight,
        'available': available,
    })
    with open('file.json', 'w') as outfile:
        json.dump(dict, outfile, sort_keys=True, indent=4)
    for tov in dict['products']:
            a+='Название: '+ str(tov['name'])+ '\n'
            a += 'Цена: ' + str(tov['price']) + '\n'
            a += 'Вес: ' + str(tov['weight']) + '\n'
            a += avail() + '\n\n'

print(a)