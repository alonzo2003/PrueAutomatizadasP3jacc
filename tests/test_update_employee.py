from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage
from pages.edit_employee_page import EditEmployeePage
import time

def test_update_employee(driver):
    login = LoginPage(driver)
    login.open()
    login.login("admin", "admin123")

    emp_list = EmployeeListPage(driver)
    #emp_list.go_to_pim()
    #emp_list.search_employee("Juan")  # asumir que existe
    #emp_list.open_first_employee()
    emp_list.click_edit()

    edit = EditEmployeePage(driver)
    new_last = "Elian Herrera"
    new_gmail = "Elian@gmail.com"
    new_poliza = "Casa-8520"
    new_numero = "809-123-4567"


    edit.change_last_name(new_last)
    edit.change_gmail(new_gmail)
    edit.change_poliza(new_poliza)
    edit.change_numero(new_numero)
    edit.save()

    time.sleep(2)

    # Verificar que se guardó (puede ser reabrir lista y buscar de nuevo)
    #emp_list.search_employee("Juan")
    #emp_list.open_first_employee()
    # validar que apellido cambió
    #assert new_last in driver.page_source
