# This is my code for the Mathematical Menu
# It is a project that I have done myself at home
# Along with this, there are five external files:
# mathematical.menu.tests.txt,
# details.txt,
# formulae.txt,
# menus.py,
# authentication.py

# How to execute this program on a command line:
# (make sure all the external files are in the same folder as the main program)
# python3 mathematicalMenu.py
# or if you have py installed instead of python3:
# py mathematicalMenu.py

#############
# LIBRARIES #
#############

from math import pi, sqrt, sin, asin, cos, acos, tan, atan, radians, degrees, lcm
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt # This module is for plotting the graphs

import logging
import doctest

import menus

#############
# CONSTANTS #
#############

EMPTY_STRING = ''
FILENAME_1 = 'formulae' # This file stores the useful formulae
FILENAME_2 = 'details' # This file stores the encrypted account details of users
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[]{};:.<>/?|~`'
MAX_LENGTH = len(SYMBOLS)

# Sets up logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="{asctime} | {levelname} | {name} | {lineno} | {funcName} | {message}",
    style="{",
    datefmt='%Y-%m-%d-%H:%M',
)
logger = logging.getLogger(__name__)

###########
# CLASSES #
###########

class Circle: # returns the area and the circumference of a circle with a given radius
    def __init__(self, radius):
        self.radius = radius
    def calculate_circumference(self):
        return 2 * pi * self.radius
    def calculate_area(self):
        return pi * self.radius ** 2

class Angle: # returns the angle given two sides of a right-angled triangle
    def __init__(self, hypotenuse, opposite, adjacent):
        self.hypotenuse = hypotenuse
        self.opposite = opposite
        self.adjacent = adjacent
    def calculate_sin_angle(self):
        return degrees(asin(self.opposite / self.hypotenuse))
    def calculate_cos_angle(self):
        return degrees(acos(self.adjacent / self.hypotenuse))
    def calculate_tan_angle(self):
        return degrees(atan(self.opposite / self.adjacent))

class Side: # returns the unknown side given the known side and the angle or a right-anled triangle
    def __init__(self, hypotenuse, opposite, adjacent, angle):
        self.hypotenuse = hypotenuse
        self.opposite = opposite
        self.adjacent = adjacent
        self.angle = angle
    def calculate_hypotenuse(self):
        if self.opposite != 0:
            return self.opposite / sin(radians(self.angle))
        elif self.adjacent != 0:
            return self.adjacent / cos(radians(self.angle))
    def calculate_opposite(self):
        if self.hypotenuse != 0:
            return self.hypotenuse * sin(radians(self.angle))
        elif self.adjacent != 0:
            return self.adjacent * tan(radians(self.angle))
    def calculate_adjacent(self):
        if self.hypotenuse != 0:
            return self.hypotenuse * cos(radians(self.angle))
        elif self.opposite != 0:
            return self.opposite / tan(radians(self.angle))

###############
# SUBPROGRAMS #
###############

# Multiple subprograms printing different menus

def get_menu_option() -> str:
    choice = EMPTY_STRING
    while len(choice) != 1:
        choice = input('Enter your choice: ').upper()
    return choice[0]

def differentiate(exp: str,respect: str) -> str: # Differentiates a given expression with respect to a given variable
    var = sym.Symbol(respect)
    for item in exp:
        if item not in 'xyz+-*/0123456789 ':
            logger.error('Invalid input: {}'.format(exp))
            return f'Invalid input: {exp}'
    if respect.isalpha():
        return f'The derivative is {sym.diff(exp, var)}'
    else:
        logger.error('Wrong input: {}'.format(respect))
        return f'Invalid input: {respect}'

def integrate(exp: str, respect: str) -> str: # Integrates a given expression with respect to a given variable
    var = sym.Symbol(respect)
    for item in exp:
        if item not in 'xyz+-*/0123456789 ':
            logger.error('Wrong input: {}'.format(exp))
            return f'Invalid input: {exp}'
    if respect.isalpha():
        return f'The integral is {(sym.integrate(exp, var))}'
    else:
        logger.error('Wrong input: {}'.format(respect))
        return f'Invalid input: {respect}'

def handle_inputs_for_searching():
    finished = False
    while not finished:
        print()
        print('The Mathematical Menu can perform a number of searches on one-dimensional arrays:')
        print('-> Linear search')
        print('-> Binary search')
        print('-> Two-pointer search')
        print('...or type X to exit this menu')
        print()
        choice: str = input('Enter your choice (1 / 2 / 3): ')
        if choice[0] == 'X':
            finished = True
        arr = input('Enter your array values separated by commas, no square brackets: ').split(',')
        arr = list(map(int, arr))
        target: int = int(input('Enter target: '))
        if choice[0] == '1':
            print(linear_search(arr, target))
        elif choice[0] == '2':
            low = 0
            high = len(arr) - 1
            result = binary_search(arr, target, low, high)
            print(result)
        elif choice[0] == '3':
            pass
        else:
            print('Invalid input')

def linear_search(arr: list[int], target: int) -> str:
    for i in range(len(arr)):
        if arr[i] == target:
            return f'Found at index {i}'
    return 'Not found'

def binary_search(arr: list[int], target: int, low: int, high: int) -> str:
    arr = sorted(arr)
    while low <= high:
        mid: int = low + (high - low) // 2
        if arr[mid] == target:
            return f'Found at index {mid}, {arr}'
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return 'Not found'

def handle_inputs_for_sorting():
    finished = False
    while not finished:
        print()
        print('The Mathematical Menu can perform a number of sorting algorithms on one-dimensional arrays:')
        print('-> Bubble sort')
        print('-> Merge sort')
        print('-> Selection sort')
        print('-> Insertion sort')
        print('...or type X to exit this menu (must be capitals)')
        print()
        choice: str = input('Enter your choice (1 / 2 / 3 / 4): ')
        if choice == 'X':
            finished = True
        arr = input('Enter your array values separated by commas, no square brackets: ').split(',')
        arr = list(map(int, arr))
        if choice[0] == '1':
            print(bubble_sort(arr))
        elif choice[0] == '2':
            pass
        elif choice[0] == '3':
            pass
        elif choice[0] == '4':
            pass
        else:
            return 'Invalid input'

def bubble_sort(arr: list[int]) -> str:
    length: int = len(arr)
    for i in range(length - 1):
        swaps = False
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
        if not swaps:
            return ' '.join(list(map(str, arr)))

def handle_inputs_linked_list():
    choice: str = input('Would you like to create a linked list? (y/n)').lower()
    if choice == 'n':
        return None
    inp = input('Initialize your first node, followed by the data type, separated by a comma: ').split(',')
    first_node, typist = inp[0], inp[1]
    pass


def simplify_simultaneous_equations(pEquation1, pEquation2): # Returns two split equations
    for item in pEquation1:
        if item not in 'xy-=+.0123456789':
            logger.error('Wrong input: {}'.format(pEquation1))
            return 0, 0
        else:
            continue

    for item in pEquation2:
        if item not in 'xy-=+.0123456789':
            logger.error('Wrong input: {}'.format(pEquation2))
            return 0, 0
        else:
            continue

    # Gets rid of the '+' and '=' but keeps the '-' in front of coefficients
    pEquation1 = pEquation1.replace('-', '+-')
    pEquation1 = pEquation1.replace('=', '+')
    pEquation1 = pEquation1.split('+')

    pEquation2 = pEquation2.replace('-', '+-')
    pEquation2 = pEquation2.replace('=', '+')
    pEquation2 = pEquation2.split('+')

    # Splitting the equation can result in some indexes containing empty strings
    for i in range(len(pEquation1)):
        if pEquation1[i] == '':
            del pEquation1[i]
            break
        else:
            continue

    for i in range(len(pEquation1)):
        if pEquation1[i] == '':
            del pEquation1[i]
            break
        else:
            continue

    for i in range(len(pEquation2)):
        if pEquation2[i] == '':
            del pEquation2[i]
            break
        else:
            continue

    for i in range(len(pEquation2)):
        if pEquation2[i] == '':
            del pEquation2[i]
            break
        else:
            continue


    return pEquation1, pEquation2

def solve_quadratic(equation: str) -> str: # Prints the result(s) of the quadratic equation
    coefficients = {
        'a': 0,
        'b': 0,
        'c': 0
    }

    for item in equation:
        if item not in 'x^+-0123456789':
            return f'Invalid input: {equation}'

    equation = equation.replace('-', '+-')
    equation = equation.split('+')

    if '' in equation: equation.remove('')
    if equation[0] == 'x^2':
        coefficients['a'] = 1

    elif equation[0] == '-x^2':
        coefficients['a'] = -1

    elif len(equation[0]) >= 4 and (('-' in equation[0] and equation[0][1:-3].isdigit()) or equation[0][:-3].isdigit()):
        coefficients['a'] = int(equation[0][:-3])

    else:
        return f'Invalid input: {equation[0]}'

    if equation[1] == 'x':
        coefficients['b'] = 1

    elif equation[1] == '-x':
        coefficients['b'] = -1

    elif len(equation[1]) >= 2 and (('-' in equation[1] and equation[1][1:-1].isdigit()) or equation[1][:-1].isdigit()):
        coefficients['b'] = int(equation[1][:-1])

    else:
        return f'Invalid input: {equation[1]}'

    if ('-' in equation[-1] and equation[-1][1:].isdigit()) or equation[-1].isdigit():
        coefficients['c'] = int(equation[-1])

    else:
        return f'Invalid input: {equation[-1]}'

    delta = (coefficients['b'] ** 2) - 4 * coefficients['a'] * coefficients['c']
    result_1 = str((-1 * coefficients['b'] + sqrt(delta)) / (2 * coefficients['a']))
    result_2 = str((-1 * coefficients['b'] - sqrt(delta)) / (2 * coefficients['a']))

    choice = input('Would you like to acquire the x-intercepts, the y-intercept and the min/max point of this graph? (y/n): ')
    if choice.startswith('y'):
        return create_quadratic_graph(coefficients['a'], coefficients['b'], coefficients['c'], result_1, result_2)

    if result_1 == result_2:
        return f'Solution: {float(result_1):.1f}' if '+0j' not in result_1 else f'Solution: {result_1}'

    else:
        return f'Solutions: {float(result_1):.1f}, {float(result_2):.1f}' if '+0j' not in result_1 and '+0j' not in result_2 else f'Solutions: {result_1}, {result_2}'

def acquire_simultaneous_coefficients(pEquation1, pEquation2): # Getting the coefficients of both equations
    x_coe_1 = EMPTY_STRING
    y_coe_1 = EMPTY_STRING
    int_1 = EMPTY_STRING
    coe_1 = []

    x_coe_2 = EMPTY_STRING
    y_coe_2 = EMPTY_STRING
    int_2 = EMPTY_STRING

    for item in pEquation1: # First equation
        # Acquiring coefficient of y
        if item == 'y':
            y_coe_1 = 1
            y_coe_1 = int(y_coe_1)
        elif item == '-y':
            y_coe_1 = -1
            y_coe_1 = int(y_coe_1)
        elif 'y' in item and item != 'y' and item != 'y':
            y_coe_1 = item[:-1]
            y_coe_1 = int(y_coe_1)
        # Acquiring coefficient of x
        elif item == 'x':
            x_coe_1 = 1
            x_coe_1 = int(x_coe_1)
        elif item == '-x':
            x_coe_1 = -1
            x_coe_1 = int(x_coe_1)
        elif 'x' in item and item != 'x' and item != '-x':
            x_coe_1 = item[:-1]
            x_coe_1 = int(x_coe_1)
        # Acquiring integer
        elif 'x' not in item and 'y' not in item:
            int_1 = item
            int_1 = int(int_1)
        else:
            logger.error('There is something wrong here!')
            return 0, 0

    # Storing the coefficients in an array for later use
    coe_1.append(y_coe_1)
    coe_1.append(x_coe_1)
    coe_1.append(int_1)

    for item in pEquation2: # Second equation
        # Acquiring coefficient of y
        if item == 'y':
            y_coe_2 = 1
            y_coe_2 = int(y_coe_2)
        elif item == '-y':
            y_coe_2 = -1
            y_coe_2 = int(y_coe_2)
        elif 'y' in item and item != 'y' and item != '-y':
            y_coe_2 = item[:-1]
            y_coe_2 = int(y_coe_2)
        # Acquiring coefficient of x
        elif item == 'x':
            x_coe_2 = 1
            x_coe_2 = int(x_coe_2)
        elif item == '-x':
            x_coe_2 = -1
            x_coe_2 = int(x_coe_2)
        elif 'x' in item and item != 'x' and item != '-x':
            x_coe_2 = item[:-1]
            x_coe_2 = int(x_coe_2)
        # Acquiring integer
        elif 'x' not in item and 'y' not in item:
            int_2 = item
            int_2 = int(int_2)
        else:
            logger.error('There is something wrong here!')
            return 0, 0

    y = 0.0
    x = 0.0

    # Dividing each coefficient by the lcm
    lcm1 = lcm(x_coe_1, x_coe_2)
    if lcm == x_coe_2:
        x_coe_1 *= (lcm1 / x_coe_1)
        y_coe_1 *= (lcm1 / x_coe_1)
        int_1 *= (lcm1 / x_coe_1)
    elif lcm == x_coe_1:
        x_coe_2 *= (lcm1 / x_coe_2)
        y_coe_2 *= (lcm1 / x_coe_2)
        int_2 *= (lcm1 / x_coe_2)
    elif lcm != x_coe_1 and lcm != x_coe_2:
        mul_1 = lcm1 / x_coe_1
        mul_2 = lcm1 / x_coe_2

        temp = x_coe_1
        x_coe_1 *= x_coe_2
        x_coe_2 *= temp

        y_coe_1 *= mul_1
        y_coe_2 *= mul_2
        int_1 *= mul_1
        int_2 *= mul_2
    else:
        logger.error('There is something wrong here!')
        return 0, 0

    # Simplifying equations using elimination method
    y_coe_1 -= y_coe_2
    int_1 -= int_2
    if y_coe_1 == 0:
        y = int_1
    else:
        y = int_1 / y_coe_1

    temp = y

    temp = temp * coe_1[0]
    x = (temp - coe_1[-1]) / coe_1[1]

    return x, y

def solve_simultaneous_equations(): # Prints the answers to simultaneous equations
    equation1 = input('Enter first equation in the form of ay=bx+c: ')
    equation2 = input('Enter second equation in the form of ay=bx+c: ')

    equation1, equation2 = simplify_simultaneous_equations(equation1, equation2)
    if equation1 == 0 or equation2 == 0: # Validation
        return 'Invalid input'
    x, y = acquire_simultaneous_coefficients(equation1, equation2)
    if x == 0 or y == 0: # Validation
        logger.error('Wrong input: {}, {}'.format(equation1, equation2))
        return 'Invalid input'
    else:
        return f'The answers are: x = {x} and y = {y}'

def display_formulae(): # Displays relevant formulae
    try:
        print()
        print("a, b and c are sides of a triangle, A, B and C are angles of the triangle opposite the respective letters' side")
        print('<pi> should be replaced with the constant 3.1415...')
        print('l, w and h are length, width and height')
        print('For the quadratic formula, a, b and c are the coefficients in the quadratic equation ax^2 + bx + c')
        print()
        print('+' + '=' * 69 + '+')
        print('|{:^31}|{:^36}|'.format('Name of formula', 'Formula'))
        print('+' + '=' * 69 + '+')
        with open(FILENAME_1 + '.txt', 'r') as file: # Gets the formulae from external file
            for line in file:
                line = line.strip()
                line = line.split(',')
                print('|{:^31}|{:^36}|'.format(line[0], line[1]))
        print('+' + '=' * 69 + '+')
        #logger.info('Formulae display successful!')
    except FileNotFoundError:
        logger.error('File not found')
        print('File not found')
    except:
        logger.error('Some other error occurred')
        print('Some other error occurred`')

