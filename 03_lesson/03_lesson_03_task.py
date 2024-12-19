from address import Address
from mailing import Mailing

to_address = Address('224220', 'Воронеж', 'Лобановского', '24', '695')
from_address = Address('112466', 'Тула', 'Маршала Жукова', '2', '48')
mailing = Mailing(to_address, from_address, '2600', '123654789')

print(mailing)
