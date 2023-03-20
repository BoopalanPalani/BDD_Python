import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given(u': Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path="C:/Users/boopalan.pilani/Downloads/Drivers/chromedriver_win32/chromedriver.exe")


@when(u': open orangehrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u': verify the logo present on the homepage')
def step_impl(context):
    #context.driver.find_element_by_xpath("//img[@alt='company-branding']").is_displayed()
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()


@then(u': Close the Browser')
def step_impl(context):
    context.driver.close()
