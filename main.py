from dates import DiasUteis
from selenium_bot import bate_ponto
from api_mail import send_email
from datetime import datetime


du = DiasUteis()
if du.verifica_dia_util():
    if du.verifica_feriado():
        try:
            bate_ponto()
            send_email(
                content="Bateu ponto! - " +
                datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        except:
            print("Erro ao bater ponto!")
            send_email(
                content="Erro ao marcar ponto! - " +
                datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    else:
        print('Feriado')
else:
    print('Fim de semana')
