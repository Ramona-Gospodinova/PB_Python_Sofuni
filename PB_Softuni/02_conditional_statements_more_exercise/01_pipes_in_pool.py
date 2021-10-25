obem_na_baseina = int(input())
p1_per_hour = int(input())
p2_per_hour = int(input())
hours_leave = float(input())

obem_zapulnen_za_otstustvieto = (p1_per_hour + p2_per_hour) * hours_leave

# Ako baseina se e napulnil (ili chastichno)
if obem_zapulnen_za_otstustvieto <= obem_na_baseina:
    zapulnenost_na_baseina_percents = (obem_zapulnen_za_otstustvieto / obem_na_baseina) * 100

    p1_zapulnenost = p1_per_hour * hours_leave
    p1_zapulnenost_percents = (p1_zapulnenost / obem_zapulnen_za_otstustvieto) * 100
    p2_zapulnenost_percents = 100 - p1_zapulnenost_percents

    print(f'The pool is {zapulnenost_na_baseina_percents}% full. '
          f'Pipe 1: {p1_zapulnenost_percents:.2f}%. '
          f'Pipe 2: {p2_zapulnenost_percents:.2f}%.')
else:
    liters_over = obem_zapulnen_za_otstustvieto - obem_na_baseina
    print(f'For {hours_leave:.2f} hours the pool overflows with {liters_over:.2f} liters.')
