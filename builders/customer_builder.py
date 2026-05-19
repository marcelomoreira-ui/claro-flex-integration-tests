from faker import Faker
from cpf_generator import CPF

fake = Faker("pt_BR")
cpf = CPF.generate()


class CustomerBuilder:

    def __init__(self):

        self.cpf = cpf

        self.customer_data = {
            "listOfPlans": [
                {
                    "planId": "154f26e7-c2b0-4c78-8d61-5d1689dba76d",
                    "type": "MOBILE",
                },
                {
                    "planId": "154f26e7-c2b0-4c78-8d61-5d1689dba76d",
                    "type": "BROADBAND",
                },
            ],
            "user": {
                "fullName": fake.name(),
                "birthDate": fake.date_of_birth(
                    tzinfo=None, minimum_age=18, maximum_age=90
                ).isoformat(),
                "document": self.cpf,
                "email": fake.email(domain="hotmail.com"),
                "phoneContact": {
                    "countryCode": "55",
                    "lineNumber": fake.random_number(digits=11, fix_len=True),
                },
            },
            "address": {
                "district": fake.neighborhood(),
                "street": fake.street_name(),
                "country": "Brasil",
                "city": fake.city(),
                "state": "SP",
                "zipCode": fake.postcode(),
                "complement": "Casa",
                "number": fake.building_number(),
            },
            "lineInfo": {
                "msisdn": fake.random_number(digits=11, fix_len=True),
                "chipType": "CHIP_FLEX",
            },
            "credential": {"password": "52814fad129145", "document": self.cpf},
        }

    def with_email(self, email):
        self.customer_data["user"]["email"] = email
        return self

    def with_invalid_cpf(self):
        self.customer_data["user"]["document"] = "12345678900"
        self.customer_data["credential"]["document"] = "12345678900"
        return self
    
    def with_underage_birthdate(self):
        self.customer_data["user"]["document"] = "12345678911"
        self.customer_data["credential"]["document"] = "12345678911"
        self.customer_data["user"]["birthDate"] = fake.date_of_birth(tzinfo=None, minimum_age=17, maximum_age=17).isoformat()
        return self

    def build(self):
        return self.customer_data
