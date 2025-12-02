from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditEmployeePage:

    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    PERSONAL_IMAGE = (By.XPATH, "//img[contains(@class,'employee-image')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def change_last_name(self, new_last):
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT)).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(new_last)

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def is_saved(self):
        return self.wait.until(EC.visibility_of_element_located(self.PERSONAL_IMAGE))
