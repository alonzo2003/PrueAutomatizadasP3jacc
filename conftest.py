import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# pytest-html extras (para incrustar imágenes en el reporte)
try:
    from pytest_html import extras
except Exception:
    extras = None


@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com/"


@pytest.fixture(scope="function")
def driver(request):
    """Inicializa el WebDriver para cada test y lo cierra al finalizar."""
    options = Options()
    # Quita headless si quieres ver el navegador
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.set_window_size(1280, 800)

    yield drv

    try:
        drv.quit()
    except Exception:
        pass


# ===== Hook: captura pantallas y las integra en pytest-html =====
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Al final de cada test (fase 'call') guarda una captura en reports/screenshots
    y la agrega al reporte HTML (si pytest-html está instalado).
    """
    outcome = yield
    rep = outcome.get_result()

    # Solo al final de la ejecución del test (no setup/teardown)
    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver is None:
            return

        # directorio para screenshots dentro de reports/
        screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # nombre de archivo con timestamp
        timestamp = int(time.time())
        fname = f"{item.name}_{timestamp}.png"
        path = os.path.join(screenshots_dir, fname)

        # intentar guardar screenshot (no debe romper el hook aunque falle)
        try:
            driver.save_screenshot(path)
        except Exception:
            path = None

        # Si pytest-html está disponible, incrustar la imagen en el reporte
        if path and extras is not None:
            # Aseguramos que rep.extra exista
            extra = getattr(rep, "extra", [])
            extra.append(extras.image(path))
            rep.extra = extra