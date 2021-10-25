broi_bitcoins = int(input())
broi_kitaiski_iuana = float(input())
commision = float(input())

bitcoins_to_bgn = broi_bitcoins * 1168
kitaiski_iuana_to_usd = broi_kitaiski_iuana * 0.15
usd_to_bgn = kitaiski_iuana_to_usd * 1.76

total_in_bgn = bitcoins_to_bgn + usd_to_bgn
total_in_eur = total_in_bgn / 1.95

commision = total_in_eur * commision / 100

total_after_commision = total_in_eur - commision
print(f'{total_after_commision:.2f}')