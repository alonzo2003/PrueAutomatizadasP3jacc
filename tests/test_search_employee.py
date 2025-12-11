from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_list_page import EmployeeListPage
import time

def test_search_employee(driver):
    login = LoginPage(driver)
   # dashboard = DashboardPage(driver)
   # employees = EmployeeListPage(driver)

    # Login
    login.open()
    login.login("admin", "admin123")

    # Ir a PIM y buscar
   # employees.go_to_pim()
    #employees.search_employee("Juan")  

    #time.sleep(2)

    # Validar resultado
    #result = employees.get_first_result_name()
    #assert "Jese" in result
