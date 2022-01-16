from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from secret_keys import SECRET_URL, SECRET_CODEMPRESA, SECRET_USER_CODE, SECRET_PASSWORD


def bate_ponto():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(os.environ.get("CHROMEDRIVER_PATH"))
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

    # Login
    driver.implicitly_wait(30)
    driver.get(SECRET_URL)

    print("Carregando a página de login...")
    Cod_Empresa = driver.find_element(By.ID, 'CodEmpresa')
    Cod_Empresa.send_keys(SECRET_CODEMPRESA)
    user = driver.find_element(By.ID, 'requiredusuario')
    user.send_keys(SECRET_USER_CODE)
    password = driver.find_element(By.ID, 'requiredsenha')
    password.send_keys(SECRET_PASSWORD)
    driver.find_element(By.NAME, 'Submit').click()

    # Go to the page
    print('Carregando o menu de informações...')
    driver.find_element(By.ID, 'menu2').click()
    driver.find_element(By.ID, 'menu2_Item2').click()

    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])

    # Click on the button to finish the process
    print("Solicitando a marcação de ponto...")
    driver.find_element(By.ID, 'Button1').click()

    # Switch to the main window and close
    driver.switch_to.window(driver.window_handles[0])
    print('Bateu ponto!')
    driver.close()


if __name__ == "__main__":
    bate_ponto()