def handle_inputs_for_find_angle_trig():
    lost_side = input('Enter the side that is not there: ').lower() # Need to use the correct trig function
    if lost_side == 'adjacent':
        opposite = input('Enter the value on the opposite side: ')
        hypotenuse = input('Enter the value on the hypotenuse side: ')
        trig_angle_sine(opposite, hypotenuse)
    elif lost_side == 'opposite':
        adjacent = input('Enter the value on the adjacent side: ')
        hypotenuse = input('Enter the value on the hypotenuse side: ')
        trig_angle_cosine(adjacent, hypotenuse)
    elif lost_side == 'hypotenuse':
        opposite = input('Enter the value on the opposite side: ')
        adjacent = input('Enter the value on the adjacent side: ')
        trig_angle_tangent(opposite, adjacent)
    else:
        logger.error('Wrong input: {}'.format(lost_side))
        print('Invalid input')

def trig_angle_sine(opposite, hypotenuse): # Using the inverse sine function
    if opposite.isdigit() and hypotenuse.isdigit():
        opposite = int(opposite)
        hypotenuse = int(hypotenuse)
        result = Angle(hypotenuse, opposite, 0)
        print('The missing angle is {:.2f}'.format(result.calculate_sin_angle()))
    else:
        logger.error('Wrong input: {}, {}'.format(opposite, hypotenuse))
        print('Invalid input')

