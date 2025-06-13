# 필요한 라이브러리 불러오기
import requests                         #  HTTP 요청을 보내기 위한 라이브러리
import xml.etree.ElementTree as ET      #  XML 데이터를 파싱하기 위한 파이썬 표준 모듈
import pandas as pd                     #  표 형태의 데이터를 다루기 위한 라이브러리

# 1. API 요청 URL (base URL + 인증키를 URL에 직접 포함시킨 형태)
url = (
    "https://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api"
    "?serviceKey=C%2BA%2ByB3pObDrsoe1nXCrW8zwq23238NAKZq%2FvT2Om3x7CLdcrNC67VVT4OQZlV7IfH05Ahl%2F7jfuLVNTMyOs6A%3D%3D"
    #  공공데이터 포털에서 발급받은 인증키 (URL 인코딩된 상태)
)

# 2. 추가 파라미터 정의 (URL에 붙이지 않고 별도 params로 전달)
params = {
    "pageNo": "1",                      #  1페이지부터 요청
    "numOfRows": "10",                 #  최대 10건의 데이터만 받아오기
    "std_day": "2021-12-15",           #  기준 날짜 (공공데이터에서 제공되는 예시일 기준)
    "gubun": "서울"                     #  조회할 지역명 (예: 서울, 경기, 부산 등)
}

# 3. 요청 보내기 (GET 방식으로 URL + 파라미터 전달)
res = requests.get(url, params=params)
res.encoding = 'utf-8'                 #응답이 한글 포함이므로 UTF-8로 명시

# 4. XML 응답 문자열을 ElementTree 객체로 파싱
root = ET.fromstring(res.text)         #문자열(XML)을 트리 구조로 변환
items = root.findall('.//item')        #<item> 태그 전부 찾아서 리스트로 반환

# 5. 각 <item> 요소에서 원하는 항목 추출하여 리스트에 저장
data = []                              #데이터를 담을 빈 리스트 생성
for item in items:
    data.append({
        "기준일자": item.findtext("stdDay"),          # 기준 날짜
        "시도명": item.findtext("gubun"),             # 시도명 (예: 서울)
        "확진자수": item.findtext("defCnt"),           # 누적 확진자 수
        "전일대비": item.findtext("incDec"),           # 전날 대비 확진자 증가 수
        "사망자수": item.findtext("deathCnt"),         # 누적 사망자 수
    })

# 6. 리스트를 pandas DataFrame으로 변환하여 보기 좋게 출력
df = pd.DataFrame(data)
print(df)
