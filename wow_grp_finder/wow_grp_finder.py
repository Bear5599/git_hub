import tkinter as tk
from tkinter import *
import pyperclip

default_gearscore = "4.5" # Change the number within "" for a different default Gearscore 

# Creates a sentence based on buttons pressed and copies to clipboard
# example of code output:
# LF {Skull}Tank & Healer for H++{Skull} Ahn'kahet: The Old Kingdom (OK), 
# Whisper Gearscore for invite, {star}4.5K+ GS Only.{star} Its the Daily!
# Depending on choices this sentence changes.
class Character_Type:

    def __init__(self, root):
        self.root = root
        self.dps = None
        self.healer = None
        self.tank = None
        self.healer_and_dps = None
        self.tank_and_dps = None
        self.tank_and_healer = None
        self.empty_label = None
        # self.mylabel = None
        self.skull_marker_in_wow = "{Skull}"
        self.selected_char_type = None
        self.x_coordinate = (app_width / 2) - 200

    def char_class_pressed_button(self):
        return self.selected_char_type

    def dps_button(self):
        self.hide_char_buttons()
        difficulty.create_difficulty_buttons()
        self.selected_char_type = f"LF {self.skull_marker_in_wow}Dps"

    def healer_button(self):
        self.hide_char_buttons()
        difficulty.create_difficulty_buttons()
        self.selected_char_type = f"LF {self.skull_marker_in_wow}Healer for"

    def tank_button(self):
        self.hide_char_buttons()
        difficulty.create_difficulty_buttons()
        self.selected_char_type = f"LF {self.skull_marker_in_wow}Tank for"

    def healer_dps_button(self):
        self.hide_char_buttons()
        difficulty.create_difficulty_buttons()
        self.selected_char_type = f"LF {self.skull_marker_in_wow}Healer & Dps for"

    def tank_dps_button(self):
        self.hide_char_buttons()
        difficulty.create_difficulty_buttons()
        self.selected_char_type = f"LF {self.skull_marker_in_wow}Tank & Dps for"

    def tank_healer_button(self):
        self.hide_char_buttons()
        difficulty.create_difficulty_buttons()
        self.selected_char_type = f"LF {self.skull_marker_in_wow}Tank & Healer for"


    def create_char_type_buttons(self):
        self.dps = Button(
            self.root,
            text="Dps",
            command=self.dps_button,
            font=("Times New Roman", 30)
        )
        self.dps.place(x=self.x_coordinate, y=0)

        self.healer = Button(
            self.root,
            text="Healer",
            command=self.healer_button,
            font=("Times New Roman", 30)
        )
        self.healer.place(x=self.x_coordinate, y=80)


        self.tank = Button(
            self.root,
            text="Tank",
            command=self.tank_button,
            font=("Times New Roman", 30)
        )
        self.tank.place(x=self.x_coordinate, y=160)

        self.healer_and_dps = Button(
            self.root,
            text="Healer & Dps",
            command=self.healer_dps_button,
            font=("Times New Roman", 30)
        )
        self.healer_and_dps.place(x=self.x_coordinate, y=240)

        self.tank_and_dps = Button(
            self.root,
            text="Tank & Dps",
            command=self.tank_dps_button,
            font=("Times New Roman", 30)
        )
        self.tank_and_dps.place(x=self.x_coordinate, y=320)

        self.tank_and_healer = Button(
            self.root,
            text="Tank & Healer",
            command=self.tank_healer_button,
            font=("Times New Roman", 30)
        )
        self.tank_and_healer.place(x=self.x_coordinate, y=400)

    def hide_char_buttons(self):
        self.dps.place_forget()
        self.healer.place_forget()
        self.tank.place_forget()
        self.healer_and_dps.place_forget()
        self.tank_and_dps.place_forget()
        self.tank_and_healer.place_forget()

