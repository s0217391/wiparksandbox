

class Pin(object):

    gpio_path = "/sys/class/gpio"
    pin_type_error_str = "Illegal type for parameter pin_number, should be an int"
    mode_value_error_str = "Illegal value for parameter direction, should be Pin.OUTPUT_MODE or Pin.INPUT_MODE"
    value_value_error_str = "Illegal value for parameter value, should be Pin.DISABLE or Pin.ENABLE"
    returnvalue_value_error_str = "Found illegal value when reading pin."

    OUTPUT_MODE = "out"
    INPUT_MODE = "in"

    DISABLE = 0
    ENABLE = 1

    def __init__(self, pin_number):
        assert type(pin_number) is int, self.pin_type_error_str
        self.pin_number = pin_number
        # Initialize pin
        self.__write_to_file( "{}/unexport".format(self.gpio_path) , self.pin_number)
        self.__write_to_file("{}/export".format(self.gpio_path), self.pin_number)

    def __write_to_file(self, filename, value):
        with open(filename, 'w') as f:
            f.write(value)

    def get_pin_value(self):
        value = 0
        with open("{}/gpio{}/value".format(self.gpio_path, self.pin_number), 'r') as f:
            contents = f.read()
            value = int(contents)
        assert value == 0 or value == 1, self.returnvalue_value_error_str
        return value

    def set_pin_direction(self, direction):
        assert direction == self.OUTPUT_MODE or direction == self.INPUT_MODE, mode_value_error_str
        self.__write_to_file('{}/gpio{}/direction'.format(self.gpio_path, pin), direction)

    def set_pin_value(self, value):
        assert value == self.DISABLE or value == self.ENABLE, mode_value_error_str
        self.__write_to_file('{}/gpio{}/value'.format(self.gpio_path, pin), value)
