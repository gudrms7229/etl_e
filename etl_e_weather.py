import requests
import pandas as pd


# 지역명과 지점 코드 매핑
STATION_CODES = {
    "서울": "108",
    "인천": "112",
    "수원": "119",
    "춘천": "101",
    "강릉": "105",
    "청주": "131",
    "대전": "133",
    "전주": "146",
    "광주": "156",
    "대구": "143",
    "부산": "159",
    "울산": "152",
    "제주": "184"
}

def get_weather_by_date(date_str, stn_ids):
    """
    입력한 날짜(date_str, 'YYYYMMDD')와 지역(stn_ids, 리스트 또는 문자열)에 대해
    평균, 최저, 최고기온을 출력합니다.
    """
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
    params = {
        "serviceKey": "C+A+yB3pObDrsoe1nXCrW8zwq23238NAKZq/vT2Om3x7CLdcrNC67VVT4OQZlV7IfH05Ahl/7jfuLVNTMyOs6A==",
        "dataType": "JSON",
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "startDt": date_str,
        "endDt": date_str,
        "stnIds": ",".join(map(str, stn_ids)) if isinstance(stn_ids, list) else str(stn_ids),
        "numOfRows": "100",
        "pageNo": "1"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json().get("response", {}).get("body", {}).get("items", {}).get("item", [])
        df = pd.DataFrame(items)
        if not df.empty:
            for idx, row in df.iterrows():
                print(f"지역코드 {row.get('stnId')} | 평균기온: {row.get('avgTa')}℃ | 최저기온: {row.get('minTa')}℃ | 최고기온: {row.get('maxTa')}℃")
        else:
            print("해당 날짜에 대한 데이터가 없습니다.")
    else:
        print(f"API 요청 실패: {response.status_code}")

if __name__ == "__main__":
    date_input = input("날짜를 입력하세요 (YYYYMMDD): ")
    stn_input = input("지역명(여러 개는 콤마로 구분, 예: 서울,인천): ")
    stn_ids = [STATION_CODES.get(s.strip()) for s in stn_input.split(",")]
    get_weather_by_date(date_input, stn_ids)