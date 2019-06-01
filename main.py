# this is a little test with input/output using python

# imports area
import datetime
import json
import includes.input_validation as input_validation

# declarations area
months_json = '{"01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril", "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto", "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"}'
months = json.dumps(months_json)

print('Hello World py') #the print command on python 3 requires that use as a function() and use with 'single cotation marks'. In python the '' is more common that ""

# waiting for inputs
name = input('Qual o seu nome? ')

print('Seja bem vindo ao mundo python', name)

birth_str = input('me diga sua data de nascimento no formato DD/MM/AAAA: ')
print(input_validation.validate_date(birth_str))
birth = datetime.datetime.strptime(birth_str, '%d/%m/%Y')

# print('O seu aniversário é em', json["birth.strftime('%m')"])

print('Obrigado. Hora do registro:', datetime.datetime.now().strftime('%d/%m/%Y %H:%M'))