def trig_angle_cosine(adjacent, hypotenuse): # Using the inverse cosine function
    if adjacent.isdigit() and hypotenuse.isdigit():
        adjacent = int(adjacent)
        hypotenuse = int(hypotenuse)
        result = Angle(hypotenuse, 0, adjacent)
        print('The missing angle is {:.2f}'.format(result.calculate_cos_angle()))
    else:
        logger.error('Wrong input: {}, {}'.format(adjacent, hypotenuse))
        print('Invalid input')

def trig_angle_tangent(opposite, adjacent): # Using the inverse tangent function
    if opposite.isdigit() and adjacent.isdigit():
        opposite = int(opposite)
        adjacent = int(adjacent)
        result = Angle(0, opposite, adjacent)
        print('The missing angle is {:.2f}'.format(result.calculate_tan_angle()))
    else:
        logger.error('Wrong input: {}, {}'.format(opposite, adjacent))
        print('Invalid input')

def handle_inputs_for_find_side_trig(): # Chooses which trig function to use depending on the sides shown
    find_side = input('Enter the side you want to find: ').lower() # Which side is unknown
    shown_side = input('Enter the side that is shown: ').lower() # Which side is known
    if find_side[0] == 'h': # Use either sine or cosine
        if shown_side[0] == 'o': # Use sine
            value = input('Enter the opposite side length: ')
            angle = input('Enter the angle shown: ')
            trig_side_hyp_opp(value, angle)
        elif shown_side[0] == 'a': # Use cosine
            value = input('Enter the adjacent side length: ')
            angle = input('Enter the angle shown: ')
            trig_side_hyp_adj(value, angle)
        else:
            logger.error('Wrong input: {}'.format(shown_side))
            print('Invalid input')
    elif find_side[0] == 'o': # Use either sine or tangent
        if shown_side[0] == 'h': # Use sine
            value = input('Enter the hypotenuse side length: ')
            angle = input('Enter the angle shown: ')
            trig_side_opp_hyp(value, angle)
        elif shown_side[0] == 'a': # Use tangent
            value = input('Enter the adjacent side length: ')
            angle = input('Enter the angle shown: ')
            trig_side_opp_adj(value, angle)
        else:
            logger.error('Wrong input: {}'.format(shown_side))
            print('Invalid input')
    elif find_side[0] == 'a': # Use either cosine or tangent
        if shown_side[0] == 'h': # Use cosine
            value = input('Enter the hypotenuse side length: ')
            angle = input('Enter the angle shown: ')
            trig_side_adj_hyp(value, angle)
        elif shown_side[0] == 'o': # Use tangent
            value = input('Enter the opposite side length: ')
            angle = input('Enter the angle shown: ')
            trig_side_adj_opp(value, angle)
        else:
            logger.error('Wrong input: {}'.format(shown_side))
            print('Invalid input')
    else:
        logger.error('Wrong input: {}'.format(find_side))
        print('Invalid input')

