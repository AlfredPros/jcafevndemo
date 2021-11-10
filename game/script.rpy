
define s = Character("Sekadi")
define m = Character("Monika")
define n = Character("Natsuki")


label start:

    scene black
    
    "game ini berlatar belakang di {w=1}coolkampus."

    show sekadi:
        xalign 1.0

    s "ur mum gae."
    
    show mona:
        xalign 0.0
    
    m "ok."
    
    hide mona
    pause 0.5
    show monb:
        xalign 0.0
    
    m "Sebebas kalian"
    
    pause 1
    
    s "gak gitu juga alfred."
    
    # Choice
    menu:
        "Dwi makan":
            
            $ dwi_point = 1
            
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

