from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:

    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")

    FIRST_NAME_INPUT = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    LAST_NAME_INPUT = (By.NAME, "lastName")

    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    PERSONAL_IMAGE = (By.XPATH, "//img[contains(@class,'employee-image')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def enter_employee_data(self, first, middle, last):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(self.MIDDLE_NAME_INPUT)).send_keys(middle)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT)).send_keys(last)

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def is_employee_created(self):
        # se valida que aparezca la foto default del perfil → señal de que estás en perfil del empleado
        return self.wait.until(EC.visibility_of_element_located(self.PERSONAL_IMAGE))
    

    