# Multiple trig functions that depend on the inputs
# The first side is the one to find, the second is the one that is given
# For example, in the subprogram below, 'hyp' is the side to find and 'opp' is the one that is given

def trig_side_hyp_opp(value, angle):
    if value.isdigit() and angle.isdigit(): # Validation
        value = int(value)
        angle = int(angle)
        result = Side(0, value, 0, angle) # Calls appropriate function
        print('The hypotenuse side length is {:.2f}'.format(result.calculate_hypotenuse()))
    else:
        logger.error('Wrong input: {}, {}'.format(value, angle))
        print('Invalid input')

def trig_side_hyp_adj(value, angle):
    if value.isdigit() and angle.isdigit(): # Validation
        value = int(value)
        angle = int(angle)
        result = Side(0, 0, value, angle) # Calls appropriate function
        print('The hypotenuse side length is {:.2f}'.format(result.calculate_hypotenuse()))
    else:
        logger.error('Wrong input: {}, {}'.format(value, angle))
        print('Invalid input')

def trig_side_opp_hyp(value, angle):
    if value.isdigit() and angle.isdigit(): # Validation
        value = int(value)
        angle = int(angle)
        result = Side(value, 0, 0, angle) # Calls appropriate function
        print('The opposite side length is {:.2f}'.format(result.calculate_opposite()))
    else:
        logger.error('Wrong input: {}, {}'.format(value, angle))
        print('Invalid input')

