from set import *


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), ('$100'))
    )

    button = browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    print(y)
    browser.find_element(By.ID, 'answer').send_keys(y)
    
    
    target = browser.find_element(By.ID, 'solve')
    actions = ActionChains(browser)
    actions.move_to_element(target)
    actions.perform()
    target.click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
