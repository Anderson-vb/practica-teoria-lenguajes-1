def tiene_parentesis(regex):
    return regex.startswith('(') and regex.endswith(')')

def remove_parentesis(regex):
    if regex.startswith('('):
        regex = regex[1:]
    if regex.endswith(')'):
        regex = regex[:-1]
    return regex

def add_parentesis(regex):
    return f'({regex})'

def caracteres_seguidos(regex):
    if '+' in regex or '(' in regex:
        return False
    return True
    
def derivar(regex, caracter):

    parentesis = False

    if tiene_parentesis(regex):
        regex = remove_parentesis(regex)
        parentesis = True
    
    if regex == caracter:
        if parentesis:
            return add_parentesis('ε')
        else:
            return 'ε'

    if regex != caracter and len(regex) == 1:
        if parentesis:
            return add_parentesis('∅')
        else:
            return '∅'

    if regex == 'ε':
        if parentesis:
            return add_parentesis('ε')
        else:
            return 'ε'

    if regex == '∅':
        if parentesis:
            return add_parentesis('∅')
        else:
            return '∅'
       
    # ab*, (ab)*
    if regex.endswith('*'):
        if '+' in regex and not tiene_parentesis(regex[:-1]):
            pass
        else:

            # ()
            if parentesis:
                if derivar(regex[:-1], caracter) == 'ε':
                    return f'({regex})'
                if derivar(regex[:-1], caracter) == '∅':
                    return '(∅)'
              
            # ()*
            if derivar(regex[:-1], caracter) == '(ε)':
                return regex
            # not ()*
            elif derivar(regex[:-1], caracter) == 'ε':
                return regex
            # ()*
            elif derivar(regex[:-1], caracter) == '(∅)':
                return '(∅)'
            # not ()*
            elif derivar(regex[:-1], caracter) == '∅':
                return '∅'
            else:
                return f'{derivar(regex[:-1], caracter)}({regex})'


    # a*b, b*a
    if '*' in regex:
        if '+' in regex:
            pass
        elif not regex.startswith('(') and '(' in regex:
            pass
        elif regex.startswith('(') and not regex.endswith(')'):
            pass
        elif regex.startswith(caracter):
            return regex
        else:
            return '∅'

    # a+b, b+a
    if '+' in regex:
        if not regex.startswith('(') and '(' in regex:
            pass
        elif regex.startswith('(') and not regex.endswith(')'):
            pass
        else:
            # ESTA AQUI
            r1 = ''
            r2 = ''
            antes_de_mas = True
            for x in regex:
 
                if x == '+':
                    antes_de_mas = False
 
                elif antes_de_mas:
                    r1 = r1 + x
 
                elif not antes_de_mas:
                    r2 = r2 + x
            if parentesis:
                if derivar(r1, caracter) == '∅':  
                    return f'({derivar(r2, caracter)})'
 
                elif derivar(r1, caracter) == 'ε':
                    if derivar(r2, caracter) == 'ε' or derivar(r2, caracter) == '∅':
                        return '(ε)'
                    else:
                        return f'(derivar(r2, caracter))'
 
                elif derivar(r2, caracter) == '∅':
                    return f'({derivar(r1, caracter)})'
 
                elif derivar(r2, caracter) == 'ε':
                    if derivar(r1, caracter) == 'ε' or derivar(r1, caracter) == '∅':
                        return '(ε)'
                    else:
                        return f'(derivar(r1, caracter))'
 
                else:
                    return f'({derivar(r1, caracter)}+{derivar(r2, caracter)})'
            else:
                if derivar(r1, caracter) == '∅':
                    return derivar(r2, caracter)
 
                elif derivar(r1, caracter) == 'ε':
                    if derivar(r2, caracter) == 'ε' or derivar(r2, caracter) == '∅':
                        return 'ε'
                    else:
                        return derivar(r2, caracter)
 
                elif derivar(r2, caracter) == '∅':
                    return derivar(r1, caracter)
 
                elif derivar(r2, caracter) == 'ε':
                    if derivar(r1, caracter) == 'ε' or derivar(r1, caracter) == '∅':
                        return 'ε'
                    else:
                        return derivar(r1, caracter)
 
                else:
                    return f'{derivar(r1, caracter)}+{derivar(r2, caracter)}'


    # ab, ba, b(a) 
    if regex.startswith(caracter) and caracteres_seguidos(regex):
        return regex[1:]
    elif not regex.startswith(caracter) and not regex.startswith('('):
        return '∅'
    # a(b+c), a(b)
    elif regex.startswith(caracter) and '(' in regex:
        r1 = '' 
        r2 = ''
        antes_de_parentesis = True

        for x in regex:
            if x == '(':
                antes_de_parentesis = False

            elif x == ')':
                break

            elif antes_de_parentesis:
                r1 = r1 + x

            elif not antes_de_parentesis:
                r2 = r2 + x

        if derivar(r1, caracter) == 'ε' or derivar(r1, caracter) == '(ε)':
            if derivar(r2, caracter) == '∅' or derivar(r2, caracter) == '(∅)' or derivar(r2, caracter) == 'ε' or derivar(r2, caracter) == '(ε)':
                return f'({r2})'
            else:
                return f'({r2})+({derivar(r2,caracter)})'
        elif derivar(r1, caracter) == '∅' or derivar(r1, caracter) == '(∅)':
            return f'({derivar(r2, caracter)})'
        else:
            if derivar(r2, caracter) == '∅' or derivar(r2, caracter) == '∅' or derivar(r2, caracter) == 'ε' or derivar(r2, caracter) == '(ε)':
                return f'({derivar(r1, caracter)}){r2}' 
            else:
                return f'{derivar(r1, caracter)}({r2})+({derivar(r2, caracter)})' 

    # (a)b, (a+b)c
    elif regex.startswith('(') and not regex.endswith(')'):
        r1 = ''
        r2 = ''
        despues_de_parentesis = False
        for x in regex:

            if x == '(':
                pass

            elif x == ')':
                despues_de_parentesis = True

            elif not despues_de_parentesis:
                r1 = r1 + x

            elif despues_de_parentesis:
                r2 = r2 + x

        if derivar(r1, caracter) == 'ε' or derivar(r1, caracter) == '(ε)':
            if derivar(r2, caracter) == '∅' or derivar(r2, caracter) == '∅' or derivar(r2, caracter) == 'ε' or derivar(r2, caracter) == '(ε)':
                return r2
            else: 
                return f'{r2}+{derivar(r2, caracter)}'
        elif derivar(r1, caracter) == '∅' or derivar(r1, caracter) == '(∅)':
            return derivar(r2, caracter) 
        else:
            if derivar(r2, caracter) == '∅' or derivar(r2, caracter) == '∅' or derivar(r2, caracter) == 'ε' or derivar(r2, caracter) == '(ε)':
                return f'({derivar(r1, caracter)}){r2}' 
            else:
                return f'({derivar(r1, caracter)}){r2}+{derivar(r2, caracter)}'

