#!/usr/bin/env python
# coding: utf-8
print('A one bedroom in the Bay Area is listed at $599,000')
offer = abs(int(input('Enter your first offer on the house: ')))
best = abs(int(input('Enter your best offer on the house: ')))
increment = abs(int(input('How much more do you want to offer each time?: ')))
offer_accepted = False
while offer <= best:  
    if offer >= 650000:
        offer_accepted = True
        print(f'Your offer of {offer}, has been accepted!')
        break
    print('We\'re sorry, you\'re offer of', offer, 'has not been accepted.' )
    offer += increment