class Difficulty:
    def __init__(self, root):
        self.root = root
        self.normal = None
        self.heroic = None
        self.heroic_alpha = None # H+
        self.heroic_beta = None  # H++
        self.skull_marker_in_wow = "{Skull}"
        self.selected_difficulty = None
        self.x_coordinates = app_width / 2 - 200

    def difficulty_button_pressed(self):
        return self.selected_difficulty

    def normal_button(self):
        self.hide_difficulty_buttons()
        dungeons.create_dungeon_buttons()
        self.selected_difficulty = " Normal"

    def heroic_button(self):
        self.hide_difficulty_buttons()
        dungeons.create_dungeon_buttons()
        self.selected_difficulty = f" Heroic (Not +){self.skull_marker_in_wow}"


    def heroic_alpha_button(self):
        self.hide_difficulty_buttons()
        dungeons.create_dungeon_buttons()
        self.selected_difficulty = f" H+{self.skull_marker_in_wow}"


    def heroic_beta_button(self):
        self.hide_difficulty_buttons()
        dungeons.create_dungeon_buttons()
        self.selected_difficulty = f" H++{self.skull_marker_in_wow}"


    def create_difficulty_buttons(self):

        self.normal = Button(
            self.root,
            text="Normal",
            command=self.normal_button,
            font=("Times New Roman", 30)
        )
        self.normal.place(x=self.x_coordinates, y=0)

        self.heroic = Button(
            self.root,
            text="Heroic",
            command=self.heroic_button,
            font=("Times New Roman", 30)
        )
        self.heroic.place(x=self.x_coordinates, y=80)

        self.heroic_alpha = Button(
            self.root,
            text="Heroic Alpha (H+)",
            command=self.heroic_alpha_button,
            font=("Times New Roman", 30)
        )
        self.heroic_alpha.place(x=self.x_coordinates, y=160)

        self.heroic_beta = Button(
            self.root,
            text="Heroic Beta (H++)",
            command=self.heroic_beta_button,
            font=("Times New Roman", 30)
        )
        self.heroic_beta.place(x=self.x_coordinates, y=240)


    def hide_difficulty_buttons(self):
        self.normal.place_forget()
        self.heroic.place_forget()
        self.heroic_alpha.place_forget()
        self.heroic_beta.place_forget()


