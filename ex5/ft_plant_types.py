class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            print(f"Invalid height {height}cm, default value set (25cm).")
            self._height = 25
        else:
            self._height = height
        if age < 0:
            print(f"Invalid age {age} days, default value set (10 days).")
            self._age = 10
        else:
            self._age = age

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"Invalid operation: height {height}cm [REJECTED]")
            print("Security: negative height rejected, no changes made.")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation: age {age} days [REJECTED]")
            print("Security: negative age rejected, no changes made.")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old.")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self._color = color
        self._hasbloom = False

    def bloom(self):
        self.hasbloom = True
        print(f"The {self._name} has bloomed succesfully.")

    def show(self):
        super().show()
        print(f"Color :{self._color}")
        if (self._hasbloom):
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet.")


class Tree(Plant):
    def __init__(
            self, name: str,
            height: float,
            age: int,
            trunk_diameter: int) -> None:
        super().__init__(name=name, height=height, age=age)
        self._trunk_diameter = trunk_diameter
        self._producing_shade = False

    def produce_shade(self):
        self.producing_shade = True
        print(f"The {self._name} is now producing shade of {self._height:.1f}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
            super().show()
            print(f"Trunk diameter: {self._trunk_diameter}cm")

class Vegetable(Plant):
    def __init__(
            self, name: str,
            height: float,
            age: int, 
            harvest_season: str,
            nutritional_value: int):
        super().__init__(name=name, height=height, age=age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Rose = Flower("Rose", 15, 10, "red")
    Rose.show()
    print("[Asking the Rose to bloom]")
    Rose.bloom()
    Rose.show()
    print("\n=== Tree")
    Oak = Tree("Oak", 200, 365, 5)
    Oak.show()
    print("[Asking the tree to produce shade]")
    Oak.produce_shade()
    print("\n=== Vegetable")
    Tomato = Vegetable("Tomato", 5, 10, "April", 0)
    Tomato.show()
    print("[Make the tomato grow and age for 20 days]")
    for i in range(20):
        Tomato.age()
        Tomato.grow()
    Tomato.show()
