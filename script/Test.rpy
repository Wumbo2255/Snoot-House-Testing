label Test:
    stop music fadeout 2
    pause 2
     
    play music "mods/Snoot House/assets/audio/OST/LuigiMansionMenu.ogg" volume 0.4 fadein 0.2
    pause 0.5
    
    scene backyard with Dissolve(2)
    pause 0.5

    show anon fear flip:
        ease 0.5 xcenter 0.5

    A "GOST!!! DERE'S A GOST 'ERE!!"

    window hide

    hide anon with Dissolve(0.1)

    call screen anonSeesAGOST

    show anon happy:
        xcenter 0.5
    with Dissolve(0.5)

    A "you are winner! congratulation!"