label shTest:
    stop music fadeout 2
    pause 2
     
    play music loogmenu volume 0.4 fadein 0.2
    pause 0.5
    
    scene backyard with Dissolve(2)
    pause 0.5

    show anon fear flip:
        ease 0.5 xcenter 0.5

    A "GOST!!! DERE'S A GOST 'ERE!!"

    window hide

    hide anon with Dissolve(0.1)

    call screen anonSeesAGOST
    if endingvar == 1:
        pause 0.5
        show anon happy:
            xcenter 0.5
        with Dissolve(0.5)
    
        A "you are winner! congratulation!"
        "E[endingvar]"
        return
    elif endingvar == 2:
        pause 0.5
        show anon fear flip:
            ease 0.5 xcenter 0.75
        with Dissolve(0.1)

        show heavy:
            xcenter 0.25
            ycenter 0.6
            xzoom 2
            yzoom 2
            ease 0.1
        play voice hegg volume 0.4
        Hvy "Heavy will now lay egg in your mouth."
        "E[endingvar]"
        return