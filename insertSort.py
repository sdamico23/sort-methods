
def insSort(lst):
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j-1] < lst[j]:
            temp = lst[j-1]
            lst[j-1] = lst[j]
            lst[j] = temp
            j -= 1
        i += 1
def main():
    inp = input("Please enter the numbers to sort: ")
    oglst = [int(x) for x in inp.split()]
    inp2 = input("Please enter the positions that are important: ")
    pos = [(int((x-1)) for x in inp2.split())]
    lst = []
    for i in range(0,len(oglst)):
        if i not in pos:
            lst.append(oglst[i])
    insSort(lst)
    ans = []
    for i in range(0,len(pos)):
        ans.append(pos[i])
    for i in range(0, len(lst)):
            ans.append(lst[i])
    print("The sequence you want is: ",end = "")
    for i in ans:
        print(i,end = " ")
main()
