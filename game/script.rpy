
define s = Character("Sekadi")
define m = Character("Monika")
define n = Character("Natsuki")
define p = Character("Pinecone")

image monaflip = im.Flip("mona.png", horizontal=True)
image monadark = im.MatrixColor("mona.png", im.matrix.brightness(-0.5))
image pinedark = im.MatrixColor("bpine.png", im.matrix.brightness(-0.2))
image suzudark = im.MatrixColor("bsuzu.png", im.matrix.brightness(-0.2))

image ripa:
    "ripa_a"
    pause 0.1
    "ripa_b"
    pause 0.1
    "ripa_c"
    pause 0.1
    "ripa_d"
    pause 0.1
    "ripa_e"
    pause 0.1
    choice:
        pass
    choice:
        pass
    choice:
        pass
    choice:
        "ripab_a"
        pause 0.1
        "ripab_b"
        pause 0.1
    repeat

image ripb:
    "ripb_a"
    pause 0.1
    "ripb_b"
    pause 0.1
    "ripb_c"
    pause 0.1
    "ripb_d"
    pause 0.1
    "ripb_e"
    pause 0.1
    choice:
        pass
    choice:
        pass
    choice:
        pass
    choice:
        "ripbb_a"
        pause 0.1
        "ripbb_b"
        pause 0.1
    repeat


transform awal_posisi(y_start):
    subpixel True
    xalign 0.5 yalign y_start alpha 1.0 zoom 0.95 blur 0.0
    ease 0.5 zoom 1.0
    
transform char_show(x_start=0.5):
    subpixel True
    xalign (x_start-0.05) alpha 0.0
    ease 0.5 xalign x_start alpha 1.0
    
transform screen_fade:
    alpha 0.0
    ease 1.0 alpha 1.0
    
transform mouth_move:
    subpixel True
    align(0.572, 0.425) zoom 0.6 rotate -5 yzoom 0.6 xzoom 0.7
    block:
        parallel:  # y
            ease_quad 1.0 yzoom 0.25
            ease_quad 1.0 yzoom 0.6
        parallel:  # x
            ease_quad 1.0 xzoom 0.5
            ease_quad 1.0 xzoom 0.7
        repeat


init python:
    renpy.music.register_channel("ambient", mixer="sound", loop=True)



default ikan = False

screen touche():
    modal True
    
    hbox:
        textbutton "Wine" action Play("music", "actionsong.mp3")
        add "blapp"
        text "Halo atau apa gitu"
    
    # Hover toggle changes variable
    imagebutton:
        align(0.5, 1.0)
        idle "bpine"
        hover "bsuzu"
        
        hovered ToggleVariable("ikan")
        
        action Play("music", "bgm005.ogg")

        
    if ikan == True:
        add "perlica"


image siji = im.Crop("cg1.png", (0,0, 400, 400))

screen pinecone():
    
    frame:
        area(500, 200, 400, 400)
        background "siji"
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "horizontal", "vertical"
            
            vbox:
                text "Perlica UwU":
                    color "#fff"
                add "perlica"
                text "Pinecone OwO":
                    color "#fff"
                add "bpine"


image bsaga = im.Blur("bsaga.png", 1)

image trasnform:
    "bsaga.png"
    pause 1.0
    "blapp.png"
    pause 1.0
    repeat
    
image blappsaga:
    "bsaga"
    pause 0.5
    "blapp"
    pause 0.5
    repeat

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 10 rotate 360
    repeat
    
screen test:
    add "bsaga.png" at rotation

image ripa:
    "ripa_a"
    pause 0.1
    "ripa_b"
    pause 0.1
    "ripa_c"
    pause 0.1
    "ripa_d"
    pause 0.1
    "ripa_e"
    pause 0.1
    choice:
        "ripa_a"
        pause 0.1
        "ripa_b"
        pause 0.1
        "ripa_c"
        pause 0.1
        "ripa_d"
        pause 0.1
        "ripa_e"
        pause 0.1
    choice:
        "ripab_a"
        pause 0.1
        "ripab_b"
        pause 0.1
    repeat
    
image ripb:
    "ripb_a"
    pause 0.1
    "ripb_b"
    pause 0.1
    "ripb_c"
    pause 0.1
    "ripb_d"
    pause 0.1
    "ripb_e"
    pause 0.1
    choice:
        "ripb_a"
        pause 0.1
        "ripb_b"
        pause 0.1
        "ripb_c"
        pause 0.1
        "ripb_d"
        pause 0.1
        "ripb_e"
        pause 0.1
    choice:
        "ripbb_a"
        pause 0.1
        "ripbb_b"
        pause 0.1
    repeat
    
