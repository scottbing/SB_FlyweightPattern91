#from random import uniform, random, choice, sample, choices
import random
import arr

class LandscapeTrees(object):
    """Tree Class"""

    """default constructor"""

    def __init__(self):
        pass

    """active constructor"""

    def trees(self, tree_name):
        return "LandscapeTree[% s]" % (tree_name)


class TreeSpecies(object):
    
    """use a dictionary to store the tree information"""
    tree_family = {}

    """This is the basis of the Flyweight pattern..."""
    """if tree already exists, use it, otherwise create a new one"""
    """trees are delineated by a unique id"""
    def __new__(cls, name, tree_family_id):
        try:
            id = cls.tree_family[tree_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.tree_family[tree_family_id] = id
        return id

    def set_tree_info(self, tree_info):
        """set the tree information"""
        cg = LandscapeTrees()
        self.tree_info = cg.trees(tree_info)

    def get_tree_info(self):
        """return the tree information"""
        return (self.tree_info)


if __name__ == '__main__':

    Evergreens = ['Red Cedar', 'Jack Pine', 'Douglas Fir', 'Live Oak', 'Holly'];
    Spruce = ['Oriental Spruce', 'Colorado Spruce', 'Norway Spruce', 'Red Spruce', 'Dragon Spruce']
    alpha = ['a', 'b', 'c', 'd', 'e', 'f']
    evergreen_tree_data = ();
    spruce_tree_data = ();

    """prompt the user"""
    print("Welcome to Bing's Landscaping")
    print("You will be asked how many trees you would like to have planted on your property.")
    evg = input("How many Evergreens? ")
    print("Number of Evergreens", evg)

    print(random, type(random))
    evergreen_tree = random.choices(tuple(Evergreens))
    print("Randomly item from Set is - ", evergreen_tree)

    spc = input("How many Spruce? ")
    print("Number of Spruce", spc)

    """Evergreen Trees"""
    evergreen_tree_data = (('a', 1, 'DouglasFir'), ('a', 2, 'Hemlock'), ('b', 1, 'Holly'))
    eg_tree_family_objects = []

    """process  the trees"""
    for i in evergreen_tree_data:
        obj = TreeSpecies(i[0], i[1])
        obj.set_tree_info(i[2])
        eg_tree_family_objects.append(obj)

    """objects with the same hash are the same object"""
    print(" \nEvergreen Trees")
    for i in eg_tree_family_objects:
        print("id = " + str(id(i)))
        print(i.get_tree_info())

    """Spruce Trees"""
    spruce_tree_data = (('a', 1, 'Blue'), ('a', 2, 'Black Hills'), ('b', 1, 'Norway'))
    sp_tree_family_objects = []

    """process  the trees"""
    for i in spruce_tree_data:
        obj = TreeSpecies(i[0], i[1])
        obj.set_tree_info(i[2])
        sp_tree_family_objects.append(obj)

    """objects with the same hash are the same object"""
    print(" \nSpruce Trees")
    for i in sp_tree_family_objects:
        print("id = " + str(id(i)))
        print(i.get_tree_info())
