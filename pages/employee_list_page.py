from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeListPage:

    # ----- SELECTORES -----
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")

    EMPLOYEE_NAME_INPUT = (
        By.XPATH,
        "//label[text()='Employee Name']/../following-sibling::div//input"
    )
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    RESULT_NAME = (
        By.XPATH,
        "//div[@role='table']//div[@class='oxd-table-card']//div[3]"
    )

    FIRST_RESULT_ROW = (
        By.XPATH,
        "//div[@role='table']//div[@class='oxd-table-card'][1]"
    )

    # Botón Edit del primer resultado (ícono lápiz)
    FIRST_RESULT_EDIT_BUTTON = (
        By.XPATH,
        "//div[@role='table']//div[@class='oxd-table-card'][1]//button[1]"
    )

    # Botón eliminar (ícono basurero)
    FIRST_RESULT_DELETE_BUTTON = (
        By.XPATH,
        "//div[@role='table']//div[@class='oxd-table-card'][1]//button[2]"
    )

    CONFIRM_DELETE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'oxd-button--label-danger')]"
    )

    NO_RECORDS_LABEL = (By.XPATH, "//span[text()='No Records Found']")

    # ----------------------


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    # ===== NAVEGAR AL MÓDULO =====
    def go_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_MENU)).click()


    # ===== BUSCAR EMPLEADO =====
    def search_employee(self, name):
        name_input = self.wait.until(
            EC.visibility_of_element_located(self.EMPLOYEE_NAME_INPUT)
        )
        name_input.clear()
        name_input.send_keys(name)

        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()


    # ===== LEER RESULTADO =====
    def get_first_result_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.RESULT_NAME)
        ).text


    # ===== ABRIR PERFIL PARA EDITAR =====
    def open_first_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_RESULT_ROW)
        ).click()


    def click_edit(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_RESULT_EDIT_BUTTON)
        ).click()


    # ===== ELIMINAR EMPLEADO =====
    def click_delete_first(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_RESULT_DELETE_BUTTON)
        ).click()


    def confirm_delete(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON)
        ).click()


    def no_records_present(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NO_RECORDS_LABEL)
        )
