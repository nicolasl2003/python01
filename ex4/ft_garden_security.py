# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_security.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/22 00:44:35 by nilinott          #+#    #+#             #
#    Updated: 2026/02/22 00:44:36 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def set_height(self, height: int) -> None:
        self.height = height


def main() -> None:
    plants = [
        Plant("Rose", 25, 30),
    ]

    plants.set_height(58)
    print(plants.height)


if __name__ == "__main__":
    main()
