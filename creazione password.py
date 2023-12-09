import random
import string

#generazione avanzata delle password
def generazione_avanzata():
    alfanumerico_avanzato = string.digits + string.ascii_letters + string.punctuation
    app = alfanumerico_avanzato
    counter = 0
    psw = ""
    while counter < 24:
        char = random.choice(app)
        psw += char
        counter += 1
    print("la tua nuova password è ", psw)

#generazione semplice delle password
def generazione_semplice():
    alfanumerico = string.digits + string.ascii_letters
    psw = ""
    counter = 0
    app = alfanumerico
    while counter < 8:
        char = random.choice(app)
        psw += char
        counter += 1
    print("la tua nuova password è", psw)

#main
scelta_utente = input("che tipo di password uoi creare, s = 8 caratteri, a = 24 caratteri:")
if scelta_utente == 's' or scelta_utente == 'S':
    print("stiamo generando la tua password semplice!")
    generazione_semplice()
elif scelta_utente == 'a' or scelta_utente == 'A':
    print("stiamo generando la tua password avanzata!")
    generazione_avanzata()
else:
    print("scelta non riconosciuta! riprova")
