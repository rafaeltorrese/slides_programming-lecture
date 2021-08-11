#%% [markdown]
# A useful way to remember how Python resolves scope is with the LEGB rule. LEGB is an initialism for Local, Enclosing, Global, Built-in, which describes the order by which Python resolves scope
x = 5

def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z
    
    return inner_func()
#%%
if __name__ == "__main__":
    print(outer_func())


        