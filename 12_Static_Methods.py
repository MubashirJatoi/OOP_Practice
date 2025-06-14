class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 / 5 * c + 32
    
convert = TemperatureConverter.celsius_to_fahrenheit(2)
print(f" {convert}")