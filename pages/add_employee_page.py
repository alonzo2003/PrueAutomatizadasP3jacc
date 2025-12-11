from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:

    #PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_BUTTON = (By.XPATH, "/html/body/div/a")

    FIRST_NAME_INPUT = (By.ID, "txtNombre")
    MIDDLE_NAME_INPUT = (By.ID, "txtGmail")
    LAST_NAME_INPUT = (By.ID, "txtPoliza")
    NUMERO_CLIENTE = (By.ID, "txtNumero")

    SAVE_BUTTON = (By.XPATH, "/html/body/div/form/div/div[2]/div[5]/input")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def enter_employee_data(self, first, middle, last, numero):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(self.MIDDLE_NAME_INPUT)).send_keys(middle)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT)).send_keys(last)
        self.wait.until(EC.visibility_of_element_located(self.NUMERO_CLIENTE)).send_keys(numero)

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    
    

    