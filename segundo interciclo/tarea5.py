def saludo (lang) :
    if lang == 'es':
        return'hola'
    elif lang == 'fr' :
             return'bonjour'
    else:
        return'hello'

print(saludo ("fr"), "glenn")
print(saludo ("es"), "sally")
print(saludo ("en"), "michael")