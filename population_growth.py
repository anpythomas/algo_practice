# Goal: Complete Mission



def nb_year(p0, percent, aug, p):
    if p0 >= p:
        return 0
    total_pop = p0 * (1 + (percent / 100)) + aug
    full_years = 1
    while True:
        if total_pop >= p:
            break
        else:
            total_pop = int(total_pop * (1 + (percent / 100)) + aug)
            full_years += 1
    return full_years

x = nb_year(1000, 2.0, 50, 1214)
print(x)