#%% [markdown]
# ## Exercise 45: Defining the Function with Keyword Arguments
def add_suffix(suffix=".com"):
    return f"google{suffix}"


# %% [markdown]
# ## Exercise 46: Defining the Function with Positional and Keyword Arguments
def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

#%% [markdown]
# ## Exercise 47: Using **kwargs
def convert_and_sum_list(usd_list, rate=0.75):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, rate=rate)
    return total
#%%
def convert_and_sum_kwarg(usd_list, **kwargs):
    total = 0
    print(kwargs)
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)
    return total
#%%
if __name__ == '__main__':
    print(add_suffix(".co.uk"))
    print(convert_usd_to_aud(100))
    print(convert_usd_to_aud(100, rate=0.78))

    print(convert_and_sum_list([1, 3]))

    print(convert_and_sum_kwarg([1, 3], rate=0.8))
# %%
