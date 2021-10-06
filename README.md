# Irresistible




We were given very few resistor values for amplifier designs, given that Q point is very sensitive to changes in resistance, I created a script "Irresistible" to find a resistance based on a list of resistors given. Simply change the resistances in the "resistor_list.py" module, and let her rip.


## Road Map
In terms of , I'm planning on implementing a voltage divider function that will generate a voltage divider network based on the resistances that were given. Also I want to make it "tiered". Ie, if 4 resistors can give an option yeilding 4% difference from ideal, and 2 resistors can offer a % difference of 4.5%, then the option should be given to the end user. 

## Example
The script only goes 2 nested layers deep. This means the maximum number of resistors per resistance value you query will be 4. 


- (R1||R2)||(R3||R4) 

- (R1+R2+R3+R4)

![Alt Text](https://i.imgur.com/WEajSjZ.gif)

