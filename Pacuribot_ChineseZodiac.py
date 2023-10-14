# variables of birth year
rat = (1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020)
ox = (1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021)
tiger = (1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022)
rabbit = (1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023)
dragon = (1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024)
snake = (1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025)
horse = (1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026)
goat = (1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027)
monkey = (1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028)
rooster = (1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029)
dog = (1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030)
pig = (1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031)

# input function from user
year = eval(input("Enter your birth year!\n"))

# If-else statements
if year in rat:
    print("Your chinese zodiac sign is Rat!")
    print("You are quite Quick-witted, resourceful, versatile and kind.")
elif year in ox:
    print("Your chinese zodiac sign is Ox!")
    print("You are quite Diligent, dependable, strong and determined.")
elif year in tiger:
    print("Your chinese zodiac sign is Tiger!")
    print("You are quite Brave, confident and competitive.")
elif year in rabbit:
    print("Your chinese zodiac sign is Rabbit!")
    print("You are quite Quiet, elegant, kind and responsible.")
elif year in dragon:
    print("Your chinese zodiac sign is Dragon!")
    print("You are quite Quiet Confident, intelligent and enthusiastic.")
elif year in snake:
    print("Your chinese zodiac sign is Snake!")
    print("You are quite Enigmatic, intelligent and wise.")
elif year in horse:
    print("Your chinese zodiac sign is Horse!")
    print("You are quite Animated, active and energetic.")
elif year in goat:
    print("Your chinese zodiac sign is Goat!")
    print("You are quite Calm, gentle and sympathetic.")
elif year in monkey:
    print("Your chinese zodiac sign is Monkey!")
    print("You are quite Sharp, smart and filled with curiosity.")
elif year in rooster:
    print("Your chinese zodiac sign is Rooster!")
    print("You are quite Observant, hardworking and courageous.")
elif year in dog:
    print("Your chinese zodiac sign is Dog!")
    print("You are quite Lovely, honest and prudent.")
elif year in pig:
    print("Your chinese zodiac sign is Pig!")
    print("You are quite Compassionate, generous and diligent.")
else:
    print("The year you have input is not in the chinese calendar :(")
