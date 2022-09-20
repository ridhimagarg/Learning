
# coding: utf-8

# ## E-commerce Navigation Tree
# It is fully dynamic. You can add any no. of nodes in a tree and traverse the whole tree using commands/functions here for this 
# implementation like -:
# <b>
#   1. Tree()(initializer/constructor function of a class)-> function for creating a mode. which takes 2 parameters
#             a. data of node.
#             b. code with associated node. 
#   2. add_child() -> function for adding child to a perticular node. Takes 2 objects-:
#             a. Parent node
#             b. Child node
#   3. node_with_code() -> Traverse the tree upto the specified code node. It takes code of the node as a parameter.
#     
#   4. move_back() -> It moves the user back upto certain(given) level. It takes level(num) as a parameter. By default level =1.
#   
#   5. goto() -> goto a certain level by giving num as a parameter </b>




## global variable for accessing the current Tree
current = None
## list of visted Trees till now 
## which path we followed
l = []


## Creating class(Tree) for making nodes and adding childrens.
## Also traversing tree using commands.
## Here for every command I created functions.

class Tree(object):
    
    """Constructor functions called when class is called
     Parameterized constructor taking data and code of a creating node"""
    
    def __init__(self, data, code):
        
        ## Storing code of the created data into current created object
        self.code = code
        
        ## Storing data of the created data into current created object
        self.data = data
        
        ## Till there are no children of a newly created node [] list.
        self.children = []
        
        
        

    """ Child function i.e, to add a child to a particular node of a tree
        self-> current object to which child should be added.
        obj-> child object should be added as a child to self object."""
    
    def add_child(self, obj):
        
        ## Adding obj as a child to self
        self.children.append(obj)
        
        
        
        
    
    """Accessing(Traversing to a node) the node using code of that particular node
        Creating it as a class method as to access the variables which are gloabally to keep
        track of current object/node of the tree.
        Parameters -> 1. cls => class 
                      2. code => code of a particular node"""
    
    @classmethod
    def node_with_code(cls,code):
        
        ## Acessing the global variables 
        ## Otherwise newly local variable will be created (without global keyword)
        global l
        global current
        
        ## If current object is none -> means user didn't open up the website. So setting it to home.
        if current == None:
            current = Home
            
        ## Similarly with list of traversed nodes => If [] then added first node => home.
        if l == []:
            l.append(Home)
            
        ## Then traverse till the given node code. Using children of home(root) node.
        for e in current.children:
            ## If code matches with one of the children code then added it to traversed list.
            if e.code == code:
                l.append(e)
        
        ## Setting current object/node to the last node traversed.
        current = l[-1]
        
        ## Now printing the traversed nodes till now.
        print('-> '.join([str(e.data) for e in l]))
        
        
        

    """This function is for MB command (Moving back upto a given level). So here if not any level
        then it will be by default=1. """
    
    @classmethod
    def move_back(cls,level=1):
        
        ## Accessing the global variables to keep track of where my current pointer/node is.
        global l
        global current
        
        ## Conditional Check if user is entering number which is less than the traversed node it will given an error message
        ## If correct, then using loop popping out the nodes upto the number he wants to move back.
        
        if level < len(l):
            for i in range(level):
                l.pop()
        else:
            print("Enter valid number")
            
        ## Again updating the final current node/pointer to the last element traversed.
        current = l[-1]
        
        ## printing the updated list of nodes he came back upto.
        print('-> '.join([str(e.data) for e in l]))
        
        
        
        
    """goto function works similarly to goto command of breadcrumb tree. In this by default=1 if user didn't
        mention upto which node he wants to go."""
    
    @classmethod
    def goto(cls,level=1):
        
        ## accessing the global variables to keep track of where my current pointer/node is.
        global l
        global current
        
        ## Popping the elements till user wants to go back.
        for i in range(((len(l))-level)):
            l.pop()
        
        ## Again updating our current pointer/Node upto which user traversed last.
        current = l[-1]
        
        ## printing the updated list
        print('-> '.join([str(e.data) for e in l]))
        
        


# ### Creating a whole tree given as an example in the assignment 




## Creating nodes for a tree

Home = Tree('Home','H')
Men = Tree('Men','M')
Women = Tree('Women','W')
Electronics = Tree('Electronics', 'E')





## Adding children to node -> here home as a parent node and Men, Women, Electronics as a children node of it.

Home.add_child(Men)
Home.add_child(Women)
Home.add_child(Electronics)





Clothing = Tree('Clothing','C')
Footwear = Tree('Footwear','F')
Accessories = Tree('Accessories','A')





Men.add_child(Clothing)
Men.add_child(Footwear)
Men.add_child(Accessories)





Women.add_child(Clothing)
Women.add_child(Footwear)
Women.add_child(Accessories)





Jeans = Tree('Jeans','J')
Trousers = Tree('Trousers','T')
Shirts = Tree('Shirts','S')





Clothing.add_child(Jeans)
Clothing.add_child(Trousers)
Clothing.add_child(Shirts)





Slippers = Tree('Slippers','L')
Shoes = Tree('Shoes','S')





Footwear.add_child(Slippers)
Footwear.add_child(Shoes)





Formal_Shoes = Tree('Formal shoes', 'F')
Casual_Shoes = Tree('Casual shoes', 'C')
Sport_Shoes = Tree('Sports shoes', 'SS')





Shoes.add_child(Formal_Shoes)
Shoes.add_child(Casual_Shoes)
Shoes.add_child(Sport_Shoes)





Wallets = Tree('Wallets','w')
Watches = Tree('Watches','T')
Bags = Tree('Bags','B')





Accessories.add_child(Wallets)
Accessories.add_child(Watches)
Accessories.add_child(Bags)





Computers = Tree('Computers','C')
Mobiles = Tree('Mobiles' , 'M')





Electronics.add_child(Computers)
Electronics.add_child(Mobiles)


# ### Traversing the created tree using functions -> goto, move back etc.




## Traversing the tree with a node code.

Tree.node_with_code('M')





Tree.node_with_code('C')





## Moving back to one level

Tree.move_back()





Tree.node_with_code('F')





## Moving back to two level.

Tree.move_back(2)





Tree.move_back()





## Traversing nodes with codes
## Each time it is printing the traversed list of nodes.

Tree.node_with_code('H')
Tree.node_with_code('M')
Tree.node_with_code('F')
Tree.node_with_code('S')
Tree.node_with_code('C')





Tree.move_back(2)





Tree.goto(2)

