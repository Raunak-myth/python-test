from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import argparse
import csv 

parser = argparse.ArgumentParser(description='Username passed as a arguement')
parser.add_argument("--username",required=True, help="Username of whoes repo you want")
args = parser.parse_args()

driver = webdriver.Firefox()
url = "https://github.com/"+ args.username + "?tab=repositories"
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-repositories-list")))
    repo_nm_list = driver.find_elements(By.XPATH, "//div[@id='user-repositories-list']/ul/li/div[1]/div/h3/a")
    repo_discp_list = driver.find_elements(By.XPATH, "//div[@id='user-repositories-list']/ul/li/div[1]/div/p")
    repo_lang_list = driver.find_elements(By.XPATH, "//div[@id='user-repositories-list']/ul/li/div[1]/div/span[1]/span[2]")
    fileName = args.username + ".csv"
    fields = ["Repo Name","Repo Link","Repo Description","Repo Language"]

    with open(fileName, 'w', newline="") as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields)
        for i in range(len(repo_nm_list)):
            if not repo_discp_list: #incase there is no description
                csvwriter.writerow([repo_nm_list[i].get_attribute("innerHTML").strip(),repo_nm_list[i].get_attribute("href"),"",repo_lang_list[i].get_attribute("innerHTML")])
            else:
                csvwriter.writerow([repo_nm_list[i].get_attribute("innerHTML").strip(),repo_nm_list[i].get_attribute("href"),repo_discp_list[i].get_attribute("innerHTML").strip(),repo_lang_list[i].get_attribute("innerHTML")])

    driver.close()
except:
    driver.close()
    print("Something Went Wrong, Please check your entered username")




