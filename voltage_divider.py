
def percent_difference(a, b):
    return 100 * abs(a - b) / ((a + b) / 2)


def voltage_divider(vin, vout, resistor_networks):
    optimal_r1 = None
    optimal_r2 = None
    best_delta_v = 1E99
    desired_vout = vout
    resistor_networks_list = list(resistor_networks)
    for i in range(len(resistor_networks_list) - 1):
        for j in range(len(resistor_networks_list) - 1):
            r1 = resistor_networks_list[i].__int__()
            r2 = resistor_networks_list[j].__int__()
            vout = r1 * vin / (r1 + r2)
            delta_v = percent_difference(vout, desired_vout)
            if delta_v < best_delta_v:
                optimal_r1 = resistor_networks_list[i]
                optimal_r2 = resistor_networks_list[j]
                best_delta_v = delta_v
    return (resistor_networks[optimal_r1], resistor_networks[optimal_r2],
            vin * resistor_networks[optimal_r1].__int__() / (
                        resistor_networks[optimal_r1].__int__() + resistor_networks[optimal_r2].__int__()),
            best_delta_v)


def print_optimal_voltage_divider(vin, vout, resistor_networks):
    (r1, r2, vout, delta_v) = voltage_divider(vin, vout, resistor_networks)
    strl1 = '\nThe best voltage divider given the resistor set is\n'
    strl2 = 'R1: ' + r1.__str__() + '\n'
    strl3 = 'R2: ' + r2.__str__() + '\n'
    strl4 = 'Vout: ' + round(vout).__str__() + '\n'
    print(strl1 + strl2 + strl3 + strl4)
    print('Percent difference from requested value =', delta_v)

def generate_voltage_divider_visual(r1,r2):
    str = "In a case where two resistors are placed in series the circuit should be: \n" \
            "r1\n" \
            "|\n" \
            "|\n" \
            "r1\n" \
            "|\n" \
            "|\n"
    return str