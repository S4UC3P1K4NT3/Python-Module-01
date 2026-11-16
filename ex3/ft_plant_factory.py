class plants:
    def __init__(self, name, Height, Age):
        self.name = name
        self.Height = Height
        self.Age = Age

    def grow(self) -> None:
        self.Height += 0.8

    def age(self) -> None:
        self.Age += 1


if __name__ == "__main__":
    p1 = plants("Rose", 25, 30)
    p2 = plants("Oak", 200, 365)
    p3 = plants("Cactus", 5, 90)
    p4 = plants("Sunflower", 80, 45)
    p5 = plants("Fern", 15, 120)
    garden = [p1, p2, p3, p4, p5]
    print("=== Plant Factory Output ===")
    for i in range(5):
        print(
            f"Created: "
            f"{garden[i].name}: {garden[i].Height}cm, "
            f"{garden[i].Age} days old"
        )
