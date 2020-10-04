#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TITLE : MERGE SORT ALGORITHM
VERSION: 0.1
MOMENT OF CREATION: Tue Jul  2 16:44:27 2019

AUTHOR = DWIJAY D SHANBHAG

input parameter: arr is a one dimentional input parameter
"""

def merge_sort_ascending(arr):
    """sorting an array in ascending order"""
    if len(arr)<=1:
        '''If the length of array is one we don't need to sort'''
        return arr
    #global count
    #count += 1
    #print("Count:",count)
    '''c is the final sorted array for each batch'''
    c = [0]*len(arr)
    #print(arr)
    '''Dividing array in two parts'''
    a = arr[0:int(len(arr)/2)]
    b = arr[int(len(arr)/2):]
    '''i is index for a and j for b'''
    i = j = 0
    #print(len(a),len(b))
    #print(a,b)
    '''keep on calling the same function until the array is of length 1'''
    if len(a)>1:
        a = merge_sort_ascending(a)
    if len(b)>1:
        b = merge_sort_ascending(b)
    '''The following block is to merge two sorted arrays'''
    for k in range(len(arr)):
        #print("c",c)
        if len(a)==i:
            c[k:]=b[j:]
            break
        elif len(b)==j:
            c[k:]=a[i:]
            break
        
        if a[i]<b[j]:
            c[k]=a[i]
            i+=1
        #elif a[i]>b[j]:
        else:
            c[k]=b[j]
            j+=1
    #print("c before ending",c)   
    return c

