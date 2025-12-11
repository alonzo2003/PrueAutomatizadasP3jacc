from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_logout(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    # Login
    login.open()
    login.login("admin", "admin123")

    # Logout
    dashboard.logout()

    time.sleep(2)

    # Verificar que estamos otra vez en la página de login
    assert "login" in driver.current_url.lower()