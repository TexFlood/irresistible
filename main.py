import math

from ResistorNetwork import ResistorNetwork
import resistor_list


def generate_all_possible_resistances(avail_resistors: list):
    resistor_configs = {}
    resistor_count = 0
    significant_digits = 2
    for i in range(len(avail_resistors) - 1):
        for j in range(len(avail_resistors) - 1):
            parallel = avail_resistors[i] * avail_resistors[j] / (avail_resistors[i] + avail_resistors[j])
            parallel = round(parallel, significant_digits - int(math.floor(math.log10(abs(parallel)))) - 1)
            series = (avail_resistors[i] + avail_resistors[j])
            series = round(series, significant_digits - int(math.floor(math.log10(abs(series)))) - 1)
            if not (parallel in resistor_configs):
                resistor_configs[parallel] = ResistorNetwork(avail_resistors[i], avail_resistors[j], True, False)
                resistor_count += 1
            if not (series in resistor_configs):
                resistor_configs[series] = ResistorNetwork(avail_resistors[i], avail_resistors[j], False, True)
                resistor_count += 1
    for resistor in avail_resistors:
        resistor_configs[resistor] = ResistorNetwork(resistor, None, False, False)
    precheck_configs = list(resistor_configs.values())

    for i in range(len(precheck_configs) - 1):
        for j in range(len(precheck_configs) - 1):
            obj = precheck_configs[i]
            r1 = precheck_configs[i]
            r2 = precheck_configs[j]
            parallel = r1.__int__() * r2.__int__() / (r1.__int__() + r2.__int__())
            series = (r1 + r2)
            parallel = round(parallel, significant_digits - int(math.floor(math.log10(abs(parallel)))) - 1)
            series = round(series, significant_digits - int(math.floor(math.log10(abs(series)))) - 1)
            if not (parallel in resistor_configs):
                resistor_configs[parallel] = ResistorNetwork(r1, r2, True, False)
                resistor_count += 1
            if not (series in resistor_configs):
                resistor_configs[series] = ResistorNetwork(r1, r2, False, True)
                resistor_count += 1
    return resistor_configs


print('Welcome to ResistorMan! \n\n')
print('Calculating resistor values...\n\n')
resistor_networks = generate_all_possible_resistances(resistor_list.avail_resistors)

print('Given the data provided, ' +
      str(len(resistor_networks)) + ' possible resistor combinations are possible.\n\n'
      )


def find_closest_resistor(resistance, resistor_dict: dict):
    lowest_delta_i = 1E99
    best_resistor_network = None
    resistor_list = list(resistor_dict)
    for k in resistor_dict:
        delta_i = abs(resistance - k) / ((resistance + k) / 2) * 100
        if delta_i < lowest_delta_i:
            lowest_delta_i = delta_i
            best_resistor_network = resistor_dict[k]
    return best_resistor_network


def print_closest_resistor(resistance, resistor_dict: dict):
    resistor = find_closest_resistor(resistance, resistor_dict)
    print('\n\n -------------------------------------')
    print('Desired resistance: ' + str(resistance) + ' Ω \n')
    print('Closest resistance available: ' + str(resistor.resistance_value) + ' Ω \n')
    print('Configuration: ' + resistor.__str__() + '\n')
    print('Percent difference from desired resistance: ' + str(
        100 * abs(resistor.__int__() - resistance) / ((resistance + resistor.__int__()) / 2)) + ' % \n')
    print('Absolute difference from desired resistance: ' + str(abs(resistor.__int__() - resistance)) + ' Ω \n')
    print(' -------------------------------------')


while True:
    requested_resistance = float(input('Please enter a resistance value that you would like to obtain: '))

    print_closest_resistor(requested_resistance, resistor_networks)

    print("Do you want to find another resistive network?")

    if input('Continue (y/n)? ') != 'y':
        break;
