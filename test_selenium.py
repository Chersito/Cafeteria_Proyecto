from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "/usr/bin/chromium"  # <- Tu instalación de Chromium
options.add_argument("--headless")             # Opcional: sin interfaz gráfica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inicia el navegador
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:8000/")  # Tu servidor Django local
    time.sleep(2)

    print("✅ Página cargada correctamente")
    print("Título de la página:", driver.title)

except Exception as e:
    print("❌ Error durante la ejecución:", e)

finally:
    driver.quit()
