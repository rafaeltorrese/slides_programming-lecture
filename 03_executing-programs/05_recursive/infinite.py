def print_next_number(start):
    print(start + 1)
    # if start >= 7:
    #     return "I'm bored"
    return print_next_number(start + 1)

if __name__ == "__main__":
    print_next_number(5)