import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF, CNH
import random
from tractorsApp.models import Driver, Tractor

def criando_drivers(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        cnh = CNH()

        name = fake.name()
        birthYear = '{}-{}-{}'.format(random.randrange(1960, 2005),random.randrange(1, 12),random.randrange(1, 31))
        cpf = cpf.generate()
        cnh = cnh.generate()
        gender = random.choice(['M', 'F', 'O', 'X'])
        p = Driver(name=name, birthYear=birthYear, cpf=cpf, cnh=cnh, gender=gender)
        p.save()

def criando_tractors(quantidade_de_tratores):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_tratores):
        identification = '{}'.format(random.randrange(100000, 9999999))
        owner = fake.name()
        tractorYear = '{}'.format(random.randrange(1990, 2023))
        manufacter = random.choice(['Valtra', 'Caterpillar', 'Komatsu', 'Mahindra'])
        lastReview = '{}-{}-{}'.format(random.randrange(2019, 2023),random.randrange(1, 12),random.randrange(1, 31))
        lastLocation = '{},{}'.format(random.uniform(20, 22), random.uniform(30, 40))
        lastFuelDate = '{}-{}-{}'.format(2023, random.randrange(1, 2),random.randrange(1, 30))
        p = Tractor(identification=identification, owner=owner, tractorYear=tractorYear, manufacter=manufacter, lastReview=lastReview, lastLocation=lastLocation, lastFuelDate=lastFuelDate)
        p.save()


criando_drivers(30)
criando_tractors(15)
print("Banco populado com dados Fakes")