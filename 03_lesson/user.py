class User:
    
    def __init__(self, first_name, last_name):
        print('Ваши имя и фамилия')
        self.user_first_name = first_name
        self.user_last_name = last_name

    def sayFirst_name(self):
        print('Моё имя', self.user_first_name)

    def sayLast_name(self):
        print('Моя фамилия', self.user_last_name)

    def sayFirst_nameLast_name(self):
        print('Мои имя и фамилия', self.user_first_name, self.user_last_name)