image rip:
    # Do normal
    choice:
        choice:
            "ripa_a"
            pause 0.1
            "ripa_b"
            pause 0.1
            "ripa_c"
            pause 0.1
            "ripa_d"
            pause 0.1
            "ripa_e"
            pause 0.1
        choice:
            "ripb_a"
            pause 0.1
            "ripb_b"
            pause 0.1
            "ripb_c"
            pause 0.1
            "ripb_d"
            pause 0.1
            "ripb_e"
            pause 0.1
    # Do blinking
    choice:
        choice:
            "ripab_a"
            pause 0.1
            "ripab_b"
            pause 0.1
        
        choice:
            "ripbb_a"
            pause 0.1
            "ripbb_b"
            pause 0.1
    repeat


screen blender():
    tag idk
    modal True
    
    textbutton "{size=50}Do something{/size}":
        xalign 0.5 yalign 0.0
        action Screenshot()
        
    textbutton "{size=50}STOPU{/size}":
        xalign 0.5 yalign 0.15
        action FileSave("TrueWay", confirm=False, page=7)
        
    timer 4.0 action Screenshot()
    timer 2.4 action Screenshot()

label idk:
    
    "hi"

define pov = Character("[povname]")


default x_pos = 0
screen mov():
    python:
        if x_pos < 720:
            x_pos += 3
        
    add "pc_b":
        xpos x_pos yalign 1.0 zoom 0.75
    
    timer 0.03 action renpy.restart_interaction repeat True
        




# Without
#transform down:
#    subpixel True
#    linear 2.0 xpos 720
    
screen apaya():
    add "mouth":
        zoom 1.5 xpos x_pos
    
    text "x_pos = [x_pos]":
        xalign 0.0 yalign 0.5
        color "#fff"
    
    if x_pos < 720:
        timer 0.01 repeat True action SetVariable('x_pos', x_pos+2)
        

default x_nat = 0
default x_mon = 500
default collided = False

screen collision:
    
    add "nata":
        xpos x_nat yalign 1.0 zoom 0.75
    
    add "monb":
        xpos x_mon yalign 1.0 zoom 0.75
    
    if collided == False:
        if x_nat < 125:
            timer 0.01 action SetVariable("x_nat", x_nat+2), SetVariable("x_mon", x_mon-2) repeat True
        else:
            timer 0.001 action SetVariable("collided", True)
    else:
        timer 0.01 action SetVariable("x_nat", x_nat-4), SetVariable("x_mon", x_mon+4) repeat True
    

default time = 0
default yyy = False

screen music_dur():
    
    python:
        time = renpy.music.get_pos(channel=u'sound')
    
    text "Duration = [time]":
        color "#fff"
    
    timer 0.1 action Play("music", "<from 5>Daylight.ogg", selected=None)
    
    #timer 0.03 action renpy.restart_interaction repeat True

