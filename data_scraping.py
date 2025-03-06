from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


USERNAME = "ramiparveen.m@gmail.com"
PASSWORD = "@rami786"

options = Options()

options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.linkedin.com/login")
time.sleep(3)


username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_button.click()

time.sleep(random.uniform(5, 8)) 


driver.get("https://www.linkedin.com/search/results/content/?keywords=Women%20Indian%20Cricket")
time.sleep(random.uniform(5, 8))


for _ in range(5): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(3, 6))  

posts = driver.find_elements(By.CLASS_NAME, "feed-shared-update-v2")  
scraped_posts = []

for post in posts:
    try:
        content = post.text.strip()
        if content:
            scraped_posts.append({"platform": "LinkedIn", "content": content})
        if len(scraped_posts) >= 15:  
            break
    except:
        pass


print(f"Total Posts Collected: {len(scraped_posts)}\n")
for i, post in enumerate(scraped_posts, 1):
    print(f"{i}. {post['content']}\n")


driver.quit()
