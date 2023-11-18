def damage_kyogre(k_health, solar_beam, Hyper_beam, Earthquake, Rock_slide, attack):
    if attack == 'solar beam':
        k_health = k_health - solar_beam
    elif attack == 'hyper beam':
        k_health = k_health - Hyper_beam
    elif attack == 'earthquake':
        k_health = k_health - Earthquake
    elif attack == 'rock slide':
        k_health = k_health - Rock_slide
    else:
        print('No damage')
    return k_health

def damage_groudon(g_health, water_gun, hydro_pump, hydro_cannon, hyper_beam, attack):
    if attack == 'water gun':
        g_health = g_health - water_gun
    elif attack == 'hydro pump':
        g_health = g_health - hydro_pump
    elif attack == 'hydro cannon':
        g_health = g_health - hydro_cannon
    elif attack == 'hyper beam':
        g_health = g_health - hyper_beam
    else:
        print('No damage')
    return g_health