# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 14:09:53 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 14:13:04 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if(plant_age < 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")