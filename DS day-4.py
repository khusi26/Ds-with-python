#Linear search in python
'''
def linearSearch(array,n,x):

    #Going through array sequentially
    for i in range(0, n):
        if (array[i] == x):
            return i
        return -1
array = [2 ,4 ,0 ,1 ,9]
x= 10
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ",result)

#Binary Search in python
def binarysearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [3, 4, 5, 6, 7, 8, 9]
x = 4 
result = binarysearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index" + str(result))
else:
    print("Not found")
'''
#tree traversing
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "-", end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')
def Preorder(root):
    if root:
        print(str(root.val) + "->",end='')
        Preorder(root.left)
        Preorder(root.right)
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current
def deleteNode(root, key):        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder traversal")
inorder(root)
print("\nPreorder traversal")
Preorder(root)
print("\nPostorder traversal")
postorder(root)
'''
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "-", end='')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
print("inorder traversal:",end=" ")
inorder(root)
'''
#question
'''
class Compartment:
    def __init__(self, name, total_seating_capacity, num_passengers):
        self.name = name
        self.total_seating_capacity = total_seating_capacity
        self.num_passengers = num_passengers

class Train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.compartment_list = compartment_list

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        return self.compartment_list

    def count_compartments(self):
        return len(self.compartment_list)

    def check_vacancy(self):
        count = 0
        for compartment in self.compartment_list:
            if compartment.num_passengers < compartment.total_seating_capacity * 0.5:
                count += 1
        return count
compartment_list = [Compartment('A', 50, 30), Compartment('B', 40, 20), Compartment('C', 30, 10)]
train = Train('Express', compartment_list)
print(train.get_train_name())
print(train.get_compartment_list())
print(train.count_compartments())
print(train.check_vacancy())

'''
#question
'''
import re

class Item:
    def _init_(self, item_name, author_name, published_year):
        self.item_name = item_name
        self.author_name = author_name
        self.published_year = published_year
        
    def get_item_name(self):
        return self.item_name
    
    def get_author_name(self):
        return self.author_name
    
    def get_published_year(self):
        return self.published_year
    
    def _str_(self):
        return f"{self.item_name} by {self.author_name} ({self.published_year})"


class Library:
    def _init_(self, new_item_list):
        self.item_list = new_item_list
        
    def get_item_list(self):
        return self.new_item_list
    
    def sort_item_list_by_author(self, new_item_list):
        sorted_list = sorted(new_item_list, key=lambda x: re.sub(r'\W+', '', x.get_author_name()).lower())
        return sorted_list
    
    def add_new_items(self, new_item_list):
        sorted_list = self.sort_item_list_by_author(new_item_list)
        self.item_list.extend(sorted_list)
        self.item_list = sorted(self.item_list, key=lambda x: re.sub(r'\W+', '', x.get_author_name()).lower())
    
    def sort_items_by_published_year(self):
        sorted_list = sorted(self.item_list, key=lambda x: (x.get_published_year(), re.sub(r'\W+', '', x.get_author_name()).lower()))
        return sorted_list
'''

#question

def find_unknown_words(text, vocabulary):
    words = text.split()
    unknown_words = set(words) - set(vocabulary)
    if len(unknown_words) == 0:
        return -1
    return unknown_words
text = "the sun rises in the east"
vocabulary = ["sun","in","east","doctor","day"]
unknown_words = find_unknown_words(text, vocabulary)
print(unknown_words)














    
    
    
