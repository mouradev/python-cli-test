from unittest import TestCase
import includes.input_validation as input_validation

# o nome da classe deve conter o prefixo Test
class TestValidateDate(TestCase):

    # aqui podemos inicializar variaveis para usar globalmente nos testes
    def setUp(self):
        TestCase.setUp(self)
        self.str_date = '06/12/1993'

    # cada metodo que executar um teste de ter o prefixo test_
    def test_validate_date(self):
        data_certa = self.str_date
        data_errada = '06121993'
        self.assertEqual(self.str_date, input_validation.validate_date(self.str_date))
        self.assertNotEqual(data_errada, input_validation.validate_date(data_errada))