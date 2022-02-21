import random
import string

def gen(length):
    all = string.ascii_letters + string.digits + string.punctuation
    passw = "".join(random.sample(all,length))
    return passw