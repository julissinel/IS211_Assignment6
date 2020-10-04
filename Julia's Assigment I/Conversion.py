import decimal


def convertCelsiusToKelvin(input):
    input = str(input)
    convert = (decimal.Decimal(input) + decimal.Decimal('273.15'))
    return float(convert)


def convertCelsiusToFahrenheit(input):
    input = str(input)
    convert = (decimal.Decimal(input) / decimal.Decimal('5') * 9) + 32
    return float(convert)


def convertFahrenheitToCelsius(input):
    input = str(input)
    convert = ((decimal.Decimal(input) - 32) * 5) / decimal.Decimal('9')
    return float(convert)


def convertFahrenheitToKelvin(input):
    input = str(input)
    convert = (((decimal.Decimal(input) + decimal.Decimal('459.67')) * 5) /
               decimal.Decimal('9'))
    return float(convert)


def convertKelvinToCelsius(input):
    input = str(input)
    convert = (decimal.Decimal(input) - decimal.Decimal('273.15'))
    return float(convert)


def convertKelvinToFahrenheit(input):
    input = str(input)
    convert = (((decimal.Decimal(input) * 9) / decimal.Decimal('5'))
               - decimal.Decimal('459.67'))
    return float(convert)

