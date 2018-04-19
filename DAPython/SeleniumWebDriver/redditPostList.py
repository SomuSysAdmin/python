from selenium import webdriver
b = webdriver.Firefox(executable_path="venv/geckodriver")
b.get("https://reddit.com")
i = pg = 1
while pg <= 4 :
    titles = b.find_elements_by_css_selector("a.title.may-blank")
    for i, post_title in enumerate(titles, i):
        print(i, "-", post_title.text)
    nxtBtn = b.find_element_by_css_selector(".next-button a")
    nxtBtn.click()
    pg += 1
b.quit()