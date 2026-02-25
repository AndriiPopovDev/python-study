bicycles = ['track', 'cannondale', 'redline', 'specialized']
print(bicycles[1].title())

message = f"My first bike was a {bicycles[-1].title()}."
print(message)

names = ['vlad', 'max', 'ostap']
congrats = "very glad to see u!"

for name in names:
    print(f"{name.title()}, {congrats}")


motorcycles = ['honda', 'suzuki', 'yamaha']
motorcycles.insert(0, 'java')
motorcycles.append('ducati')
first_owned = motorcycles.pop(0)
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The first motorcycle I owned was {first_owned.title()}.")
print(f"The last motorcycle I owned was {last_owned.title()}.")
too_expansive = 'suzuki'
motorcycles.remove(too_expansive)
print(f"\nA {too_expansive.title()} is too expensive for me.")