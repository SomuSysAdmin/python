# Wards according to BBMP (Bangalore Municipality)

from selenium import webdriver
b = webdriver.Firefox(executable_path="../venv/geckodriver")
b.get("http://www.vigeyegpms.in/bbmp/?module=public&action=wards")

# Prepare for bullshit - the BBMP site is a goddamn mess. They still use tables to align elements instead of CSS. -_- What is this, 1999?!
loc = [data.text for data in b.find_elements_by_css_selector(".table_middle > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > table:nth-child(2) td:nth-child(2) a")]
b.quit()

for i,l in enumerate(loc):  # Use sorted(loc) for sorted list
    print("{:>3} - {}".format(i+1, l))