import logging

logging.basicConfig(
	level=logging.DEBUG,                   
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filename="33_Logging/app.log"    
)

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

num1 = 10
num2 = 20

# Logging
# There are 5 levels of logging
# DEBUG, INFO, WARNING, ERROR, CRITICAL


add_result = add(num1, num2)
subtract_result = subtract(num1, num2)
multiply_result = multiply(num1, num2)
divide_result = divide(num1, num2)

logging.debug(f"{num1} + {num2} = {add_result}")
logging.debug(f"{num1} - {num2} = {subtract_result}")
logging.debug(f"{num1} * {num2} = {multiply_result}")
logging.debug(f"{num1} / {num2} = {divide_result}")

logging.info(f"{num1} + {num2} = {add_result}")
logging.info(f"{num1} - {num2} = {subtract_result}")
logging.info(f"{num1} * {num2} = {multiply_result}")
logging.info(f"{num1} / {num2} = {divide_result}")

logging.warning(f"{num1} + {num2} = {add_result}")
logging.warning(f"{num1} - {num2} = {subtract_result}")
logging.warning(f"{num1} * {num2} = {multiply_result}")
logging.warning(f"{num1} / {num2} = {divide_result}")

logging.error(f"{num1} + {num2} = {add_result}")
logging.error(f"{num1} - {num2} = {subtract_result}")
logging.error(f"{num1} * {num2} = {multiply_result}")
logging.error(f"{num1} / {num2} = {divide_result}")

logging.critical(f"{num1} + {num2} = {add_result}")
logging.critical(f"{num1} - {num2} = {subtract_result}")
logging.critical(f"{num1} * {num2} = {multiply_result}")        