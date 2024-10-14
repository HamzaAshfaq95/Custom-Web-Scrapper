# Using Selenium for Web Scrapping
from selenium import webdriver
# From selenium importing By function to use in find_element function
from selenium.webdriver.common.by import By
# From selenium importing Keys function to use in send_keys function
from selenium.webdriver.common.keys import Keys
# Importing pandas to create csv file
import pandas as pd
# Import time to sleep for 5 seconds
import time
# Creating chrome options to keep it open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Creating a driver for chrome
driver = webdriver.Chrome(options=chrome_options)
# Opening a URL
driver.get("https://www.daraz.pk/#?")
# Sleeping the program for 5 seconds
time.sleep(5)
# Find element (search bar) by Name "q"
search_bar = driver.find_element(By.NAME, value="q")
# Writing search keyword in search bar and hitting enter
search_bar.send_keys("Laptop Table", Keys.ENTER)
# Creating a list
data = []
# Sleeping the program for 5 seconds
time.sleep(5)
# Starting a for loop in range 1 to 11 will return 10 values
for i in range(1, 11):
# Using try keyword to check if code works
    try:
# Find element (Name and Price of Product) by XPATH
        search_values = driver.find_element(By.XPATH, value=f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[2]/a')
        price = driver.find_element(By.XPATH, value=f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[3]/span')
# Appending data in list in the form of dictionary having key and value
        data.append({
            "name": search_values.text,
            "price": price.text
        })
# Using except keyword raising exception if occur as e
    except Exception as e:
        print(f"An error occurred: {e}")
# Convrting the list into dataframe
df = pd.DataFrame(data)
# Converting the dataframe to csv
df.to_csv("data.csv", index=False)
# Quiting the driver after code executed
driver.quit()