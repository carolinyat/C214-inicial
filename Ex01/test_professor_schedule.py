import unittest
from professor_schedule import ProfessorSchedule


class TestProfessorSchedule(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "nomeDoProfessor": "Renzo",
            "horarioDeAtendimento": "08:00 - 10:00",
            "periodo": "integral",
            "sala": "3"
        }
        self.invalid_data = {
            "nomeDoProfessor": "",
            "horarioDeAtendimento": "",
            "periodo": "",
            "sala": ""
        }

    # Testes de sucesso

    # Verificar se o método get_predio retorna o prédio correto (1) para salas numeradas de 1 a 5
    def test_predio_correct_for_sala_1_to_5(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("3"), 1)

    # Verificar se o método get_predio retorna o prédio correto (2) para salas numeradas de 6 a 10
    def test_predio_correct_for_sala_6_to_10(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("7"), 2)

    # Verificar se o método get_predio retorna o prédio correto para salas acima de 10, calculando adequadamente.
    def test_predio_correct_for_sala_above_10(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("12"), 3)

    # Verificar se o método populate_schedule processa os dados corretamente e retorna todas as informações esperadas
    def test_populate_schedule_success(self):
        ps = ProfessorSchedule(self.valid_data)
        result = ps.populate_schedule()
        self.assertEqual(result['predio'], 1)
        self.assertEqual(result['nomeDoProfessor'], "Renzo")
        self.assertEqual(result['horarioDeAtendimento'], "08:00 - 10:00")
        self.assertEqual(result['periodo'], "integral")
        self.assertEqual(result['sala'], "3")

    def test_predio_for_edge_sala_5(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("5"), 1)

    def test_predio_for_edge_sala_10(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("10"), 2)

    def test_predio_correct_for_sala_11_to_15(self):
        ps = ProfessorSchedule(self.valid_data)
        self.assertEqual(ps.get_predio("14"), 3)

    def test_populate_schedule_success_with_different_sala(self):
        data = self.valid_data.copy()
        data["sala"] = "8"
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertEqual(result['predio'], 2)
        self.assertEqual(result['sala'], "8")

    def test_populate_schedule_success_with_periodo_noturno(self):
        data = self.valid_data.copy()
        data["periodo"] = "noturno"
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertEqual(result['periodo'], "noturno")

    def test_populate_schedule_success_full_data(self):
        data = {
            "nomeDoProfessor": "Dr. Ana",
            "horarioDeAtendimento": "14:00 - 16:00",
            "periodo": "noturno",
            "sala": "6"
        }
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertEqual(result['nomeDoProfessor'], "Dr. Ana")
        self.assertEqual(result['horarioDeAtendimento'], "14:00 - 16:00")
        self.assertEqual(result['periodo'], "noturno")
        self.assertEqual(result['sala'], "6")
        self.assertEqual(result['predio'], 2)

    # Testes de falha

    # Verificar se um ValueError é lançado quando a sala é vazia
    def test_invalid_sala_empty(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.get_predio("")

    # Verificar se um ValueError é lançado quando a sala contém caracteres não numéricos
    def test_invalid_sala_non_numeric(self):
        ps = ProfessorSchedule(self.valid_data)
        with self.assertRaises(ValueError):
            ps.get_predio("abc")

    # Verificar se um ValueError é lançado quando nome do professor está ausente ou vazio
    def test_missing_nome_do_professor(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    # Verificar se um ValueError é lançado quando horarioDeAtendimento está ausente ou vazio
    def test_missing_horario_de_atendimento(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    # Verificar se um ValueError é lançado quando periodo está ausente ou vazio
    def test_missing_periodo(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    # Verificar se um ValueError é lançado quando sala está ausente ou vazia
    def test_missing_sala(self):
        ps = ProfessorSchedule(self.invalid_data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_sala_with_spaces(self):
        ps = ProfessorSchedule(self.valid_data)
        with self.assertRaises(ValueError):
            ps.get_predio("   ")

    def test_null_values_in_fields(self):
        data = {
            "nomeDoProfessor": None,
            "horarioDeAtendimento": "08:00 - 10:00",
            "periodo": "integral",
            "sala": "4"
        }
        ps = ProfessorSchedule(data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()

    def test_invalid_period_value(self):
        data = self.valid_data.copy()
        data["periodo"] = "manhã"
        ps = ProfessorSchedule(data)
        result = ps.populate_schedule()
        self.assertNotEqual(result['periodo'], "integral")
        self.assertEqual(result['periodo'], "manhã")

    def test_invalid_field_format(self):
        data = self.valid_data.copy()
        data["horarioDeAtendimento"] = "no horário da tarde"
        ps = ProfessorSchedule(data)
        with self.assertRaises(ValueError):
            ps.populate_schedule()


if __name__ == "__main__":
    unittest.main()
