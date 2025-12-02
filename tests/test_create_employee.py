from pages.login_page import LoginPage
from pages.add_employee_page import AddEmployeePage
import time

def test_create_employee(driver):

    login = LoginPage(driver)
    add = AddEmployeePage(driver)

    # Login
    login.open()
    login.login("Admin", "admin123")

    # Ir a Add Employee
    add.go_to_add_employee()

    # Datos a crear
    first = "Juan"
    middle = "Francisco"
    last = "Auto"

    add.enter_employee_data(first, middle, last)

    # Guardar
    add.save()

    time.sleep(2)

    # Validar que cargó el perfil del empleado
    assert add.is_employee_created()