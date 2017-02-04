
# function to calculate the power of 2 nearest to the value of the input

def eval_power(val):
    val1 = 1

    while val1 <= val:
        val1 *= 2

    v = val1/2
    z = 1
    while v/2 > 1:
        v = v/2
        z += 1

    return (val1/2),z