class Dungeons:
    # Gearscore and Daily functions of this code are in this class for simplicity
    def __init__(self, root):
        self.root = root
        self.ok = None
        self.an = None
        self.dtk = None
        self.gun = None
        self.hol = None
        self.hos = None
        self.cos = None
        self.nex = None
        self.oc = None
        self.toc = None
        self.uk = None
        self.up = None
        self.vh = None
        self.fos = None
        self.pos = None
        self.daily = None
        self.gearscore = None
        self.yes_gs = None
        self.no_gs = None
        self.yes_daily = None
        self.not_daily = None
        self.copy_text = None
        self.star_mark = "{star}"
        self.dungeon_type_button_pressed = None
        self.gearscore_button_pressed = None
        self.daily_button_pressed = None
        self.skull_mark = "{Skull}"
        self.x_first_row = (app_width / 2) - 400
        self.x_second_row = (app_width / 2) + 90
        self.x_for_gearscore_label = app_width / 2 - 200
        self.x_for_daily_label = app_width / 2 - 200
        self.x_for_copy_button = app_width / 2 - 300
        self.x_yes_and_no_buttons = app_width / 2 - 100

    def dungeon_button_pressed(self):
        return self.dungeon_type_button_pressed
    
    def ok_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Ahn'kahet: The Old Kingdom (Lvl 73-75 Minimum 71)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Ahn'kahet: The Old Kingdom (OK)"
            self.create_gearscore_button()

    def an_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Ajzol-Nerub (Lvl 72-74 Minimum 70)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Ajzol-Nerub (AN)"
            self.create_gearscore_button()

    def dtk_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Drak'Tharon Keep (Lvl 74-76 Minimum 72)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Drak'Tharon Keep (DTK)"
            self.create_gearscore_button()

    def gun_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Gundrak (Lvl 76-78 Minimum 73)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Gundrak (GUN)"
            self.create_gearscore_button()

    def hol_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Halls of Lightning (Lvl 78-80 Minimum 75)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Halls of Lightning (HOL)"
            self.create_gearscore_button()

    def hos_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Halls of Stone (Lvl 77-79 Minimum 73)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Halls of Stone (HOS)"
            self.create_gearscore_button()

    def cos_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} The Culling of Stratholme (Lvl 78-80 Minimum 75)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " The Culling of Stratholme (COS)"
            self.create_gearscore_button()

    def nex_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Nexus (Lvl 69-73 Minimum 67)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Nexus (Nex)"
            self.create_gearscore_button()

    def oc_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} The Occulus (Lvl 79-80 Minimum 75)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " The Occulus (OC)"
            self.create_gearscore_button()

    def toc_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Trial of Champion (Lvl 80 Minimum 80)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Trial of Champion (TOC)"
            self.create_gearscore_button()

    def uk_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Utgarde Keep (Lvl 69-72 Minimum 67)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Utgarde Keep (UK)"
            self.create_gearscore_button()

    def up_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Utgarde Pinnacle (Lvl 79-80 Minimum 75)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Utgarde Pinnacle (UP)"
            self.create_gearscore_button()

    def vh_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Violet Hold (Lvl 75-77 Minimum 73)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Violet Hold (VH)"
            self.create_gearscore_button()

    def fos_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Forge of Souls (Lvl 80 Minimum 78)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Forge of Souls (FOS)"
            self.create_gearscore_button()

    def pos_button(self):
        self.hide_dungeon_buttons()
        if difficulty.difficulty_button_pressed() == " Normal":
            self.dungeon_type_button_pressed = f"{self.skull_mark} Pit of Saron (Lvl 80 Minimum 78)"
            self.gearscore_button_pressed = ""
            self.daily_button_pressed = ""
            self.create_copy_button()
        else:
            self.dungeon_type_button_pressed = " Pit of Saron (POS)"
            self.create_gearscore_button()

    def create_dungeon_buttons(self):
        
        self.ok = Button(
            self.root,
            text="Ahn'kahet: The Old Kingdom",
            command=self.ok_button,
            font=("Times New Roman", 20)
        )
        self.ok.place(x=self.x_first_row, y=0)

        self.an = Button(
            self.root,
            text="Ajzol-Nerub",
            command=self.an_button,
            font=("Times New Roman", 20)
        )
        self.an.place(x=self.x_first_row, y=60)

        self.dtk = Button(
            self.root,
            text="Drak'Tharon Keep",
            command=self.dtk_button,
            font=("Times New Roman", 20)
        )
        self.dtk.place(x=self.x_first_row, y=120)

        self.gun = Button(
            self.root,
            text="Gundrak",
            command=self.gun_button,
            font=("Times New Roman", 20)
        )
        self.gun.place(x=self.x_first_row, y=180)

        self.hol = Button(
            self.root,
            text="Halls of Lightning",
            command=self.hol_button,
            font=("Times New Roman", 20)
        )
        self.hol.place(x=self.x_first_row, y=240)

        self.hos = Button(
            self.root,
            text="Halls of Stone",
            command=self.hos_button,
            font=("Times New Roman", 20)
        )
        self.hos.place(x=self.x_first_row, y=300)

        self.cos = Button(
            self.root,
            text="The Culling of Stratholme",
            command=self.cos_button,
            font=("Times New Roman", 20)
        )
        self.cos.place(x=self.x_first_row, y=360)

        self.nex = Button(
            self.root,
            text="Nexus",
            command=self.nex_button,
            font=("Times New Roman", 20)
        )
        self.nex.place(x=self.x_first_row, y=420)


        self.oc = Button(
            self.root,
            text="The Oculus",
            command=self.oc_button,
            font=("Times New Roman", 20)
        )
        self.oc.place(x=self.x_second_row, y=0)

        self.toc = Button(
            self.root,
            text="Trial of Champion",
            command=self.toc_button,
            font=("Times New Roman", 20)
        )
        self.toc.place(x=self.x_second_row, y=60)

        self.uk = Button(
            self.root,
            text="Utgarde Keep",
            command=self.uk_button,
            font=("Times New Roman", 20)
        )
        self.uk.place(x=self.x_second_row, y=120)

        self.up = Button(
            self.root,
            text="Utgarde Pinnacle",
            command=self.up_button,
            font=("Times New Roman", 20)
        )
        self.up.place(x=self.x_second_row, y=180)

        self.vh = Button(
            self.root,
            text="Violet Hold",
            command=self.vh_button,
            font=("Times New Roman", 20)
        )
        self.vh.place(x=self.x_second_row, y=240)

        self.fos = Button(
            self.root,
            text="Forge of Souls",
            command=self.fos_button,
            font=("Times New Roman", 20)
        )
        self.fos.place(x=self.x_second_row, y=300)

        self.pos = Button(
            self.root,
            text="Pit of Saron",
            command=self.pos_button,
            font=("Times New Roman", 20)
        )
        self.pos.place(x=self.x_second_row, y=360)

