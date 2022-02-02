
define s = Character("Sekadi")
define m = Character("Monika")
define n = Character("Natsuki")
define p = Character("Pinecone")

image monaflip = im.Flip("mona.png", horizontal=True)
image monadark = im.MatrixColor("mona.png", im.matrix.brightness(-0.5))
image pinedark = im.MatrixColor("bpine.png", im.matrix.brightness(-0.2))
image suzudark = im.MatrixColor("bsuzu.png", im.matrix.brightness(-0.2))


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





label start:
    
    jump atl
    
label atl:
    
    "OwO!"
    
    "Input text here."
    
    "Input text here volume 2."
    
    
    
    
    show pc_b as pinecone at awal_posisi(0.5)
    
    "Hi everyone!"
    
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

