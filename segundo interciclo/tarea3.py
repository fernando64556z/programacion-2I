def saludo (lang) :
    if lang == 'es':
        print('hola')
    elif lang == 'fr' :
        print('bonjour')
    else:
        print('hello')

saludo ("fr")
saludo ("es")
saludo ("en")