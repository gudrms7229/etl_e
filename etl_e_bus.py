import requests

# ▶️ 사용자 입력 부분
service_key = "C+A+yB3pObDrsoe1nXCrW8zwq23238NAKZq/vT2Om3x7CLdcrNC67VVT4OQZlV7IfH05Ahl/7jfuLVNTMyOs6A=="
bus_route_id = "100100118"

# ▶️ API 호출
url = "http://ws.bus.go.kr/api/rest/buspos/getBusPosByRoute"
params = {
    "serviceKey": service_key,
    "busRouteId": bus_route_id
}

# ▶️ 요청 및 원문 출력
response = requests.get(url, params=params)
print(response.text)  # ← 바로 XML 원문 출력
