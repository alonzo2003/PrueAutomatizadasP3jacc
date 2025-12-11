from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage
import time

def test_delete_employee(driver):
    login = LoginPage(driver)
    login.open()
    login.login("admin", "admin123")

    emp = EmployeeListPage(driver)
   # emp.go_to_pim()

    employee_name = "Juan"  # REEMPLAZA por el que creaste antes

   

    # Eliminar
    emp.click_delete_first()
    emp.confirm_delete()

    time.sleep(2)

 