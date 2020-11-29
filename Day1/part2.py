def calc_fuel(mass):
    total_fuel = 0
    while True:
        fuel = int(mass / 3) - 2
        if fuel <= 0:
            return total_fuel
        total_fuel += fuel
        mass = fuel


if __name__ == '__main__':
    with open('input') as f:
        numbers = map(lambda s: int(s), filter(None, f.read().split('\n')))
    fuel_req = map(calc_fuel, numbers)
    sum_fuel = sum(fuel_req)
    print(sum_fuel)