from selenium import webdriver
from time import sleep

b = webdriver.Firefox(executable_path="../venv/geckodriver")

url = "https://www.nobroker.in/property/rent/bangalore/JP%20Nagar/?nbPlace=ChIJK6dJcw0VrjsRRj3d4aE-0PM&&lat_lng=12.910491,77.5857168&sharedAccomodation=0&type=BHK1&orderBy=nbRank,desc&radius=2&propertyType=rent"
b.get(url)

resCount = int(b.find_element_by_css_selector("#resultsCount").text)

# Handling Infinite Scroll
while True:     # Emulating a do-while loop
    listingsContainer = b.find_elements_by_css_selector("a.card-link-detail")
    loadedElements = len(listingsContainer)
    if not loadedElements < resCount:
        break
    else:
        print(loadedElements, "/", resCount, "elements in the list; Scrolling...")
        b.execute_script('window.scroll(0, document.body.scrollHeight);')
        sleep(1)

basicStatsCon = [str(data.text).replace(" sqft","") for data in b.find_elements_by_css_selector("div.overview.open_detail_page div h3")][:(resCount*3)]
siteID = [data.get_attribute("data-id") for data in b.find_elements_by_css_selector("div.overview.open_detail_page")]

listings = []
listLinks = []
area=[]
dep=[]
rent=[]
priceSqftRatio=[]

for each_link in listingsContainer:
    listLinks.append(each_link.get_attribute("href"))
    listings.append(each_link.find_element_by_css_selector("h2").text)

rng = (len(basicStatsCon))
i=0
while i+2<rng:
    try:
        v1 = int(basicStatsCon[i].replace(",", ""))
        v2 = float(basicStatsCon[i+1].replace(",", ""))
        v3 = float(basicStatsCon[i+2].replace(",", ""))
    except ValueError:
        print("Skipping invalid data {:>3}/{:>3} : (".format((i//3 + 1), rng//3), basicStatsCon[i], ", ", basicStatsCon[i + 1], ", ", basicStatsCon[i + 2], ") ", sep="")
        basicStatsCon.pop(i + 2)
        basicStatsCon.pop(i + 1)
        basicStatsCon.pop(i)  # Written in reverse to avoid problems with shifting index!
        resCount -= 1
        rng = (len(basicStatsCon))
        print("Max Idx: ", rng)
        continue
    except IndexError:
        print("MaxIdx:", rng-1, "Attempted Idx:", i)
        print(basicStatsCon)
        exit(2)
    i += 3

    print("Inserting set {:>3}/{:>3} : (".format((i//3 +1), rng//3), v1, ", ", v2, ", ", v3, ") [{},{},{}]".format(i,i+1,i+2), sep="")
    area.append(v1)
    dep.append(v2)
    rent.append(v3)
    priceSqftRatio.append(v3/v1)

for i in range(resCount):
    if i>resCount or i>=len(listings):
        break

    print("%3d" % (i+1), "-", listings[i], "; Rent/Area Ratio:", priceSqftRatio[i], "; Area:", area[i], "; Deposit:", dep[i], "; Rent:", rent[i], "; Link -", listLinks[i], "; ID:", siteID[i])

#b.quit()
