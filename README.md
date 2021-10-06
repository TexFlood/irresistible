# Irresistible

We were given very few resistor values for amplifier designs, given that Q point is very sensitive to changes in resistance, I created a script "Irresistible" to find a resistance based on a list of resistors given. Simply change the resistances in the "resistor_list.py" module, and let her rip.

The script only goes 2 nested layers deep. This means the maximum number of resistors per resistance value you query will be 4. 


For example:
- (R1||R2)||(R3||R4) 

- (R1+R2+R3+R4)

![Alt Text](https://i.imgur.com/WEajSjZ.gif)
