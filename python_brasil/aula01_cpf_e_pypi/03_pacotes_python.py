# instalando pacote achado no PyPI
# no terminal:
# pip install validate-docbr

from python_brasil.validate_docbr import CPF
cpf = CPF()
print(cpf.validate('54671486130'))
