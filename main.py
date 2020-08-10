import random

class Node():

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree():
#Binary Tree algorithms
    def __init__(self):
      self.root = None


    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.data <= current.data:
                    if current.left_child == None:
                        current.left_child = new_node
                        return
                    else:
                        current = current.left_child
                else:
                    if current.right_child == None:
                        current.right_child = new_node
                        return
                    else:
                        current = current.right_child

    def printTree(self):
        def printSubTree(node):
            if node.left_child != None:
                temp = printSubTree(node.left_child) + " {0}".format(node.data)
                if node.right_child != None:
                    return temp + " " + printSubTree(node.right_child)
                else:
                    return temp
            elif node.right_child != None:
                return "{0} ".format(node.data) + printSubTree(node.right_child)
            else:
                return "{0}".format(node.data)
                
        print(printSubTree(self.root.left_child)
              + " {0} ".format(self.root.data)
              + printSubTree(self.root.right_child))
        

def main():
    bst = BinarySearchTree()
    arr = [100, 58, 75, 70, 74]
#    for i in range(5):
#      r = random.randint(0, 100)
#      arr.append(r)
#      bst.insert(r)
#    for n in arr:
#      print(n, end=" ")
#    print("\n")
    for n in arr:
      bst.insert(n)
    bst.printTree()
    

if __name__ == "__main__":
    main()
            
        
        
        
        
        
    
    
        
