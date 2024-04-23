

def cancellation(list, stop_word):
    '''
    Copy elements one by one from input_list into output_list. 
    If one of the elements is equal to the stop_word, then stop the function,
    and return what you have so far.
    '''
    pass

def copy_all_but_skip_word(input_list, skip_word):
    '''
    This function should copy elements one by one from input_list into output_list.
    If one of the elements is equal to the skip_word, then you should skip that element,
    but keep checking all of the other elements.
    '''
    pass

def my_average(input_list):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    pass


def cancellation(input_list, stop_word):
    output_list=[]
    for x in input_list:
        if x== stop_word:
            break# When python sees this command, it skips to the next value of 
        output_list.append(x)
    return output_list

def copy_all_but_skip_word(input_list, skip_word):
    output_list=[]
    for x in input_list:
        if x== skip_word:
            continue# When python sees this command, it skips to the next value of 
        output_list.append(x)
    return output_list


def my_average(input_list):
    '''
    You may assume that `input_list` is a non-empty list, in which every element is a number.  
    Calculate the average value, and return it. 
    '''
    sum=0
    for x in input_list:
        sum=sum+x
    return sum / len(input_list)
