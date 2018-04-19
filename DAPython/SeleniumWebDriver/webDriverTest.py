from time import sleep
from selenium import webdriver
browser = webdriver.Firefox(executable_path="venv/geckodriver")
browser.get("https://www.google.com")

# Shows the current URL in the browser
print("Now visiting: ", browser.current_url)

sleep(2)
# Goes to a new URL in the same browser window
browser.get("https://www.facebook.com")
print("Now visiting: ", browser.current_url)

sleep(1.5)
# Go back to google, and then close the browser
browser.back()
sleep(1)

# Execute JavaScript
browser.execute_script("alert('hello')")
sleep(3)

# Take a screenshot of the current page
browser.save_screenshot("sc1.png")
browser.quit()