from pydoc import text

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('Launch the Chrome Browser')
def launchBrowser(context):
     context.driver=webdriver.Chrome(executable_path="C:/Users/boopalan.pilani/Downloads/Drivers/chromedriver_win32/chromedriver.exe")
     context.driver.implicitly_wait(5)

@when('User enters the Orangehrm homepage')
def orangehrmPage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('User enter the username')
def entersUsername(context,username):
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)

@when('User enters the password')
def entersPassword(context,Password):
   context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(Password)


@then('Click on login button')
def loginButton(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

@then('User enters in the orangehrm dashboard page')
def step_impl(context):
    try:
        k=context.driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").text

    except:
        context.driver.close()
        assert False,"Test Failed"

    if  k =="Dashboard":
        context.driver.close()
        assert True,"Test Passed"