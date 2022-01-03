def bainary_search(data,terget,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if terget == data[mid]:
            return True
        elif terget < data[mid]:
            return bainary_search(data,terget,low,high)
        else:
            return bainary_search(data,terget,mid+1,high)
bainary_search
