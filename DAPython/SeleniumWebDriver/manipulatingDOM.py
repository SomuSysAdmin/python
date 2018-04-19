from selenium import webdriver
browser = webdriver.Firefox(executable_path="venv/geckodriver")
browser.get("https://www.google.com")
searchBar = browser.find_element_by_css_selector("#lst-ib")  # The search bar has the id: #lst-ib
searchBar.send_keys("Selenium WebDriver")
okButton = browser.find_element_by_name("btnK") # Google button has the name btnK
okButton.click()
# Obtaining the NEW search bar on the results page
searchBar = browser.find_element_by_css_selector("#lst-ib")
searchBar.clear()
searchBar.send_keys("Next query!")
okButton = browser.find_element_by_css_selector("#mKlEF")  # The search button has the id: #mKlEF
okButton.click()