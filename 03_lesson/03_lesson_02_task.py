from smartphone import Smartphone

catalog = []
phone_1 = Smartphone('Apple', 'iPhone 13', '+79592233654')
phone_2 = Smartphone('Samsung', 'Galaxy S24', '+79592526654')
phone_3 = Smartphone('Poco', 'X5 Pro 5G', '+79598987456')
phone_4 = Smartphone('Realme', 'C53', '+79596363321')
phone_5 = Smartphone('Nokia', '3310', '+79595456258')

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')