class LandscapeTrees(object):
    """Tree Class"""

    """default constructor"""

    def __init__(self):
        pass

    """active constructor"""

    def trees(self, tree_name):
        return "LandscapePattern[% s]" % (tree_name)


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
