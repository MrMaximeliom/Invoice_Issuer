import random
import string
# Create random string and specify its length
def random_string_generator(str_size):
    chars = "#" + string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for x in range(str_size))