def flowchart(code):
    import pyautogui
    import pyperclip
    import time
    from selenium import webdriver 
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from pyflowchart import Flowchart

    fc = Flowchart.from_code(code)
    pyperclip.copy(fc.flowchart())
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(executable_path='gui/chrome/chromedriver.exe', options = options)
    driver.maximize_window()
    driver.get("http://flowchart.js.org/")
    try:
        ele = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "strong"))
    )
    except:
        print("Timeout Exception: Page did not load within time.")
    pyautogui.moveTo(504, 637)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl', 'v')
    print("done")