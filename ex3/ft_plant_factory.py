# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_factory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/21 23:55:22 by nilinott          #+#    #+#             #
#    Updated: 2026/02/21 23:55:25 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    
    def get_info(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def display_plant(plants, max_plant: int):
    i: int = 0
    while (i < max_plant):
        print(plants[i].get_info())
        i += 1


def main() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]
    max_plant = len(plants)
    print("=== Plant Factory Output ===")
    display_plant(plants, max_plant)
    print(f"\nTotal plants created: {max_plant}")


if __name__ == "__main__":
    main()