# Character Callbacks example
init python:
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("SayoText.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

define pike = Character("Christopher Pike", callback=beepy_voice)


image reap:
    choice:
        "ripa_a"
        pause 0.1
        "ripa_b"
        pause 0.1
        "ripa_c"
        pause 0.1
        "ripa_d"
        pause 0.1
        "ripa_e"
        pause 0.1
        
        choice:
            "ripab_a"
            pause 0.1
            "ripab_b"
            pause 0.1
        choice:
            pass
        choice:
            pass
        
    choice:
        "ripb_a"
        pause 0.1
        "ripb_b"
        pause 0.1
        "ripb_c"
        pause 0.1
        "ripb_d"
        pause 0.1
        "ripb_e"
        pause 0.1
        
        choice:
            "ripbb_a"
            pause 0.1
            "ripbb_b"
            pause 0.1
        choice:
            pass
        choice:
            pass

    repeat
    

style text_poem:
    xsize 700
    text_align 0.0
    justify True
    font "nnb_poem.otf"
    size 50
    pos(300, 75)
    slow_cps True
    outlines [ (absolute(1), "#f55", absolute(1), absolute(1)), (absolute(1), "#5f5", absolute(0), absolute(-1)), (absolute(1), "#55f", absolute(-1), absolute(1)) ]
    color "#fff0"
    kerning 5

default uwu = True

screen poem():
    
    modal True
    
    add "poem":
        xalign 0.5
        
    text "Thank you everyone!":
        pos (350, 50)
        size 50
    
    bar value Preference("text speed"):
        xsize 552
        ysize 57
        pos(350, 100)
        left_bar "gui/volume_fill.png"
        right_bar "gui/volume_empty.png"
        thumb "gui/volume_knob.png"
        left_gutter -10
        right_gutter -10
        thumb_offset 30
        
    textbutton "Go Home Go Bed":
        area(350, 300, 545, 80)
        
        text_color "#999"
        text_bold True
        text_size 40
        text_hover_color "#368CD6"
        text_selected_idle_color "#000"
        text_selected_hover_color "#D0D300"
        text_insensitive_color "#D100AE"
        text_selected_insensitive_color "#00CE3A"
        text_xalign 0.5
        
        idle_background "gui/choice_idle_background.png"
        hover_background "gui/choice_hover_background.png"
        
        sensitive uwu == True
        
        action Preference("skip", "toggle")
        
    textbutton "Toggle Variable":
        area(350, 400, 545, 80)
        
        text_color "#999"
        text_bold True
        text_size 40
        text_hover_color "#368CD6"
        text_selected_idle_color "#000"
        text_selected_hover_color "#D0D300"
        text_xalign 0.5
        
        idle_background "gui/choice_idle_background.png"
        hover_background "gui/choice_hover_background.png"
        
        action ToggleVariable("uwu")
    

label start:
    
    "asdasd"
    window hide
    
    show screen poem
    
    pause
    
    hide screen poem
    
    window show
    "asdasd"
    
    "asdadasd"
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
label fbf_anim:

    $ quick_menu = False
    
    scene reap
    
    camera:
        subpixel True
        zoom 1.5 align (0.4, 0.9)
        ease 3.0 align (0.6, 0.2)
        ease 2.0 zoom 1.0
    
    pause
    
    scene black
    
    pause 
    
    camera:
        zoom 1.0 align(0.0, 0.0)
        perspective True gl_depth True pos(0, 0) subpixel True
        ease 2.0 zoom 1.4 ypos 250
        ease 2.0 pos(400, 150) rotate 10
        ease 2.0 zoom 1.0 pos(70, 40) rotate 0
        
    
    scene bg1:
        zpos 125
    
    show natc:
        zoom 0.5 align(0.25, 1.0)
        zpos 250
    
    show monb:
        zoom 0.5 align(0.75, 1.0)
        zpos 400
        
    pause
    
    return
    
    

label before_frame_by_frame:
    
    scene rip
    
    pause
    
    camera:
        subpixel True
        align(0.4, 0.4)
        ease 2.5 zoom 1.6
        ease 3.0 xalign 1.0
        ease 2.5 zoom 1.0
    
    pause
    
    scene black
    
    pause
    
    camera:
        perspective True subpixel True
        zoom 1.0 ypos 360 xpos 1400
        ease 2.0 zoom 1.2 ypos 480
        ease 4.0 xpos 1820 ypos 420
        ease 2.0 ypos 360 xpos 1320 zoom 1.0
    
    scene bg1:
        align (0.5, 1.0) zpos 200
    
    show natc:
        align(0.25, 1.0) zoom 0.5 zpos 300
        
    show monb:
        align(0.75, 1.0) zoom 0.5 zpos 450
        
    pause
    
    return
    
    
    
label timed_based_screen:

    play sound "Mysterious_Noise.mp3"

    pause
    
    #show screen apaya
    
    # Simulate
    #show mouth:
    #    xpos 0
    #    linear 2.0 xpos 720
    
    #show screen collision
    
    show screen music_dur
    
    pause
    
    "[time]"
    
    #hide screen apaya
    
    #hide screen collision
    
    hide screen music_dur
    
    pause
    
    return
    
    

label ctb_stuffs:
    
    pause
    
    show screen ctb
    
    pause
    
    # 10/10 implementation of text input
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Pat Smith"
             
        if "rick" in povname:
            renpy.run(OpenURL('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))

    pov "My name is [povname]!"
    
    
    
    return
    
    
    
label matrixcol:
    
    scene ripa 
    
    pause
    
    scene ripb
    
    pause
    
    scene rip
    
    pause
    
    
    show perlicute as perlica:
        xalign 0.5
        matrixcolor InvertMatrix(value=1.0)
        block:
            ease 1.0 matrixcolor InvertMatrix(value=0.0)
            ease 1.0 matrixcolor InvertMatrix(value=1.0)
            repeat
    
    show perlicute as kak_dwi:
        xalign 0.5 alpha 0.9
        blend "add"
        matrixcolor TintMatrix("#f00")
        block:
            ease 1.0 matrixcolor TintMatrix("#00f")
            ease 1.0 matrixcolor TintMatrix("#f00")
            repeat
    
    
    pause
    
    show bsaga:
        xalign 0.0 yalign 0.5 alpha 0
        
        easein 2.0 xalign 0.8 alpha 1
        
    show screen test
    
    show trasnform
    
    show blappsaga
    
    pause
    hide bsaga
    hide trasnform
    hide blappsaga
    hide screen test
    
    show mouth :
        xalign 0.5 yalign 0.5
        parallel:
            block:
                easein 0.7 zoom 0.5
                ease 1.0 zoom 0.56
                repeat
                
        parallel:
             block:
                ease 2.0 xalign 0.9
                ease 1.0 yalign 0.0
                ease 2.0 xalign 0.5
                ease 1.0 yalign 0.5
                repeat
    
    pause
    hide mouth
    
    show blapp at rotation
    
    pause
    
    return
    
    
    
label rgb:
    
    "a"
    window hide Dissolve(0.2)
    
    
    # Back
    show perlicute as perliAB:  # RGB
        subpixel True
        align(0.6, 1.0) alpha 0.2
        matrixcolor TintMatrix("fff")
        
        parallel:
            block:
                linear 1.0 matrixcolor TintMatrix("f00")
                linear 1.0 matrixcolor TintMatrix("00f")
                linear 1.0 matrixcolor TintMatrix("0f0")
                repeat
        parallel:
            block:
                ease 2.0 xalign 0.65
                ease 2.0 xalign 0.6
                repeat
                
    show perlicute as perliBB:  # Brightness
        subpixel True
        align(0.6, 1.0) alpha 0.2
        blend "add"
        matrixcolor BrightnessMatrix(-0.85)
        
        parallel:
            pause 1.32
            block:
                ease_quad 1.0 matrixcolor BrightnessMatrix(-0.55)
                ease_quad 1.0 matrixcolor BrightnessMatrix(-0.85)
                repeat
        parallel:
            block:
                ease 2.0 xalign 0.65
                ease 2.0 xalign 0.6
                repeat
    
    # Middle
    show perlicute as perliAA:  # RGB
        subpixel True
        align(0.55, 1.0) alpha 0.6
        matrixcolor TintMatrix("fff")
        
        parallel:
            block:
                linear 1.0 matrixcolor TintMatrix("0f0")
                linear 1.0 matrixcolor TintMatrix("f00")
                linear 1.0 matrixcolor TintMatrix("00f")
                repeat
        parallel:
            block:
                ease 2.0 xalign 0.575
                ease 2.0 xalign 0.55
                repeat
                
    show perlicute as perliBA:  # Brightness
        subpixel True
        align(0.55, 1.0) alpha 0.6
        blend "add"
        matrixcolor BrightnessMatrix(-0.75)
        
        parallel:
            pause 0.66
            block:
                ease_quad 1.0 matrixcolor BrightnessMatrix(-0.5)
                ease_quad 1.0 matrixcolor BrightnessMatrix(-0.75)
                repeat
        parallel:
            block:
                ease 2.0 xalign 0.575
                ease 2.0 xalign 0.55
                repeat
    
    # Front
    show perlicute as perliA:  # RGB
        align(0.5, 1.0)
        matrixcolor TintMatrix("fff")
        
        block:
            linear 1.0 matrixcolor TintMatrix("00f")
            linear 1.0 matrixcolor TintMatrix("0f0")
            linear 1.0 matrixcolor TintMatrix("f00")
            repeat
    
    show perlicute as perliB:  # Brightness
        align(0.5, 1.0)
        blend "add"
        matrixcolor BrightnessMatrix(-0.5)
        
        block:
            ease_quad 1.0 matrixcolor BrightnessMatrix(-0.4)
            ease_quad 1.0 matrixcolor BrightnessMatrix(-0.5)
            repeat
    with dissolve
    
    
    pause
    window show Dissolve(0.2)
    
    "b"
    
    return
    
    
    
label viewport_label:
    
    "test"
    
    show screen test_drag
    
    window hide
    pause
    window show
    
    "ok"
    
    return


    
label voic:
    
    "your mom"
    
    play ambient ["bgm005.ogg", "Daylight.ogg", "MoniTalk.ogg"]
    
    "emosonal demeg"
    
    "Noice."
    
    play ambient "Daylight.ogg"
    
    "Kokodayo"
    
    play ambient "bgm005.ogg"
    
    "UmU"
    
    "Super Idol"
    
    "gak tau gua"
    
    return
    
    
label vc:
    
    "hi"
    
    play music "Daylight.ogg"
    
    "Daylight ogg"
    
    "ok, next."
    
    play voice "SayoText.ogg" loop
    
    "Speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak speak s{nw}"
    
    play voice ["NatText.ogg"]*6
    
    "no no no no no no"
    
    stop voice
    stop music
    
    "ok, stop"
    
    
    return
    
    
    
label atl:
    
    window show
    "OwO"
    
    show pc_b as pinecone at awal_posisi(0.5)
        
    window hide
    "Hi everyone!"
    window show
    
    show mouth at mouth_move

    p "I'm out."
    
    hide pinecone
    hide mouth
    
    show lisa_a at awal_posisi(0.0)
    
    "random 1"
    
    hide lisa_a
    show bpine at char_show
    
    "random 2"
    
    show bpine as bpine:
        choice:
            ease 1.0 xalign 0.0
        choice:
            ease 1.0 xalign 1.0
        choice:
            ease 1.0 xalign 1.0
        choice:
            ease 1.0 xalign 1.0
        choice:
            pass
    
    "random 3"
    
    "random 4"
    
    return



label pinecone:
    
    hide screen intensechoice
    
    show bpine:
        zoom 2.0 align(0.5, 1.0)
    
    "You chose to be with Pinecone!"
    
    return
    
label suzuran:
    
    hide screen intensechoice
    
    show bsuzu:
        zoom 2.0 align(0.5, 1.0)
    
    "You chose to be with Suzuran!"
    
    return



label start_gaktau:
    
    scene bg1
    
    "game ini berlatar belakang di {w=1}coolkampus.{nw}"
    
    show sekadi:
        xalign 0.0
    show mona:
        xalign 1.0 zoom 0.75
    
    m "Hello"
    
    show monadark as mona with Dissolve(0.1)

    s "ur mum gae."
    
    show mona as mona with Dissolve(0.1)
    
    m "ok."
    
    
    hide mona
    pause 0.5
    show monb:
        xalign 0.0
    
    m "Sebebas kalian"
    
    stop music fadeout 2
    stop sound fadeout 2
    
    pause 1
    
    s "gak gitu juga alfred."
    
    # Choice
    menu:
        "Dwi makan":
            
            $ dwi_point = 1
            
            scene cg1 with fade
            
            "Dwi kemudian makan."
            
            jump choice1
            
        "Dwi tidur":
            
            $ dwi_point = 0
            
            "Dwi kemudian trdr"
            
            jump choice2
        
        "Suzuran the best":
            "Obviously!"

    return
    
label choice1:
    n "Gais hello."
    
    m "hello channel welcome to my gais."
    
    scene cg2 with ImageDissolve("tr-clockwipe", 2, ramplen=21)

    n "salam dari bijai"
    
    s "ok, im out"
    
    jump main2
    
label choice2:
    
    s "ok, im out"
    
    n "salam dari bijai"
    
    m "hello channel welcome to my gais."
    
    n "Gais hello."
    
    jump main2
    
label main2:
    
    "Time to check dwi_point"
    
    if dwi_point == 1:
        "Dwi point anda satu."
        
        if dwi_point == 0:
            menu:
                "Dwi hebat!":
                    $ dwi_point = 2
                    
                    "Anda bilang Dwi hebat"
                    
                    jump ending
                

                "Dwi bruh":
                    $ dwi_point = 0
                    
                    "Bruh."
                    
        else:
            menu:
                "Dwi hebat!":
                    $ dwi_point = 2
                    
                    "Anda bilang Dwi hebat"
                    
                    jump ending
                

                "Dwi bruuuuuuuuuuuuuuuh":
                    $ dwi_point = 0
                    
                    "Bruh."
            
    else:
        "Dwi point anda noll."
        
    return

