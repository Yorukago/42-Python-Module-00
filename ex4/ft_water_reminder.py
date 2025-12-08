# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 14:15:02 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 14:16:11 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    water = int(input("Days since last watering: "))
    if(water > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")