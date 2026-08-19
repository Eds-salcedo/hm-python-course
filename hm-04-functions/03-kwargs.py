"""
LET'S LEARN HOW KWARGS WORK
"""

# KWARGS are used in case that you want to enter an undetermined number of arguments into a DEF function, but in this case, we are going to use a dictionary to do so.


def get_product(**data):
    print(data)


# In this first attempt, we receive an error message because we are not providing any name for the parameter)
# get_product("id")

# Thus, when we call a previously created  DEF function that uses KWARGS (**), we must provide a name and the respective parameter over which we want to apply the function.
get_product(id=23,
            name="Laptop",
            price=1000)
# Internatlly, Python will convert the provided arguments () into a dictionary {}.

# In case we want to access to the values of specific parameters of the dictionary, we can do so by using the following syntax, naming the dictionary and the parameter within [" "]:


def product_dates(**dates):
    print(dates["expiry_date"], dates["harvest_date"])


product_dates(expiry_date="2025-05-22",
              harvest_date="2024-12-30")
