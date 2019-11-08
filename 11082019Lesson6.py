# return 改成 print,可以将All Values显示。


# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                 for (i,d ) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word



##Recap of what learned in this unit:
#1. python features: 
# #1.list comprehensions, eg:[x**2 for x in ......if.....]
# #2.generator expressions, eg(..for... if .....)
# #3.generator(functions), 用yield statment
# #4.handling different types
# #5.eval function,eg: string-->object/function
#2. instrumentation, eg: time.clock()