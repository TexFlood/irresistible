# Calculation for RC
import math

import sympy as sym
import numpy as np


def generate_all_possible_resistances(avail_resistors:list):
    parallel_configs = []
    series_configs = []
    resistor_count = 0
    significant_digits = 2
    for i in range(len(avail_resistors)-2):
        for j in range(len(avail_resistors) - 2):
            parallel = avail_resistors[i]*avail_resistors[j]/(avail_resistors[i]+avail_resistors[j])
            parallel = round(parallel, significant_digits - int(math.floor(math.log10(abs(parallel)))) - 1)
            series = (avail_resistors[i] + avail_resistors[j])
            series = round(series, significant_digits - int(math.floor(math.log10(abs(series)))) - 1)
            if not (parallel_configs.__contains__(parallel) and avail_resistors.__contains__(parallel) and series_configs.__contains__(parallel)):
                parallel_configs.append(parallel)
                resistor_count+=1
                print('Resistor Count: ' + str(resistor_count))
            if not (parallel_configs.__contains__(series) and avail_resistors.__contains__(series) and series_configs.__contains__(series)):
                series_configs.append(series)
                parallel_configs.append(parallel)
                resistor_count += 1
                print('Resistor Count: ' + str(resistor_count))
    all_configs = parallel_configs + series_configs + avail_resistors
    parallel_configs = []
    series_configs = []
    for i in range(len(all_configs)-2):
        print(i)
        for j in range(len(all_configs) - 2):
            parallel = (all_configs[i]*all_configs[j]/(all_configs[i]+all_configs[j]))
            series = (all_configs[i] + all_configs[j])
            parallel = round(parallel, significant_digits - int(math.floor(math.log10(abs(parallel)))) - 1)
            series = round(series, significant_digits - int(math.floor(math.log10(abs(series)))) - 1)
            if not (parallel_configs.__contains__(parallel) and avail_resistors.__contains__(parallel) and all_configs.__contains__(parallel)):
                parallel_configs.append(parallel)
                parallel_configs.append(parallel)
                resistor_count += 1
                print('Resistor Count: ' + str(resistor_count))
            if not (parallel_configs.__contains__(series) and avail_resistors.__contains__(series) and all_configs.__contains__(series)):
                series_configs.append(series)
                parallel_configs.append(parallel)
                resistor_count += 1
                print('Resistor Count: ' + str(resistor_count))
    all_configs = all_configs + series_configs + parallel_configs
    all_configs.sort()
    [print(x) for x in all_configs]
    return(all_configs)



avail_resistors = [
    1.5E3,
    100E3,
    180E3,
    1E3,
    2.2E3,
    200E3,
    3.3E3,
    33E3,
    390E3,
    39E3,
    3E3,
    8.2E3,
    9.1E3,
    1.5E6,
    4.7E6,
    10,
]

V_CE = 0.2
R_R = 400
I_C = 33E-3

# R_C = sym.Symbol('x')
# R_C = sym.solveset(-VCC+R_R*I_C+R_C*I_C+V_CE, R_C)


# for resistor in avail_resistors:
#     avail_currents = np.arange(15E-3, 120E-3, 0.5E-3).tolist()
#     for current in avail_currents:
#         R_C = resistor
#         VCC = sym.Symbol('x')
#         VCC = sym.solveset(-VCC + R_R * current + R_C * current + V_CE, VCC)
#         for item in VCC:
#             if item.evalf() <= 30:
#                 print('RC of ' + str(R_C) + ' is possible with VCC of ' + str(item) + ' and a current of ' + str(current*1000) + 'mA')

print(len(generate_all_possible_resistances(avail_resistors)))