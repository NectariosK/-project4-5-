from add import Addition
from subtract import Subtraction
from multiple import Multiplication
from divide import Division

operation1 = Addition()
operation2 = Subtraction(operation1)
operation3 = Division(operation2)
operation4 = Multiplication(operation3)

calculation = operation4.request_handler("2 * 3")

print(f"The answer of the operation is: {calculation}")
