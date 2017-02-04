from math import floor

arr = []

def change_coin(val, arr):


    if floor(val/50) != 0:
        arr.append("50 : " + str(floor(val/50)))
        x = val % 50
        change_coin(x,arr)
    else:
        if floor(val/25) != 0:
            arr.append("25 : " + str(floor(val/25)))
            x = val % 25
            change_coin(x,arr)
        else:
            if floor(val / 10) != 0:
                arr.append("10 : " + str(floor(val / 10)))
                x = val % 10
                change_coin(x,arr)
            else:
                if floor(val / 5) != 0:
                    arr.append("5 : " + str(floor(val / 5)))
                    x = val % 5
                    change_coin(x,arr)
                else:
                        arr.append("1 : " + str(floor(val / 1)))

    return arr

