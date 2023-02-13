import random

quotes = ["Life like a puzzle earth like a maze-T H MAHIR" ,
 "Life is 10% what happens to you and 90% how you react to it. - Charles R. Swindoll",   
"The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it. - Steve Jobs",   
 "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",  
   "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson", 
      "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis"]

def get_quote():
    return random.choice(quotes)

print(get_quote())
