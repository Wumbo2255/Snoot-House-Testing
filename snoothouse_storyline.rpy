define Hvy = Character ("Heavy", color="#D8A09A", who_outlines=[(gui.name_text_thickness, '#461B1F')], ctc="ctc_end_marker", ctc_pause="ctc_mid_marker")
image heavy = Image(hoovy)

define slenderbro = "mods/SnootHouse/assets/images/screens/slenderbro.png"
define stalker = 'mods/SnootHouse/assets/audio/SFX/stalker.ogg'
define loogmenu =  "mods/SnootHouse/assets/audio/OST/LuigiMansionMenu.ogg"
define hoovy = "mods/SnootHouse/assets/images/sprites/heavy.png"
define pootis = "mods/SnootHouse/assets/audio/SFX/pootis.mp3"
define hegg = "mods/SnootHouse/assets/audio/SFX/heavyegg.ogg"
define endingvar = 0

label snoothouse_storyline:
    call Test
    return