from numpy import random

def exponential_random(scale = None):
    if scale:
        return random.exponential(scale = scale)

    return random.exponential()