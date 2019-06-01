from unittest import TestCase
import includes.input_validation as input_validation

# o nome da classe deve conter o prefixo Test
class TestValidateDate(TestCase):

    # aqui podemos inicializar variaveis para usar globalmente nos testes
    def setUp(self):
        TestCase.setUp(self)
        self.str_date = '06/12/1993'

    # cada metodo que executar um teste de ter o prefixo test_
    def test_data_certa(self):
        data_certa = self.str_date
        self.assertEqual(data_certa, input_validation.validate_date(data_certa))

    def test_data_errada(self):
        data_errada = '99151993'
        self.assertRaises(ValueError, input_validation.validate_date, data_errada)

    def test_data_numeros_errados(self):
        data_errada = '99/15/1993'
        data_errada2 = '063323 ddd/12/555555555'
        self.assertRaises(ValueError, input_validation.validate_date, data_errada)
        self.assertRaises(ValueError, input_validation.validate_date, data_errada2)