from heapq import nsmallest

def load_input():
    with open('./2015/inputs/day02_input.txt') as input:
        output = []
        for line in input.readlines():
            dimensions = line.split('x')
            dimension_tuple = (int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
            output.append(dimension_tuple)
        return output

def part1(present_list):
    initial_calc = []
    for present in present_list:
        x,y,z = present
        initial_calc.append((x*y, x*z, y*z))
    final_calc = 0
    for calc in initial_calc:
        final_calc += min(calc) + sum(calc) * 2
    print(final_calc)

def part2(present_list):
    initial_calc = []
    for present in present_list:
        smallest_two = nsmallest(3, present)
        initial_calc.append(present[0]*present[1]*present[2] + (smallest_two[0]+smallest_two[1])*2)
    print(sum(initial_calc))

def main():
    present_list = load_input()
    part1(present_list)
    part2(present_list)

if __name__ == "__main__":
    main()