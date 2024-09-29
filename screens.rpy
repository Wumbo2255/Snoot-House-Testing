screen anonSeesAGOST():
    #This shows the button to press.
    #It is a singular image, unbound
    #To any other object in the scene,
    #And 
    imagebutton:
        xcenter 0.6964
        ycenter 0.45
        idle "mods/SnootHouseTest/assets/images/screens/blankextra.png"
        #^This is what is shown when you aren't hovering over it with your mouse.

        hover slenderbro
        hovered Play('sound', stalker)
        #^This is what runs when you hover over it.

        unhovered Stop('sound')
        #^This is what runs when you move your mouse away.
        
        action [SetVariable('endingvar', 1), Return()]
        #^This is when you click the button,
        #Which in this case, just returns you back
        #To rest of the script and continues.
    imagebutton:
        xcenter 0.25
        ycenter 0.45
        idle "mods/SnootHouseTest/assets/images/screens/blankextra.png"

        hover hoovy
        hovered Play('sound', pootis)
        unhovered Stop('sound')
        action [SetVariable('endingvar', 2), Return()]