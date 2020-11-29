
if __name__ == '__main__':
    with open('input') as f:
        numbers = map(lambda s: int(s), filter(None, f.read().split('\n')))
    fuel_req = map(lambda mass: int(mass / 3) - 2, numbers)
    sum_fuel = sum(fuel_req)
    print(sum_fuel)