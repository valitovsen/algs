
def huffman_encode(frequencies):
    '''
    huffman_encode(frequencies) -> optimal binary encoding of alphabet

    Given list of frequencies return list of optimal binary codes:
        frequencies: list of non-negative values

    A. Valitov 2017
    '''
    from heap import Heap

    # 1. Create mappings
    char_to_freq = {}   # create {dummy char -> frequency} mapping
    freq_to_chars = {}   # create {frequency -> set of dummy chars} mapping
    for freq in frequencies:
        if freq >= 0:
            freq_to_chars[freq] = set()
        else:
            raise ValueError('frequencies must be non-negative')
    for char in range(len(frequencies)):
        char_to_freq[str(char)] = frequencies[char]
        freq_to_chars[char_to_freq[str(char)]].add(str(char))
    char_encoding = {char:'' for char in char_to_freq}  # create codes dict

    # 2. Create heap to hold frequencies
    freq_heap = Heap()
    freq_heap.heapify(list(freq_to_chars.keys()))
    freq_heap_size = len(freq_to_chars.keys())

    # 3. Loop through heap
    while freq_heap_size > 1:
        freq_a, freq_b = freq_heap.extract(),freq_heap.extract() # extract two lowest frequencies
        char_a, char_b = freq_to_chars[freq_a].pop(), freq_to_chars[freq_b].pop() # pop random chars with given freqs (chars may share frequencies)
        freq_ab = freq_a + freq_b # frequency for union of chars
        char_ab = char_a + '_' + char_b # char for union of chars
        freq_heap.insert(freq_ab) # re-insert union frequency
        if freq_ab in freq_to_chars:
            freq_to_chars[freq_ab].add(char_ab)
        else:
            freq_to_chars[freq_ab] = set([char_ab])
        #update codes a -> 0, b -> 1
        for union_char in (char_a,char_b):
            for char in union_char.split('_'):
                char_encoding[char] = {char_a:'0', char_b:'1'}[union_char] + char_encoding[char]
        freq_heap_size -= 1
    # 4. Return codes in order of given frequencies
    return [char_encoding[str(i)] for i in map(int, sorted(list(char_encoding.keys())))]


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        raw = sys.stdin.readlines()
    else:
        raw = open(sys.argv[1]).readlines()
    data = [int(char.strip()) for char in raw]
    res = huffman_encode(data)
    print('Huffman codes:')
    for line in res:
        print(line)
