import getpass
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "https://open.kattis.com"

# To be used if the other login alternatives were to be implemented
login_forms = {
    0: "Azure",
    1: "Facebook",
    2: "Github",
    3: "Google",
    4: "LinkedIn",
    5: "email"
}
# loginform = login_forms[int(input("Choose login form: \n 0: Azure \n 1: Facebook \n 2: Github \n 3: Google \n 4: LinkedIn \n 5: email \n"))]

username = input("Enter your google email or phone number:\n")
password = getpass.getpass(prompt="Enter your google password:\n")
score = ""
ranking = ""
solved = {}

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_xpath('//*[@id="wrapper"]/header/div/div/div[2]/nav/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/section/div[2]/div[2]/div/form[4]/button').click()

# Login to Kattis through Google
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element_by_id("passwordNext").click()
time.sleep(1)

score = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[1]/section/div/div/div[2]/div/table/tbody/tr[2]/td[2]').text
ranking = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[1]/section/div/div/div[2]/div/table/tbody/tr[2]/td[1]').text

print("Score:", score, ", Ranking:", ranking)

driver.get(url + "/problems?show_solved=on&show_tried=off&show_untried=off")
time.sleep(1)
solved = driver.find_elements_by_class_name('name_column')

for problem in solved:
    # TODO: Get problem names and URLs
    print("found")


driver.quit()
