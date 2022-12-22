from set import *
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    # confirm.dismiss (если нужно отменить)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    print(y)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    #переход на алерт
    print(browser.switch_to.alert.text)
finally:
    time.sleep(10)
    browser.quit()
