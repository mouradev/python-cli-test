# helper para traduzir meses em pt-br

months = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

# def months():
#     print(months)

def month(month_number):
    month_number = int(month_number)
    if(month_number > 0 and month_number < 13):
        return months[month_number-1]
    else:
        raise ValueError('Invalid number for month')