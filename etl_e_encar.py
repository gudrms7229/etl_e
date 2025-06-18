from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 크롬 드라이버 경로 설정
service = Service('c:/Users/yoo02/Desktop/python/etl_project/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 명시적 대기 설정
wait = WebDriverWait(driver, 10)

try:
    # 1. 엔카 메인 페이지 열기
    driver.get("https://www.encar.com/")
    driver.maximize_window()
    time.sleep(2)

    # 2. 제조사 드롭다운 열기
    maker_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='제조사']]")))
    maker_button.click()
    time.sleep(1)

    # 3. 제조사 리스트에서 "현대" 클릭
    hyundai = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='현대']")))
    hyundai.click()
    time.sleep(2)



    # 6. 검색 버튼 클릭
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='검색']]")))
    search_btn.click()
    time.sleep(3)

    # 7. 검색 결과 크롤링
    cars = driver.find_elements(By.CSS_SELECTOR, "table.car_list > tbody > tr")
    print(f"🚨 수집된 차량 수: {len(cars)}대")  

    for car in cars:
        try:
            title = car.find_element(By.CLASS_NAME, "inf").text
            price = car.find_element(By.CLASS_NAME, "prc_hs").text
            print(f"🚗 {title} | 💰 {price} ")
        except:
            continue

except Exception as e:
    print("에러 발생:", e)

finally:
    input("엔터 브라우저 닫기.")
    driver.quit()
