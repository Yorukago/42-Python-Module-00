# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 14:17:08 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 14:23:22 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    n = int(input("Enter days until harvest: "))
    day = 1
    while day <= n:
        print(day)
        day += 1
    print("Harvest time!")
