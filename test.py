if __name__ == "__main__":
    import random
    import string
    # Create random string and specify its lenght
    def random_string_generator(str_size):
        chars = "#" + string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for x in range(str_size))



    size = 12
    print('Random String of length 12 =', random_string_generator(size))

