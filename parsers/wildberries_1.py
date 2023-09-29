import requests
import json
import csv


arts = []

with open('links2.csv', 'r', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     arts = ([i[0] for i in spamreader])[320:350]


result = {
    'objects':[]
}

def getDataArt(art):
    res = {}
    for i in range(1,12+1):
        if (i<10):
            i = '0'+ str(i)
        else: i = str(i)

        r = requests.get(f'https://basket-{i}.wb.ru/vol{art[:-5]}/part{art[:-3]}/{art}/info/ru/card.json')

        if r.status_code == 200:
            r_seller = requests.get(f'https://basket-{i}.wb.ru/vol{art[:-5]}/part{art[:-3]}/{art}/info/sellers.json')
            seller = r_seller.json()
            card = r.json()
            
            options = []

            for option in card['options']:
                type_ = 'category'
                if option['value'].split(' ')[0].isnumeric():
                    type_ = 'range'

                options.append(
                    {
                        'verbose_name': option['name'],
                        'value': option['value'],
                        'type': type_
                    }
                )

            res = {
                'okpd2':'Электродвигатели, генераторы и трансформаторы',
                'okpd2_number': '27.11',
                'tittle': card['imt_name'],
                'wb_category':card['subj_name'],
                'wb_root_category':card['subj_root_name'],
                'description':card['description'],
                'options':options,
                'seller_inn': seller['inn'],
                'seller_name': seller['supplierName'],
                'link': f'https://www.wildberries.ru/catalog/{art}/detail.aspx'
            }

            break
    print('OK', art)

    if res == {}:
        print('FUCK')
    return res


# with open("электродвигатель3.json", "w") as outfile:
#     json.dump(result, outfile, ensure_ascii=False)
    
for art in arts:
    data = getDataArt(art)
    file_name = 'электродвигатель3.json'
    json_data = json.load(open(file_name, encoding='utf-8'))
    json_data['objects'].append(data)
    json.dump(json_data, open(file_name, mode='w', encoding='utf-8'),  ensure_ascii=False,)

