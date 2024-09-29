screen anonSeesAGOST():
    imagebutton:
        xcenter 0.6964
        ycenter 0.45
        idle "mods/Snoot House/assets/images/screens/blankextra.png"

        hover "mods/Snoot House/assets/images/screens/slenderbro.png"
        hovered Play('sound', stalker)
        unhovered Stop('sound')

        action Return()