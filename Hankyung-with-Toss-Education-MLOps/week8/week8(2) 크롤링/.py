from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# chrome driver 설치 코드
def get_chrome_driver():
    # 1. 크롬 옵션 세팅
    chrome_options = webdriver.ChromeOptions()
    # 2. Driver 생성
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver
url = "https://www.youtube.com/watch?v=qC5k6fEXv9M"
driver = get_chrome_driver()
driver.get(url)
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,"#items")
    )
)
driver.execute_script("window.scrollTo(0, 99999)")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,"#contents")
    )
)
driver.execute_script("window.scrollTo(0, 99999)")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,"#content-text")
    )
)
# 대댓글 까지 포함된 count
comment_count = int(driver.find_element(
    By.CSS_SELECTOR,
    "#count > yt-formatted-string > span:nth-child(2)"
).text)
all_comments = {}
current_count = 0
before_count = 0
while True :
    driver.execute_script("window.scrollTo(0, 99999)")
    # 1초 강제로 기다기기
    time.sleep(1)
    # 모든 댓글의 element가 동일한 id(html. #content-text가 동일), 동일한 class를 띄고 있어서 어쩔 수 없이
    #   매번 스크롤 할 때마다 전체를 다 긁어옴.
    comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")
    # 각 댓글 element의 id를 키로 갖는 dictionary를 만들었음
    #  id : 메모리 주소값
    # 없어도 스크롤만 해서 구현은 가능하지 않을까...
    # all_comments = {id(comment) : comment.text for comment in comments}
    # 개수 세주기
    #   크롤링을 한 번 진행 했을 때 이전 개수랑 같으면 반복 중지
    current_count = len(comments)
    if before_count == current_count:
        break
    else:
        before_count = current_count
    print(current_count, before_count, all_comments)
all_comments = [ comment.text for comment in comments ]