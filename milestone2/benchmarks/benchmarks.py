from random import randint
from time import time

from milestone2.merge_sort import merge_sort
from milestone2.insertion_sort import insertion_sort


# Dictionary of labeled sort functions. If you decide to try writing a more optimized sort
# function, you can add it in an entry in this dictionary to see how it compares to the others.
sort_functions = {
    'merge_sort': merge_sort,
    'insertion_sort': insertion_sort
}


def benchmark(sort_fns, list_length, num_passes):
    """
    For each sorting function provided, generate a list with the specified length, then
    track the time to sort it. Repeat the specified number of times, then return the average
    run time for each sorting function.

    Because lists with shorter lengths can be sorted extremely quickly on modern hardware,
    it is helpful to take the average of many run times to avoid noisiness in the data.

    :param sort_fns: dictionary of sorting functions
    :param list_length: length of the list to generate that will be passed to sorting functions
    :param num_passes: number of times to run each sorting function
    :return: dictionary of sorting function name to average run time for given list length
    """

    raise NotImplementedError('Must complete TODOs in `milestone2/benchmarks/benchmarks.py before running!')

    times = {} # TODO: add entries to dictionary with the same keys as `sort_fns`, and all values as `0`

    for _ in range(num_passes):
        items = generate_list(list_length)

        # TODO: loop over each entry in the `sort_fns` dictionary
        #     items_copy = list(items) # insertion sort changes input array, so work with a copy
        #     start = time()
        #     TODO: call sort function with `items_copy` argument
        #     end = time()
        #     TODO: add the time duration (end - start) to the corresponding entry in the `times` dictionary

    # TODO: loop over each entry in `sort_fns` dictionary and divide the time duration by `num_passes`

    return times


def generate_list(length):
    """
    Generates a list of random integers between 0 and 100,000 to help with our benchmarking.

    :param length: length of list to be returned
    :return: list of random integers between 0 and 100,000
    """
    example = randint(0, 100000)

    # TODO: fill array with random numbers, up to specified `length`;
    # call `randint(0, 1000000)` for each number to generate
    return []


if __name__ == '__main__':
    list_length = 10
    num_passes = 10000

    # Since this can run rather slowly, you may want to skip the last benchmark by doing:
    # while num_passes >= 10
    while num_passes >= 1:
        results = benchmark(sort_functions, list_length, num_passes)

        print('Time to sort list length %s:\n%s\n' % (list_length, results))

        list_length = list_length * 10
        num_passes = int(num_passes / 10)
