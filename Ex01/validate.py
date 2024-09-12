import re


def validate_horario(horario):
    # Expressão regular para validar formato "HH:MM - HH:MM"
    pattern = r'^\d{2}:\d{2} - \d{2}:\d{2}$'
    if not re.match(pattern, horario):
        raise ValueError("O formato do horário de atendimento é inválido.")
