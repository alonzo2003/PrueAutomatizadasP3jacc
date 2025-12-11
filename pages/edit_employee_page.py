from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditEmployeePage:

    LAST_NAME_INPUT = (By.ID, "txtNombre")
    GMAIL_INPUT = (By.ID, "txtEmail")
    POLIZA_INPUT = (By.ID, "txtPoliza")
    NUMERO_INPUT = (By.ID, "txtNumero")
    SAVE_BUTTON = (By.XPATH, "/html/body/div/form/div/div[2]/div[5]/input")
  #  PERSONAL_IMAGE = (By.XPATH, "//img[contains(@class,'employee-image')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def change_last_name(self, new_last):
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT)).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(new_last)

    def change_gmail(self, new_gmail):
        self.wait.until(EC.visibility_of_element_located(self.GMAIL_INPUT)).clear()
        self.driver.find_element(*self.GMAIL_INPUT).send_keys(new_gmail)    

    def change_poliza(self, new_poliza):
        self.wait.until(EC.visibility_of_element_located(self.POLIZA_INPUT)).clear()
        self.driver.find_element(*self.POLIZA_INPUT).send_keys(new_poliza)

    def change_numero(self, new_numero):
        self.wait.until(EC.visibility_of_element_located(self.NUMERO_INPUT)).clear()
        self.driver.find_element(*self.NUMERO_INPUT).send_keys(new_numero)

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

