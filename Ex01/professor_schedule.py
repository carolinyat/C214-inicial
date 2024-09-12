# professor_schedule.py
from validate import validate_horario

class ProfessorSchedule:
    def __init__(self, json_data):
        self.data = json_data

    def get_predio(self, sala):
        if not sala or not sala.isdigit():
            raise ValueError("A sala deve ser um número válido.")
        sala_num = int(sala)
        if 1 <= sala_num <= 5:
            return 1
        elif 6 <= sala_num <= 10:
            return 2
        else:
            return (sala_num - 1) // 5 + 1

    def populate_schedule(self):
        required_fields = ["nomeDoProfessor", "horarioDeAtendimento", "periodo", "sala"]
        for field in required_fields:
            if not self.data.get(field):
                raise ValueError(f"O campo {field} está faltando ou vazio.")

        # Valida o formato do horário de atendimento usando a função importada
        validate_horario(self.data["horarioDeAtendimento"])

        professor_info = {
            "nomeDoProfessor": self.data["nomeDoProfessor"],
            "horarioDeAtendimento": self.data["horarioDeAtendimento"],
            "periodo": self.data["periodo"],
            "sala": self.data["sala"],
            "predio": self.get_predio(self.data["sala"]),
        }
        return professor_info