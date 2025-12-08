# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 14:17:27 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 14:46:05 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    n = int(input("Enter days until harvest: "))
    def ft_counter(days):
        if days > n:
            print("Harvest time!")
            return
        print(f"Day {days}");
        ft_counter(days + 1)
    ft_counter(1)


