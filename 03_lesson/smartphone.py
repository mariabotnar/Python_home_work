class Smartphone:

    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.brand = phone_brand
        self.model = phone_model
        self.number = subscriber_number

    def sayPhone_brand(self):
        print('Марка телефона', self.brand)

    def sayPhone_model(self):
        print('Модель телефона', self.model)

    def saySubscriber_number(self):
        print('Абонентский номер', self.number)
