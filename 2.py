class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 6) + 32


temp = Temperature(0)
print(f'temperature fahrenheit: {temp.fahrenheit}')