# Gearscore portion of the code
    # def input_a_gs(self):
    #     pass

    def gearscore_press(self):
        return self.gearscore_button_pressed
        
    def yes_button(self):
        self.forget_gs()
        self.create_daily_button()
        self.gearscore_button_pressed = f", Whisper Gearscore for invite, {self.star_mark}{default_gearscore}K+ GS Only.{self.star_mark}"

    def no_button(self):
        self.forget_gs()
        self.create_daily_button()
        self.gearscore_button_pressed = ""
        
    def forget_gs(self):
        self.gearscore.place_forget()
        self.yes_gs.place_forget()
        self.no_gs.place_forget()

    def create_gearscore_button(self):

        self.gearscore = Label(
            self.root,
            text="Gearscore needed?  ",
            font=("Times New Roman", 30)
        )
        self.gearscore.place(x=self.x_for_gearscore_label, y=0)

        self.yes_gs = Button(
            self.root,
            text="Yes",
            command=self.yes_button,
            font=("Times New Roman", 40)
        )
        self.yes_gs.place(x=self.x_yes_and_no_buttons, y=100)

        self.no_gs = Button(
            self.root,
            text="No",
            command=self.no_button,
            font=("Times New Roman", 40)
        )
        self.no_gs.place(x=self.x_yes_and_no_buttons, y=200)

# is it the daily portion of the code


    def daily_button_press(self):
        return self.daily_button_pressed
    
    def daily_yes(self):
        self.daily_forget()
        self.create_copy_button()
        self.daily_button_pressed = " Its the Daily!"

    def daily_no(self):
        self.daily_forget()
        self.create_copy_button()
        self.daily_button_pressed = ""
        
    def daily_forget(self):
        self.daily.place_forget()
        self.yes_daily.place_forget()
        self.not_daily.place_forget()

    def create_daily_button(self):

        self.daily = Label(
            self.root,
            text="  Todays Daily?  ",
            font=("Times New Roman", 30)
        )
        self.daily.place(x=self.x_for_daily_label, y=0)

        self.yes_daily = Button(
            self.root,
            text="Yes",
            command=self.daily_yes,
            font=("Times New Roman", 40)
        )
        self.yes_daily.place(x=self.x_yes_and_no_buttons, y=100)

        self.not_daily = Button(
            self.root,
            text="No",
            command=self.daily_no,
            font=("Times New Roman", 40)
        )
        self.not_daily.place(x=self.x_yes_and_no_buttons, y=200)

    def hide_dungeon_buttons(self):
        self.ok.place_forget()
        self.an.place_forget()
        self.dtk.place_forget()
        self.gun.place_forget()
        self.hol.place_forget()
        self.hos.place_forget()
        self.cos.place_forget()
        self.nex.place_forget()
        self.oc.place_forget()
        self.toc.place_forget()
        self.uk.place_forget()
        self.up.place_forget()
        self.vh.place_forget()
        self.fos.place_forget()
        self.pos.place_forget()

        

# Copies the generated message from a file and copies it to clipboard

    def copy_message(self):
        char_message = char_type_instance.char_class_pressed_button()
        difficulty_message = difficulty.difficulty_button_pressed()
        dungeon_message = dungeons.dungeon_button_pressed()
        gearscore_message = dungeons.gearscore_press()
        daily_message = dungeons.daily_button_press()
        lfg_message = f"{char_message}{difficulty_message}{dungeon_message}{gearscore_message}{daily_message}"
        pyperclip.copy(lfg_message)
        print("Successfully copied message to clipboard")
        print(lfg_message)
        
    def create_copy_button(self):
        self.copy_text = Button(
        self.root,
        text="Copy to Clipboard?",
        command=self.copy_message,
        font=("Times New Roman", 40)
        )
        self.copy_text.place(x=self.x_for_copy_button, y=40)


if __name__ == "__main__":
    root = tk.Tk()

    root.title("Easy LFG Tool for WOTLK Classic")
    app_width = 810
    app_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    char_type_instance = Character_Type(root)
    char_type_instance.create_char_type_buttons()
    difficulty = Difficulty(root)
    dungeons = Dungeons(root)
    
    

    root.mainloop()
