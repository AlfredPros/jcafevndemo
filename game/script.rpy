
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

label start:
    
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

