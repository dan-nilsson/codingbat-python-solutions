'''
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
    index = len(str)
    str_out = ''
    while index >= 0:
        str_out = str[:index] + str_out
        index -= 1
    return str_out