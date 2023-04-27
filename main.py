import json
file='file.json'
a=''
def avail(x):
    if x== True or x==1 or x=='Да' or 'да':
        return 'В наличии'
    else:
        return 'Нет в наличии!'
with open(file, encoding='utf-8 ') as js:
    dict=json.load(js)
    name=input('Введите название')
    price=int(input('Введите Цену'))
    weight=int(input('Введите вес'))
    available=bool(input('В наличии?'))
    dict['products'].append({
        'name': name,
        'price': price,
        'weight': weight,
        'available': avail(available),
    })
    with open('file.json', 'w') as outfile:
        json.dump(dict, outfile, indent=4)
    for tov in dict['products']:
            a+='Название: '+ str(tov['name'])+ '\n'
            a += 'Цена: ' + str(tov['price']) + '\n'
            a += 'Вес: ' + str(tov['weight']) + '\n'
            a += avail(tov['available']) + '\n\n'

print(a)