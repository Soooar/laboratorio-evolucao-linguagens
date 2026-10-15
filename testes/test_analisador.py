import math
import unittest

from python.analisador import analisar_turma


class AnalisarTurmaTests(unittest.TestCase):
    def test_calcula_estatisticas_e_classificacoes(self):
        resultado = analisar_turma([8.5, 6.0, 9.0, 4.5, 7.0, 5.5, 3.0])

        self.assertEqual(resultado["quantidade"], 7)
        self.assertAlmostEqual(resultado["media"], 6.214285714285714)
        self.assertEqual(resultado["maior"], 9.0)
        self.assertEqual(resultado["menor"], 3.0)
        self.assertEqual(resultado["aprovados"], 3)
        self.assertEqual(resultado["recuperacao"], 2)
        self.assertEqual(resultado["reprovados"], 2)

    def test_aceita_notas_nos_limites(self):
        resultado = analisar_turma([0, 10])

        self.assertEqual(resultado["menor"], 0)
        self.assertEqual(resultado["maior"], 10)
        self.assertEqual(resultado["reprovados"], 1)
        self.assertEqual(resultado["aprovados"], 1)

    def test_rejeita_lista_vazia(self):
        with self.assertRaisesRegex(ValueError, "não pode estar vazia"):
            analisar_turma([])

    def test_rejeita_valor_nao_numerico_e_booleano(self):
        for notas in ([8, "7"], [True, 8]):
            with self.subTest(notas=notas):
                with self.assertRaises(TypeError):
                    analisar_turma(notas)

    def test_rejeita_valores_fora_do_intervalo_e_nao_finitos(self):
        for nota in (-0.1, 10.1, math.nan, math.inf, -math.inf):
            with self.subTest(nota=nota):
                with self.assertRaises(ValueError):
                    analisar_turma([nota])


if __name__ == "__main__":
    unittest.main()
