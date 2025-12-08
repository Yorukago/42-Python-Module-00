# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 14:47:27 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 14:50:35 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name: ")
    n_plants = int(input("Enter number of plants: "))
    print("Garden:", name)
    print("Plants:", n_plants)
    print("Status: Growing well!")