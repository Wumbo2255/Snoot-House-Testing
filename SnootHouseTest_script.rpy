init python:
    # Modding Support variables
    # All mod rpy files must have title of their mod (this shows up on a button)
    # and finally the label that controls the flow of dialogue

    mod_menu_access += [{
        'Name': "Snoot House Test",
        'Label': "snoothousetest"
    }];

label snoothousetest:
    call snoothousetest_storyline

    return
