#-*- encoding: utf-8 -*-

from random import randint
from collections import OrderedDict
import subprocess as sp


cards = {
    1: "Ace",
    11: "J",
    12: "Q",
    13: "K"
}


suits = [
    "♠",
    "♥",
    "♦",
    "♣"
]


main_menu = OrderedDict()
main_menu["1"] = ("Pick a card", "get_card")
main_menu["2"] = ("Pick a card from suit", "get_suit_menu")
main_menu["3"] = ("Roll die (1d4)", "roll_die")
main_menu["4"] = ("Toss coin (1d2)", "toss_coin")
main_menu["5"] = ("Resources", "set_stock_resources")
main_menu["6"] = ("Treasury", "set_stock_treasury")
main_menu["7"] = ("Soldiers", "set_stock_soldiers")


# Initial values
stocks = {
	"treasury": 20,
	"resources": 20,
	"soldiers": 20
}


def clear_screen():
    sp.call('clear',shell=True)


def print_exit():
    print_pre_result()
    print("    Q. Quit game")
    

def print_pre_result():
	print("    ------------")


def print_press_enter():
    print("    Press Enter to continue...")
    raw_input("    ")


def get_card(suit=False):
    value = randint(1, 13)
    suit = randint(0, 3) if not suit else suit
    print_pre_result()
    print("    %s%s" % (
        cards.get(value, value),
        suits[suit]
    ))
    print_press_enter()


def get_main_menu():
    return "\n".join([("    %s. %s" % (item, main_menu[item][0])) for item in main_menu])


def get_suit_menu():
    menu = 0
    clear_screen()
    while menu != "Q":
        print("\n".join(["    %s. %s" % (key, value) for key, value in enumerate(suits)]))
        print_exit()
        menu = str(raw_input("    Option: "))
        get_card(int(menu))
        menu = "Q"


def set_stock_resources():
    set_stock_dialog("resources")


def set_stock_treasury():
    set_stock_dialog("treasury")


def set_stock_soldier():
    set_stock_dialog("soldiers")


def set_stock_dialog(resource):
    print_pre_result()
    value = raw_input("    Modify %s stock by: " % resource)
    set_stock(resource, value)
    print_press_enter()
	

def get_stock():
    return """
    ----------------
    - STOCKS
    ----------------
    - Resources: %s
    - Treasury: %s
    - Soldiers: %s
    ----------------
    """ % (
    	stocks["resources"],
    	stocks["treasury"],
    	stocks["soldiers"]
    )


def read_main_menu_response(response):
    eval("%s()" % main_menu[response][1])
    

def set_stock(stock_type, value):
	stocks[stock_type] = stocks[stock_type] + eval(value)
	
	
def roll_die():
	print_pre_result()
	print("    %s" % randint(1,4))
	print_press_enter()
	

def toss_coin():
    print_pre_result()
    print("%s" % "    Head" if randint(1,2) == 1 else "    Tail")
    print_press_enter()
	

if __name__ == "__main__":
    menu = 0
    while menu != "Q":
    	clear_screen()
    	print("    ###########################")
    	print("    # Welcome to DELVE!")
    	print("    ###########################")
    	print(get_stock())
        print(get_main_menu())
        print_exit()
        print("\n")
        menu = str(raw_input("    Option: "))
        if menu != "Q":
        	read_main_menu_response(menu)
