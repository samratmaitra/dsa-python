def binary_search(lst:list, data, head:int=0, tail:int=None) -> int:
    if tail is None:
        tail = len(lst)-1
    idx = (head + tail) // 2
    if data == lst[idx]:
        return idx
    if idx == 0 or idx >= tail:
        return
    if data < lst[idx]:
        tail = idx-1
        return binary_search(lst, data, head, tail)
    if data > lst[idx]:
        head = idx+1
        return binary_search(lst, data, head, tail)

if __name__ == "__main__":
    elements = [1,4,7,9,12,15,19,24,28]
    for element in elements:
        print(binary_search(elements, element))
    
    print(binary_search(elements, -15))
    print(binary_search(elements, 17))
    print(binary_search(elements, 107))
