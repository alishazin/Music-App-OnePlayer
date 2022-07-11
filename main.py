from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader, Sound
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton, MDFloatingActionButton, MDTextButton
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.list import OneLineAvatarIconListItem, ThreeLineAvatarIconListItem, OneLineListItem
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import NoTransition, CardTransition
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.snackbar import Snackbar
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.uix.modalview import ModalView
from kivymd.uix.button import MDIconButton
from kivy.uix.behaviors.button import ButtonBehavior
from kivymd.uix.dialog import MDDialog
from kivy import utils
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.animation import Animation
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior, CircularElevationBehavior, CircularRippleBehavior, RectangularElevationBehavior
from kivymd.utils.fitimage import FitImage
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
# from kivymd.uix.menu import MDMenuItem
from kivymd.uix.menu import MDDropdownMenu

import sqlite3

from pathlib import Path

import os

from django.core.validators import URLValidator

import re

class CustomDropdownListItem(OneLineListItem, HoverBehavior):
    def on_enter(self):
        self.md_bg_color = (1,1,1,1)

    def on_leave(self):
        self.md_bg_color = (1,1,1,.5)

class FocusMDSlider(MDSlider, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.thumb_size_normal = 16

    def on_leave(self):
        self.thumb_size_normal = .1

class ShadowFitImage(RoundedRectangularElevationBehavior, HoverBehavior, FitImage):
    def on_enter(self):
        self._elevation = 20

    def on_leave(self):
        self._elevation = 5


class ShadowFitImage2(RectangularElevationBehavior, HoverBehavior, FitImage):
    def on_enter(self):
        self._elevation = 20

    def on_leave(self):
        self._elevation = 0


class MenuListContent(OneLineAvatarIconListItem,ThemableBehavior, HoverBehavior):
    text = StringProperty()
    icon = StringProperty()

    def on_enter(self):
        self.font_style = 'H6'

    def on_leave(self):
        self.font_style = 'Subtitle1'

class MenuContent(MDBoxLayout):
    pass


class SettingsListContentFormat1(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()


class SettingsListContentFormat2(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()

class SettingsListContentFormat3(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()

class SettingsListContentFormat4(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()

class RightLayout(IRightBodyTouch, MDRelativeLayout):
    pass


class FocusMDIconButton4(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.opacity = 3

    def on_leave(self):
        self.opacity = .5


class AddImage(MDCard, ButtonBehavior):
    def on_enter(self):
        self.opacity = .7

    def on_leave(self):
        self.opacity = 1


class FocusMDIconButton5(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_leave(self):
        self.user_font_size = 25


class FocusMDTextButton(MDTextButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.color = (1,1,1,1) if self.theme_cls.theme_style == 'Dark' else (0,0,0,1)

    def on_leave(self):
        self.color = (1,1,1,.6) if self.theme_cls.theme_style == 'Dark' else (0,0,0,.6)


class ImageTile(MDCard, ThemableBehavior, HoverBehavior):
    text = StringProperty()
    source = StringProperty()


class SongDetailsItem(MDCard, ThemableBehavior, HoverBehavior):
    text = StringProperty()
    text_sec = StringProperty()
    song_duration = StringProperty()
    img = StringProperty()

    def on_enter(self):
        animate_enlarge = Animation(
            size_hint_x = 1,
            height = 3,
            md_bg_color = self.theme_cls.primary_color,
            duration = .2
        )

        animate_enlarge.start(self.ids.separator_)

    def on_leave(self):
        animate_shrink = Animation(
            size_hint_x = .1,
            height = 1,
            md_bg_color = (1,1,1,.3),
            duration = .2
        )

        animate_shrink.start(self.ids.separator_)


class FocusMDIconButton(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.user_font_size = 35

    def on_leave(self):
        self.user_font_size = 25


class FocusMDIconButton2(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.user_font_size = 30

    def on_leave(self):
        self.user_font_size = 20


class FocusMDIconButton3(MDIconButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.user_font_size = 30

    def on_leave(self):
        self.user_font_size = 25


class FocusMDRoundFlatButton(MDRoundFlatButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.line_width = 2

    def on_leave(self):
        self.line_width = 1


class FocusMDFlatButton(MDFlatButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.curr_pos = self.pos_hint
        self.pos_hint = {'center_y': .6}

    def on_leave(self):
        self.pos_hint = self.curr_pos


class FocusMDRaisedButton(MDRaisedButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        self.curr_pos = self.pos_hint
        self.pos_hint = {'center_y': .6}
    
    def on_leave(self):
        self.pos_hint = self.curr_pos


class CircularElevationButton(CircularElevationBehavior, CircularRippleBehavior, ButtonBehavior, HoverBehavior, MDRelativeLayout):   
    pass


class CircularElevationButton2(CircularElevationBehavior, CircularRippleBehavior, ButtonBehavior, HoverBehavior, MDRelativeLayout):
    pass

class ContentDialog(MDRelativeLayout):
    pass


class ArtistSort(ThreeLineAvatarIconListItem):
    icon = StringProperty()


class FocusMDTextButton2(MDTextButton, ThemableBehavior, HoverBehavior):
    def on_enter(self):
        if self.text != 'Unknown':
            self.underline = True

    def on_leave(self):
        self.underline = False

class OnePlayer(MDApp):

    # some variables 
    path = ''
    duration = ''
    curr_delete_song_name = ''
    curr_playlist_songs = []
    curr_playlist_songs_path = []
    curr_playlist_songs_artist = []
    curr_active_song_path = ''
    curr_active_song_name = ''
    curr_active_song_duration_in_format = ''
    song_controller = None
    list_pause_seek = []
    song_clearing_period = False
    slider_press = False
    coming_from = None
    first_time = True
    coming_from_exclusive = None
    song_slider_tracker = [100]
    recently_played_record = []
    theme_ = ''
    list_of_images = []
    updates_menu = False
    default_img = 'https://images.pexels.com/photos/6320/smartphone-vintage-technology-music.jpg?auto=compress&cs=tinysrgb&dpr=2&w=500'
    search_cur = False
    single_occurence_artist = []
    search_timer = None


    # initialisation of database
    conn = sqlite3.connect('OneP.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS darktheme(
                state text
                )""")
    c.execute("SELECT *,oid FROM darktheme")
    dark_theme_check_db1 = c.fetchall()
    if len(dark_theme_check_db1) == 0: 
        c.execute(r"INSERT INTO darktheme VALUES ('off')")

    c.execute("""CREATE TABLE IF NOT EXISTS themecolor(
                color text
                )""")
    c.execute("SELECT *,oid FROM themecolor")
    theme_color_check_db1 = c.fetchall()
    if len(theme_color_check_db1) == 0: 
        c.execute(r"INSERT INTO themecolor VALUES ('Amber')")

    c.execute("""CREATE TABLE IF NOT EXISTS songdetails(
                path text,
                artistname text,
                songname text PRIMARY KEY,
                duration text
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS pathstart(
                path text
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS songcon(
                conf text
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS songimg(
                link text,
                name text PRIMARY KEY
                )""")

    c.execute("SELECT *,oid FROM songcon")
    song_con_db = c.fetchall()
    if len(song_con_db) == 0:
        c.execute(r"INSERT INTO songcon VALUES ('needed')")
        song_delete_confirmation = True
    else:
        if song_con_db[0][0] == 'needed':
            song_delete_confirmation = True
        else:
            song_delete_confirmation = False

    c.execute("SELECT *,oid FROM pathstart")
    path_check_db1 = c.fetchall()
    if len(path_check_db1) == 0:
        c.execute(r"INSERT INTO pathstart VALUES ('C:/')")

    c.execute("SELECT *,oid FROM darktheme")
    dark_theme_check_db2 = c.fetchall()
    for i in dark_theme_check_db2:
        dark_theme = i[0]

    c.execute("SELECT *,oid FROM themecolor")
    theme_color_check_db2 = c.fetchall()
    for i in theme_color_check_db2:
        theme_color = i[0]

    conn.commit()
    conn.close()
    #-----------------------------

    def build(self):
        self.screen = Builder.load_file('main.kv')

        if self.dark_theme == 'off':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

        self.theme_cls.primary_palette = str(self.theme_color)
        return self.screen

    def on_start(self):

        self.title = 'OnePlayer'
        self.icon = 'icon_One.png'

        # initialisation
        self.screen.ids._screen_manager.transition = NoTransition()
        self.on_entering_menu_configurations(1)
        #--------------------

        self.menu_list_items_dict = {
            'image' : 'Image List',
            'music-note-plus' : 'Add Songs',
            'cog' : 'Settings',
            '' : 'About Us'
        }

        for _icon,_text in self.menu_list_items_dict.items():
            self.screen.ids.menu_list_.add_widget(
                MenuListContent(icon=_icon,text=_text)
            )

        self.screen.ids.settings_list_.add_widget(
            SettingsListContentFormat1(text='Dark Theme',icon='theme-light-dark')
        )

        self.screen.ids.settings_list_.add_widget(
            SettingsListContentFormat2(text='Theme Color',icon='format-color-fill')
        )

        self.screen.ids.settings_list_.add_widget(
            SettingsListContentFormat3(text='Path While Opening File Manager',icon='file-code')
        )

        self.screen.ids.settings_list_.add_widget(
            SettingsListContentFormat4(text='Confirmation While Deleting A Song',icon='sticker-check')
        )

    def song_confirmation_check(self,switch,value):
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM songcon")
        if value == True:
            c.execute("UPDATE songcon SET conf = 'needed' WHERE oid = 1")
        else:
            c.execute("UPDATE songcon SET conf = 'not needed' WHERE oid = 1")
        conn.commit()
        conn.commit()

    def artist_search(self):
        self.entry_latest = ['aaaaaa']
        self.search_timer = Clock.schedule_interval(self.search_caller,.5)

    def search_caller(self,interval):
        self.search_text = self.screen.ids.artist_name_.text.strip()
        if len(self.search_text) != 0:
            if self.search_text != self.entry_latest[-1]:
                try:
                    self.search_menu.dismiss()
                except:
                    pass
                self.entry_latest.append(self.search_text)
                self.search_list_items = []
                for i in self.single_occurence_artist:
                    x = re.search(f'^{self.search_text.upper()}',i.upper())
                    if x:
                        self.search_list_items.append(i)
                self.search_labels = [
                {
                    'viewclass': 'CustomDropdownListItem',
                    'text': i,
                    } for i in self.search_list_items
                ]

                self.search_menu = MDDropdownMenu(
                    caller=self.screen.ids.artist_name_,
                    items=self.search_labels,
                    position='bottom',
                    width_mult=5,
                )
                self.search_menu.open()
        else:
            self.entry_latest = ['aaaaaa']
            try:
                self.search_menu.dismiss()
            except:
                pass

    def search_press(self,text):
        try:
            self.search_menu.dismiss()
        except:
            pass
        self.screen.ids.artist_name_.text = text
        Clock.unschedule(self.search_timer)
        self.search_menu.dismiss()

    def sort_artist(self,artist):
        if artist != 'Unknown':
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute('SELECT *,oid FROM songdetails')
            db_check = c.fetchall()
            song_name_list = []
            artist_name_list = []
            duration_list = []
            for i in db_check:
                if i[1] == artist:
                    song_name_list.append(i[2])
                    artist_name_list.append(i[1])
                    duration_list.append(i[3])
            self.screen.ids.artist_sort_toolbar.title = artist
            self.screen.ids.artist_sort_list.clear_widgets()
            for j in range(len(song_name_list)):
                self.screen.ids.artist_sort_list.add_widget(
                    ArtistSort(
                        icon='music',
                        text=song_name_list[j-1],
                        secondary_text=artist_name_list[j-1],
                        tertiary_text=duration_list[j-1]
                    )
                )
            self.screen.ids._screen_manager.current = '_artist_sort_screen'
        else:
            pass

    def menu_list_click(self,item_clicked):
        if item_clicked == "Settings":
            def child_func1_settings(interval):
                def child_func2_settings(interval):
                    self.screen.ids._screen_manager.current = '_settings_screen'
                self.screen.ids.menu_.set_state('close')
                Clock.schedule_once(child_func2_settings,.3)

            Clock.schedule_once(child_func1_settings,.45)

        if item_clicked == 'About Us':
            def child_func1_abt(interval):
                def child_func2_abt(interval):
                    self.screen.ids._screen_manager.current = '_about_us_screen'
                self.screen.ids.menu_.set_state('close')
                Clock.schedule_once(child_func2_abt,.3)

            Clock.schedule_once(child_func1_abt,.45)

        if item_clicked == 'Add Songs':
            def child_func1_add(interval):
                def child_func2_add(interval):
                    self.open_file_manager()
                self.screen.ids.menu_.set_state('close')
                Clock.schedule_once(child_func2_add,.3)

            Clock.schedule_once(child_func1_add,.45)

        if item_clicked == 'Image List':
            def child_func1_img(interval):
                def child_func2_img(interval):
                    self.screen.ids._screen_manager.current = '_image_screen'
                self.screen.ids.menu_.set_state('close')
                Clock.schedule_once(child_func2_img,.3)

            Clock.schedule_once(child_func1_img,.45)

    def back_to_menu(self,instance):
        if instance == 0:
            self.screen.ids.song_name_.text = ''
            self.screen.ids.artist_name_.text = ''
            if self.search_timer:
                Clock.unschedule(self.search_timer)
            self.on_entering_menu_configurations(0,True)
        if instance == 2:
            self.on_entering_menu_configurations(0,False)
        else:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM songdetails")
            song_details_check_db3 = c.fetchall()
            if len(song_details_check_db3) == 0:
                self.screen.ids._screen_manager.current = '_empty_screen'
            else:
                self.screen.ids._screen_manager.current = '_menu_screen'
            conn.commit()
            conn.close()

    def enter_img_screen(self):
        self.screen.ids.image_list_.clear_widgets()
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM songimg")
        db_check = c.fetchall()
        count = 1
        for i in db_check:
            self.screen.ids.image_list_.add_widget(
                ImageTile(source=i[0],text=f'   {i[1]}')
            )
            count += 1
        conn.commit()
        conn.close()      
        self.screen.ids.image_list_.add_widget(
            AddImage()
        )

    def delete_image(self,name):
        img_name = name.strip()
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM songimg")
        keyword = f"DELETE FROM songimg WHERE name = '{img_name}'"
        c.execute(keyword)
        conn.commit()
        conn.close()
        self.updates_menu = True
        self.enter_img_screen()   

    def add_image(self):
        self.add_img = MDDialog(
            type='custom',
            content_cls=ContentDialog()
        )
        self.add_img.open()

    def check_link(self,link):
        check = self.check_url_using_django(link)
        if check:
            self.add_img.dismiss()
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute('SELECT *,oid FROM songimg')
            for_naming = c.fetchall()
            if len(for_naming) == 0:
                keyword = f"INSERT INTO songimg VALUES ('{link}','Image 1')"
                c.execute(keyword)
            else:
                image_name = str(for_naming[len(for_naming) - 1][1])[6::]
                keyword = f"INSERT INTO songimg VALUES ('{link}','Image {int(image_name) + 1}')"
                c.execute(keyword)
                c.execute('SELECT *,oid FROM songimg')
            conn.commit()
            conn.close()
            self.updates_menu = True 
            self.enter_img_screen()
        else:
            pass

    def check_url_using_django(self,url):
        validate = URLValidator()
        try:
            validate(str(url))
            return True
        except:
            return False

    def check_any_updates(self):
        if self.updates_menu == True:
            self.updates_menu = False
            self.on_entering_menu_configurations(1)
        else:
            pass

    def settings_dark_theme_switch(self,switch,value):
        if value == True:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            self.theme_cls.theme_style = "Dark"
            c.execute("SELECT *,oid FROM darktheme")
            c.execute("UPDATE darktheme SET state = 'on' WHERE oid = 1")
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            self.theme_cls.theme_style = "Light"
            c.execute("SELECT *,oid FROM darktheme")
            c.execute("UPDATE darktheme SET state = 'off' WHERE oid = 1")
            conn.commit()
            conn.close()

    def theme_picker(self):
        theme_color_list = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        bottom_sheet_color_picker = MDListBottomSheet()
        for colors_ in theme_color_list:
            bottom_sheet_color_picker.add_item(
                str(colors_),
                lambda z, y=colors_: self.theme_color_change_confirm(str(y))
            )
        bottom_sheet_color_picker.open()

    def theme_color_change_confirm(self,color):
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        self.theme_cls.primary_palette = color
        c.execute("SELECT *,oid FROM themecolor")
        keyword = "UPDATE themecolor SET color = '" + str(color) + "' WHERE oid = 1"
        c.execute(keyword)
        conn.commit()
        conn.close()

    def open_file_manager(self):
        self.file_manager = MDFileManager(
            exit_manager=self.file_manager_exit,
            select_path=self.file_manager_select_path,
            preview=False
        )
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM pathstart")
        path_check_db2 = c.fetchall()
        if self.is_valid_directory(path_check_db2[0][0]) == True:
            self.file_manager.show(path_check_db2[0][0])
        else:
            self.error2 = MDDialog(
                type='alert',
                text="[color=#000000]Provided Path is Currently Inaccessible, So Starting from 'C:/'[/color]" if self.theme_cls.theme_style == 'Light' else f"[color=#FFFFFF]Provided Path is Currently Inaccessible, So Starting from 'C:/'[size=18]?[/size][/color]",
                buttons=[
                    MDRaisedButton(
                        text='GOT IT',on_release= lambda x: self.dismiss_dialog()
                    )
                ]
            )
            self.error2.open()
        conn.commit()
        conn.close()

    def dismiss_dialog(self):
        self.error2.dismiss()
        self.file_manager.show('C:/')

    def file_manager_exit(self,*args):
        self.file_manager.close()

    def file_manager_select_path(self,path):
        checker = None
        org_path = str(path).replace("\\","/")
        song_name_making = ''

        for i in org_path[::-1]:
            if i == '/':
                break
            else:
                song_name_making += i

        song_name_making2 = song_name_making[::-1]

        if song_name_making2[-3::] == 'mp3':
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM songdetails")
            repeatation_path_check = c.fetchall()
            for i in repeatation_path_check:
                if i[0] == org_path:
                    checker = True

            if checker == True:
                Snackbar(
                    text='Selected Song is Already Added',
                    size_hint_x=1
                ).open()
                conn.commit()
                conn.close()
            else:
                self.file_accepted_as_mp3(org_path)
                conn.commit()
                conn.close()
        else:
            toast('Should Be An mp3 File')

    def file_accepted_as_mp3(self,path):
        self.file_manager.close()
        self.path = path
        self.screen.ids._screen_manager.current = '_add_song_screen'

    def split_and_add_space(self,string):
        if string.strip() != '':
            string_list = string.split()
            output_string = ""
            for i in range(len(string_list)):
                output_string += str(string_list[i]) + " "
            return output_string.strip().title()
        else:
            return string.strip()

    def confirm_song_details(self,song_name_,artist_name_):
        if artist_name_.strip() == 'Unknown':
            Snackbar(
                text='Invalid Artist Name, Try Changing It',
                size_hint_x=1
            ).open()
        else:
            checker = None
            song_name = self.split_and_add_space(song_name_)
            if artist_name_.isupper() == True:
                artist_name = artist_name_.strip()
            else:
                artist_name = self.split_and_add_space(artist_name_)
            if song_name != '' and len(song_name) <= 30 and len(artist_name) <= 30:
                if artist_name == '':
                    artist_name_py = 'Unknown'
                else:
                    artist_name_py = artist_name

                conn = sqlite3.connect('OneP.db')
                c = conn.cursor()
                c.execute("SELECT *,oid FROM songdetails")
                repeatation_song_name_check = c.fetchall()
                for i in repeatation_song_name_check:
                    if i[2] == song_name:
                        checker = True

                if checker == True:
                    Snackbar(
                        text='Song Name is Common, Try Changing It',
                        size_hint_x=1
                    ).open()
                    conn.commit()
                    conn.close()
                else:
                    test_duration = SoundLoader.load(filename=self.path)
                    self.duration = self.convert_to_format(int(test_duration._get_length())) 
                    keyword = f"INSERT INTO songdetails VALUES ('{self.path}','{artist_name_py}','{song_name}','{self.duration}')"  
                    c.execute(keyword)
                    c.execute("SELECT *,oid FROM songdetails")
                    conn.commit()
                    conn.close()
                    self.screen.ids.song_name_.text = ''
                    self.screen.ids.artist_name_.text = ''
                    self.path = ''
                    self.duration = ''
                    Clock.unschedule(self.search_timer) 
                    self.on_entering_menu_configurations(1)

    def on_entering_menu_configurations(self,refresh,toast_=False):
        if refresh == 1:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM songdetails")
            song_details_check_db = c.fetchall()

            if len(song_details_check_db) == 0:
                self.song_details = None
            else:
                self.song_details = []
                self.curr_playlist_songs.clear()
                self.curr_playlist_songs_path.clear()
                self.curr_playlist_songs_artist.clear()
                for i in song_details_check_db:
                    self.curr_playlist_songs.append(i[2])
                    self.curr_playlist_songs_path.append(i[0])
                    self.curr_playlist_songs_artist.append(i[1])
                self.single_occurence_artist = []
                for i in self.curr_playlist_songs_artist:
                    if i not in self.single_occurence_artist:
                        self.single_occurence_artist.append(i)

            if self.song_details == None:
                self.screen.ids._dummy_label.text = "Empty Playlist"
                self.screen.ids._screen_manager.current = '_empty_screen'
            else:
                c.execute("SELECT *,oid FROM songimg")
                db_img_check = c.fetchall()
                self.list_of_images.clear()
                for i in db_img_check:
                    self.list_of_images.append(i[0])
                self.screen.ids._song_list.clear_widgets()
                count = 0
                for i in song_details_check_db:
                    if count < len(self.list_of_images):
                        self.screen.ids._song_list.add_widget(
                            SongDetailsItem(text=i[2], text_sec=i[1], song_duration=i[3], img=self.list_of_images[count])
                        )
                    else:
                        self.screen.ids._song_list.add_widget(
                            SongDetailsItem(text=i[2], text_sec=i[1], song_duration=i[3], img='https://images.pexels.com/photos/6320/smartphone-vintage-technology-music.jpg?auto=compress&cs=tinysrgb&dpr=2&w=500')
                        )
                    count += 1
                self.screen.ids.all_details.text = f'   [size=20]All Songs[/size] ~ [size=15][font=Calibri]{len(self.curr_playlist_songs)} songs[/font][/size]'
                self.screen.ids._screen_manager.current = '_menu_screen'
            conn.commit()
            conn.close()
        if refresh == 0:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM songdetails")
            song_details_check_db2 = c.fetchall()

            if len(song_details_check_db2) == 0:
                self.screen.ids._screen_manager.current = '_empty_screen'
            else:
                self.screen.ids._screen_manager.current = '_menu_screen'

            conn.commit()
            conn.close()
            
        if toast_ == True:
            toast('No Songs Added')

    def delete_confirmation(self,song_name):
        if song_name == self.curr_active_song_name:
            self.denied = MDDialog(
                text=f"[color=#000000]'{song_name}' Is Currently Playing, Try Again After Changing It" if self.theme_cls.theme_style == 'Light' else f"[color=#FFFFFF]'{song_name}' Is Currently Playing, Try Again After Changing It",
                buttons=[
                    FocusMDRaisedButton(
                        text="GOT IT", on_release = self.got_it_delete
                    )
                ]
            )
            self.denied.open()
        else:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM songcon")
            db_check = c.fetchall()
            if db_check[0][0] == 'needed':
                self.curr_delete_song_name = song_name
                self.confirmation_widget = MDDialog(
                    text=f"[color=#000000]Are You Sure You Want To Delete '{song_name}' [size=18]?[/size][/color]" if self.theme_cls.theme_style == 'Light' else f"[color=#FFFFFF]Are You Sure You Want To Delete '{song_name}' [size=18]?[/size][/color]",
                    buttons=[
                        FocusMDFlatButton(
                            text="CANCEL", on_release = self.cancel_delete
                        ),
                        FocusMDRaisedButton(
                            text="DELETE", on_release = self.delete_song
                        ),
                    ],
                )
                self.confirmation_widget.open()
            else:
                self.curr_delete_song_name = song_name
                self.delete_song(1,1)

    def got_it_delete(self, instance):
        self.denied.dismiss()

    def delete_song(self,instance,extra=0):
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM songdetails")
        keyword = f"DELETE FROM songdetails WHERE songname = '{self.curr_delete_song_name}'"
        c.execute(keyword)
        conn.commit()
        conn.close()
        if extra == 0:
            self.confirmation_widget.dismiss()
        toast(f'{self.curr_delete_song_name} Deleted')
        self.on_entering_menu_configurations(1)

    def cancel_delete(self,instance):
        self.curr_delete_song_name = ''
        self.confirmation_widget.dismiss()

    def convert_to_format(self,seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        
        return "%02d:%02d:%02d" % (hour, minutes, seconds)

    def song_play_menu_screen(self,song_name,song_img,song_artist,screen_change,from_=0,auto=0):
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        keyword = f"SELECT * FROM songdetails WHERE songname = '{song_name}'"
        c.execute(keyword)
        details_song = c.fetchall()
        song_path = details_song[0][0]
        song_duration = details_song[0][3]
        conn.commit()
        conn.close()
        if self.is_valid_directory(song_path) == False:
            if auto == 1:
                self.screen.ids._screen_manager.current = '_menu_screen'
            self.show_error = MDDialog(
                text= f"[color=#000000]'{song_name}' Is Currently Inaccessible, Might Have Replaced, Removed or Renamed, Delete It And Re-add It To Solve The Issue[/color]" if self.theme_cls.theme_style == 'Light' else f"[color=#FFFFFF]'{song_name}' Is Currently Inaccessible, Might Have Replaced, Removed or Renamed, Delete It And Re-add It To Solve The Issue[/color]",
                buttons=[
                    MDRaisedButton(
                        text='GOT IT',on_release= lambda x: self.show_error.dismiss()
                    )
                ]
            )
            self.show_error.open()
        else:
            self.first_time = False
            self.screen.ids._song_name_song.text = song_name
            self.screen.ids._song_img_song.source = song_img
            self.screen.ids._artist_name_song.text = song_artist
            try:
                if self.song_controller._get_status() == 'play':
                    self.song_controller.stop()
                    self.list_pause_seek.clear()
            except:
                pass
            self.song_controller = SoundLoader.load(filename=str(song_path))
            self.song_controller.play()
            self.curr_active_song_path = str(song_path)
            self.curr_active_song_name = str(song_name)
            self.curr_active_song_duration_in_format = str(song_duration)
            self.screen.ids._song_slider.max = self.format_to_seconds(str(song_duration))
            self.screen.ids._play_pause_icon.icon = 'pause'
            self.screen.ids.song_duration_complete.text = self.curr_active_song_duration_in_format
            self.song_clearing_period = False
            if screen_change == 0:
                self.screen.ids.song_name_bottom_bar.text = ''
                self.screen.ids.song_name_bottom_bar2.text = ''
                # self.screen.ids._back_to_song_screen.font_size = 1
                # self.screen.ids._back_to_song_screen2.font_size = 1
                self.screen.ids.bottom_bar.size_hint_y = .00001   
                self.screen.ids.bottom_bar2.size_hint_y = .00001  
                def child_func(interval):
                    animate = Animation(
                        angle = 180,
                        duration = .2
                    )
                    animate.start(self.screen.ids._back_to_menu_from_song_screen)

                self.screen.ids._screen_manager.transition = CardTransition()
                self.screen.ids._screen_manager.transition.mode = 'push'
                self.screen.ids._screen_manager.transition.direction = 'up'
                self.screen.ids._screen_manager.transition.duration = .7
                Clock.schedule_once(child_func, .75)
                self.screen.ids._screen_manager.current = '_song_screen'
                self.screen.ids._screen_manager.transition = NoTransition()
                self.screen.ids._screen_manager.transition.duration = 0
                self.screen.ids._back_to_menu_from_song_screen.angle = 180
                if from_ == 1:
                    self.coming_from = '_menu_screen'
                else:
                    self.coming_from = self.coming_from_exclusive
            if self.screen.ids._screen_manager.current == '_menu_screen' or self.screen.ids._screen_manager.current == '_settings_screen':
                self.screen.ids.song_name_bottom_bar.text = str(song_name)
                self.screen.ids.song_name_bottom_bar2.text = str(song_name)
            
            self.song_slider_controller()

    def format_to_seconds(self,format):
        list_ = format.split(':')
        duration_in_sec = int(list_[0]) * 3600 + int(list_[1]) * 60 + int(list_[2])
        return duration_in_sec

    def back_from_song_screen(self):
        def child_func(interval):
            def chil_func2(interval):
                animate = Animation(
                    angle = 0,
                    duration = .2 
                )
                animate.start(self.screen.ids._back_to_song_screen)
                animate.start(self.screen.ids._back_to_song_screen2)

            self.screen.ids.bottom_bar.size_hint_y = .1
            self.screen.ids.bottom_bar2.size_hint_y = .09
            # self.screen.ids._back_to_song_screen.font_size = 24
            # self.screen.ids._back_to_song_screen2.font_size = 24
            self.screen.ids.song_name_bottom_bar.text = self.curr_active_song_name
            self.screen.ids.song_name_bottom_bar2.text = self.curr_active_song_name
            self.screen.ids._back_to_menu_from_song_screen.angle = 0
            Clock.schedule_once(chil_func2, .2)

        self.screen.ids._back_to_song_screen.angle = 180
        self.screen.ids._back_to_song_screen2.angle = 180
        self.screen.ids._screen_manager.transition = CardTransition()
        self.screen.ids._screen_manager.transition.mode = 'pop'
        self.screen.ids._screen_manager.transition.direction = 'down'
        self.screen.ids._screen_manager.transition.duration = .7
        Clock.schedule_once(child_func, .5)
        self.screen.ids._screen_manager.current = str(self.coming_from)
        self.screen.ids._screen_manager.transition = NoTransition()
        self.screen.ids._screen_manager.transition.duration = 0

    def scroll_toolbar_controller(self,position_):
        if len(self.curr_playlist_songs) >= 6: 
            position = round(position_,2)
            animate_toolbar_shrink = Animation(
                height = 80,
                duration = .3
            )

            animate_toolbar_enlarge = Animation(
                height = 150,
                duration = .3
            )
            if position < .90 :
                if self.screen.ids.toolbar_menu.height != 80:
                    animate_toolbar_shrink.start(self.screen.ids.toolbar_menu)
            elif position > .90:
                if self.screen.ids.toolbar_menu.height != 150:
                    animate_toolbar_enlarge.start(self.screen.ids.toolbar_menu)
        else:
            if self.screen.ids.toolbar_menu.height != 150:
                animate_toolbar_enlarge2 = Animation(
                    height = 150,
                    duration = .3
                )
                animate_toolbar_enlarge2.start(self.screen.ids.toolbar_menu)

    def pause_play(self):
        if self.song_controller._get_status() == 'play':
            print(10)
            self.screen.ids._play_pause_icon.icon = 'play'
            self.song_clearing_period = True
            self.pause_song()
        else:
            print(20)
            self.song_clearing_period = True
            self.song_controller.play()
            self.song_controller.volume = 0
            self.screen.ids._play_pause_icon.icon = 'pause'
            self.play_song_from_pause()

    def play_song_from_pause(self):
        def play_from_seek(interval):
            self.song_controller.seek(self.list_pause_seek[-1])
            self.song_clearing_period = False
            self.song_controller.volume = 0
            Clock.schedule_once(play_from_seek2,.03)
        def play_from_seek2(interval):
            self.song_controller.volume = (self.screen.ids._song_sound_slider.value/100) / 2
            Clock.schedule_once(play_from_seek3,.02)
        def play_from_seek3(interval):
            self.song_controller.volume = self.screen.ids._song_sound_slider.value/100

        Clock.schedule_once(play_from_seek,.5)

    def pause_song(self):
        def child_pause(interval):
            self.list_pause_seek.append(self.song_controller.get_pos())
            self.song_controller.volume = 0
            print(self.list_pause_seek)
            self.song_controller.stop()

        self.song_controller.volume = (self.screen.ids._song_sound_slider.value/100) / 2
        Clock.schedule_once(child_pause,.1)

    def song_slider_controller(self):
        def child_func(inteval):
            if self.song_clearing_period == False:
                if self.song_controller._get_status() == 'play':
                    self.screen.ids.song_duration_covered.text = self.convert_to_format(int(self.song_controller.get_pos()))
                    if self.slider_press == False:
                        self.screen.ids._song_slider.value = int(self.song_controller.get_pos())
                else:
                    index = self.curr_playlist_songs.index(self.curr_active_song_name)
                    length = len(self.curr_playlist_songs)
                    if length != index + 1:
                        try:
                            self.song_play_menu_screen(self.curr_playlist_songs[index + 1], self.list_of_images[index + 1], self.curr_playlist_songs_artist[index + 1],1)
                        except:
                            self.song_play_menu_screen(self.curr_playlist_songs[index + 1], self.default_img, self.curr_playlist_songs_artist[index + 1],1)
                    else:
                        try:
                            self.song_play_menu_screen(self.curr_playlist_songs[0], self.list_of_images[0], self.curr_playlist_songs_artist[0],1,0,1)
                        except:
                            self.song_play_menu_screen(self.curr_playlist_songs[0], self.default_img, self.curr_playlist_songs_artist[0],1,0,1)

            else:
                pass

        Clock.schedule_interval(child_func, .1)

    def song_seek(self,slider,state,value):
        self.slider_press = True
        if state == False:
            if self.song_controller._get_status() == 'play':
                self.song_controller.seek(value)
                self.slider_press = False
            else:
                self.list_pause_seek.append(value)
                self.slider_press = False

    def song_volume_controller(self,slider,state,value):
        global event
        if state == True:
            event = Clock.schedule_interval(self.song_volume_controller_child,.10)
        if state == False:
            Clock.unschedule(event)

    def song_volume_controller_child(self,interval):
        self.song_controller.volume = self.screen.ids._song_sound_slider.value/100
        if self.screen.ids._song_sound_slider.value/100 > .75:
            self.screen.ids.volume_icon.icon = 'volume-high'
        elif self.screen.ids._song_sound_slider.value/100 > .25:
            self.screen.ids.volume_icon.icon = 'volume-medium'
        elif self.screen.ids._song_sound_slider.value/100 > 0:
            self.screen.ids.volume_icon.icon = 'volume-low'
        elif self.screen.ids._song_sound_slider.value/100 == 0:
            self.screen.ids.volume_icon.icon = 'volume-off'

    def next_song_play(self):
        index = self.curr_playlist_songs.index(self.curr_active_song_name)
        length = len(self.curr_playlist_songs)
        if length != index + 1:
            try:
                self.song_play_menu_screen(self.curr_playlist_songs[index + 1], self.list_of_images[index + 1], self.curr_playlist_songs_artist[index + 1],1)
            except:
                self.song_play_menu_screen(self.curr_playlist_songs[index + 1], self.default_img, self.curr_playlist_songs_artist[index + 1],1)
        else:
            pass

    def previous_song_play(self):
        index = self.curr_playlist_songs.index(self.curr_active_song_name)
        if index != 0:
            try:
                self.song_play_menu_screen(self.curr_playlist_songs[index - 1], self.list_of_images[index - 1], self.curr_playlist_songs_artist[index - 1],1)
            except:
                self.song_play_menu_screen(self.curr_playlist_songs[index - 1], self.default_img, self.curr_playlist_songs_artist[index - 1],1)
        else:
            pass

    def move_to_song_menu(self, screen, coming_from):
        self.coming_from = str(screen)
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM songdetails")
        check_first = c.fetchall()
        song_name = check_first[0][2]
        song_artist = check_first[0][1]
        try:
            song_img = self.list_of_images[0]
        except:
            song_img = self.default_img
        song_path = check_first[0][0]
        conn.commit()
        conn.close()
        if self.is_valid_directory(song_path) == False:
            self.show_error = MDDialog(
                text= f"[color=#000000]'{song_name}' Is Currently Unaccessible, Might Have Replaced, Removed or Renamed, Delete It And Re-add It To Solve The Issue[/color]" if self.theme_cls.theme_style == 'Light' else f"[color=#FFFFFF]'{song_name}' Is Currently Unaccessible, Might Have Replaced, Removed or Renamed, Delete It And Re-add It To Solve The Issue[/color]",
                buttons=[
                    MDRaisedButton(
                        text='GOT IT',on_release= lambda x: self.show_error.dismiss()
                    )
                ]
            )
            self.show_error.open()
        else:
            if self.first_time == True:
                self.song_play_menu_screen(song_name,song_img,song_artist,0,1)
            else:
                # self.screen.ids._back_to_song_screen.font_size = 1
                # self.screen.ids._back_to_song_screen2.font_size = 1
                self.screen.ids.song_name_bottom_bar.text = ''
                self.screen.ids.song_name_bottom_bar2.text = ''
                self.screen.ids.bottom_bar.size_hint_y = .00001
                self.screen.ids.bottom_bar2.size_hint_y = .00001
                def child_func(interval):
                    animate = Animation(
                        angle = 180,
                        duration = .2
                    )
                    animate.start(self.screen.ids._back_to_menu_from_song_screen)

                self.screen.ids._screen_manager.transition = CardTransition()
                self.screen.ids._screen_manager.transition.mode = 'push'
                self.screen.ids._screen_manager.transition.direction = 'up'
                self.screen.ids._screen_manager.transition.duration = .7
                Clock.schedule_once(child_func, .75)
                self.screen.ids._screen_manager.current = '_song_screen'
                self.screen.ids._screen_manager.transition = NoTransition()
                self.screen.ids._screen_manager.transition.duration = 0

    def check_empty_playlist(self):
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM songdetails")
        check_empty = c.fetchall()
        if len(check_empty) == 0:
            self.screen.ids.song_name_bottom_bar2.text = ''
            # self.screen.ids._back_to_song_screen.font_size = 1
            # self.screen.ids._back_to_song_screen2.font_size = 1
            self.screen.ids.bottom_bar2.size_hint_y = .00001
        else:
            pass
        conn.commit()
        conn.close()

    def sound_icon_button(self):
        if self.screen.ids._song_sound_slider.value != 0:
            self.song_controller.volume = 0
            self.screen.ids.volume_icon.icon = 'volume-off'
            self.song_slider_tracker.append(self.screen.ids._song_sound_slider.value)
            self.screen.ids._song_sound_slider.value = 0
        else:
            self.song_controller.volume = self.song_slider_tracker[-1]/100
            self.screen.ids.volume_icon.icon = 'volume-high'
            self.screen.ids._song_sound_slider.value = self.song_slider_tracker[-1]
            self.song_volume_controller_child(1)

    def is_valid_directory(self,filename):
        p = Path(filename)
        return p.exists()

    def show_current_path(self):
        conn = sqlite3.connect('OneP.db')
        c = conn.cursor()
        c.execute("SELECT * FROM pathstart")
        db_check = c.fetchall()
        path = db_check[0][0]
        toast(str(path))
        conn.commit()
        conn.close()

    def open_file_manager_for_path_change(self):
        self.file_manager_path = MDFileManager(
            exit_manager=self.file_manager_path_exit,
            select_path=self.file_manager_path_select_path,
            preview=False
        )
        self.file_manager_path.show('C:/')
        
    def file_manager_path_exit(self, *args):
        self.file_manager_path.close()

    def file_manager_path_select_path(self,path_):
        path = str(path_).replace("\\","/")
        is_file = os.path.isfile(path)
        if is_file:
            pass
        else:
            conn = sqlite3.connect('OneP.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM pathstart")
            keyword = f"UPDATE pathstart SET path = '{path}' WHERE oid = 1"
            c.execute(keyword)
            self.file_manager_path.close()
            conn.commit()
            conn.close()

if __name__ == '__main__':
    OnePlayer().run()
