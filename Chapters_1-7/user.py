user_0 = {
    'user': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v.title()}")

for name in user_0.keys():
    print(name.title())
    
