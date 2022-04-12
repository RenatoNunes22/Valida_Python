from Cpf_Cnpj import Documento
from TelefonesBr import TelefonesBr
from acesso_cep import BuscaEndereco
#Teste CPF:
cpf = "11889653446"
documento = Documento.cria_documento(cpf)
print(documento)
#Teste CNPJ:
cnpj = "01394972000170"
documento = Documento.cria_documento(cnpj)
print(documento)
#Teste Telefone:
telefone = "5581996847547"
telefone_obj = TelefonesBr(telefone)
print(telefone_obj)
#Teste CEP
cep = 50711120
objeto_cep = BuscaEndereco(cep)
a = objeto_cep.acessa_via_cep()
print(objeto_cep)
print(a)
