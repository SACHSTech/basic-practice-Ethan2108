temperature = float(input("What is the temperature in celsius?: "))
wind_speed = float(input("What is the windspeed in km/h?: "))

windchill = 13.12 + (0.6215 * temperature) - (11.37 * wind_speed**0.16) + (0.3965 * temperature * wind_speed**0.16)

print("The windchill is",windchill,"Degrees Celsius")
