import requests

# 1. API 기본 URL
url = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

# 2. 요청 파라미터 (디코딩된 인증키 사용)
params = {
    "serviceKey": "C+A+yB3pObDrsoe1nXCrW8zwq23238NAKZq/vT2Om3x7CLdcrNC67VVT4OQZlV7IfH05Ahl/7jfuLVNTMyOs6A==",
    "returnType": "json",     # JSON으로 응답
    "numOfRows": "10",        # 10개만 받아오기
    "pageNo": "1",            # 1페이지
    "sidoName": "서울",        # 서울 지역 데이터
    "ver": "1.0"              # API 버전
}

# 3. 요청 보내기
response = requests.get(url, params=params)

# 4. 응답 결과 확인
if response.status_code == 200:
    data = response.json()
    print("✅ 요청 성공. 데이터 미리보기:\n")
    for item in data['response']['body']['items']:
        print(item)
else:
    print("❌ 요청 실패. 상태 코드:", response.status_code)
