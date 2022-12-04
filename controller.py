from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from mainwindowyahtzee import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

die_roll_list = []
yahtzee_bonus = 0
total_score_upper = 0
total_score_lower = 0
grand_total_score = 0
dice_rolls = 0
die_1 = 0
die_2 = 0
die_3 = 0
die_4 = 0
die_5 = 0
die_6 = 0
master_die_roll_list = {}
master_zeros_list = {}


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Function to set up the game app with the initial window, showing and hiding necessary widgets.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_roll_dice.clicked.connect(lambda: self.roll_dice())
        self.button_die_1.clicked.connect(lambda: self.save_die_1())
        self.button_die_1.setCheckable(True)
        self.button_die_2.clicked.connect(lambda: self.save_die_2())
        self.button_die_2.setCheckable(True)
        self.button_die_3.clicked.connect(lambda: self.save_die_3())
        self.button_die_3.setCheckable(True)
        self.button_die_4.clicked.connect(lambda: self.save_die_4())
        self.button_die_4.setCheckable(True)
        self.button_die_5.clicked.connect(lambda: self.save_die_5())
        self.button_die_5.setCheckable(True)
        self.button_aces.clicked.connect(lambda: self.aces_score())
        self.button_twos.clicked.connect(lambda: self.twos_score())
        self.button_threes.clicked.connect(lambda: self.threes_score())
        self.button_fours.clicked.connect(lambda: self.fours_score())
        self.button_fives.clicked.connect(lambda: self.fives_score())
        self.button_sixes.clicked.connect(lambda: self.sixes_score())
        self.button_3_of_a_kind.clicked.connect(lambda: self._3_of_a_kind_score())
        self.button_4_of_a_kind.clicked.connect(lambda: self._4_of_a_kind_score())
        self.button_full_house.clicked.connect(lambda: self.full_house_score())
        self.button_sm_straight.clicked.connect(lambda: self.sm_straight_score())
        self.button_lg_straight.clicked.connect(lambda: self.lg_straight_score())
        self.button_yahtzee.clicked.connect(lambda: self.yahtzee_score())
        self.button_chance.clicked.connect(lambda: self.chance_score())
        self.button_yahtzee_bonus.clicked.connect(lambda: self.yahtzee_bonus_score())
        self.button_choose_zero_score.clicked.connect(lambda: self.zero())
        self.button_new_game.clicked.connect(lambda: self.new_game())
        self.label_die_1.setStyleSheet("border :3px solid blue;"
                                        "border-radius : 13px")
        self.label_die_2.setStyleSheet("border :3px solid blue;"
                                        "border-radius : 13px")
        self.label_die_3.setStyleSheet("border :3px solid blue;"
                                        "border-radius : 13px")
        self.label_die_4.setStyleSheet("border :3px solid blue;"
                                        "border-radius : 13px")
        self.label_die_5.setStyleSheet("border :3px solid blue;"
                                        "border-radius : 13px")
        self.label_keep_die_1.setStyleSheet("border :3px solid red;"
                                        "border-radius : 13px")
        self.label_keep_die_2.setStyleSheet("border :3px solid red;"
                                        "border-radius : 13px")
        self.label_keep_die_3.setStyleSheet("border :3px solid red;"
                                        "border-radius : 13px")
        self.label_keep_die_4.setStyleSheet("border :3px solid red;"
                                        "border-radius : 13px")
        self.label_keep_die_5.setStyleSheet("border :3px solid red;"
                                        "border-radius : 13px")

        self.label_score_aces.hide()
        self.label_score_twos.hide()
        self.label_score_threes.hide()
        self.label_score_fours.hide()
        self.label_score_fives.hide()
        self.label_score_sixes.hide()
        self.label_score_3_of_a_kind.hide()
        self.label_score_4_of_a_kind.hide()
        self.label_score_full_house.hide()
        self.label_score_sm_straight.hide()
        self.label_score_lg_straight.hide()
        self.label_score_yahtzee.hide()
        self.label_score_chance.hide()
        self.label_score_yahtzee_bonus.hide()
        self.label_keep_die_1.hide()
        self.label_keep_die_2.hide()
        self.label_keep_die_3.hide()
        self.label_keep_die_4.hide()
        self.label_keep_die_5.hide()
        self.label_warning.show()
        self.label_warning.setText('Good\nLuck!\nRoll\nthe\nDice')

    def roll_dice(self):
        """
        Function to perform a dice roll with 5 dice; it also counts how many dice rolls there have been
        so that the user cannot roll more than 3 times per turn. This function also assigns a picture of
        a die to the label in the GUI.
        """
        global dice_rolls
        global die_1
        global die_2
        global die_3
        global die_4
        global die_5

        dice_rolls += 1
        self.label_warning.show()
        self.label_warning.setText('Choose\nwhich\ndice to\nkeep\nand roll\nagain')
        global die_roll_list

        if dice_rolls <= 3:
            die_roll_list = []
            for i in range(5):
                die_roll = random.randrange(1, 7)
                die_roll = str(die_roll)
                die_roll_list.append(die_roll)
            die_1 = die_roll_list[0]
            die_2 = die_roll_list[1]
            die_3 = die_roll_list[2]
            die_4 = die_roll_list[3]
            die_5 = die_roll_list[4]
        else:
            self.label_warning.setText('Out of\nrolls -\nChoose\nscore\nbutton')

        image1 = QPixmap('Single-Die-with-1-Showing.png')
        image2 = QPixmap('Single-Die-with-2-Showing.png')
        image3 = QPixmap('Single-Die-with-3-Showing.png')
        image4 = QPixmap('Single-Die-with-4-Showing.png')
        image5 = QPixmap('Single-Die-with-5-Showing.png')
        image6 = QPixmap('Single-Die-with-6-Showing.png')

        if die_1 == '1':
            self.label_die_1.setPixmap(image1)
        elif die_1 == '2':
            self.label_die_1.setPixmap(image2)
        elif die_1 == '3':
            self.label_die_1.setPixmap(image3)
        elif die_1 == '4':
            self.label_die_1.setPixmap(image4)
        elif die_1 == '5':
            self.label_die_1.setPixmap(image5)
        else:
            self.label_die_1.setPixmap(image6)

        if die_2 == '1':
            self.label_die_2.setPixmap(image1)
        elif die_2 == '2':
            self.label_die_2.setPixmap(image2)
        elif die_2 == '3':
            self.label_die_2.setPixmap(image3)
        elif die_2 == '4':
            self.label_die_2.setPixmap(image4)
        elif die_2 == '5':
            self.label_die_2.setPixmap(image5)
        else:
            self.label_die_2.setPixmap(image6)

        if die_3 == '1':
            self.label_die_3.setPixmap(image1)
        elif die_3 == '2':
            self.label_die_3.setPixmap(image2)
        elif die_3 == '3':
            self.label_die_3.setPixmap(image3)
        elif die_3 == '4':
            self.label_die_3.setPixmap(image4)
        elif die_3 == '5':
            self.label_die_3.setPixmap(image5)
        else:
            self.label_die_3.setPixmap(image6)

        if die_4 == '1':
            self.label_die_4.setPixmap(image1)
        elif die_4 == '2':
            self.label_die_4.setPixmap(image2)
        elif die_4 == '3':
            self.label_die_4.setPixmap(image3)
        elif die_4 == '4':
            self.label_die_4.setPixmap(image4)
        elif die_4 == '5':
            self.label_die_4.setPixmap(image5)
        else:
            self.label_die_4.setPixmap(image6)

        if die_5 == '1':
            self.label_die_5.setPixmap(image1)
        elif die_5 == '2':
            self.label_die_5.setPixmap(image2)
        elif die_5 == '3':
            self.label_die_5.setPixmap(image3)
        elif die_5 == '4':
            self.label_die_5.setPixmap(image4)
        elif die_5 == '5':
            self.label_die_5.setPixmap(image5)
        else:
            self.label_die_5.setPixmap(image6)

    def save_die_1(self):
        """
        Function to keep the roll for Die 1 and not re-roll it.
        """
        image1 = QPixmap('Single-Die-with-1-Showing.png')
        image2 = QPixmap('Single-Die-with-2-Showing.png')
        image3 = QPixmap('Single-Die-with-3-Showing.png')
        image4 = QPixmap('Single-Die-with-4-Showing.png')
        image5 = QPixmap('Single-Die-with-5-Showing.png')
        image6 = QPixmap('Single-Die-with-6-Showing.png')

        global master_die_roll_list

        if self.button_die_1.isChecked():
            self.button_die_1.setCheckable(False)
            if die_1 == '1':
                self.label_keep_die_1.show()
                self.label_keep_die_1.setPixmap(image1)
                self.label_die_1.hide()
            elif die_1 == '2':
                self.label_keep_die_1.show()
                self.label_keep_die_1.setPixmap(image2)
                self.label_die_1.hide()
            elif die_1 == '3':
                self.label_keep_die_1.show()
                self.label_keep_die_1.setPixmap(image3)
                self.label_die_1.hide()
            elif die_1 == '4':
                self.label_keep_die_1.show()
                self.label_keep_die_1.setPixmap(image4)
                self.label_die_1.hide()
            elif die_1 == '5':
                self.label_keep_die_1.show()
                self.label_keep_die_1.setPixmap(image5)
                self.label_die_1.hide()
            else:
                self.label_keep_die_1.show()
                self.label_keep_die_1.setPixmap(image6)
                self.label_die_1.hide()
            master_die_roll_list['1'] = die_1
        else:
            x = master_die_roll_list['1']
            if x == '1':
                x = QPixmap('Single-Die-with-1-Showing.png')
            if x == '2':
                x = QPixmap('Single-Die-with-2-Showing.png')
            if x == '3':
                x = QPixmap('Single-Die-with-3-Showing.png')
            if x == '4':
                x = QPixmap('Single-Die-with-4-Showing.png')
            if x == '5':
                x = QPixmap('Single-Die-with-5-Showing.png')
            if x == '6':
                x = QPixmap('Single-Die-with-6-Showing.png')

            self.label_keep_die_1.hide()
            self.label_die_1.show()
            self.label_die_1.setPixmap(x)

            self.button_die_1.setCheckable(True)
            master_die_roll_list.pop('1')

    def save_die_2(self):
        """
        Function to keep the roll for Die 2 and not re-roll it.
        """
        image1 = QPixmap('Single-Die-with-1-Showing.png')
        image2 = QPixmap('Single-Die-with-2-Showing.png')
        image3 = QPixmap('Single-Die-with-3-Showing.png')
        image4 = QPixmap('Single-Die-with-4-Showing.png')
        image5 = QPixmap('Single-Die-with-5-Showing.png')
        image6 = QPixmap('Single-Die-with-6-Showing.png')

        global master_die_roll_list

        if self.button_die_2.isChecked():
            self.button_die_2.setCheckable(False)
            if die_2 == '1':
                self.label_keep_die_2.show()
                self.label_keep_die_2.setPixmap(image1)
                self.label_die_2.hide()
            elif die_2 == '2':
                self.label_keep_die_2.show()
                self.label_keep_die_2.setPixmap(image2)
                self.label_die_2.hide()
            elif die_2 == '3':
                self.label_keep_die_2.show()
                self.label_keep_die_2.setPixmap(image3)
                self.label_die_2.hide()
            elif die_2 == '4':
                self.label_keep_die_2.show()
                self.label_keep_die_2.setPixmap(image4)
                self.label_die_2.hide()
            elif die_2 == '5':
                self.label_keep_die_2.show()
                self.label_keep_die_2.setPixmap(image5)
                self.label_die_2.hide()
            else:
                self.label_keep_die_2.show()
                self.label_keep_die_2.setPixmap(image6)
                self.label_die_2.hide()
            master_die_roll_list['2'] = die_2
        else:
            x = master_die_roll_list['2']
            if x == '1':
                x = QPixmap('Single-Die-with-1-Showing.png')
            if x == '2':
                x = QPixmap('Single-Die-with-2-Showing.png')
            if x == '3':
                x = QPixmap('Single-Die-with-3-Showing.png')
            if x == '4':
                x = QPixmap('Single-Die-with-4-Showing.png')
            if x == '5':
                x = QPixmap('Single-Die-with-5-Showing.png')
            if x == '6':
                x = QPixmap('Single-Die-with-6-Showing.png')

            self.label_keep_die_2.hide()
            self.label_die_2.show()
            self.label_die_2.setPixmap(x)

            self.button_die_2.setCheckable(True)
            master_die_roll_list.pop('2')

    def save_die_3(self):
        """
        Function to keep the roll for Die 3 and not re-roll it.
        """
        image1 = QPixmap('Single-Die-with-1-Showing.png')
        image2 = QPixmap('Single-Die-with-2-Showing.png')
        image3 = QPixmap('Single-Die-with-3-Showing.png')
        image4 = QPixmap('Single-Die-with-4-Showing.png')
        image5 = QPixmap('Single-Die-with-5-Showing.png')
        image6 = QPixmap('Single-Die-with-6-Showing.png')

        global master_die_roll_list

        if self.button_die_3.isChecked():
            self.button_die_3.setCheckable(False)
            if die_3 == '1':
                self.label_keep_die_3.show()
                self.label_keep_die_3.setPixmap(image1)
                self.label_die_3.hide()
            elif die_3 == '2':
                self.label_keep_die_3.show()
                self.label_keep_die_3.setPixmap(image2)
                self.label_die_3.hide()
            elif die_3 == '3':
                self.label_keep_die_3.show()
                self.label_keep_die_3.setPixmap(image3)
                self.label_die_3.hide()
            elif die_3 == '4':
                self.label_keep_die_3.show()
                self.label_keep_die_3.setPixmap(image4)
                self.label_die_3.hide()
            elif die_3 == '5':
                self.label_keep_die_3.show()
                self.label_keep_die_3.setPixmap(image5)
                self.label_die_3.hide()
            else:
                self.label_keep_die_3.show()
                self.label_keep_die_3.setPixmap(image6)
                self.label_die_3.hide()
            master_die_roll_list['3'] = die_3
        else:
            x = master_die_roll_list['3']
            if x == '1':
                x = QPixmap('Single-Die-with-1-Showing.png')
            if x == '2':
                x = QPixmap('Single-Die-with-2-Showing.png')
            if x == '3':
                x = QPixmap('Single-Die-with-3-Showing.png')
            if x == '4':
                x = QPixmap('Single-Die-with-4-Showing.png')
            if x == '5':
                x = QPixmap('Single-Die-with-5-Showing.png')
            if x == '6':
                x = QPixmap('Single-Die-with-6-Showing.png')

            self.label_keep_die_3.hide()
            self.label_die_3.show()
            self.label_die_3.setPixmap(x)

            self.button_die_3.setCheckable(True)
            master_die_roll_list.pop('3')

    def save_die_4(self):
        """
        Function to keep the roll for Die 4 and not re-roll it.
        """
        image1 = QPixmap('Single-Die-with-1-Showing.png')
        image2 = QPixmap('Single-Die-with-2-Showing.png')
        image3 = QPixmap('Single-Die-with-3-Showing.png')
        image4 = QPixmap('Single-Die-with-4-Showing.png')
        image5 = QPixmap('Single-Die-with-5-Showing.png')
        image6 = QPixmap('Single-Die-with-6-Showing.png')

        global master_die_roll_list

        if self.button_die_4.isChecked():
            self.button_die_4.setCheckable(False)
            if die_4 == '1':
                self.label_keep_die_4.show()
                self.label_keep_die_4.setPixmap(image1)
                self.label_die_4.hide()
            elif die_4 == '2':
                self.label_keep_die_4.show()
                self.label_keep_die_4.setPixmap(image2)
                self.label_die_4.hide()
            elif die_4 == '3':
                self.label_keep_die_4.show()
                self.label_keep_die_4.setPixmap(image3)
                self.label_die_4.hide()
            elif die_4 == '4':
                self.label_keep_die_4.show()
                self.label_keep_die_4.setPixmap(image4)
                self.label_die_4.hide()
            elif die_4 == '5':
                self.label_keep_die_4.show()
                self.label_keep_die_4.setPixmap(image5)
                self.label_die_4.hide()
            else:
                self.label_keep_die_4.show()
                self.label_keep_die_4.setPixmap(image6)
                self.label_die_4.hide()
            master_die_roll_list['4'] = die_4
        else:
            x = master_die_roll_list['4']
            if x == '1':
                x = QPixmap('Single-Die-with-1-Showing.png')
            if x == '2':
                x = QPixmap('Single-Die-with-2-Showing.png')
            if x == '3':
                x = QPixmap('Single-Die-with-3-Showing.png')
            if x == '4':
                x = QPixmap('Single-Die-with-4-Showing.png')
            if x == '5':
                x = QPixmap('Single-Die-with-5-Showing.png')
            if x == '6':
                x = QPixmap('Single-Die-with-6-Showing.png')

            self.label_keep_die_4.hide()
            self.label_die_4.show()
            self.label_die_4.setPixmap(x)

            self.button_die_4.setCheckable(True)
            master_die_roll_list.pop('4')

    def save_die_5(self):
        """
        Function to keep the roll for Die 5 and not re-roll it.
        """
        image1 = QPixmap('Single-Die-with-1-Showing.png')
        image2 = QPixmap('Single-Die-with-2-Showing.png')
        image3 = QPixmap('Single-Die-with-3-Showing.png')
        image4 = QPixmap('Single-Die-with-4-Showing.png')
        image5 = QPixmap('Single-Die-with-5-Showing.png')
        image6 = QPixmap('Single-Die-with-6-Showing.png')

        global master_die_roll_list

        if self.button_die_5.isChecked():
            self.button_die_5.setCheckable(False)
            if die_5 == '1':
                self.label_keep_die_5.show()
                self.label_keep_die_5.setPixmap(image1)
                self.label_die_5.hide()
            elif die_5 == '2':
                self.label_keep_die_5.show()
                self.label_keep_die_5.setPixmap(image2)
                self.label_die_5.hide()
            elif die_5 == '3':
                self.label_keep_die_5.show()
                self.label_keep_die_5.setPixmap(image3)
                self.label_die_5.hide()
            elif die_5 == '4':
                self.label_keep_die_5.show()
                self.label_keep_die_5.setPixmap(image4)
                self.label_die_5.hide()
            elif die_5 == '5':
                self.label_keep_die_5.show()
                self.label_keep_die_5.setPixmap(image5)
                self.label_die_5.hide()
            else:
                self.label_keep_die_5.show()
                self.label_keep_die_5.setPixmap(image6)
                self.label_die_5.hide()
            master_die_roll_list['5'] = die_5
        else:
            x = master_die_roll_list['5']
            if x == '1':
                x = QPixmap('Single-Die-with-1-Showing.png')
            if x == '2':
                x = QPixmap('Single-Die-with-2-Showing.png')
            if x == '3':
                x = QPixmap('Single-Die-with-3-Showing.png')
            if x == '4':
                x = QPixmap('Single-Die-with-4-Showing.png')
            if x == '5':
                x = QPixmap('Single-Die-with-5-Showing.png')
            if x == '6':
                x = QPixmap('Single-Die-with-6-Showing.png')

            self.label_keep_die_5.hide()
            self.label_die_5.show()
            self.label_die_5.setPixmap(x)

            self.button_die_5.setCheckable(True)
            master_die_roll_list.pop('5')

    def aces_score(self):
        """
        Function to add score from roll to the Aces score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            if num == 1:
                total += 1

        global total_score_upper
        global grand_total_score
        global die_roll_list

        if total == 0:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            total_score_upper += (total * 1)
            grand_total_score += (total * 1)
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_score.setText(total_score_upper_str)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)
            total = str(total*1)
            self.button_aces.hide()
            self.label_score_aces.show()
            self.label_score_aces.setText(total)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)

        if total_score_upper >= 63:
            self.label_box_bonus.setText('35')
            total_score_upper += 35
            grand_total_score += 35
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)

    def twos_score(self):
        """
        Function to add score from roll to the Twos score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            if num == 2:
                total += 1

        global total_score_upper
        global grand_total_score
        global die_roll_list

        if total == 0:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            total_score_upper += (total * 2)
            grand_total_score += (total * 2)
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_score.setText(total_score_upper_str)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)
            total = str(total * 2)
            self.button_twos.hide()
            self.label_score_twos.show()
            self.label_score_twos.setText(total)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)

        if total_score_upper >= 63:
            self.label_box_bonus.setText('35')
            total_score_upper += 35
            grand_total_score += 35
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)

    def threes_score(self):
        """
        Function to add score from roll to the Threes score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            if num == 3:
                total += 1

        global total_score_upper
        global grand_total_score
        global die_roll_list

        if total == 0:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            total_score_upper += (total * 3)
            grand_total_score += (total * 3)
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_score.setText(total_score_upper_str)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)
            total = str(total * 3)
            self.button_threes.hide()
            self.label_score_threes.show()
            self.label_score_threes.setText(total)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)

        if total_score_upper >= 63:
            self.label_box_bonus.setText('35')
            total_score_upper += 35
            grand_total_score += 35
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)

    def fours_score(self):
        """
        Function to add score from roll to the Fours score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            if num == 4:
                total += 1

        global total_score_upper
        global grand_total_score
        global die_roll_list

        if total == 0:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            total_score_upper += (total * 4)
            grand_total_score += (total * 4)
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_score.setText(total_score_upper_str)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)
            total = str(total * 4)
            self.button_fours.hide()
            self.label_score_fours.show()
            self.label_score_fours.setText(total)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)

        if total_score_upper >= 63:
            self.label_box_bonus.setText('35')
            total_score_upper += 35
            grand_total_score += 35
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)

    def fives_score(self):
        """
        Function to add score from roll to the Fives score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            if num == 5:
                total += 1

        global total_score_upper
        global grand_total_score
        global die_roll_list

        if total == 0:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            total_score_upper += (total * 5)
            grand_total_score += (total * 5)
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_score.setText(total_score_upper_str)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)
            total = str(total * 5)
            self.button_fives.hide()
            self.label_score_fives.show()
            self.label_score_fives.setText(total)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)

        if total_score_upper >= 63:
            self.label_box_bonus.setText('35')
            total_score_upper += 35
            grand_total_score += 35
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)

    def sixes_score(self):
        """
        Function to add score from roll to the Sixes score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            if num == 6:
                total += 1

        global total_score_upper
        global grand_total_score
        global die_roll_list

        if total == 0:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            total_score_upper += (total * 6)
            grand_total_score += (total * 6)
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_score.setText(total_score_upper_str)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)
            total = str(total * 6)
            self.button_sixes.hide()
            self.label_score_sixes.show()
            self.label_score_sixes.setText(total)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)

        if total_score_upper >= 63:
            self.label_box_bonus.setText('35')
            total_score_upper += 35
            grand_total_score += 35
            total_score_upper_str = str(total_score_upper)
            grand_total_score_str = str(grand_total_score)
            self.label_box_total_upper.setText(total_score_upper_str)
            self.label_box_total_upper_repeat.setText(total_score_upper_str)
            self.label_box_grand_total.setText(grand_total_score_str)

    def _3_of_a_kind_score(self):
        """
        Function to add score from roll to the 3 of a kind score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        score = 0
        x = final_list.count(1)
        if x == 3:
            score += 1
        else:
            score = score

        y = final_list.count(2)
        if y == 3:
            score += 1
        else:
            score = score

        z = final_list.count(3)
        if z == 3:
            score += 1
        else:
            score = score

        a = final_list.count(4)
        if a == 3:
            score += 1
        else:
            score = score

        b = final_list.count(5)
        if b == 3:
            score += 1
        else:
            score = score

        c = final_list.count(6)
        if c == 3:
            score += 1
        else:
            score = score

        global die_roll_list

        added_list = []

        added_list = []
        if '1' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[0]
            added_list.append(x)

        if '2' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[1]
            added_list.append(x)

        if '3' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[2]
            added_list.append(x)

        if '4' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[3]
            added_list.append(x)

        if '5' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[4]
            added_list.append(x)

        other_total = []
        for i in added_list:
            num = int(i)
            other_total.append(num)
        sum_of_other_nums = sum(other_total)

        global total_score_lower
        global grand_total_score

        if score == 1:
            score = sum(final_list) + sum_of_other_nums
            total_score_lower += score
            grand_total_score += score
            total_score_lower_str = str(total_score_lower)
            self.label_box_total_lower.setText(total_score_lower_str)
            grand_total_score_str = str(grand_total_score)
            self.label_box_grand_total.setText(grand_total_score_str)
            score = str(score)
            self.button_3_of_a_kind.hide()
            self.label_score_3_of_a_kind.show()
            self.label_score_3_of_a_kind.setText(score)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []
            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)
        else:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')

    def _4_of_a_kind_score(self):
        """
        Function to add score from roll to the 4 of a kind score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        score = 0
        x = final_list.count(1)
        if x == 4:
            score = +1
        else:
            score = score

        y = final_list.count(2)
        if y == 4:
            score += 1
        else:
            score = score

        z = final_list.count(3)
        if z == 4:
            score += 1
        else:
            score = score

        a = final_list.count(4)
        if a == 4:
            score += 1
        else:
            score = score

        b = final_list.count(5)
        if b == 4:
            score += 1
        else:
            score = score

        c = final_list.count(6)
        if c == 4:
            score += 1
        else:
            score = score

        global die_roll_list

        added_list = []
        if '1' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[0]
            added_list.append(x)

        if '2' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[1]
            added_list.append(x)

        if '3' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[2]
            added_list.append(x)

        if '4' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[3]
            added_list.append(x)

        if '5' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[4]
            added_list.append(x)

        other_total = []
        for i in added_list:
            num = int(i)
            other_total.append(num)
        sum_of_other_nums = sum(other_total)

        global total_score_lower
        global grand_total_score

        if score == 1:
            score = sum(final_list) + sum_of_other_nums
            total_score_lower += score
            grand_total_score += score
            total_score_lower_str = str(total_score_lower)
            self.label_box_total_lower.setText(total_score_lower_str)
            grand_total_score_str = str(grand_total_score)
            self.label_box_grand_total.setText(grand_total_score_str)
            score = str(score)
            self.button_4_of_a_kind.hide()
            self.label_score_4_of_a_kind.show()
            self.label_score_4_of_a_kind.setText(score)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []
            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)
        else:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')

    def full_house_score(self):
        """
        Function to add score from roll to the Full House score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        full_house = 0
        x = final_list.count(1)
        if x == 3:
            full_house += 2
        elif x == 2:
            full_house += 1
        else:
            full_house = full_house

        y = final_list.count(2)
        if y == 3:
            full_house += 2
        elif y == 2:
            full_house += 1
        else:
            full_house = full_house

        z = final_list.count(3)
        if z == 3:
            full_house += 2
        elif z == 2:
            full_house += 1
        else:
            full_house = full_house

        a = final_list.count(4)
        if a == 3:
            full_house += 2
        elif a == 2:
            full_house += 1
        else:
            full_house = full_house

        b = final_list.count(5)
        if b == 3:
            full_house += 2
        elif b == 2:
            full_house += 1
        else:
            full_house = full_house

        c = final_list.count(6)
        if c == 3:
            full_house += 2
        elif c == 2:
            full_house += 1
        else:
            full_house = full_house

        global total_score_lower
        global grand_total_score
        global die_roll_list

        if full_house == 3:
            total_score_lower += 25
            grand_total_score += 25
            total_score_lower_str = str(total_score_lower)
            self.label_box_total_lower.setText(total_score_lower_str)
            grand_total_score_str = str(grand_total_score)
            self.label_box_grand_total.setText(grand_total_score_str)
            self.button_full_house.hide()
            self.label_score_full_house.show()
            self.label_score_full_house.setText('25')
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []
            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.hide()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)
        else:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')

    def sm_straight_score(self):
        """
        Function to add score from roll to the Small Straight score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        new_list = []
        [new_list.append(x) for x in num_list if x not in new_list]

        new_list.sort()
        final_list = []
        for i in new_list:
            num = int(i)
            final_list.append(num)

        global total_score_lower
        global grand_total_score
        global dice_rolls
        global die_roll_list

        if len(final_list) < 4:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        elif len(final_list) == 4:
            if sorted(final_list) == list(range(min(final_list), max(final_list) + 1)):
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                global dice_rolls
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            else:
                self.label_warning.show()
                self.label_warning.setText('No score\nChoose\nagain')

        if len(final_list) == 5:
            if final_list[:4] == [1, 2, 3, 4]:
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            elif final_list[:4] == [2, 3, 4, 5]:
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            elif final_list[:4] == [3, 4, 5, 6]:
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            elif final_list[1:] == [1, 2, 3, 4]:
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            elif final_list[1:] == [2, 3, 4, 5]:
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            elif final_list[1:] == [3, 4, 5, 6]:
                total_score_lower += 30
                grand_total_score += 30
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('30')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            else:
                self.label_warning.show()
                self.label_warning.setText('No score\nChoose\nagain')

    def lg_straight_score(self):
        """
        Function to add score from roll to the Large Straight score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        new_list = []
        [new_list.append(x) for x in num_list if x not in new_list]

        new_list.sort()
        final_list = []
        for i in new_list:
            num = int(i)
            final_list.append(num)

        global total_score_lower
        global grand_total_score
        global die_roll_list

        if len(final_list) < 5:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')
        else:
            if sorted(final_list) == list(range(min(final_list), max(final_list) + 1)):
                total_score_lower += 40
                grand_total_score += 40
                total_score_lower_str = str(total_score_lower)
                self.label_box_total_lower.setText(total_score_lower_str)
                grand_total_score_str = str(grand_total_score)
                self.label_box_grand_total.setText(grand_total_score_str)
                self.button_lg_straight.hide()
                self.label_score_lg_straight.show()
                self.label_score_lg_straight.setText('40')
                global dice_rolls
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
                self.label_keep_die_1.hide()
                self.label_keep_die_2.hide()
                self.label_keep_die_3.hide()
                self.label_keep_die_4.hide()
                self.label_keep_die_5.hide()
                self.label_die_1.show()
                self.label_die_1.clear()
                self.label_die_2.show()
                self.label_die_2.clear()
                self.label_die_3.show()
                self.label_die_3.clear()
                self.label_die_4.show()
                self.label_die_4.clear()
                self.label_die_5.show()
                self.label_die_5.clear()
                self.label_warning.hide()
                self.button_die_1.setCheckable(True)
                self.button_die_2.setCheckable(True)
                self.button_die_3.setCheckable(True)
                self.button_die_4.setCheckable(True)
                self.button_die_5.setCheckable(True)
            else:
                self.label_warning.show()
                self.label_warning.setText('No score\nChoose\nagain')

    def yahtzee_score(self):
        """
        Function to add score from roll to the Yahtzee score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        yahtzee = 0
        x = final_list.count(1)
        if x == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        y = final_list.count(2)
        if y == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        z = final_list.count(3)
        if z == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        a = final_list.count(4)
        if a == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        b = final_list.count(5)
        if b == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        c = final_list.count(6)
        if c == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        global total_score_lower
        global grand_total_score
        global yahtzee_bonus
        global die_roll_list

        if yahtzee == 1:
            yahtzee_bonus = 1
            self.button_yahtzee.hide()
            self.label_score_yahtzee.show()
            self.label_score_yahtzee.setText('50')
            total_score_lower += 50
            grand_total_score += 50
            total_score_lower_str = str(total_score_lower)
            self.label_box_total_lower.setText(total_score_lower_str)
            grand_total_score_str = str(grand_total_score)
            self.label_box_grand_total.setText(grand_total_score_str)
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []
            self.label_warning.show()
            self.label_warning.setText('Hooray!!')
            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)
        else:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')

    def chance_score(self):
        """
        Function to add score from roll to the Chance score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        total = 0
        for num in final_list:
            total += num

        global die_roll_list

        added_list = []
        if '1' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[0]
            added_list.append(x)

        if '2' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[1]
            added_list.append(x)

        if '3' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[2]
            added_list.append(x)

        if '4' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[3]
            added_list.append(x)

        if '5' in master_die_roll_list:
            print('present')
        else:
            x = die_roll_list[4]
            added_list.append(x)

        other_total = []
        for i in added_list:
            num = int(i)
            other_total.append(num)
        sum_of_other_nums = sum(other_total)

        global total_score_lower
        global grand_total_score

        total_score_lower += total + sum_of_other_nums
        grand_total_score += total + sum_of_other_nums
        total_score_lower_str = str(total_score_lower)
        self.label_box_total_lower.setText(total_score_lower_str)
        grand_total_score_str = str(grand_total_score)
        self.label_box_grand_total.setText(grand_total_score_str)
        total = str(total + sum_of_other_nums)
        self.button_chance.hide()
        self.label_score_chance.show()
        self.label_score_chance.setText(total)
        global dice_rolls
        dice_rolls = 0
        master_die_roll_list = {}
        die_roll_list = []

        self.label_keep_die_1.hide()
        self.label_keep_die_2.hide()
        self.label_keep_die_3.hide()
        self.label_keep_die_4.hide()
        self.label_keep_die_5.hide()
        self.label_die_1.show()
        self.label_die_1.clear()
        self.label_die_2.show()
        self.label_die_2.clear()
        self.label_die_3.show()
        self.label_die_3.clear()
        self.label_die_4.show()
        self.label_die_4.clear()
        self.label_die_5.show()
        self.label_die_5.clear()
        self.label_warning.hide()
        self.button_die_1.setCheckable(True)
        self.button_die_2.setCheckable(True)
        self.button_die_3.setCheckable(True)
        self.button_die_4.setCheckable(True)
        self.button_die_5.setCheckable(True)

    def yahtzee_bonus_score(self):
        """
        Function to add score from roll to the Yahtzee Bonus score box and reset the player's turn.
        It also adds this score to the corresponding total score boxes.
        """
        global master_die_roll_list
        self.label_warning.setText('')
        num_list = list(master_die_roll_list.values())

        final_list = []
        for i in num_list:
            num = int(i)
            final_list.append(num)

        yahtzee = 0
        x = final_list.count(1)
        if x == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        y = final_list.count(2)
        if y == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        z = final_list.count(3)
        if z == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        a = final_list.count(4)
        if a == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        b = final_list.count(5)
        if b == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        c = final_list.count(6)
        if c == 5:
            yahtzee += 1
        else:
            yahtzee = yahtzee

        yahtzee = yahtzee + yahtzee_bonus

        global total_score_lower
        global grand_total_score
        global die_roll_list

        if yahtzee == 2:
            total_score_lower += 100
            grand_total_score += 100
            total_score_lower_str = str(total_score_lower)
            self.label_box_total_lower.setText(total_score_lower_str)
            grand_total_score_str = str(grand_total_score)
            self.label_box_grand_total.setText(grand_total_score_str)
            self.button_yahtzee_bonus.hide()
            self.label_score_yahtzee_bonus.show()
            self.label_score_yahtzee_bonus.setText('100')
            global dice_rolls
            dice_rolls = 0
            master_die_roll_list = {}
            die_roll_list = []

            self.label_keep_die_1.hide()
            self.label_keep_die_2.hide()
            self.label_keep_die_3.hide()
            self.label_keep_die_4.hide()
            self.label_keep_die_5.hide()
            self.label_die_1.show()
            self.label_die_1.clear()
            self.label_die_2.show()
            self.label_die_2.clear()
            self.label_die_3.show()
            self.label_die_3.clear()
            self.label_die_4.show()
            self.label_die_4.clear()
            self.label_die_5.show()
            self.label_die_5.clear()
            self.label_warning.show()
            self.label_warning.setText('Awesome!')
            self.button_die_1.setCheckable(True)
            self.button_die_2.setCheckable(True)
            self.button_die_3.setCheckable(True)
            self.button_die_4.setCheckable(True)
            self.button_die_5.setCheckable(True)
        else:
            self.label_warning.show()
            self.label_warning.setText('No score\nChoose\nagain')

    def zero(self):
        """
        Function allows user to enter a zero for one of the score boxes in case
        they don't have a play with their final roll of a turn.
        """
        user_input = self.comboBox.currentText()
        global dice_rolls
        global die_roll_list
        global master_die_roll_list
        global master_zeros_list

        if user_input == 'Aces':
            if '1' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['1'] = 'aces'
                self.button_aces.hide()
                self.label_score_aces.show()
                self.label_score_aces.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        elif user_input == 'Twos':
            if '2' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['2'] = 'twos'
                self.button_twos.hide()
                self.label_score_twos.show()
                self.label_score_twos.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        elif user_input == 'Threes':
            if '3' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['3'] = 'threes'
                self.button_threes.hide()
                self.label_score_threes.show()
                self.label_score_threes.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        elif user_input == 'Fours':
            if '4' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['4'] = 'fours'
                self.button_fours.hide()
                self.label_score_fours.show()
                self.label_score_fours.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        elif user_input == 'Fives':
            if '5' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['5'] = 'fives'
                self.button_fives.hide()
                self.label_score_fives.show()
                self.label_score_fives.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Sixes':
            if '6' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['6'] = 'sixes'
                self.button_sixes.hide()
                self.label_score_sixes.show()
                self.label_score_sixes.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == '3 of a kind':
            if '7' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['7'] = '3 of a kind'
                self.button_3_of_a_kind.hide()
                self.label_score_3_of_a_kind.show()
                self.label_score_3_of_a_kind.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == '4 of a kind':
            if '8' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['8'] = '4 of a kind'
                self.button_4_of_a_kind.hide()
                self.label_score_4_of_a_kind.show()
                self.label_score_4_of_a_kind.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Full House':
            if '9' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['9'] = 'full house'
                self.button_full_house.hide()
                self.label_score_full_house.show()
                self.label_score_full_house.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Small Straight':
            if '10' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['10'] = 'small straight'
                self.button_sm_straight.hide()
                self.label_score_sm_straight.show()
                self.label_score_sm_straight.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Large Straight':
            if '11' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['11'] = 'large straight'
                self.button_lg_straight.hide()
                self.label_score_lg_straight.show()
                self.label_score_lg_straight.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Yahtzee':
            if '12' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['12'] = 'yahtzee'
                self.button_yahtzee.hide()
                self.label_score_yahtzee.show()
                self.label_score_yahtzee.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Chance':
            if '13' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['13'] = 'chance'
                self.button_chance.hide()
                self.label_score_chance.show()
                self.label_score_chance.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []
        if user_input == 'Yahtzee Bonus':
            if '14' in master_zeros_list:
                self.label_warning.show()
                self.label_warning.setText('Already\nused\nChoose\nanother')
            else:
                self.label_warning.hide()
                self.label_warning.setText('')
                master_zeros_list['14'] = 'yahtzee bonus'
                self.button_yahtzee_bonus.hide()
                self.label_score_yahtzee_bonus.show()
                self.label_score_yahtzee_bonus.setText('0')
                dice_rolls = 0
                master_die_roll_list = {}
                die_roll_list = []

        self.label_keep_die_1.hide()
        self.label_keep_die_2.hide()
        self.label_keep_die_3.hide()
        self.label_keep_die_4.hide()
        self.label_keep_die_5.hide()
        self.label_die_1.show()
        self.label_die_1.clear()
        self.label_die_2.show()
        self.label_die_2.clear()
        self.label_die_3.show()
        self.label_die_3.clear()
        self.label_die_4.show()
        self.label_die_4.clear()
        self.label_die_5.show()
        self.label_die_5.clear()
        self.button_die_1.setCheckable(True)
        self.button_die_2.setCheckable(True)
        self.button_die_3.setCheckable(True)
        self.button_die_4.setCheckable(True)
        self.button_die_5.setCheckable(True)

    def new_game(self):
        """
        Function resets all of the settings for the app and starts
        a new user game.
        """
        self.label_score_aces.hide()
        self.label_score_twos.hide()
        self.label_score_threes.hide()
        self.label_score_fours.hide()
        self.label_score_fives.hide()
        self.label_score_sixes.hide()
        self.label_box_total_score.setText('')
        self.label_box_bonus.setText('')
        self.label_box_total_upper.setText('')
        self.label_score_3_of_a_kind.hide()
        self.label_score_4_of_a_kind.hide()
        self.label_score_full_house.hide()
        self.label_score_sm_straight.hide()
        self.label_score_lg_straight.hide()
        self.label_score_yahtzee.hide()
        self.label_score_chance.hide()
        self.label_score_yahtzee_bonus.hide()
        self.label_box_total_lower.setText('')
        self.label_box_total_upper_repeat.setText('')
        self.label_box_grand_total.setText('')
        self.label_warning.show()
        self.label_warning.setText('Good\nLuck!\nRoll\nthe\nDice')

        self.label_keep_die_1.hide()
        self.label_keep_die_2.hide()
        self.label_keep_die_3.hide()
        self.label_keep_die_4.hide()
        self.label_keep_die_5.hide()
        self.label_die_1.show()
        self.label_die_1.clear()
        self.label_die_2.show()
        self.label_die_2.clear()
        self.label_die_3.show()
        self.label_die_3.clear()
        self.label_die_4.show()
        self.label_die_4.clear()
        self.label_die_5.show()
        self.label_die_5.clear()
        self.button_die_1.setCheckable(True)
        self.button_die_2.setCheckable(True)
        self.button_die_3.setCheckable(True)
        self.button_die_4.setCheckable(True)
        self.button_die_5.setCheckable(True)

        self.button_aces.show()
        self.button_twos.show()
        self.button_threes.show()
        self.button_fours.show()
        self.button_fives.show()
        self.button_sixes.show()
        self.button_3_of_a_kind.show()
        self.button_4_of_a_kind.show()
        self.button_full_house.show()
        self.button_sm_straight.show()
        self.button_lg_straight.show()
        self.button_yahtzee.show()
        self.button_chance.show()
        self.button_yahtzee_bonus.show()

        global yahtzee_bonus
        global total_score_upper
        global total_score_lower
        global grand_total_score
        global dice_rolls
        global master_die_roll_list
        global die_roll_list
        global master_zeros_list

        yahtzee_bonus = 0
        total_score_upper = 0
        total_score_lower = 0
        grand_total_score = 0
        dice_rolls = 0
        master_die_roll_list = {}
        master_zeros_list = {}
        die_roll_list = []
