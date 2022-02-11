#!/usr/bin/env python
# 2022-02-11: ST

import math
from random import random
from fractions import Fraction

def fill_tile_with_square(width, height):
    '''
    Fill the given rectangle region of the (width x height) dimension with the same-sized square tiles.
    The sizes of region and tile must be integer.
    '''
    x = math.gcd(width, height)
    return {
        'tile': x,
        'cols': int(width / x),
        'rows': int(height / x)
    }


def generate_random_areas(num=10, max_repeat=5, max_size=300):
    '''
    Generate (width, height) randomly based on combination of primes for testing purpose.
    Returns a num set of (width, height) in the list.
    The number of prime combination is limited to max_repeat and
    the maximum size of (width, height) is set by max_size.
    '''
    primes = [2, 3, 5, 7]
    areas = []
    for n in range(num):
        pair = []
        for wh in range(2):
            length = 1
            for repeat in range(int(random()*(max_repeat - 1)) + 1):
                next_prime = primes[int(random() * len(primes))]
                if length * next_prime > max_size:
                    break
                length *= next_prime
            pair.append(length)
        areas.append(pair)
    return areas


def thumbnail_size(num):
    ''' This does not work '''
    aspect = math.sqrt(4 / 3 * num)
    cols = round(aspect)
    rows = math.floor(aspect)
    if aspect % 1.0 == 0:                                # Perfectly filled (multiple of 4*3=12)
        print('xxx', num, rows)
        rows -= 1

    return {
        'cols': cols,
        'rows': rows
    }


def fraction_tuple(wh):
    ''' A wrapper for the two elements tuple '''
    return Fraction(wh[0], wh[1])

def closer(wh1, wh2, target=(4, 3)):
    '''
    Auxiliary function for picking the one with the aspect ratio closer to the target (4/3).
    If equal, pick that one with wider width.
    Use fraction to avoid float rounding
    '''
    ret = ()
    target_aspect = fraction_tuple(target)
    wh1_aspect = fraction_tuple(wh1)
    wh2_aspect = fraction_tuple(wh2)
    wh1_distance = abs(wh1_aspect - target_aspect)
    wh2_distance = abs(wh2_aspect - target_aspect)
    if wh1_distance < wh2_distance:
        ret = wh1
    elif wh1_distance > wh2_distance:
        ret = wh2
    else:                                                # Same distance. Pick the positive distance (wider)
        if wh1_aspect < wh2_aspect:
            ret = wh2
        else:
            ret = wh1
    return ret

def thumbnail_size2(num):
    '''
    Find (width, height) that best represent 4:3 aspect ration with a given number of thumbnails.
    1) Find the optimal width range by obtaining two integers on both sides of sqrt(4 * n / 3).
    2) Using the list of widths, get the range of height.
    3) From both ranges, get combinations. Certain crteria apply.
    4) Select the (w, h) that has the aspect ration close to 4:3.
    '''
    # 1)
    w_float = math.sqrt(4 * num / 3)                     # Float.
    w_range = list({math.floor(w_float), math.ceil(w_float)})
    # 2)
    h_max = math.ceil(num / min(w_range))
    h_min = math.floor(num / max(w_range))
    h_range = [*range(h_min, h_max+1)]
    # 3)
    combinations = []
    for w in w_range:
        for h in h_range:
            # Do not include if the region is too small to fit the tiles.
            if h * w < num:
                continue
            # Do not include if portraited (pick landscape)
            if h > w:
                continue
            # Do not include if residual empty row exists
            if h * w - num >= h:
                continue
            combinations.append( (w, h) )

    # 4)
    best_hw = (100, 1)
    for comb in combinations:
        best_hw = closer(best_hw, comb)

    return {
        'cols': best_hw[0],
        'rows': best_hw[1]
    }


def draw_tiles(wh, num=None):
    cols = wh['cols']
    rows = wh['rows']
    if num == None:
        num = cols * rows

    squares = [ ['■'] * cols ] * rows
    residual = num - cols * rows
    if residual != 0:                                    # cavity
        squares[-1] = squares[-1][:residual]

    for row in squares:
        print(''.join(row))


if __name__ == '__main__':

    # Testing the Fill-with-Title problem
    for pattern in generate_random_areas():
        answer = fill_tile_with_square(*pattern)
        print(f'{pattern} → {answer}')

    ''' Single test
    thumbnail_size2(13)
    '''

    # Testing the Thumbnail fill problem
    for num in [*range(1, 19), *range(24, 120, 12)]:
        thumb = thumbnail_size2(num)
        print(num, thumb)
        draw_tiles(thumb, num)
