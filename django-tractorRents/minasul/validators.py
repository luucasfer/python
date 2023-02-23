import re
from validate_docbr import CPF, CNH

def validateOwner(owner):
    return owner.isalpha()

def validateTractorYear(tractorYear):
    model = '[1-2]{1}[9]{1}[8-9]{1}[0-9]{1}'
    response = re.findall(model, tractorYear)
    return response

def validateName(name):
    return name.isalpha()
        
def validateCPF(cpfNumber):
    cpf = CPF()
    return cpf.validate(cpfNumber)
       
def validateCNH(cnhNumber):
    cnh = CNH()
    return cnh.validate(cnhNumber)
