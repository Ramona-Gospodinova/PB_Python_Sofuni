type_gorivo = input()
litri_koito_ima_v_rezervoara = float(input())

if type_gorivo == 'Diesel' or type_gorivo == 'Gasoline' or type_gorivo == 'Gas':
    type_gorivo = type_gorivo.lower()
    if litri_koito_ima_v_rezervoara >= 25:
        print(f'You have enough {type_gorivo}.')
    elif litri_koito_ima_v_rezervoara < 25:
        print(f'Fill your tank with {type_gorivo}!')
else:
    print(f'Invalid fuel!')
