import tkinter as tk #line:1
from tkinter import ttk #line:2
import json #line:3
import os #line:4
import threading #line:5
import time #line:6
from datetime import datetime ,timedelta #line:7
import matplotlib .pyplot as plt #line:8
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:9
import winreg #line:10
from pystray import Icon ,MenuItem ,Menu #line:11
from PIL import Image ,ImageDraw #line:12
DATA_FILE ="usage_data.json"#line:15
BG_COLOR ="#1e1e1e"#line:16
BTN_COLOR ="#333333"#line:17
FG_COLOR ="#ffffff"#line:18
APP_NAME ="GDCE Time Tracker"#line:19
def load_data ():#line:22
    if os .path .exists (DATA_FILE ):#line:23
        with open (DATA_FILE ,"r")as OO00OOO000000OO00 :#line:24
            return json .load (OO00OOO000000OO00 )#line:25
    return {}#line:26
def save_data (OOOO0OOOOO0O0O0O0 ):#line:28
    with open (DATA_FILE ,"w")as O00OOO00O000O0O00 :#line:29
        json .dump (OOOO0OOOOO0O0O0O0 ,O00OOO00O000O0O00 )#line:30
class Tracker :#line:33
    def __init__ (OO0OOO0O0OO00OO0O ):#line:34
        OO0OOO0O0OO00OO0O .running =True #line:35
        OO0OOO0O0OO00OO0O .data =load_data ()#line:36
        OO0OOO0O0OO00OO0O .today =datetime .now ().date ().isoformat ()#line:37
        OO0OOO0O0OO00OO0O .data .setdefault (OO0OOO0O0OO00OO0O .today ,0 )#line:38
        threading .Thread (target =OO0OOO0O0OO00OO0O .track ,daemon =True ).start ()#line:39
    def track (O000OO0O0O0O00O0O ):#line:41
        while O000OO0O0O0O00O0O .running :#line:42
            time .sleep (1 )#line:43
            O000OO0O0O0O00O0O .data [O000OO0O0O0O00O0O .today ]+=1 #line:44
            save_data (O000OO0O0O0O00O0O .data )#line:45
    def stop (O0O0OO0O00OO0OO0O ):#line:47
        O0O0OO0O00OO0OO0O .running =False #line:48
        save_data (O0O0OO0O00OO0OO0O .data )#line:49
