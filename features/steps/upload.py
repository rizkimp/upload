import os
from selenium import webdriver
from behave import *
from locators import *
from selenium.webdriver.common.by import By
from time import sleep

@given(u'in upload page')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.form_page)

@when(u'enter first name and last name')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.NAME,locator.input_first_name).send_keys("rizki")
    sleep(1)
    context.browser.find_element(By.NAME,locator.input_last_name).send_keys("mp")

@when(u'choose gender')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.gender_male).click()

@when(u'years experience')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.experience_three).click()

@when(u'enter date')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.input_date).send_keys("21 April 2021")

@when(u'choose profession')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.input_automation).click()

@when(u'choose automated tools')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.input_selenium).click()

@when(u'select continents')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.XPATH,locator.select_asia).click()

@when(u'select automation command')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.XPATH,locator.select_web_element).click()

@when(u'upload image')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.input_image).send_keys(os.getcwd()+ "/assets/hw.jpg")

@then(u'click button')
def step_impl(context):
    sleep(1)
    context.browser.find_element(By.ID,locator.button).click()
