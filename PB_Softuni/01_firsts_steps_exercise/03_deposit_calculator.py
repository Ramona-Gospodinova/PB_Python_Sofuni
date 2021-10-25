# Inputs
deposit = float(input())
period_in_months = int(input())
percent = float(input())

natrupana_godishna_lihva = deposit * percent / 100
mesechna_lihva = natrupana_godishna_lihva / 12

# Calculations
total = deposit + (period_in_months * mesechna_lihva)

# Outputs
print(total)