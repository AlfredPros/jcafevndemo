
define s = Character("Sekadi")
define m = Character("Monika")
define n = Character("Natsuki")

image monaflip = im.Flip("mona.png", horizontal=True)
image monadark = im.MatrixColor("mona.png", im.matrix.brightness(-0.5))
image pinedark = im.MatrixColor("bpine.png", im.matrix.brightness(-0.2))
image suzudark = im.MatrixColor("bsuzu.png", im.matrix.brightness(-0.2))





label start:
    
    jump atl
    
label atl:
    
    "Hi everyone!"
    
    "Ok. Cool."
    
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

