from unittest import TestCase
import includes.months as months

class TestMonths(TestCase):

    # aqui podemos inicializar variaveis para usar globalmente nos testes
    def setUp(self):
        TestCase.setUp(self)
        self.meses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def test_month(self):
        self.assertEqual('Março', months.month(3))

    def test_month_numero_errado(self):
        self.assertRaises(ValueError, months.month, 13)
        self.assertRaises(ValueError, months.month, 0)
        self.assertRaises(ValueError, months.month, -1)

    def test_month_mes_a_mes(self):
        self.assertEqual('Janeiro', months.month(1))
        self.assertEqual('Fevereiro', months.month(2))
        self.assertEqual('Março', months.month(3))
        self.assertEqual('Abril', months.month(4))
        self.assertEqual('Maio', months.month(5))
        self.assertEqual('Junho', months.month(6))
        self.assertEqual('Julho', months.month('07'))
        self.assertEqual('Agosto', months.month(8))
        self.assertEqual('Setembro', months.month(9))
        self.assertEqual('Outubro', months.month(10))
        self.assertEqual('Novembro', months.month(11))
        self.assertEqual('Dezembro', months.month(12))

    def test_month_nao_numerico(self):
        self.assertRaises(ValueError, months.month, 'thing')
        self.assertRaises(ValueError, months.month, '1thing12')