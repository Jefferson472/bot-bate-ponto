from datetime import date
from secret_keys import THE_CITY


class DiasUteis():
    def __init__(self):
        self.feriados_nacionais_2022 = [
            date(2022, 1, 1),  # Confraternização
            date(2022, 2, 28),  # Carnaval
            date(2022, 3, 1),  # Carnaval
            date(2022, 3, 2),  # quarta-feira de cinzas
            date(2022, 4, 15),  # Paixão de Cristo
            date(2022, 4, 21),  # Tiradentes
            date(2022, 5, 1),  # Dia do trabalhador
            date(2022, 6, 16),  # Corpus Christi
            date(2022, 9, 7),  # Dia da Independência
            date(2022, 10, 12),  # Nossa Senhora Aparecida
            date(2022, 11, 2),  # Finados
            date(2022, 11, 15),  # Proclamação da República
            date(2022, 12, 25),  # Natal
        ]

        self.feriados_regionais_2022 = THE_CITY

        self.hoje = date.today()

    def verifica_dia_util(self):
        dia_semana = self.hoje.weekday()
        if dia_semana < 5:
            return True
        else:
            return False

    def verifica_feriado(self):
        feriados_2022 = self.feriados_nacionais_2022 + self.feriados_regionais_2022
        if self.hoje in feriados_2022:
            return False
        else:
            return True
