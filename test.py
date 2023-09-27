#-*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from openpyxl import Workbook,load_workbook
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.

chrome_options = webdriver.ChromeOptions()
# user_data = r"C:\Users\com\AppData\Local\Google\Chrome\User Data"
# chrome_options.add_argument(f"user-data-dir={user_data}")

# chrome_options.add_experimental_option("detach", True)  # 화면이 꺼지지 않고 유지

# chrome_options.add_argument("--start-maximized")  # 최대 크기로 시작

# chrome_options.add_argument('--headless')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windo9ws NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service("C:\\Users\com\\everytime-timetable-crawling\\chromedriver.exe")




driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get('https://everytime.kr/login')
# # 암묵적으로 웹 자원 로드를 위해 5초까지 기다려 준다.
# driver.implicitly_wait(5)

# id = 'tlarlguswh'
# pasword = "shim315709!"
# # 아이디/비밀번호를 입력해준다.
# driver.execute_script("document.getElementsByName('userid')[0].value=\'" + id + "\'")
# driver.execute_script("document.getElementsByName('password')[0].value=\'" + pasword + "\'")
# # driver.find_element(By.NAME, 'userid').send_keys('tlarlguswh')
# # driver.find_element(By.NAME, 'password').send_keys('shim315709!')

# # # 로그인 버튼을 눌러주자.
# # driver.find_element(By.XPATH, '//*[@id="container"]/form/p[3]/input').click()
 
driver.get('https://everytime.kr/timetable')

# # 클래스가 "cols"인 모든 요소 가져오기
# cols_elements = driver.find_elements(By.CSS_SELECTOR, '.cols')

# # 각 "cols" 클래스를 가진 요소에서 데이터 추출
# for cols_element in cols_elements:
#     # "subject color" 클래스 이름이 있는 모든 하위 요소 찾기
#     subject_col_elements = cols_element.find_elements(By.CSS_SELECTOR, '[class*="subject color"]')
    
#     # 각 "subject color" 클래스를 가진 하위 요소에서 데이터 추출
#     for subject_col_element in subject_col_elements:
#         # "h3" 요소에서 과목명 추출
#         subject_name = subject_col_element.find_element(By.CSS_SELECTOR, 'h3').text
        
#         # "em" 요소에서 교수명 추출
#         professor_name = subject_col_element.find_element(By.CSS_SELECTOR, 'em').text
        
#         # "span" 요소에서 코드 추출
#         course_code = subject_col_element.find_element(By.CSS_SELECTOR, 'span').text
        
#         # 추출한 데이터 출력 또는 다른 용도로 사용
#         print(f"과목명: {subject_name}")
#         print(f"교수명: {professor_name}")
#         print(f"과목 코드: {course_code}")

sleep(0.1)
# td 요소를 모두 가져오기
td_elements = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr/td[1]')
print("---------월요일----------")
# td 요소를 순회하면서 작업 수행
for td in td_elements:
    # 원하는 작업을 수행
    subject_col_elements = td.find_elements(By.CSS_SELECTOR, '[class*="subject color"]')

    for subject_col_element in subject_col_elements:
        # "h3" 요소에서 과목명 추출
        subject_name = subject_col_element.find_element(By.CSS_SELECTOR, 'h3').text
        # "em" 요소에서 교수명 추출
        professor_name = subject_col_element.find_element(By.CSS_SELECTOR, 'em').text
        # "span" 요소에서 코드 추출
        course_code = subject_col_element.find_element(By.CSS_SELECTOR, 'span').text

        print(f"과목명: {subject_name}")
        print(f"교수명: {professor_name}")
        print(f"과목 코드: {course_code}")

sleep(0.1)
td_elements = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr/td[2]')
print("---------화요일----------")
# td 요소를 순회하면서 작업 수행
for td in td_elements:
    # 원하는 작업을 수행
    subject_col_elements = td.find_elements(By.CSS_SELECTOR, '[class*="subject color"]')

    for subject_col_element in subject_col_elements:
        # "h3" 요소에서 과목명 추출
        subject_name = subject_col_element.find_element(By.CSS_SELECTOR, 'h3').text
        # "em" 요소에서 교수명 추출
        professor_name = subject_col_element.find_element(By.CSS_SELECTOR, 'em').text
        # "span" 요소에서 코드 추출
        course_code = subject_col_element.find_element(By.CSS_SELECTOR, 'span').text

        print(f"과목명: {subject_name}")
        print(f"교수명: {professor_name}")
        print(f"과목 코드: {course_code}")

sleep(0.1)
td_elements = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr/td[3]')
print("---------수요일----------")
# td 요소를 순회하면서 작업 수행
for td in td_elements:
    # 원하는 작업을 수행
    subject_col_elements = td.find_elements(By.CSS_SELECTOR, '[class*="subject color"]')

    for subject_col_element in subject_col_elements:
        # "h3" 요소에서 과목명 추출
        subject_name = subject_col_element.find_element(By.CSS_SELECTOR, 'h3').text
        # "em" 요소에서 교수명 추출
        professor_name = subject_col_element.find_element(By.CSS_SELECTOR, 'em').text
        # "span" 요소에서 코드 추출
        course_code = subject_col_element.find_element(By.CSS_SELECTOR, 'span').text

        print(f"과목명: {subject_name}")
        print(f"교수명: {professor_name}")
        print(f"과목 코드: {course_code}")


sleep(0.1)
td_elements = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr/td[4]')
print("---------목요일----------")
# td 요소를 순회하면서 작업 수행
for td in td_elements:
    # 원하는 작업을 수행
    subject_col_elements = td.find_elements(By.CSS_SELECTOR, '[class*="subject color"]')

    for subject_col_element in subject_col_elements:
        # "h3" 요소에서 과목명 추출
        subject_name = subject_col_element.find_element(By.CSS_SELECTOR, 'h3').text
        # "em" 요소에서 교수명 추출
        professor_name = subject_col_element.find_element(By.CSS_SELECTOR, 'em').text
        # "span" 요소에서 코드 추출
        course_code = subject_col_element.find_element(By.CSS_SELECTOR, 'span').text

        print(f"과목명: {subject_name}")
        print(f"교수명: {professor_name}")
        print(f"과목 코드: {course_code}")


sleep(0.1)
td_elements = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr/td[5]')
print("---------금요일----------")
# td 요소를 순회하면서 작업 수행
for td in td_elements:
    # 원하는 작업을 수행
    subject_col_elements = td.find_elements(By.CSS_SELECTOR, '[class*="subject color"]')

    for subject_col_element in subject_col_elements:
        # "h3" 요소에서 과목명 추출
        subject_name = subject_col_element.find_element(By.CSS_SELECTOR, 'h3').text
        # "em" 요소에서 교수명 추출
        professor_name = subject_col_element.find_element(By.CSS_SELECTOR, 'em').text
        # "span" 요소에서 코드 추출
        course_code = subject_col_element.find_element(By.CSS_SELECTOR, 'span').text

        print(f"과목명: {subject_name}")
        print(f"교수명: {professor_name}")
        print(f"과목 코드: {course_code}")
