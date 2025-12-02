from pages.login_page import LoginPage
import time

def test_login_success(driver):
    login = LoginPage(driver)

    login.open()
    login.login("Admin", "admin123")

    # Esperar unos segundos para observar el resultado (no es lo ideal para pruebas reales)
    time.sleep(3)

    assert "dashboard" in driver.current_url.lower()