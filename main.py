# this is a little test with input/output using python

# imports area
import datetime
import includes.input_validation as input_validation
import includes.months as months

# declarations area

print('Hello World py') #the print command on python 3 requires that use as a function() and use with 'single cotation marks'. In python the '' is more common that ""

# waiting for inputs
name = input('Qual o seu nome? ')

print('Seja bem vindo ao mundo python', name)

date_is_valid = False
while not date_is_valid:
    birth_str = input('me diga sua data de nascimento no formato DD/MM/AAAA: ')
    try:
        birth_str = input_validation.validate_date(birth_str)
        date_is_valid = True
    except ValueError as e:
        print(e)

birth = datetime.datetime.strptime(birth_str, '%d/%m/%Y')

print('O seu aniversário é em', months.month(birth.strftime('%m')))
print('Obrigado. Hora do registro:', datetime.datetime.now().strftime('%d/%m/%Y %H:%M'))