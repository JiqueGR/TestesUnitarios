import unittest
from main import fibonacci, fatorial, int_para_romano

class TestesFuncoes(unittest.TestCase):

    def test_fibonacci_caso_de_uso(self):
        print("\nTeste caso de uso Fibonacci: ENTRADA(5), SAIDA ESPERADA(8)")
        self.assertEqual(fibonacci(5), 8)
        print("Teste caso de uso Fibonacci foi um sucesso")

    def test_fibonacci_com_valor_incorreto(self):
        with self.assertRaises(ValueError):
            print("\nTeste exceção Fibonacci: ENTRADA(5), SAIDA (10)")
            self.assertEqual(fibonacci(5), 10)

    def test_fibonacci_com_valor_string(self):
        try:
            print("\nTeste exceção Fibonacci: ENTRADA tipo string")
            fibonacci("5")
        except (ValueError, TypeError) as mensagem:
            print("Erro ao calcular Fibonacci:", str(mensagem))

    def test_fibonacci_com_valor_negativo(self):
        try:
            print("\nTeste exceção Fibonacci: ENTRADA fora do intervalo")
            fibonacci(-1)
        except (ValueError, TypeError) as mensagem:
            print("Erro ao calcular Fibonacci:", str(mensagem))

    def test_fatorial_caso_de_uso(self):
        print("\nTeste caso de uso Fatorial: ENTRADA(5), SAIDA ESPERADA(120)")
        self.assertEqual(fatorial(5), 120)
        print("Teste caso de uso Fatorial foi um sucesso")

    def test_fatorial_com_valor_negativo(self):
        try:
            print("\nTeste exceção Fatorial: ENTRADA negativa")
            fatorial(-5)
        except ValueError as mensagem:
            print("Erro ao calcular Fatorial:", str(mensagem))

    def test_int_para_romano_caso_de_uso(self):
        print("\nTeste caso de uso Inteiro para Romano: ENTRADA(3549), SAIDA ESPERADA('MMMDXLIX')")
        self.assertEqual(int_para_romano(3549), 'MMMDXLIX')
        print("Teste caso de uso Inteiro para Romano foi um sucesso")

    def test_int_para_romano_com_valor_zero(self):
        try:
            print("\nTeste exceção Inteiro para Romano: ENTRADA zero")
            int_para_romano(0)
        except ValueError as mensagem:
            print("Erro ao converter Inteiro para Romano:", str(mensagem))


if __name__ == '__main__':
    unittest.main()
