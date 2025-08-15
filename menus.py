import mathematicalMenu as mm
import authentication as auth
import logging
import doctest
logger = logging.getLogger(__name__)

def main_menu(): # The first UI that the user sees
    print()
    print('Welcome to the Mathematical Menu!')
    print()
    print('In order to use the facilities, you will need to sign up, or login using an existing account. Select an option below.')
    print()
    print('L - Login')
    print('S - Signup')
    print('...or type X to exit')
    print()
    finish = False
    while not finish:
        choice = mm.get_menu_option()
        if choice == 'L':
            return 'l' # Triggers the login() subprogram
        elif choice == 'S':
            return 's' # Triggers the sign_up() subprogram
        elif choice == 'X':
            finish = True
            return 'x'
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input')
    print('See you later!')

def display_main_menu() -> None:
    print()
    print('MATHEMATICAL MENU')
    print('=================')
    print()
    print('Maths')
    print('-----')
    print('C - Calculus')
    print('E - Equations')
    print('G - Geometry')
    print('P - Graphs')
    print('O - Other helpful things')
    print('X - Exit Mathematical Menu')
    print()
    print('Computers')
    print('---------')
    print('A - Algorithms')
    print('D - Data Structures')
    print()

def display_calculus_menu() -> None:
    print()
    print('Calculus Menu')
    print('-------------')
    print('D - Differentiation')
    print('I - Integration')
    print('...or type X to exit this menu')
    print()

def display_algorithms_menu():
    print()
    print('Algorithms')
    print('---')
    print('C - Searching')
    print('T - Sorting')
    print('O - Other')
    print('...or type X to exit this menu')
    print()

def display_data_structures_menu():
    print()
    print('Data Structures')
    print('---------------')
    print('A - Array')
    print('L - Linked list')
    print('Q - Queue')
    print('S - Stack')
    print('...or type X to exit this menu')
    print()

def display_equations_menu() -> None:
    print()
    print('Equations')
    print('---------')
    print('Q - Quadratic')
    print('S - Simultaneous')
    print('...or type X to exit this menu')
    print()

def display_geometry_menu() -> None:
    print()
    print('Geometry Menu')
    print('-------------')
    print('C - Circles')
    print('O - Other shapes')
    print('T - Trigonometry')
    print('...or type X to exit this menu')
    print()

def display_graph_menu() -> None:
    print()
    print('Graph Menu')
    print('----------')
    print('P - Plot a graph')
    print('T - Other graph methods')
    print('...or type X to exit this menu')
    print()

def display_other_helpful_things_menu():
    print()
    print('Other helpful things')
    print('--------------------')
    print('C - Conversions')
    print('F - Formulae sheet')
    print('...or type X to exit this menu')
    print()

def calculus_menu(): # Asks the user to choose between differentiation and integration
    finish = False
    while not finish:
        display_calculus_menu()
        choice = mm.get_menu_option()
        if choice[0] == 'X':
            finish = True
        else:
            mm.handle_inputs_for_calculus(choice)
    print('You have chosen to exit the calculus menu')

def algorithms_menu():
    finished = False
    while not finished:
        display_algorithms_menu()
        choice = mm.get_menu_option()
        if choice[0] == 'C':
            mm.handle_inputs_for_searching()
        elif choice[0] == 'T':
            mm.handle_inputs_for_sorting()
        elif choice[0] == 'O':
            pass
        elif choice[0] == 'X':
            finished = True
        else:
            logger.error(f'Invalid input: {choice}')
            print('Invalid input')

def data_structures_menu():
    finished = False
    while not finished:
        display_data_structures_menu()
        choice = mm.get_menu_option()
        if choice[0] == 'A':
            pass
        elif choice[0] == 'L':
            pass
        elif choice[0] == 'Q':
            pass
        elif choice[0] == 'S':
            pass
        elif choice[0] == 'X':
            finished = True
        else:
            logger.error(f'Invalid input: {choice}')
            print('Invalid input')

def equations_menu(): # Asks the user to choose between quadratic and simultaneous equations
    finish = False
    while not finish:
        display_equations_menu()
        choice = mm.get_menu_option()
        if choice[0] == 'Q':
            equation = input('Enter a quadratic equation: ')
            print(mm.solve_quadratic(equation))
        elif choice[0] == 'S':
            print(mm.solve_simultaneous_equations())
        elif choice[0] == 'X':
            finish = True
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input')
    print('You have chosen to exit the equations menu')

def geometry_menu(): # Asks the user for geometry-related calculation
    finish = False
    while not finish:
        display_geometry_menu()
        choice = mm.get_menu_option()
        if choice[0] == 'C':
            mm.handle_inputs_for_circles()
        elif choice[0] == 'O':
            mm.other_shapes()
        elif choice[0] == 'T':
            mm.trig()
        elif choice[0] == 'X':
            finish = True
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input')
    print('You have chosen to exit the geometry menu')

def graph_menu(): # Asks the user for graph-related calculation
    finish = False
    while not finish:
        display_graph_menu()
        choice = mm.get_menu_option()
        if choice[0] == 'P':
            mm.plot_graph()
        elif choice[0] == 'T':
            mm.other_graph_methods()
        elif choice[0] == 'X':
            finish = True
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input')
    print('You have chosen to exit the graphs menu')

def other_helpful_things_menu():
    finish = False
    while not finish:
        display_other_helpful_things_menu()
        choice: str = mm.get_menu_option()
        if choice[0] == 'C':
            mm.handle_inputs_for_converter()
        elif choice[0] == 'F':
            mm.display_formulae()
        elif choice[0] == 'X':
            finish = True
        else:
            logger.error(f'Wrong input: {choice}')
            print('Invalid input')
    print('You have chosen to exit the helpful things menu')

def mathematical_menu(): # Main UI
    finish = False
    begin: str = input('Do you wish to be authenticated? (y/n): ')
    if begin.startswith('y'):
        thing = main_menu()
        if thing == 'l':
            result = auth.login()
            if not result:
                finish = True
        elif thing == 's':
            auth.sign_up()
        elif thing == 'x':
            finish = True
    while not finish:
        display_main_menu()
        choice = mm.get_menu_option()
        if choice == 'A':
            algorithms_menu()
        elif choice == 'C':
            calculus_menu()
        elif choice == 'D':
            data_structures_menu()
        elif choice == 'E':
            equations_menu()
        elif choice == 'G':
            geometry_menu()
        elif choice == 'P':
            graph_menu()
        elif choice == 'O':
            other_helpful_things_menu()
        elif choice == 'X':
            finish = True
        else:
            logger.error('Wrong input: {}'.format(choice))
            print('Invalid input. Please try again')
    logger.info('Closing Program')
    print('You have chosen to exit Mathematical Menu, or you have entered the wrong credentials')

if __name__ == '__main__':
    doctest.testfile('mathematical.menu.tests.txt')
    mathematical_menu()