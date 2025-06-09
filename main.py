import requests
import json

class SHOPIFY:
    def __init__(self, shop_domain="tuneglobal.myshopify.com", access_token="토큰"):
        self.shop_domain = shop_domain
        self.endpoint = f"https://{self.shop_domain}/api/2023-07/graphql.json"
        self.headers = {
            "Content-Type": "application/json",
            "X-Shopify-Storefront-Access-Token": access_token,
            "Accept": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            ),
        }

    def url_setting(self, url_or_handle):
        """
        URL 전체를 넘겨도, handle 값만 넘겨도
        /products/ 뒤의 첫 부분을 handle 로 추출합니다.
        """
        if "products/" in url_or_handle:
            return url_or_handle.split("products/")[-1].split("?")[0].split("/")[0]
        return url_or_handle

    def run(self, product_code):
        handle = self.url_setting(product_code)

        # GraphQL 쿼리: 총재고와 변형별 수량만 요청
        query = """
        query GetInventory($handle: String!) {
          product(handle: $handle) {
            title
            totalInventory
            variants(first: 50) {
              edges {
                node {
                  title
                  quantityAvailable
                }
              }
            }
          }
        }
        """
        payload = {
            "query": query,
            "variables": {"handle": handle}
        }

        resp = requests.post(self.endpoint, headers=self.headers, json=payload)
        resp.raise_for_status()
        data = resp.json().get("data", {}).get("product")
        if not data:
            raise RuntimeError("상품 정보를 불러올 수 없습니다.")

        # 결과 구성
        output = {
            "Name": data["title"],
            "TotalInventory": data["totalInventory"],
            "Url": f"https://{self.shop_domain}/products/{handle}",
            "Stock": {}
        }
        for edge in data["variants"]["edges"]:
            node = edge["node"]
            output["Stock"][node["title"]] = node["quantityAvailable"]

        return output


if __name__ == "__main__":
    url = "상품 URL"
    result = SHOPIFY().run(url)
    print(json.dumps(result, ensure_ascii=False, indent=4))
