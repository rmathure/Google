__author__ = 'rohanmathure'


class Node(object):
    def __init__(self):
        self.next = None
        self.data = None
        #list1 and list2 means the starting node of the list


def addList(outputList,smallList):
    outputList.next = smallList
    outputList = outputList.next
    smallList =smallList.next
    return outputList,smallList

def mergeList(list1, list2):
    outputList = None
    retNode = None
    if list1 is not None and list2 is not None:
        if list1.data < list2.data:
            retNode = list1
        else:
            retNode = list2
    elif list1 is not None:
        retNode = list1
    elif list2 is not None:
        retNode = list2

    while True:
        if list1 is None and list2 is None:
            break
        elif list1 is None:
            outputList,list2 = addList(outputList, list2)
        elif list2 is None:
            outputList,list1 = addList(outputList, list1)
        else:
            if list1.data < list2.data:
                outputList,list1 = addList(outputList, list1)
            else:
                outputList,list2 = addList(outputList, list2)
    return retNode
