from selenium import webdriver

admin_email = 'admin@admin.com'
admin_pw = '6yEJedUJsxsQY2s'

driver = webdriver.Firefox()
driver.get("http://www.wsb.com/Assignment2/case20/login.php")

login_email = driver.find_element_by_name('email')
login_password = driver.find_element_by_id('password')

login_email.send_keys(admin_email)
login_password.send_keys(admin_pw)

login_attempt = driver.find_element_by_xpath("//*[@type='button']")
login_attempt.click()
