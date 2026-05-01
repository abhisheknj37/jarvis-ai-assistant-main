from os import getcwd

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    selenium_available = True
except ImportError:
    webdriver = None
    By = None
    WebDriverWait = None
    EC = None
    Service = None
    ChromeDriverManager = None
    Options = None
    selenium_available = False
if selenium_available:
    # Setting up Chrome options with specific arguments
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--headless=old")  # Remove this if you want to see the browser UI
    # Manually set the path to the ChromeDriver executable
    chrome_driver_path = f"{getcwd()}\\chromedriver.exe"
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        service = Service(executable_path=chrome_driver_path)
        # Setting up the Chrome driver with the service and options
        driver = webdriver.Chrome(service=service, options=chrome_options)
        website = "https://allorizenproject1.netlify.app/"
        # Opening the website in the Chrome browser
        driver.get(website)
    except Exception as e:
        print(f"Unable to initialize Selenium driver: {e}")
        driver = None
else:
    driver = None
Recog_File = f"{getcwd()}\\input.txt"
def listen():
    if not selenium_available or driver is None:
        print("selenium not installed or driver unavailable; voice listen disabled")
        return
    print("Support in Youtube @NetHyTech")
    try:
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'output')))
            current_text = output_element.text.strip()
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
            if current_text != output_text:
                output_text = current_text
                with open(Recog_File, "w") as file:
                    file.write(output_text.lower())
                    print("User:", output_text)
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()