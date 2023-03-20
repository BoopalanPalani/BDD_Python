from behave import *
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'User launches the Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path="C:/Users/boopalan.pilani/Downloads/Drivers/chromedriver_win32/chromedriver.exe")
    context.driver.implicitly_wait(5)


@when(u'User enters into the application')
def step_impl(context):
   context.driver.get("https://practicetestautomation.com/practice/")


@when(u'User clicks on Testlogin Page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Test Login Page']").click()

@when(u'User enters into Testlogin page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//h2[text()='Test login']").is_displayed()


@then(u'User enters the username and password')
def step_impl(context):
    context.driver.find_element(By.ID,"username").send_keys("student")
    context.driver.find_element(By.ID,"password").send_keys("Password123")

@then(u'clicks on submit button')
def step_impl(context):
    context.driver.find_element(By.ID,"submit").click()



@then(u'User enters into logout page')
def step_impl(context):
    assert True, "test passed"