def trig_side_opp_adj(value, angle):
    if value.isdigit() and angle.isdigit(): # Validation
        value = int(value)
        angle = int(angle)
        result = Side(0, 0, value, angle) # Calls appropriate function
        print('The opposite side length is {:.2f}'.format(result.calculate_opposite()))
    else:
        logger.error('Wrong input: {}, {}'.format(value, angle))
        print('Invalid input')

def trig_side_adj_hyp(value, angle):
    if value.isdigit() and angle.isdigit(): # Validation
        value = int(value)
        angle = int(angle)
        result = Side(value, 0, 0, angle) # Calls appropriate function
        print('The adjacent side length is {:.2f}'.format(result.calculate_adjacent()))
    else:
        logger.error('Wrong input: {}, {}'.format(value, angle))
        print('Invalid input')

def trig_side_adj_opp(value, angle):
    if value.isdigit() and angle.isdigit(): # Validation
        value = int(value)
        angle = int(angle)
        result = Side(0, value, 0, angle) # Calls appropriate function
        print('The adjacent side length is {:.2f}'.format(result.calculate_adjacent()))
    else:
        logger.error('Wrong input: {}, {}'.format(value, angle))
        print('Invalid input')

def trig(): # Asks the user to choose between angles and sides
    finished = False
    while not finished:
        choice = input('Do you want to solve for angles or sides? (A / S): ').upper()
        if choice[0] == 'A':
            handle_inputs_for_find_angle_trig()
            finished = True
        elif choice[0] == 'S':
            handle_inputs_for_find_side_trig()
            finished = True
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Please enter A or S')

def handle_inputs_for_circles():
    radius = input('Enter the radius: ')
    circles(radius)

def circles(radius): # Prints the area and circumference
    if radius.isdigit(): # Validation
        radius = int(radius)
        result = Circle(radius) # Calls appropriate function
        print('The area is {:.2f}'.format(result.calculate_area()))
        print('The circumference is {:.2f}'.format(result.calculate_circumference()))
    else:
        logger.error('Wrong input: {}'.format(radius))
        print('Invalid input')

def other_shapes(): # Shows the user the range of functions the Mathematical Menu can do with other shapes
    print()
    print('The Mathematical Menu can perform tasks on different shapes: ')
    print('-> Find the volume and surface area of a sphere')
    print('-> Find the volume and surface area of a cylinder')
    print('-> Find the volume and surface area of a square-based pyramid')
    print('-> Find the interior and exterior angles of different 2D polygons')
    print('...or type -1 to exit this menu')
    print()
    finish = False
    while not finish:
        choice = int(input('Which shape method would you like to do (1/2/3/4)?: '))
        if choice == 1:
            handle_input_for_sphere()
        elif choice == 2:
            handle_inputs_for_cylinder()
        elif choice == 3:
            handle_inputs_for_pyramid()
        elif choice == 4:
            handle_inputs_for_interior_and_exterior_angles()
        elif choice == -1:
            finish = True
        else:
            logger.info('Wrong input: {}'.format(choice))
            print('Please enter 1,2,3 or 4, or enter -1 to exit')

def handle_input_for_sphere():
    radius = input('Enter radius of sphere: ')
    sphere(radius)

def sphere(radius): # Prints the volume and surface area
    if radius.isdigit(): # Validation
        radius = int(radius)
        volume = (4/3) * pi * radius ** 3
        surface_area = 4 * pi * radius ** 2
        print('The volume of the sphere is {:.2f} and the surface area is {:.2f}'.format(volume, surface_area))
    else:
        logger.error('Wrong input: {}'.format(radius))
        print('Invalid input')

