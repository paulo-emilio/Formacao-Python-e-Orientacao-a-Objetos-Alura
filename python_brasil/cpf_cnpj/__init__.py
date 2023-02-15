from validate_docbr import CPF, CNPJ

# Usado em exercícios finais


class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos incorreta!')


class DocCpf:
    def __init__(self, documento):
        if self.valido(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')

    def __str__(self):
        return self.format

    def valido(self, documento):
        return CPF().validate(documento)

    @property
    def format(self):
        return CPF().mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valido(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')

    def __str__(self):
        return self.format

    def valido(self, documento):
        return CNPJ().validate(documento)

    @property
    def format(self):
        return CNPJ().mask(self.cnpj)





# Usado em exercícios iniciais


class CpfCnpj:
    def __init__(self, documento, tipo_doc):
        self.tipo_doc = tipo_doc
        if self.tipo_doc == 'cpf':
            self.cpf = str(documento)
            if not self.cpf_e_valido:
                raise ValueError('CPF inválido!')
        elif self.tipo_doc == 'cnpj':
            self.cnpj = str(documento)
            if not self.cnpj_e_valido:
                raise ValueError('CNPJ inválido!')
        else:
            raise ValueError('Documento inválido!')

    def __str__(self):
        if self.tipo_doc == 'cpf':
            return self.format_cpf()
        elif self.tipo_doc == 'cnpj':
            return self.format_cnpj()

    @property
    def cpf_e_valido(self):
        if len(self.cpf) == 11:
            validador = CPF()
            return validador.validate(self.cpf)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    @property
    def cnpj_e_valido(self):
        if len(self.cnpj) == 14:
            validador = CNPJ()
            return validador.validate(self.cnpj)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
