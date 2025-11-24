# PE06 - Classes
# Restaurant 클래스를 정의하고,
# 객체 3개를 생성한 뒤,
# 그 중에서 영업 중인 식당을 추천하는 예제입니다.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, open_status):
        """
        생성자
        restaurant_name: 식당 이름 (문자열)
        cuisine_type: 음식 종류 (문자열)
        open_status: 영업 중 여부 (불리언, True/False)
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_status = open_status

    def describe_restaurant(self):
        """식당의 모든 멤버 변수를 출력하는 메서드"""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Open status: {self.open_status}")

    def is_open(self):
        """영업 여부에 따라 문구를 출력하는 메서드"""
        if self.open_status:
            print("Currently open")
        else:
            print("Currently closed")

    @staticmethod
    def recommend(r1, r2, r3):
        """
        세 개의 Restaurant 객체를 전달받아
        영업 중인 식당 하나를 추천하는 메서드.
        가장 먼저 발견되는 open_status == True 인 식당을 반환.
        모두 닫혀 있으면 None 반환.
        """
        for restaurant in (r1, r2, r3):
            if restaurant.open_status:
                return restaurant
        return None


# 문제에서 예로 준 객체 생성 방식:
restaurant1 = Restaurant("McDonalds", "Burgers", True)
restaurant2 = Restaurant("Subway", "Sandwiches", False)
restaurant3 = Restaurant("Starbucks", "Coffee", True)

# 2) 3개의 객체에 대해 describe_restaurant() 호출
print("=== All restaurants ===")
restaurant1.describe_restaurant()
restaurant1.is_open()
print()

restaurant2.describe_restaurant()
restaurant2.is_open()
print()

restaurant3.describe_restaurant()
restaurant3.is_open()
print()

# 3) recommend 메서드를 사용해 영업 중인 식당 하나 추천
opened = Restaurant.recommend(restaurant1, restaurant2, restaurant3)

print("=== Recommended restaurant ===")
if opened is not None:
    opened.describe_restaurant()
    opened.is_open()
else:
    print("No restaurant is open right now.")
