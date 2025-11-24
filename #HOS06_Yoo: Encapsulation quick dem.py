# CS11A - HOS06: Encapsulation quick demo
# goal: keep the price controlled; change it through a method (not by poking the attribute)

class Computer:
    def __init__(self, max_price: float):
        # name-mangled on purpose; prevents easy outside access
        self.__maxprice = float(max_price)

    def sell(self) -> str:
        return f"Selling price: ${self.__maxprice:,.2f}"

    def set_max_price(self, price: float) -> None:
        price = float(price)
        if price <= 0:
            raise ValueError("price must be greater than 0")
        self.__maxprice = price


if __name__ == "__main__":
    c = Computer(1500)
    print("Before:", c.sell())

    # direct change like c.__maxprice = 500 won't actually touch the hidden value
    # the right way:
    c.set_max_price(1299.99)
    print("After:", c.sell())
