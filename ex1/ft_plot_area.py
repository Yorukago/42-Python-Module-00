# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jzorreta <jzorreta@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 13:56:18 by jzorreta          #+#    #+#              #
#    Updated: 2025/12/08 14:01:11 by jzorreta         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    print("The area is: ", area)