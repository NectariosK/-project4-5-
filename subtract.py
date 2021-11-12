from operation import Operation


class Subtraction(Operation):
    def request_handler(self, text):
        chars = text.split()

        if chars[1] == '-':
            print(int(chars[0]) - int(chars[2]))
            return int(chars[0]) - int(chars[2])
        elif self._successor is not None:
            return self._successor.request_handler(text)
        else:
            print("The operation you fed in is not supported.")
            return None
