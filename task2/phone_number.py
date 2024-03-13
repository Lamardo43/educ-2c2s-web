def wrapper(f):
    def fun(l):
        sorted_numbers = f(l)
        formatted_numbers = []
        for number in sorted_numbers:
            prefix = '+7'
            if len(number) > 10:
                number = number[1:]

            formatted_number = f"{prefix} ({number[:3]}) {number[3:6]}-{number[6:8]}-{number[8:]}"
            formatted_numbers.append(formatted_number)
        return formatted_numbers

    return fun


@wrapper
def sort_phone(l):
    return sorted(l)


if __name__ == '__main__':
    n = int(input())
    phone_numbers = [input() for _ in range(n)]
    formatted_numbers = sort_phone(phone_numbers)
    print(*formatted_numbers, sep='\n')
