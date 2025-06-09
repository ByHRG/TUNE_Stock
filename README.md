## TUNE 재고 조회

Shopify Storefront GraphQL API를 사용하여 특정 상품의 전체 재고(`totalInventory`)와 변형별 재고(`quantityAvailable`)를 간편하게 조회

---

### 📦 주요 기능

* 상품 URL 또는 handle 문자열만으로 조회 가능
* 전체 재고 수량(`TotalInventory`) 출력
* 변형(Variant)별 재고 수량 출력
* JSON 형태로 깔끔한 결과 반환

---

### 🔧 설치

1. Python 3.7 이상 설치
2. `httpx` 패키지 설치

   ```bash
   pip install httpx
   ```

---

### 📝 출력 예시

```json
{
    "Name": "AIR JORDAN 4 RETRO",
    "TotalInventory": 24,
    "Url": "https://tuneglobal.myshopify.com/products/air-jordan-4-retro-nk254xsesn56",
    "Stock": {
        "FV5029-100 / 250": 0,
        "FV5029-100 / 255": 0,
        "FV5029-100 / 260": 0,
        "FV5029-100 / 265": 0,
        "FV5029-100 / 270": 5,
        "FV5029-100 / 275": 9,
        "FV5029-100 / 280": 10,
        "FV5029-100 / 285": 0,
        "FV5029-100 / 290": 0,
        "FV5029-100 / 300": 0
    }
}
```


---

### 🔐 토큰 발급

1. Shopify 관리자(Admin)에서 **스토어프론트 API 액세스 토큰** 생성
2. `X-Shopify-Storefront-Access-Token`에 복사한 토큰 값 입력
