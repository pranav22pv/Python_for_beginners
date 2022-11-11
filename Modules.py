# A Module is basically a file with some python code nd we use modules to organise code into multiple files just like in a supermarket
# in a supermarket we have sections for fruits, vegetables, cleaning products,etc.
# Instead of writing all the functions and classes, we r goin to break the code into multiple files . we refer each file as module
# With modues, not only our code is organised and structured but also will have the ability to reuse our code

#So we can do it by writing our functions and saving it in the working directory . and import them and use them .
# Converters is the module we are goin to use here.. so write and save the code for the module pre-requisitely.

import converters    # without extensions . i.e .py
print(converters.lbs_to_kg(70))


# We also have another method to import modules, without importing the entire module, we can just simply import a particular
# funtion
from converters import kg_to_lbs
print(kg_to_lbs(100))     # converters.kg_to_lbs()  not needed


# If u compare the difference btw the 2 methods, u can see if we import the entire module we need to call the function
# using the module name and dot operator . (converter.lbs_to_kg) || Nut whereas if we import a single function from the
# module using from converters import ...  we can simply call the function alone without the module name .(kg_to_lbs() )

