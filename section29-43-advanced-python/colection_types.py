
DASH = 50
from pprint import pprint as pp

def list_types():
    print(' 1. List types '.center(DASH,'-'))
    names1 = ['Juan', 'Karla', 'Pedro']
    names2 = 'Laura Maria Ernesto Gonzalo'.split()

    # Original lists
    print(f'Original lists: {names1} {names2}')

    # Adding lists
    print(f'Added list: {names1+names2}')

    # Extend lists
    names1.extend(names2)
    print(f'Extended list: {names1}')

    numbers1 = [10, 50, 15, 4, 90, 4]

    # Index lists
    print(f'Index list (4): {numbers1.index(4)}')

    # Reverse lists
    numbers1.reverse()
    print(f'Reversed list: {numbers1}')

    # Order lists
    numbers1.sort()
    print(f'Ordered list: {numbers1}')

    numbers1.sort(reverse=True)
    print(f'Ordered list (reverse): {numbers1}')

    # Max and Min lists
    print(f'Max: {max(numbers1)}, Min: {min(numbers1)}')

    # Copy values lists
    numbers2 = numbers1.copy()
    print(f'Copied list: {numbers2}')

    # List multiplication
    numbers3 = [[1,2]]*5
    print(f'Multiplication list: {numbers3}')

    numbers3[0][1] = 3
    print(f'Multiplication list (not deep): {numbers3}')

    # Python matrix
    matrix1 = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
    print(f'Original matrix: {matrix1}')


def unpacking():
    print(' 2. Unpacking '.center(DASH,'-'))
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]

    # Original list
    print(f'Original list: {numbers1}')

    # Unpacking
    print('Unpacked list: ')
    print(*numbers1,sep='-')

    # In functions
    def sum(a, b, c):
        print('Result of sum:',a+b+c)

    sum(*numbers1)

    # To append in one list
    numbers3 = [*numbers1, *numbers2]
    print(f'Unpacked list: {numbers3}')


def zipping():
    print(' 3. Zipping '.center(DASH,'-'))
    numbers1 = [1, 2, 3]
    words1 = ['A', 'B', 'C', 'E']
    sets1 = {4, 5, 6, 1, 2, 9}
    
    mixing = list(zip(numbers1, words1, sets1))
    print(f'Zipped list: {mixing}')

    # Iterations
    for n, w, s in zip(numbers1, words1, sets1):
        print(f'Zipping iterations: {n} {w} {s}')
    
    # Unzipping
    numbers2, words2, sets2 = zip(*mixing)
    print(f'Unzipped lists: {numbers2} {words2} {sets2}')

    # Creating dictionaries from lists
    dictionary = dict(zip(words1, numbers1))
    print(f'Dictionary by lists: {dictionary}')


def tuple_types():
    print(' 4. Tuple types '.center(DASH,'-'))
    a, b = 'Hello', 'Bye'

    # Original tuples
    print(f'Original tuples: a={a} b={b}')

    # Swapping
    a, b = b, a
    print(f'Swapping tuples: a={a} b={b}')

    # Returning multiples values
    def minmax(*elements):
        return min(elements), max(elements)
    
    m, M = minmax(1, 2, 3, 4, 5)
    print(f'Unpacking tuples: Min={m} Max={M}')


def set_types():
    print(' 5. Set types '.center(DASH,'-'))

    try:
        # A set cannot include list
        set1 = {[1,2], [3,4]} 
    except:
        # A set can include tuples
        set1 = {(1,2), (3,4), 4, 1, 2} 
    print(f'Original set: {set1}')

    # Empty set
    set2 = set()
    print(f'Empty set: {set2}')

    # Adding values
    set2.add(1)
    set2.add(1) # This is skipeed
    set2.add(2)
    print(f'Adding values (not repeated): {set2}')

    # Update values
    set2.update(set1)
    print(f'Updating values (not repeated): {set2}')

    # Copying values
    set3 = set2.copy()
    print(f'Copying values: {set3}')
    print(f'Same content? {set3 == set2}')
    print(f'Same reference? {set3 is set2}')

    
    a = set([2, 4, 6, 8, 10])
    b = set([6, 7, 8, 9, 10])
    c = set([2, 4])

    # Union sets
    ab = a.union(b)
    print(f'Union sets: {ab}')

    # Difference sets
    ab = a.difference(b)
    print(f'Difference sets: {ab}')

    # Intersection sets
    ab = a.intersection(b)
    print(f'Intersection sets: {ab}')

    # Symmetric difference sets
    ab = a.symmetric_difference(b)
    print(f'Symmetric difference sets: {ab}')

    # Subsets
    ca = c.issubset(a)
    print(f'C {c} is in A {a}? {ca}')
    cb = c.issubset(b)
    print(f'C {c} is in B {b}? {cb}')

    # Supersets
    ca = c.issuperset(a)
    print(f'C {c} contains A {a}? {ca}')
    ac = a.issuperset(c)
    print(f'A {a} contains C {c}? {ac}')

    bc = b.isdisjoint(c)
    print(f'B {b} not contains any C {c}? {bc}')


def dict_types():
    print(' 6. Dict types '.center(DASH,'-'))

if __name__ == '__main__':
    list_types()
    unpacking()
    zipping()
    tuple_types()
    set_types()
    dict_types()