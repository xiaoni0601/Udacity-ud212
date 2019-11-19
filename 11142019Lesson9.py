
# ---------------
# User Instructions
#
# Modify the function, trace, so that when it is used
# as a decorator it gives a trace as shown in the previous
# video. You can test your function by applying the decorator
# to the provided fibonnaci function.
#
# Note: Running this in the browser's IDE will not display
# the indentations.

from functools import update_wrapper


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print('%s--> %s' % (trace.level*indent, signature))
        trace.level += 1
        try:
            result = f(*args) # your code here
            print('%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result))
        finally:
            trace.level -= 1  # your code here
        return result   # your code here
    trace.level = 0
    return _f

@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(6) #running this in the browser's IDE  will not display the indentations!



### Parser解析器
# parse(symbol, text, grammar)


# ---------------
# User Instructions
#
# Modify the parse function so that it doesn't repeat computations.
# You have learned about a tool in this unit that prevents 
# repetitive computations. Try using that!
#
# For this question, the grader will be looking for a specific 
# solution. Hint: it should only involve adding one line of code
# (and that line should only contain 5 characters).

from functools import update_wrapper
import re

def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'"""

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text
    @memo
    def parse_atom(atom, text):
        if atom in grammar:  # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem  
            return Fail
        else:  # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])
    
    # Body of parse:
    return parse_atom(start_symbol, text)

Fail = (None, None)

# The following decorators may help you solve this question. HINT HINT!

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f
