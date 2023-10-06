import time
import random
from collections import Counter
import matplotlib.pyplot as plt
from string import ascii_lowercase, ascii_uppercase


class NodeTree(object):
     '''
     Tree Nodes
     '''
     def __init__(self, left=None, right=None):
         self.left = left
         self.right = right

     def children(self):
         return self.left, self.right



def huffman_code_tree(node, binString=''):
     '''
     Function to find Huffman Code
     '''
     if type(node) is str:
         return {node: binString}
     (l, r) = node.children()
     d = dict()
     d.update(huffman_code_tree(l, binString + '0'))
     d.update(huffman_code_tree(r, binString + '1'))
     return d


def make_tree(nodes):
     '''
     Function to make tree
     return: Root of the tree
     '''
     while len(nodes) > 1:
         (key1, c1) = nodes[-1]
         (key2, c2) = nodes[-2]
         nodes = nodes[:-2]
         node = NodeTree(key1, key2)
         nodes.append((node, c1 + c2))
         nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
     return nodes[0][0]


def main(string):
    start_time = time.time()
    for _ in range(300):
      freq = dict(Counter(string))
      freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
      node = make_tree(freq)
      encoding = huffman_code_tree(node)
    end_time = time.time()
    final_time = (end_time - start_time)/300
    return final_time


def make_strings(by_freq):
  x = []
  string_list = []
  chars = ascii_uppercase+ascii_lowercase
  chars_4 = ['A', 'B', 'C', 'D']
  for i in range(5,500,20):
    x.append(i)
    string = ''
    if by_freq:
      num = int(i/4)
      for char in chars_4:
        char = char*num
        string = string + char  
      string_list.append(string)
    else:
      for _ in range(i):
          char = random.choice(chars)
          string = string + char
      string_list.append(string)
  return x, string_list


x, string1 = make_strings(False)
x, string2 = make_strings(True)
list_time_1 = []
list_time_2 = []

for i in string1:
    list_time_1.append(main(i))
for i in string2:
    list_time_2.append(main(i))


plt.plot(x, list_time_1, '-b', label='by num')
plt.plot(x, list_time_2, '-r', label='by freq')
plt.legend()
plt.show()
