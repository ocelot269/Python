def loose_change(cents):
    monedero = {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0, }
    # Valor monedas Nickels" : 5, "Pennies" : 1, "Dimes" : 10, "Quarters" : 25

    if cents >= 25:
            monedero["Quarters"] = cents // 25
            cambio = cents % 25
            
    if cambio >= 10:
            monedero["Dimes"] = cambio // 10
            cambio = cents % 10
            

    if cambio >= 5:
            monedero["Nickels"] = cambio // 5
            cambio = cents % 5
            
    if cambio > 0:
            monedero["Pennies"] = cambio // 1
            cambio = cents % 1
            

    return monedero    


if __name__ == '__main__':

    assert loose_change(
        29), {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change( 
        91), {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    """assert(loose_change(
        0), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert(
        loose_change(-2), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert(loose_change(
        3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})"""
