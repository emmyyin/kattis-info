from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

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

score = ""
ranking = ""

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

driver.find_element_by_xpath('//*[@id="wrapper"]/header/div/div/div[2]/nav/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/section/div[2]/div[2]/div/form[4]/button').click()

# Login to Kattis through Google
driver.find_element_by_id("identifierId").send_keys(input("Enter your google email or phone number:\n"))
driver.find_element_by_id("identifierNext").click()
time.sleep(2)
driver.find_element_by_name("password").send_keys(input("Enter your google password:\n"))
driver.find_element_by_id("passwordNext").click()
time.sleep(2)

score = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[1]/section/div/div/div[2]/div/table/tbody/tr[2]/td[2]').text
ranking = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[1]/section/div/div/div[2]/div/table/tbody/tr[2]/td[1]').text

print("Score:", score, ", Ranking:", ranking)

driver.quit()
