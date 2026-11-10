if __name__ == "__main__":
    plants = [
        {"name": "Rose", "Height": "25", "Age": "30"},
        {"name": "Sunflower", "Height": "80", "Age": "45"},
        {"name": "Cactus", "Height": "15", "Age": "120"}
    ]
    print("=== Garden Plant Registry ===")
    for flowers in plants:
        print(
            f"{flowers['name']}: {flowers['Height']}cm, "
            f"{flowers['Age']} days old"
        )
