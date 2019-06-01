# garantir que a string deve conter o formato xx/xx/xxxx
def validate_date(str_date):
    import re
    regex = re.compile('.{2}/.{2}/.{4}')
    if regex.match(str_date) is not None:

        # fazer o split da data para garantir que dias terão mais que 0 e menos que 32
        # meses mais que 0 e menos que 13
        # ano mais de 1000
        splited_date = str_date.split('/')

        valid_date = True
        if(not (int(splited_date[0]) > 0 and int(splited_date[0]) < 32)):
            valid_date = False
        if(not (int(splited_date[1]) > 0 and int(splited_date[1]) < 13)):
            valid_date = False
        if(not (int(splited_date[2]) > 1000)):
            valid_date = False
        
        if(not valid_date):
            raise ValueError('Invalid date. Check the numbers')

        return str_date
    else:
        raise ValueError('Invalid format for date. Please type a date in format dd/mm/yyyy')