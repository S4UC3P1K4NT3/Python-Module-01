class Plant:
    class Stats:
        def __init__(self):
            self._growcount = 0
            self._showcount = 0
            self._agecount = 0

        def addgrow(self) -> None:
            self._growcount += 1

        def addage(self) -> None:
            self._agecount += 1

        def addshow(self) -> None:
            self._showcount += 1

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._stats = self.Stats()
        if height < 0:
            print(f"Invalid height {height}cm, default value set (25cm).")
            self._height = 25.0
        else:
            self._height = height
        if age < 0:
            print(f"Invalid age {age} days, default value set (10 days).")
            self._age = 10.0
        else:
            self._age = age

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0, 0)

    @staticmethod
    def olderthanyear(days: int) -> bool:
        return days > 364

    def grow(self) -> None:
        self._height += 8.0
        self._stats.addgrow()

    def age(self) -> None:
        self._age += 1
        self._stats.addage()

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

    def get_age(self) -> int | float:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old.")
        self._stats.addshow()

    def getstats(self) -> str:
        return (f"Stats: {self._stats._growcount} grow, "
                f"{self._stats._agecount} age, "
                f"{self._stats._showcount} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self._color = color
        self._hasbloom = False

    def bloom(self):
        self._hasbloom = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if (self._hasbloom):
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet.")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shadecount = 0

        def addshade(self) -> None:
            self._shadecount += 1

        def getstatsshade(self) -> int:
            return self._shadecount

    def __init__(
            self, name: str,
            height: float,
            age: int,
            trunk_diameter: int) -> None:
        super().__init__(name=name, height=height, age=age)
        self._trunk_diameter = trunk_diameter
        self._producing_shade = False

    def produce_shade(self):
        self._producing_shade = True
        print(
            f"The {self._name} is now producing shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def getstats(self):
        return super().getstats() + f"\n{self._stats._shadecount} shade"


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


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 color: str,
                 seeds: int
                 ) -> None:
        super().__init__(name=name, height=height, age=age, color=color)
        self._seeds = 0
        self._seedstoadd = seeds

    def addseeds(self):
        self._seeds = self._seedstoadd

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self):
        super().bloom()
        self.addseeds()


def showstats(plant: Plant):
    print(f"{plant.getstats()}")


if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    print(f"is Is 30 days more than a year? -> {Plant.olderthanyear(30)}")
    print(f"is Is 400 days more than a year? -> {Plant.olderthanyear(400)}")
    print("\n=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red")
    Rose.show()
    print("[statistics for Rose]")
    showstats(Rose)
    print("[asking the Rose to grow and Bloom]")
    Rose.grow()
    Rose.bloom()
    Rose.show()
    print("[statistics for Rose]")
    showstats(Rose)
    print("\n=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5)
    print("[statistics for Oak]")
    showstats(Oak)
    print("[asking the Oak to produche shade]")
    Oak.produce_shade()
    print("[statistics for Oak]")
    showstats(Oak)
    print("\n=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "Yellow", 42)
    Sunflower.show()
    print("[make sunflower age, grow and bloom]")
    Sunflower.age()
    Sunflower.grow()
    Sunflower.bloom()
    Sunflower.show()
    print("[statistics for Sunflower]")
    showstats(Sunflower)
    print("\n=== Anonymous")
    Unknown = Plant.create_anonymous()
    Unknown.show()
    print("[statistics for Unknown plant]")
    showstats(Unknown)