def handle_inputs_for_cylinder():
    radius = input('Enter the radius of the base of the cylinder: ')
    height = input('Enter the height of the cylinder: ')
    cylinder(radius, height)

def cylinder(radius, height): # Prints the volume and surface area
    if radius.isdigit() and height.isdigit(): # Validation
        radius = int(radius)
        height = int(height)
        volume = pi * (radius ** 2) * height
        surface_area = 2 * pi * radius * (height + radius)
        print('The volume of the cylinder is {:.2f} and the surface area is {:.2f}'.format(volume, surface_area))
    else:
        logger.error('Wrong input: {}, {}'.format(radius, height))
        print('Invalid input')

def handle_inputs_for_pyramid():
    base = input('Enter the base length of the pyramid: ')
    side = input('Enter the slanted side length of the pyramid: ')
    height = input('Enter the height of the pyramid: ')
    pyramid(base, side, height)

def pyramid(base, side, height): # Prints the volume and surface area
    if base.isdigit() and side.isdigit() and height.isdigit(): # Validation
        base = int(base)
        side = int(side)
        height = int(height)
        volume = (1/3) * (base ** 2) * height
        surface_area = (base ** 2) + ((1/2) * base * 4 * side)
        print('The volume of the pyramid is {:.2f} and the surface area is {:.2f}'.format(volume, surface_area))
    else:
        logger.error('Wrong input: {}, {}, {}'.format(base, side, height))
        print('Invalid input')

def handle_inputs_for_interior_and_exterior_angles():
    sides = input('Enter the number of sides the polygon has: ')
    interior_and_exterior_angles(sides)

def interior_and_exterior_angles(sides): # Prints the interior and exterior angles and the total of interior angles
    if sides.isdigit(): # Validation
        sides = int(sides)
        interior_angle_total = 180 * (sides - 2)
        interior_angle = interior_angle_total / sides
        exterior_angle = 180 - interior_angle
        print('The total value of all the interior angles is {} degrees, each interior angle is {} degrees and the exterior angle is {} degrees'.format(interior_angle_total, interior_angle, exterior_angle))
    else:
        logger.error('Wrong input: {}'.format(sides))
        print('Invalid input')

def plot_graph(): # Plots a graph given a set of x and y coordinates
    x_cords = input('Enter list of x-coordinates, separated by commas: ').split(',')
    for i in range(len(x_cords)):
        if x_cords[i].isdigit(): # Validation
            continue
        else:
            return print('Invalid input')

    y_cords = input('Enter list of y-coordinates, separated by commas: ').split(',')
    for i in range(len(y_cords)):
        if y_cords[i].isdigit(): # Validation
            continue
        else:
            return print('Invalid input')

    if len(x_cords) != len(y_cords): # Validation
        return print('Lengths are not equal')
    else:
        pass

    x_label = input('Enter x-axis label: ')
    y_label = input('Enter y-axis label: ')
    title = input('Enter title of graph: ')
    x_points = []
    y_points = []

    for cord in x_cords:
        cord = float(cord)
        x_points.append(cord)

    for cord in y_cords:
        cord = float(cord)
        y_points.append(cord)

    x_points = np.array(x_points)
    y_points = np.array(y_points)

    # Gives the graph a title and labels on each axis
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Plots the points
    plt.plot(x_points, y_points)

    # Shows the graph
    plt.show()

    best = input('Would you like a line of best fit (Y/N)?: ').upper()
    if best.startswith('Y'):
        make_line_of_best_fit(x_points, y_points, title, x_label, y_label)
    else:
        pass

def make_line_of_best_fit(pXPoints, pYPoints, pTitle, pXLabel, pYLabel): # Creates a line of best fit
    a, b = np.polyfit(pXPoints, pYPoints, 1)

    plt.title(pTitle)
    plt.xlabel(pXLabel)
    plt.ylabel(pYLabel)
    plt.plot(pXPoints, pYPoints, 'o')
    plt.plot(pXPoints, a * pXPoints + b, color = 'black', linestyle = '--', linewidth = '2')

    plt.show()

def create_quadratic_graph(a, b, c, result_1, result_2): # Provides the details for a quadratic graph
    y_intercept = c

    temp = a
    a = a / temp
    b = b / temp
    c = c / temp

    # Completes the square
    min_max_point_x = (b / 2) * -1
    min_max_point_y = temp * (c - ((b / 2) ** 2))

    return f'The y-intercept is {y_intercept}\nThe x-intercepts are {result_1} and {result_2}, which are the solutions to the quadratic equation\nThe min/max point is ({min_max_point_x}, {min_max_point_y})'

