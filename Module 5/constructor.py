class Phone:
    manufactured = 'china'
    def __init__(self,owner,brand,price):
        self.owner =owner
        self.brand=brand
        self.price=price
    def send_sms(self,phone,sms):
        text=f'seding to: {phone} {sms}'
        return text


my_phone=Phone('kala chan','oppo',9400 )
print(my_phone.brand,my_phone.owner,my_phone.price)
print(my_phone.send_sms('oppo','you are the owner'))

