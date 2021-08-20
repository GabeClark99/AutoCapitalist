
from numpy import true_divide
import screenstuff as ss


# ----------------------------------------
# Global Variables
# ----------------------------------------
time_multiplier_global = 1.0            # this is halved when all businesses reach a time milestone
increment_max_cord = (1630, 140)        # location of the increment button, well as the pixel that is white only when MAX is selected
increment_max_color_enabled = (240, 233, 226)
popupcheck_cord = (1042, 671)              # used to check this location and its color to determine if there is a popup on the screen
popupcheck_color_nopopup = (115, 105, 96)           # control color used to check if there is a popup
popup_hot_cord_exit = (1321, 180)
popup_insider_cord_exit = (1260, 290)
popup_moon_cord_exit = (1312, 295)

# ----------------------------------------
# Classes
# ----------------------------------------
class Business:
    # revenue_current: can get through OCR on business, or find multiplier through OCR on upgrades
    # time_multiplier: global multiplier (through OCR) on all businesses multiplied by business multiplier (through self.count)

    # constructor
    def __init__(self, name, cord_buy, cord_run, cost_initial, cost_multiplier, time_initial, revenue_initial, count_bbox):
        self.name = name
        self.cord_buy = cord_buy
        self.cord_run = cord_run
        self.cost_initial = cost_initial        # the cost for the first count
        self.cost_multipler = cost_multiplier   # what will be multiplied with the current price to get the price of the next count
        self.time_intial = time_initial         # initial time it takes to complete a cycle and receive money
        self.revenue_initial = revenue_initial  # intial amount of money gained at the end of a cycle
        self.count_bbox = count_bbox            # area that countains the visual count data

        self.revenue_current = revenue_initial  # revenue_current = count * revenue_initial

        self.color_running = (76, 102, 115)
        self.color_idle = (115, 149, 167)
        self.count = 0              # how many of this business there is
        self.time_multiplier = 1.0  # current multiplier on time_initial to reduce cycle time

class Menu:
    # constructor
    def __init__(self, cord_open, cord_buy, cord_submenu, cord_confirm_yes, cord_confirm_no, cord_exit, 
    color_open_on, color_open_off, color_buy_on, color_buy_off, color_confirm_yes, color_confirm_no):
        self.cord_open = cord_open
        self.cord_buy = cord_buy
        self.cord_submenu = cord_submenu
        self.cord_confirm_yes = cord_confirm_yes
        self.cord_confirm_no = cord_confirm_no
        self.cord_exit = cord_exit

        self.color_open_on = color_open_on
        self.color_open_off = color_open_off
        self.color_buy_on = color_buy_on
        self.color_buy_off = color_buy_off
        self.color_confirm_yes = color_confirm_yes
        self.color_confirm_no = color_confirm_no

# ----------------------------------------
# Global Objects
# ----------------------------------------
lemonaide = Business ("lemonaide",  (716, 380), (544, 284),   3.738,          1.07,   0.6,    1,              (499, 357, 587, 393))
newspaper = Business ("newspaper",  (716, 510), (541, 422),   60,             1.15,   3,      60,             (499, 491, 587, 525))
car =       Business ("car",        (716, 640), (538, 551),   720,            1.14,   6,      540,            (499, 623, 587, 657))
pizza =     Business ("pizza",      (716, 780), (538, 684),   8640,           1.13,   12,     4320,           (499, 755, 587, 789))
donut =     Business ("donut",      (716, 910), (542, 821),   103680,         1.12,   24,     51840,          (499, 892, 587, 926))
shrimp =    Business ("shrimp",     (1301, 380), (1129, 291), 1244160,        1.11,   96,     622080,         (1074, 357, 1161, 393))
hockey =    Business ("hockey",     (1301, 510), (1113, 419), 14929920,       1.10,   384,    7464960,        (1074, 491, 1161, 525))
movie =     Business ("movie",      (1301, 640), (1114, 548), 179159040,      1.09,   1536,   89579520,       (1074, 623, 1161, 657))
bank =      Business ("bank",       (1301, 775), (1114, 682), 2149908480,     1.08,   6144,   1074954240,     (1074, 755, 1161, 789))
oil =       Business ("oil",        (1301, 910), (1114, 820), 25798901760,    1.07,   36864,  296668737024,   (1074, 892, 1161, 926)) 

