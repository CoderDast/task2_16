earth_year = int(input('Your weight in earth = '))
moon_year = earth_year * 0.165
for i in range(16):
    print(i, '-year = ', moon_year)
    moon_year = moon_year + 0.165