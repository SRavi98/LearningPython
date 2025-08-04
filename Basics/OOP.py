class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type


Customers = [Customer('Ravi', 'Gold'),Customer('Shailu', 'Bronze')]

print('Customer Name: ' + Customers[1].name, 
    '\nMembership Type: ' + Customers[1].membership_type)