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
    plant1 = plants("Rose", 25, 30)
    print(
        f"{plant1.name}: {plant1.Height}cm, "
        f"{plant1.Age} days old"
    )
    for i in range(1, 8):
        plant1.age()
        plant1.grow()
        print(f"=== Day {i} ===")
        print(
            f"{plant1.name}: {plant1.Height:.1f}cm, "
            f"{plant1.Age} days old"
        )
    print(f"Grow this week: {i*0.8:.1f}")
