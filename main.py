from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

# Replace meet link..

driver.get("https://meet.google.com/iqicoyczsg")

driver.implicitly_wait(5)

audio_mute_button = driver.find_element_by_xpath("//div[@aria-label='Mute audio']")
audio_mute_button.click()
video_mute_button = driver.find_element_by_xpath("//div[@aria-label='Turn off video']")
video_mute_button.click()

join_button = driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac']")
join_button.click()