def other_graph_methods(): # Shows the user the different graph methods the Menu can do
    finish = False
    while not finish:
        print()
        print('The Mathematical Menu can perform a number of graph methods: ')
        print('-> Obtaining the equation given two points')
        print('-> Finding the midpoint given two points')
        print('-> Finding the point between two points given a ratio')
        print('-> Finding the distance between two points')
        print('...or type -1 to exit this menu')
        print()
        choice = input('Which graph method would you like to do (1/2/3/4): ')
        if choice == '1':
            handle_inputs_for_lines(choice)
        elif choice == '2':
            handle_inputs_for_lines(choice)
        elif choice == '3':
            handle_inputs_for_lines(choice)
        elif choice == '4':
            handle_inputs_for_lines(choice)
        elif choice == '-1':
            finish = True
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input')
    print('You have chosen to exit the graph methods menu')

def handle_inputs_for_lines(choice):
    x1 = input('Enter coordinate x1: ')
    y1 = input('Enter coordinate y1: ')
    x2 = input('Enter coordinate x2: ')
    y2 = input('Enter coordinate y2: ')
    if choice == '1':
        find_line_equation(x1, y1, x2, y2)
    elif choice == '2':
        find_midpoint(x1, y1, x2, y2)
    elif choice == '3':
        p = input('Enter the left side of the ratio: ')
        q = input('Enter the right side of the ratio: ')
        find_point_with_ratio(x1, y1, x2, y2, p, q)
    elif choice == '4':
        find_distance(x1, y1, x2, y2)

def find_line_equation(x1, y1, x2, y2): # Finds the equation of a line
    cords = [x1, y1, x2, y2]
    cords = [int(num) for num in cords if ('-' in num and num[1:].isdigit()) or num.isdigit()]
    if len(cords) == 4: # Validation
        gradient = (cords[3] - cords[1]) / (cords[2] - cords[0])
        y_intercept = cords[1] - (gradient * cords[0])
        print('The gradient of the line is {:.1f} and the y-intercept is {:.1f}'.format(gradient, y_intercept))
    else:
        logger.error('Wrong input: ({}, {}), ({}, {})'.format(x1, y1, x2, y2))
        print('Invalid input')

def find_midpoint(x1, y1, x2, y2): # Finds the midpoint between two points
    cords = [x1, y1, x2, y2]
    cords = [int(num) for num in cords if ('-' in num and num[1:].isdigit()) or num.isdigit()]
    if len(cords) == 4: # Validation
        x_coordinate = (cords[0] + cords[2]) / 2
        y_coordinate = (cords[1] + cords[3]) / 2
        print('The coordinates of the midpoint of the line are ({:.1f}, {:.1f})'.format(x_coordinate, y_coordinate))
    else:
        logger.error('Wrong input: ({}, {}), ({}, {})'.format(x1, y1, x2, y2))
        print('Invalid input')

def find_point_with_ratio(x1, y1, x2, y2, p, q): # Finds the point between two points given a ratio
    cords_and_ratio = [x1, y1, x2, y2, p, q]
    cords_and_ratio = [int(num) for num in cords_and_ratio if ('-' in num and num[1:].isdigit()) or num.isdigit()]
    if len(cords_and_ratio) == 6: # Validation
        x_coordinate = (cords_and_ratio[-1] * cords_and_ratio[0] + cords_and_ratio[-2] * cords_and_ratio[2]) / (cords_and_ratio[-2] + cords_and_ratio[-1])
        y_coordinate = (cords_and_ratio[-1] * cords_and_ratio[1] + cords_and_ratio[-2] * cords_and_ratio[3]) / (cords_and_ratio[-2] + cords_and_ratio[-1])
        print('The point between point A and point B given the ratio {}:{} is ({:.1f}, {:.1f})'.format(p, q, x_coordinate, y_coordinate))
    else:
        logger.error('Wrong input: ({}, {}), ({}, {}), {}:{}'.format(x1, y1, x2, y2, p, q))
        print('Invalid input')

def find_distance(x1, y1, x2, y2): # Finds the distance between two points
    cords = [x1, y1, x2, y2]
    cords = [int(num) for num in cords if ('-' in num and num[1:].isdigit()) or num.isdigit()]
    if len(cords) == 4: # Validation
        distance = sqrt((cords[2] - cords[0]) ** 2 + (cords[3] - cords[1]) ** 2)
        print('The distance between point A and point B is {:.2f}'.format(distance))
    else:
        logger.error('Wrong input: ({}, {}), ({}, {})'.format(x1, y1, x2, y2))
        print('Invalid input')

def handle_inputs_for_calculus(choice: str):
    exp = input('Enter expression: ')
    respect = input('Enter variable to apply function with respect to: ')
    if respect.isalpha():
        if choice[0] == 'D':
            print(differentiate(exp, respect))
        elif choice[0] == 'I':
            print(integrate(exp, respect))
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input')
    else:
        logger.error(f'Wrong input: {respect}')
        print('Invalid input')

