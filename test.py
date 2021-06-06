gender = {'m' : 'Дорогий', 'f' : 'Дорога'}
a = [["Семен", "Семенович", 13.13, 'm'], ["Тарас", "Іванович", 20.21, 'm'], ["Тамара", "Петрівна", 38.35, 'f']]
for name, mid_name, balance, g in a:
    text = f"{gender[g]} {name} {mid_name}, баланс вашого власного рахунку складає {balance} грн."
    print(text)

Name = input()
print(f"Мое имя {Name}")