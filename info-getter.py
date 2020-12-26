import getpass
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_credentials():
    username = input("Enter your google email or phone number:\n")
    password = getpass.getpass(prompt="Enter your google password:\n")
    return username, password

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
username, password = get_credentials()
score = ""
ranking = ""
solved = {}

driver = webdriver.Chrome()

driver.get(url + "/login")
driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/section/div[2]/div[2]/div/form[4]/button').click()

# Login to Kattis through Google
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

trying = True
while trying:
    try:
        #Wait up to 5s until page loaded
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
        element.send_keys(password)
        driver.find_element_by_id('passwordNext').click()
    except TimeoutException:
        print("Something went wrong")
        driver.quit()
        break

    try:
        #Wait up to 10s until page loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//ul[@class="profile-header-list"]'))
        )
        score = driver.find_element_by_xpath('//ul[@class="profile-header-list"]/li[1]').text
        ranking = driver.find_element_by_xpath('//ul[@class="profile-header-list"]/li[2]').text
        print(score, ranking)
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        break


    driver.get(url + "/problems?show_solved=on&show_tried=off&show_untried=off")

    try:
        #Wait up to 5s until page loaded
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'problem_list_wrapper'))
        )
        solved_problems = driver.find_elements_by_class_name('name_column')
        print("Solved:")
        for problem in solved_problems:
            # TODO: Get problem names and URLs
            name = problem.find_element_by_xpath('.//a').text
            if name != "SOLVED":
                link = problem.find_element_by_xpath('.//a').get_attribute('href')
                solved.update({name:link})
                print(name, link)

    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        break


    driver.quit()
    trying = False
