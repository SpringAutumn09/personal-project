def KelvinToCelsius(k):
    c = k - 273

def CelsiusToFahrenheit(c):
    f = (c)*9/5 + 32

def FahrenheitToCelsius(f):
    c = (5/9)(f-32)

def hPaToInHg(hpa):
    inhg = hpa * 0.02953

def round_float(num, decimals=0):
    # Shift the decimal point to the right
    multiplier = 10 ** decimals
    
    # Multiply the number by the multiplier, round it to the nearest integer, and then shift the decimal back
    rounded = int(num * multiplier + 0.5) if num > 0 else int(num * multiplier - 0.5)
    
    # Divide back to get the rounded value
    return rounded / multiplier