def handle_inputs_for_converter():
    finish = False
    while not finish:
        print()
        print('The Mathematical Menu can perform a number of conversions:')
        print('-> Distance conversions (mi / km)')
        print('-> Fluid conversions (ml / floz / pt (pints) / gl (gallons))')
        print('-> Mass conversions (kg / lb / oz / st (stone))')
        print('-> Temperature conversions (oF / oC')
        print('...or enter X to exit this menu')
        print()
        print("PLEASE NOTE: SOME ANSWERS MAY BE INCORRECT. Due to python's method of truncation instead of rounding, some conversions may result in an incorrect answer.")
        print('The Mathematical Menu highly recommends to check your answers on the internet or calculator.')
        print()
        choice: str = input('Enter your choice (D / F / M / T): ').upper()
        if choice == 'D':
            exp: str = input('Enter distance in km or mi: ')
            val: str = exp[:-2]
            unit: str = exp[-2:]
            result: str = distance_conversions(val, unit)
            if result != '-1':
                print(f'{val}{unit} = {result}')
            else:
                print('You may have provided invalid input')
        elif choice == 'F':
            exp: str = input('Enter volume in ml / floz / pt (pints) / gl (gallons): ')
            if 'floz' in exp:
                val: str = exp[:-4]
                unit: str = exp[-4:]
            else:
                val: str = exp[:-2]
                unit: str = exp[-2:]
            result: str = fluid_conversions(val, unit)
            if result != '-1':
                print(f'{val}{unit} ={result}')
            else:
                print('You may have provided invalid input')
        elif choice == 'M':
            exp: str = input('Enter mass in kg or lb or oz or st (stone): ')
            val: str = exp[:-2]
            unit: str = exp[-2:]
            result: str = mass_conversions(val, unit)
            if result != '-1':
                print(f'{val}{unit} = {result}')
            else:
                logger.error(f'Wrong input: {val}, {unit}')
                print('You may have provided invalid input')
        elif choice == 'T':
            exp: str = input('Enter temperature in oC or oF: ')
            val: str = exp[:-2]
            unit: str = exp[-2:]
            result: str = temperature_conversions(val, unit)
            if result != 'Invalid input':
                print(f'{val} {unit} = {result}')
            else:
                logger.error(f'Wrong input: {val}, {unit}')
                print('You may have provided invalid input')
        elif choice == 'X':
            finish = True
        else:
            logger.error(f'Wrong input: {choice}')
            print('Invalid input')
    print('You have chosen to exit the conversions menu')

def distance_conversions(val: str, unit: str) -> str:
    if (unit == 'mi' or unit == 'km') and val.isdigit():
        val = int(val)
        if unit == 'mi':
            return f'{(val * 8) / 5:.2f} km'
        else:
            return f'{(val * 5) / 8:.2f} miles'
    else:
        return '-1'

def fluid_conversions(val: str, unit: str) -> str:
    if (unit == 'ml' or unit == 'floz' or unit == 'pt' or unit == 'gl') and val.isdigit():
        val = int(val)
        if unit == 'ml':
            return f'\n{val * 0.035195:.3f} fl oz\n{val * 0.00175975:.3f} pints\n{(val * 0.00175975) / 8:.3f} gallons\n'
        elif unit == 'floz':
            return f'\n{val * 28.4131:.3f} ml\n{val * 0.05:.3f} pints\n{(val * 0.05) / 8:.3f} gallons\n'
        elif unit == 'pt':
            return f'\n{val * 568.26:.3f} ml\n{val * 20:.3f} fl oz\n{val / 8:.3f} gallons\n'
        elif unit == 'gl':
            return f'\n{(val * 8) * 568.26:.3f} ml\n{(val * 8) * 20:.3f} fl oz\n{val * 8:.3f} pints\n'
    else:
        return '-1'

def mass_conversions(val: str, unit: str) -> str:
    if (unit == 'kg' or unit == 'lb' or unit == 'oz' or unit == 'st') and val.isdigit():
        val = int(val)
        if unit == 'kg':
            return f'\n{val * 2.204623:.3f} lb\n{val * 35.27396:.3f} oz\n{val * 0.157473:.3f} stone\n'
        elif unit == 'lb':
            return f'\n{val * 0.4535924:.3f} kg\n{val * 16:.3f} oz\n{val * 0.07142857:.3f} stone\n'
        elif unit == 'oz':
            return f'\n{val * 0.02834952:.3f} kg\n{val * 0.0625:.3f} lb\n{val * 0.004464286:.3f} stone\n'
        elif unit == 'st':
            return f'\n{val * 6.350293:.3f} kg\n{val * 14:.3f} lb\n{val * 224:.3f} oz\n'
    else:
        logger.error(f'Wrong input: {val}, {unit}')
        return '-1'

def temperature_conversions(val: str, unit: str) -> str:
    if (unit == 'oF' or unit == 'oC') and (val.isdigit() or ('-' in val and val[1:].isdigit())):
        val = int(val)
        if unit == 'oF':
            result = ((val - 32) * 5) / 9
            return f'{result} oC'
        elif unit == 'oC':
            result = ((val * 9) / 5) + 32
            return f'{result} oF'
    else:
        logger.error(f'Wrong input: {val} {unit}')
        return 'Invalid input'

################
# MAIN PROGRAM #
################

if __name__ == '__main__':
    logger.info('Starting program')
    # Acquires tests from external file
    doctest.testfile('mathematical.menu.tests.txt')
    menus.mathematical_menu()