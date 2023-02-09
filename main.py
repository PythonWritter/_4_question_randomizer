import random
import time
import sys

import json
#import keyboard

def main_menu():
    """ Visual side of 'Main menu.' """
    selector = None
    try:
        selector = int(input('_' * 58 + '\n' + \
                             '|__________________________Menu__________________________|\n' + \
                             'Enter "1" if you want to watch all questions and answers\n' + \
                             'Enter "2" if you want to start random question\n' + \
                             'Enter "3" if you want to add new question and answer\n' + \
                             'Enter "4" save and exit\n' + \
                             '*' * 58 + '\n' + \
                             '\nMake your choice -->: '))
        if selector == 1:
            p_1()
        elif selector == 2:
            p_2()
        elif selector == 3:
            p_3()
        elif selector == 4:
            p_4()
    except ValueError:
        print('Incorrect contribution!')
        print('You must enter an integer!')
        time.sleep(1.5)
        main_menu()
    return selector

def p_1():
    """ Menu p. № 1 'Watch all questions and answers'. """
    selector = None
    with open(f'questions.json', 'r') as f:
        quest = json.loads(str(f.read()))

    questions = quest.keys()
    list_quest = list(questions)
    list_quest = str(list_quest)
    time.sleep(1)
    for i in questions:
        i = str(i)
        time.sleep(0.1)
        list_quest = list_quest.replace('(', '')
        list_quest = list_quest.replace(')', '')
        list_quest = list_quest.replace('\'', '')
        list_quest = list_quest.replace(',', '-->')
        print(i)


    try:
        time.sleep(0.5)
        selector = int(input('\n' + '_' * 52 + '\n' + \
                             'If you want  to watch answer --> Press [1] \n' + \
                             'If you want to go back to "Main menu" --> Press [2] \n' + \
                             'If you want to exit --> Press [3] \n' + \
                             '*' * 52 + '\n' + \
                             '\nMake your choice -->: '))
        if selector == 1:
            for key, value in quest.items():
                print(key)
                print(value)
            return_end()
        elif selector == 2:
            main_menu()
        elif selector == 3:
            print('Key "3" has been pressed. ')
            print('The program will be closed. ')
            time.sleep(1)
            sys.exit()
    except ValueError:
        print('Incorrect contribution!')
        print('You must enter an integer!')
        p_1()
    return selector

def p_2():
    """ Menu p. № 2 'Random question'. """
    selector = None
    with open(f'questions.json', 'r') as f:
        quest = json.loads(str(f.read()))

    dict_items = quest.items()
    list_items = list(dict_items)

    try:
        print('Enter 1, or press "ENTER": ')
        while True:
            selector = input()
            if selector == '1' or keyboard.is_pressed('enter') == True:
                rand = random.choice(list_items)
                id_list = list_items.index(rand)
                del list_items[id_list]

                one_item_list = list(rand)
                print(one_item_list[0])
                selector_2 = input('Press Enter: ')
                if selector_2 == '1' or keyboard.is_pressed('enter') == True:
                    print(one_item_list[1])
    except ValueError:
        print('Incorrect contribution!')
        print('You must enter an integer!')
        p_2()
    except IndexError:
        print('Questions have been finished!')
        print('Congratulations!')
        return_end()
    return selector

def p_3():
    """ Menu p. № 3 'Add new question and answer'. """
    with open('questions.json', 'r') as f:
        quest = json.loads(str(f.read()))

    dict_items = quest.items()
    list_items = list(dict_items)
    print(list_items)
    question = input('Enter your question: ')
    answer = input('Ente the answer: ')
    list_items.append(tuple([question, answer]))
    dict_items = dict(list_items)

    with open('questions.json', 'w') as f:
        f.write(json.dumps(dict_items, indent=2))

    print('\nQuestion has been saved.')
    return_end()

def p_4():
    """ Menu p. № 4 'Save and exit'. """
    print('The program will be saved and closed')
    time.sleep(1)
    sys.exit()

def return_end():
    """ Return, or finish the program. """
    selector = None
    try:
        selector = int(input('\n' + '_' * 52 + '\n' + \
                                 'If you want to go back to "Main menu" --> Press [1] \n' + \
                                 'If tou want to save and close the program --> Press [2] \n' + \
                                 '*' * 52 + '\n' + \
                                 '\nMake your choice -->: '))
        if selector == 1:
            main_menu()
        elif selector == 2:
            print('Key "2" has been pressed. ')
            print('The program will be closed. ')
            time.sleep(1)
            sys.exit()
        else:
            pass
    except ValueError:
        print('Incorrect contribution!')
        print('You must enter an integer!')
        return_end()
    return selector

main_menu()