class TimeTrackerApp :#line:52
    def __init__ (O0OOOO00OO0OOO0O0 ,O0000O00OOO0OO0O0 ):#line:53
        O0OOOO00OO0OOO0O0 .root =O0000O00OOO0OO0O0 #line:54
        O0OOOO00OO0OOO0O0 .root .title ("GDCE Time Tracker")#line:55
        O0OOOO00OO0OOO0O0 .root .configure (bg =BG_COLOR )#line:56
        O0OOOO00OO0OOO0O0 .tracker =Tracker ()#line:58
        O0OOOO00OO0OOO0O0 .label =tk .Label (O0000O00OOO0OO0O0 ,text ="🕒 GDCE Time Tracker",font =("Segoe UI",16 ,"bold"),bg =BG_COLOR ,fg =FG_COLOR )#line:60
        O0OOOO00OO0OOO0O0 .label .pack (pady =5 )#line:61
        O0OOOO00OO0OOO0O0 .today_time_label =tk .Label (O0000O00OOO0OO0O0 ,text ="",font =("Segoe UI",12 ),bg =BG_COLOR ,fg =FG_COLOR )#line:63
        O0OOOO00OO0OOO0O0 .today_time_label .pack ()#line:64
        O0OOOO00OO0OOO0O0 .total_time_label =tk .Label (O0000O00OOO0OO0O0 ,text ="",font =("Segoe UI",12 ),bg =BG_COLOR ,fg =FG_COLOR )#line:66
        O0OOOO00OO0OOO0O0 .total_time_label .pack ()#line:67
        O0OOOO00OO0OOO0O0 .btn_frame =tk .Frame (O0000O00OOO0OO0O0 ,bg =BG_COLOR )#line:70
        O0OOOO00OO0OOO0O0 .btn_frame .pack (pady =10 )#line:71
        O0OOOO00OO0OOO0O0 .btn_today =tk .Button (O0OOOO00OO0OOO0O0 .btn_frame ,text ="Today",bg =BTN_COLOR ,fg =FG_COLOR ,command =O0OOOO00OO0OOO0O0 .show_today )#line:73
        O0OOOO00OO0OOO0O0 .btn_week =tk .Button (O0OOOO00OO0OOO0O0 .btn_frame ,text ="This Week",bg =BTN_COLOR ,fg =FG_COLOR ,command =O0OOOO00OO0OOO0O0 .show_week )#line:74
        O0OOOO00OO0OOO0O0 .btn_month =tk .Button (O0OOOO00OO0OOO0O0 .btn_frame ,text ="This Month",bg =BTN_COLOR ,fg =FG_COLOR ,command =O0OOOO00OO0OOO0O0 .show_month )#line:75
        for OO00OOO0O00O0000O in [O0OOOO00OO0OOO0O0 .btn_today ,O0OOOO00OO0OOO0O0 .btn_week ,O0OOOO00OO0OOO0O0 .btn_month ]:#line:77
            OO00OOO0O00O0000O .config (width =12 )#line:78
            OO00OOO0O00O0000O .pack (side =tk .LEFT ,padx =5 )#line:79
        O0OOOO00OO0OOO0O0 .graph_frame =tk .Frame (O0000O00OOO0OO0O0 ,bg =FG_COLOR )#line:82
        O0OOOO00OO0OOO0O0 .graph_frame .pack (fill =tk .BOTH ,expand =True )#line:83
        O0OOOO00OO0OOO0O0 .update_today_label ()#line:85
        O0OOOO00OO0OOO0O0 .update_total_usage_label ()#line:86
        O0OOOO00OO0OOO0O0 .show_today ()#line:87
        O0OOOO00OO0OOO0O0 .update_clock ()#line:88
    def update_clock (OO00OO00O0O0OO0OO ):#line:90
        OO00OO00O0O0OO0OO .update_today_label ()#line:91
        OO00OO00O0O0OO0OO .update_total_usage_label ()#line:92
        OO00OO00O0O0OO0OO .root .after (1000 ,OO00OO00O0O0OO0OO .update_clock )#line:93
    def update_today_label (O00000OOOOOOOOOOO ):#line:95
        O00OO0O0O00000000 =load_data ()#line:96
        O000000OOOO0OOO00 =O00OO0O0O00000000 .get (datetime .now ().date ().isoformat (),0 )#line:97
        O00OO0O000O0O0O0O ,O0O000OO000O0O0OO =divmod (O000000OOOO0OOO00 //60 ,60 )#line:98
        O000OO000O0000O00 =O000000OOOO0OOO00 %60 #line:99
        O00000OOOOOOOOOOO .today_time_label .config (text =f"Today: {O00OO0O000O0O0O0O}h {O0O000OO000O0O0OO}m {O000OO000O0000O00}s")#line:100
    def update_total_usage_label (OOO0O0OOOO000O0O0 ):#line:102
        O0OOO0OOO0000OO00 =load_data ()#line:103
        O0O0OOOOO0O00O000 =sum (O0OOO0OOO0000OO00 .values ())#line:104
        OOO00OOO00O0OOOO0 ,O0O000OOOOOOO0O0O =divmod (O0O0OOOOO0O00O000 //60 ,60 )#line:105
        OO0OOO00OOO0OOO00 =O0O0OOOOO0O00O000 %60 #line:106
        OOO0O0OOOO000O0O0 .total_time_label .config (text =f"Total: {OOO00OOO00O0OOOO0}h {O0O000OOOOOOO0O0O}m {OO0OOO00OOO0OOO00}s")#line:107
    def get_data_range (OO00OOOOO0O0OOO0O ,O000OOOOO0O000OOO ):#line:109
        OOOO0OOOOO00OOO0O =load_data ()#line:110
        OO0O0O0000OO0O00O =datetime .now ().date ()#line:111
        OOOO0O000O000O000 =[]#line:112
        for OOOOOO0000OOO0O0O in range (O000OOOOO0O000OOO ):#line:113
            O000O00OOOOOO0OO0 =OO0O0O0000OO0O00O -timedelta (days =OOOOOO0000OOO0O0O )#line:114
            OOOOOOOO00000O0O0 =O000O00OOOOOO0OO0 .isoformat ()#line:115
            OO0O0OOOO00OO0OOO =OOOO0OOOOO00OOO0O .get (OOOOOOOO00000O0O0 ,0 )#line:116
            OOOO0O000O000O000 .append ((OOOOOOOO00000O0O0 ,round (OO0O0OOOO00OO0OOO /3600 ,2 )))#line:117
        return list (reversed (OOOO0O000O000O000 ))#line:118
    def show_graph (O0OOOO0OO0000OOOO ,OOOO00O0O0O000000 ,OOO0OO00O0O0O000O ):#line:120
        for O000O0OO0O0O0O0OO in O0OOOO0OO0000OOOO .graph_frame .winfo_children ():#line:121
            O000O0OO0O0O0O0OO .destroy ()#line:122
        O00OOOOOOO00OOO00 ,O0OO00O000OO00OO0 =plt .subplots (figsize =(6 ,3 ),facecolor ='white')#line:124
        OOOOOO0O00000O000 =[O0OO0O0OOOO0OOO00 [0 ]for O0OO0O0OOOO0OOO00 in OOO0OO00O0O0O000O ]#line:125
        O000OOO00OOO00O00 =[OOOO0O000O0OO0O00 [1 ]for OOOO0O000O0OO0O00 in OOO0OO00O0O0O000O ]#line:126
        O0OO00O000OO00OO0 .bar (OOOOOO0O00000O000 ,O000OOO00OOO00O00 ,color ="#4da6ff")#line:128
        O0OO00O000OO00OO0 .set_title (OOOO00O0O0O000000 )#line:129
        O0OO00O000OO00OO0 .set_ylabel ("Hours")#line:130
        plt .xticks (rotation =45 )#line:131
        O0O00O00OOOO0OOO0 =FigureCanvasTkAgg (O00OOOOOOO00OOO00 ,master =O0OOOO0OO0000OOOO .graph_frame )#line:133
        O0O00O00OOOO0OOO0 .draw ()#line:134
        O0O00O00OOOO0OOO0 .get_tk_widget ().pack (fill =tk .BOTH ,expand =True )#line:135
        plt .close (O00OOOOOOO00OOO00 )#line:138
    def show_today (OOO0OOOO0O0OO0OOO ):#line:140
        OOOOO0O00000O0OO0 =OOO0OOOO0O0OO0OOO .get_data_range (1 )#line:141
        OOO0OOOO0O0OO0OOO .show_graph ("Usage (Today)",OOOOO0O00000O0OO0 )#line:142
    def show_week (OOOO0OOO00O0OO00O ):#line:144
        OO00OOO000OO0OOO0 =OOOO0OOO00O0OO00O .get_data_range (7 )#line:145
        OOOO0OOO00O0OO00O .show_graph ("Usage (Last 7 Days)",OO00OOO000OO0OOO0 )#line:146
    def show_month (OO00OO000000000OO ):#line:148
        OO0O0OOOOO0O00000 =OO00OO000000000OO .get_data_range (30 )#line:149
        OO00OO000000000OO .show_graph ("Usage (Last 30 Days)",OO0O0OOOOO0O00000 )#line:150
    def on_close (O0OO0000OOO000OOO ):#line:152
        O0OO0000OOO000OOO .tracker .stop ()#line:153
        O0OO0000OOO000OOO .root .withdraw ()#line:154
def set_startup ():#line:157
    OOO0O0OOO0OOO000O =os .path .abspath (__file__ )#line:158
    OO0OOOOO0O00OO0O0 =winreg .HKEY_CURRENT_USER #line:159
    OOOOOOO0O000O000O =r"Software\Microsoft\Windows\CurrentVersion\Run"#line:160
    OOOOO0000OO0OOO00 =winreg .OpenKey (OO0OOOOO0O00OO0O0 ,OOOOOOO0O000O000O ,0 ,winreg .KEY_SET_VALUE )#line:161
    winreg .SetValueEx (OOOOO0000OO0OOO00 ,APP_NAME ,0 ,winreg .REG_SZ ,OOO0O0OOO0OOO000O )#line:162
    winreg .CloseKey (OOOOO0000OO0OOO00 )#line:163
def create_tray_icon (OOOO0OOO00O0OO0OO ):#line:166
    try :#line:168
        O000OOO00000000O0 =Image .open ("logo.png")#line:169
    except FileNotFoundError :#line:170
        print ("logo.png not found. Using a default icon.")#line:171
        O000OOO00000000O0 =Image .new ('RGB',(64 ,64 ),color ='gray')#line:172
    O0000OOOOO0000OO0 =Icon (APP_NAME )#line:174
    O0000OOOOO0000OO0 .icon =O000OOO00000000O0 #line:175
    O0000OOOOO0000OO0 .menu =Menu (MenuItem ("Show",lambda O00OO00O0OOO0O0OO ,O0O0OOO0OOOO00000 :OOOO0OOO00O0OO0OO .root .deiconify ()),MenuItem ("Exit",lambda OO0OOO0OOOO0OOO00 ,O000000O000O000OO :OO0OOO0OOOO0OOO00 .stop ()))#line:176
    O0000OOOOO0000OO0 .run ()#line:177
if __name__ =="__main__":#line:180
    set_startup ()#line:181
    root =tk .Tk ()#line:182
    app =TimeTrackerApp (root )#line:183
    root .protocol ("WM_DELETE_WINDOW",app .on_close )#line:184
    threading .Thread (target =create_tray_icon ,args =(app ,),daemon =True ).start ()#line:187
    root .mainloop ()#line:189
