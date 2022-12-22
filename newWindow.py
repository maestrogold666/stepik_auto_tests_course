from set import *

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# Поиск и открытие новой вкладки
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    print(y)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    #переход на алерт
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
