import json
filename = r'/home/nik/data/datasun4.json'


with open(filename, 'r', encoding='utf-8') as fh: #открываем файл на чтение
    data = json.load(fh)



for i in data:
    beach = Beach.objects.create(
        name  = data[i]['name'],
        full_name = data[i]['full_name'],
        address = data[i]['address'],
        phone = data[i]['phone'],
        email = data[i]['email'],
        region = data[i]['region'],
        accredited_organization = data[i]['accredited_organization'],
        certificate_number =data[i]['certificate_number'],
        registrated_num = data[i]['registrated_num'],
        inn = data[i]['inn'],
        ogrn = data[i]['ogrn'],
        category = data[i]['category'],
        slug = data[i]['ogrn']
    )
    beach.save()


from .models import Beach, Rock, Hotel




import json
filename = r'/home/nik/data/datarock.json'


with open(filename, 'r', encoding='utf-8') as fh: #открываем файл на чтение
    data = json.load(fh)



for i in data:
    rock = Rock.objects.create(
        name  = data[i]['name'],
        full_name = data[i]['full_name'],
        address = data[i]['address'],
        phone = data[i]['phone'],
        email = data[i]['email'],
        region = data[i]['region'],
        accredited_organization = data[i]['accredited_organization'],
        certificate_number =data[i]['certificate_number'],
        registrated_num = data[i]['registrated_num'],
        inn = data[i]['inn'],
        ogrn = data[i]['ogrn'],
        category = data[i]['category'],
        slug = data[i]['ogrn']
        )
    rock.save()








from sunrise.models import  Hotel
import json
filename = r'/home/nik/data/datahotel.json'


with open(filename, 'r', encoding='utf-8') as fh: #открываем файл на чтение
    data = json.load(fh)


for i in data:
    hotel = Hotel.objects.create(
        name  = data[i]['name'],
        full_name = data[i]['full_name'],
        address = data[i]['address'],
        phone = data[i]['phone'],
        email = data[i]['email'],
        region = data[i]['region'],
        accredited_organization = data[i]['accredited_organization'],
        certificate_number =data[i]['certificate_number'],
        registrated_num = data[i]['registrated_num'],
        inn = data[i]['inn'],
        ogrn = data[i]['ogrn'],
        category = data[i]['category'],
        slug = data[i]['ogrn']
        )
    hotel.save()
