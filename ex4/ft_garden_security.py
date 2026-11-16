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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print(f"Plant created: {rose.get_name()}")

    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-5)
    rose.set_age(-3)

    print()
    print(f"Current plant: {rose.get_name()} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")

    print()
    bad = Plant("Cactus", -10, -2)
    print(f"Current plant: {bad.get_name()} "
          f"({bad.get_height()}cm, {bad.get_age()} days)")
