def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value + 459.67) * 5/9
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value * 9/5) - 459.67
    else:
        return None

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'liters_gallons': 0.264172,
        'gallons_liters': 3.78541
    }
    key = f'{from_unit}_{to_unit}'
    return value * conversions.get(key, 1)

def convert_mass(value, from_unit, to_unit):
    conversions = {
        'kilograms_pounds': 2.20462,
        'pounds_kilograms': 0.453592
    }
    key = f'{from_unit}_{to_unit}'
    return value * conversions.get(key, 1)

# Main program
print("Select conversion type: \n1. Temperature \n2. Volume \n3. Mass")
conversion_type = input("Enter 1, 2, or 3: ")

if conversion_type == '1':
    from_unit = input("Convert from (Celsius, Fahrenheit, Kelvin): ")
    to_unit = input("Convert to (Celsius, Fahrenheit, Kelvin): ")
    value = float(input("Enter the value to convert: "))
    result = convert_temperature(value, from_unit, to_unit)
elif conversion_type == '2':
    from_unit = input("Convert from (liters, gallons): ")
    to_unit = input("Convert to (liters, gallons): ")
    value = float(input("Enter the value to convert: "))
    result = convert_volume(value, from_unit, to_unit)
elif conversion_type == '3':
    from_unit = input("Convert from (kilograms, pounds): ")
    to_unit = input("Convert to (kilograms, pounds): ")
    value = float(input("Enter the value to convert: "))
    result = convert_mass(value, from_unit, to_unit)
else:
    result = None

if result is not None:
    print(f"Converted value: {result}")
else:
    print("Invalid conversion type or units.")
