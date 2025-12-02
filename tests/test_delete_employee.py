from pages.login_page import LoginPage
from pages.employee_list_page import EmployeeListPage
import time

def test_delete_employee(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")

    emp = EmployeeListPage(driver)
    emp.go_to_pim()

    employee_name = "Juan Automation"  # REEMPLAZA por el que creaste antes

    # Buscar el empleado
    emp.search_employee(employee_name)
    time.sleep(1)

    # Eliminar
    emp.click_delete_first()
    emp.confirm_delete()

    time.sleep(2)

    # Buscar nuevamente para verificar que ya no existe
    emp.search_employee(employee_name)

    assert emp.no_records_present()  # debe aparecer “No Records Found”