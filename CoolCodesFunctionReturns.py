def returnFahrenheitEquivalent(TemperatureInCelcius):
    temp = TemperatureInCelcius * 1.8 + 32
    return temp

TemperatureInFahrenheit = returnFahrenheitEquivalent(45)
print("45 degrees on Celsius scale is equivalent to ",TemperatureInFahrenheit," degrees on fahrenheit scale, how cool!")