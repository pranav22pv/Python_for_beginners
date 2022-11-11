# Every python file that we cab see under the helloworld dir are called modules
# In a dress shop, we have men's, women's and kid's sections called packages
# and in every section there are items namely shirts, pants, trousers, etc called modules
# and every module can have a funtion.
# directory with "__init.py" is a package. files in that dir are modules and each module can have functions.
# __init__.py is package
# Manual creation of package -> right click -> new directory"ecommerce" -> new file "__init.py" .
# The interpreter treats the folder as package
# Another method -> right click -> new package and name it"ecommerce" -> we can automatically see "__init.py" inside the directory



# 3 ways to import packages:
# 1:
import ecommerce.shipping     # shipping is a module present in the ecommerce package directory
ecommerce.shipping.calc_shipping()   # calc_shipping is a function present in the shipping module.
print("\n")    # in this method we need to call ecommerce.shipping. every time
#2:
from ecommerce.shipping import calc_shipping, blank_lines    # can import multiple functions using comma in the current module.
calc_shipping()     # we can call it how much ever times we want
calc_shipping()      # in this method we can simply call the function alone
blank_lines()
calc_shipping()
calc_shipping()


#3:
from ecommerce import shipping
shipping.calc_shipping()          # in this method we need call shipping. each time