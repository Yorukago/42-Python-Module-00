def ft_count_harvest_iterative():
    n = int(input("Enter days until harvest: "))
    day = 1
    while day <= n:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")
