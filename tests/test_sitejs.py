from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_webpage_is_up(client):
    res = client.get('/')
    assert res.status_code == 200

def test_text_display(app, client):
    #Click the button and get the resulting text
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    driver.execute_script("return document.getElementsByTagName('input')[0].click()")
    returned_text = driver.execute_script("return document.body.innerText")

    expected_text = "Lorem ipsum dolor sit amet."
    assert expected_text == returned_text