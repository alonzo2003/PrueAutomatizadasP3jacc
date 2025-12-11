from pages.login_page import LoginPage
from pages.add_employee_page import AddEmployeePage
import time

def test_create_employee(driver):

    login = LoginPage(driver)
    add = AddEmployeePage(driver)

    # Login
    login.open()
    login.login("admin", "admin123")

    # Ir a Add Employee
    add.go_to_add_employee()

    # Datos a crear
    nombre = "Juan Soto"
    gmail = "tureal@gmail.com"
    poliza= "Auto-7531"
    numero = "809-598-6577"


    add.enter_employee_data(nombre, gmail, poliza, numero)

    # Guardar
    add.save()

    time.sleep(2)

    # Validar que cargó el perfil del empleado
   # assert add.is_employee_created()