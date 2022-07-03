# -*- coding: utf-8 -*-
from distutils.spawn import spawn
from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
from spotify import Spotify

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "google-chrome"  # My browser of choice

keys = [
    ### The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show drun"),
        desc='Run Launcher'
        ),
    Key([mod, "shift"], "n",
        lazy.spawn("rofi-wifi-menu.sh"),
        desc='Run Launcher'
        ),    
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='Qutebrowser'
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod, "shift"], "c",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    Key(["control", "shift"], "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc='Doom Emacs'
        ),

    ### Media and Brightness Keys
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+"),
        desc='Function Key'
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%-"),
        desc='Function Key'
        ),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl --player=spotify,%any play-pause"),
        desc='Function Key'
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl --player=spotify,%any next"),
        desc='Function Key'
        ),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl --player=spotify,%any previous"),
        desc='Function Key'
        ),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 20+"),
        desc='Function Key'
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 20-"),
        desc='Function Key'
        ),
    Key([], "Print",
        lazy.spawn("flameshot gui"),
        desc='Function Key'
        ),

    ### Switch focus to specific monitor (out of three)
    Key([mod], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    Key([mod], "r",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 3'
        ),
    ### Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    ### Treetab controls
    Key([mod, "shift"], "h",
        lazy.layout.move_left(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.move_right(),
        desc='Move down a section in treetab'
        ),
    ### Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    ### Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    ### Shortcuts 
        Key([mod, "shift"], "m",
        lazy.spawn("flatpak run com.spotify.Client"),
        desc='Open Spotify'
        )
]

groups = [Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='floating')]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "#ebdbb2",
                "border_normal": "#458588"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #   layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #      section_fontsize = 10,
    #      border_width = 2,
    #      bg_color = "1c1f24",
    #      active_bg = "c678dd",
    #      active_fg = "000000",
    #      inactive_bg = "a9a1e1",
    #      inactive_fg = "1c1f24",
    #      padding_left = 0,
    #      padding_x = 0,
    #      padding_y = 5,
    #      section_top = 10,
    #      section_bottom = 20,
    #      level_shift = 8,
    #      vspace = 3,
    #      panel_width = 200
    #      ),
     layout.Floating(**layout_theme)
]

colors = [["#282828", "#282828"],#0
          ["#32302f", "#32302f"],#1
          ["#ebdbb2", "#ebdbb2"],#2
          ["#ff6c6b", "#ff6c6b"],#3
          ["#b8bb26", "#b8bb26"],#4
          ["#fabd2f", "#fabd2f"],#5
          ["#b16286", "#b16286"],#6
          ["#458588", "#458588"],#7
          ["#3c3836", "#3c3836"],#8
          ["#00000000", "#00000000"]]#9

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=12,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[5]
        ),
        # widget.Image(
        #     filename="~/.config/qtile/icons/fedora.png",
        #     scale="True",
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
        #     background=colors[5],
        #     margin=4
        # ),
        widget.TextBox(
            text='',
            font="Font Awesome 6 Free",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
            background=colors[5],
            foreground=colors[0],
            padding=4,
            fontsize=16,
        ),

        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[0],
            foreground=colors[5],
            padding=0,
            fontsize=30,
        ),
                widget.Sep(
            linewidth=0,
            padding=8,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Font Awesome 6 Free",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=1,
            borderwidth=1,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[5],
            this_screen_border=colors[4],
            other_current_screen_border=colors[2],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[7],
            foreground=colors[0],
            padding=0,
            fontsize=30,
        ),
        widget.CurrentLayout(
            fmt=' {}',
            foreground=colors[2],
            background=colors[7],
            padding=5
        ),
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[2],
            foreground=colors[7],
            padding=0,
            fontsize=30,
        ),
        widget.WindowName(
            foreground=colors[0],
            background=colors[2],
            padding=8,
            max_chars=40,
            width=300
        ),
        widget.Sep(
            linewidth=0,
            padding=0,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[0],
            foreground=colors[2],
            padding=0,
            fontsize=37
        ),
        widget.Spacer(
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        Spotify(
            background=colors[0],
            foreground=colors[2]
        ),
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[0],
            foreground=colors[2],
            padding=0,
            fontsize=37
        ),
        widget.Memory(
            foreground=colors[0],
            background=colors[2],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm)},
            fmt='Mem:{}',
            measure_mem='G',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[2],
            foreground=colors[7],
            padding=0,
            fontsize=30
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[7],
            fmt='Vol:{} ',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[7],
            foreground=colors[0],
            padding=0,
            fontsize=30
        ),
        widget.Clock(
            foreground=colors[2],
            background=colors[0],
            format="%H:%M %d "
        ), 
        ### Battery 
        widget.TextBox(
            text='',
            font="JetBrainsMonoMedium Nerd Font Mono",
            background=colors[0],
            foreground=colors[5],
            padding=0,
            fontsize=30
        ),
        widget.Battery(
            foreground=colors[0],
            background=colors[5],
            format='{percent:2.0%} ',
            padding=2
        ),
        widget.Systray(
            foreground=colors[0],
            background=colors[5],
            padding=2
        )
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # Slicing removes unwanted widgets (systray) on Monitors 1,3
    del widgets_screen1[9:10]
    return widgets_screen1



def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20, margin=[0, 0, 0, 0]))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    #widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


wmname = "Qtile"


start = [
    "xinput set-prop \"Asus TouchPad\" \"libinput Tapping Enabled\" 1",
    "xinput set-prop \"Asus TouchPad\" \"libinput Natural Scrolling Enabled\" 1",
    "setxkbmap latam",
    "nitrogen --restore",
    "picom --experimental-backends &",
#    "xfce4-power-manager &",
#    "xcape -e 'Super_L=Super_L|Shift_L|Return'"
]

for x in start:
    os.system(x)

