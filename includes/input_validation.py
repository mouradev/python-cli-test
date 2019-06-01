# garantir que a string deve conter o formato xx/xx/xxxx
def validate_date(str_date):
    import re
    regex = re.compile('.{2}/.{2}/.{4}')
    if regex.match(str_date) is not None:
        return str_date
    else:
        return '00/00/0000'