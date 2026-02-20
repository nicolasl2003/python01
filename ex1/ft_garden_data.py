# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_data.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/20 16:33:47 by nilinott          #+#    #+#             #
#    Updated: 2026/02/20 16:33:56 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    plant_a = Plant(name='Rose', height=25, age=30)
    plant_b = Plant(name='Sunflower', height=80, age=45)
    plant_c = Plant(name='Cactus', height=15, age=120)
    print("=== Garden Plant Registry ===")
    print(f"{plant_a.name}: {plant_a.height}cm, {plant_a.age} days old")
    print(f"{plant_b.name}: {plant_b.height}cm, {plant_b.age} days old")
    print(f"{plant_c.name}: {plant_c.height}cm, {plant_c.age} days old")


if __name__ == "__main__":
    main()
