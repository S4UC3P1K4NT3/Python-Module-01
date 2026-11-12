
class plants:
    def __init__(self,name,Height,Age):
        self.name = name
        self.Height = Height
        self.Age = Age

if __name__ == "__main__":
    plant1 = plants("Rose",25,30)
    plant2 = plants("Sunflower",80,45)
    plant3 = plants("Cactus",15,120)
    garden = [plant1,plant2,plant3]
    print("=== Garden Plant Registry ===")
    for flowers in garden:
        print(
            f"{flowers.name}: {flowers.Height}cm, "
            f"{flowers.Age} days old"    
        )
