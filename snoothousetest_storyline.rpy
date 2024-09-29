define Hvy = Character ("Heavy", color="#D8A09A", who_outlines=[(gui.name_text_thickness, '#461B1F')], ctc="ctc_end_marker", ctc_pause="ctc_mid_marker")
image heavy = Image(hoovy)

define slenderbro = "mods/SnootHouseTest/assets/images/screens/slenderbro.png"
define stalker = 'mods/SnootHouseTest/assets/audio/SFX/stalker.ogg'
define loogmenu =  "mods/SnootHouseTest/assets/audio/OST/LuigiMansionMenu.ogg"
define hoovy = "mods/SnootHouseTest/assets/images/sprites/heavy.png"
define pootis = "mods/SnootHouseTest/assets/audio/SFX/pootis.mp3"
define hegg = "mods/SnootHouseTest/assets/audio/SFX/heavyegg.ogg"
define endingvar = 0

label snoothousetest_storyline:
    call shTest
    return