businessList = [lemonaide, newspaper, car, pizza, donut, shrimp, hockey, movie, bank, oil]



upgrades = Menu ((212, 536),    (778, 641),     (952, 333),       (-1, -1),   (-1, -1),       (1660, 180), 
(220, 124, 47),     (116, 106, 98),     (241, 140, 76),     (171, 171, 171),    (-1, -1, -1),   (-1, -1, -1))

managers = Menu ((212, 621),    (776, 648),     (1030, 320),    (680, 620), (678, 612),    (1650, 180), 
(220, 124, 47),     (116, 106, 98),     (143, 188, 211),    (171, 171, 171),    (-1, -1, -1),   (224, 100, 100))

investors = Menu ((212, 704),   (1524, 665),    (-1, -1),       (767, 735), (-1, -1),       (-1, -1), 
(220, 124, 47),     (-1, -1, -1),       (164, 112, 149),    (164, 112, 149),    (-1, -1, -1),   (-1, -1, -1)) # very unfinished, add coordinates and colors

# ----------------------------------------
# Global Functions
# ----------------------------------------
def setBusinessesCount():
    # # lemonaide
    # bbox = gd.lemonaide.count_bbox
    # count_str = ss.bboxToText(bbox)
    # gd.lemonaide.count = int(count_str)
    # # print(gd.lemonaide.count)             #

    for cur_business in businessList:
        bbox = cur_business.count_bbox
        count_str = ss.bboxToText(bbox)
        cur_business.count = int(count_str)
        print(cur_business.count)           #-------------DEBUGGING

def setTimeMultipliers():
    # calculate and set business.time_multiplier and time_multiplier_global
    # time_multiplier_global is halved when all business reach a count of 25, 50, 100, 200, 300, and 400
    global time_multiplier_global
    
    milestone = 0
    while milestone < 400:
        if milestone == 0 or milestone == 25:
            milestone = milestone + 25
        elif milestone == 50:
            milestone = 100  # new milestone is 100
        elif milestone > 50:    # if milestone is 100, 200, or 300...
            milestone = milestone + 100

        # print('current milestone to check: ' + str(milestone))          #

        globalMilestone = True          # keeps track of if all businesses have reached the milestone

        for cur_business in businessList:
            # print('-current business: ' + cur_business.name)            #

            if cur_business.count >= milestone:
                # print('--has met the milestone!')                      #
                # print('--current time_multiplier: ' + str(cur_business.time_multiplier))                #
                cur_business.time_multiplier = cur_business.time_multiplier / 2     # half the current time multiplier
                # print('--new time_multiplier: ' + str(cur_business.time_multiplier))                    #
            else:   # if this business has not reached this milestone...
                # print('--has NOT met the milestone!')                      #
                globalMilestone = False     # flag that not all businesses have reached this milestone

        if globalMilestone == True:         # if all businesses have reached this milestone...
            print ('all businesses met the milstone!')
            time_multiplier_global = time_multiplier_global / 2     # half the current global time multiplier
    # local multiplers have been set and global multipler is ready to be applied

    # print('time_multiplier_global: ' + str(time_multiplier_global))              #

    for cur_business in businessList:
        # print('current business: ' + cur_business.name)             #
        # print('-current time_multiplier: ' + str(cur_business.time_multiplier))         #
        cur_business.time_multiplier = cur_business.time_multiplier * time_multiplier_global
        # print('-new time_multiplier: ' + str(cur_business.time_multiplier))                 #

