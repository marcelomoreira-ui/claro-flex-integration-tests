from faker import Faker
from cpf_generator import CPF

fake = Faker("pt_BR")


class CustomerBuilder:

    def __init__(self):
        self.customer_data = {
            {
                "customer": {
                    "name": fake.name(),
                    "birthDate": fake.date_of_birth(
                        minimum_age=18, maximum_age=120).isoformat("YYYY-MM-DDThh:mm:ss.sTZD"),
                    "partyIdentifications": [
                        {
                            "identificationType": "CPF",
                            "identificationId": CPF().generate(),
                        }
                    ],
                    "phoneContacts": [
                        {"phoneType": "Residencial", "phoneNumber": fake.phone_number()}
                    ],
                    "emailAddress": fake.email(domain="hotmail.com.br"),
                    "channelId": "Now On Line",
                    "contact": {
                        "firstName": fake.first_name,
                        "lastName": fake.last_name(),
                        "email": fake.email(domain="hotmail.com.br"),
                    },
                    "address": {
                        "streetName": fake.street_name(),
                        "complement": fake.secondary_address(),
                        "number": fake.building_number(),
                        "neighborhood": fake.neighborhood(),
                        "city": fake.city(),
                        "state": fake.estado_sigla(),
                        "postalCode": fake.postcode(),
                        "country": "Brasil",
                    },
                }
            }
        }

    def with_email(self, email):
        self.customer_data["customer"]["emailAddress"] = email
        return self

    def with_invalid_cpf(self):
        self.customer_data["customer"]["partyIdentifications"][0][
            "identificationId"
        ] = "12345678900"
        return self

    def build(self):
        return self.customer_data
