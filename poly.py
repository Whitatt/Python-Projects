
class Bird:#Parent class created
    genus = 'bird'
    family = 'vertebrates'

    def intro(self):
      print("There are many types of birds.")
     
    def flight(self):
      print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):#example of 2 child classes with methods
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()

class Tree:#parent class tree
    genus = 'grass'
    genus = 'tree'
    family = 'tree'

    def tree_type(self):
        print("There_are_many_types_of_trees.")

    def grass(self):
        print("Most of the grasses have no_category.")

class herbs(Tree):#child classes with methods
    def tree_type(self):
        print("herbs are also one form of tree and plant.")

class root(Tree):
    def tree_type(self):
        print("root don’t lie in any tree category.")


obj_tree = Tree()
obj_gr = root()
obj_herbs = herbs()
obj_tree.tree_type()
obj_gr.grass()
obj_herbs.tree_type()
obj_herbs.tree_type()
obj_gr.tree_type()
obj_herbs.grass()
