from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeListPage:

    
    FIRST_RESULT_EDIT_BUTTON = (
        By.XPATH,
        "/html/body/div/table/tbody/tr[1]/td[6]/a[1]"
    )

    # Botón eliminar (ícono basurero)
    FIRST_RESULT_DELETE_BUTTON = (
        By.XPATH,
        "/html/body/div/table/tbody/tr[1]/td[6]/a[2]"
    )

    CONFIRM_DELETE_BUTTON = (
        By.XPATH,
        "/html/body/div/table/tbody/tr[1]/td[6]/a[2]"
    )

   # NO_RECORDS_LABEL = (By.XPATH, "//span[text()='No Records Found']")

    # ----------------------


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


   

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


 