import string
import random
# function that returns random slug string
# it will be used in IDs creation
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))



