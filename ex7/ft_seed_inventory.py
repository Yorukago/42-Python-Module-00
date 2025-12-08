# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 14:51:31 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 15:06:11 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_name, quantity, unit):
    seed_name = seed_name.capitalize()
    if unit == "packets":
        print(f"{seed_name} seeds: {quantity} packets available.")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} grams total.")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters.")
    else:
        print(f"{seed_name} seeds: {quantity} {unit}")