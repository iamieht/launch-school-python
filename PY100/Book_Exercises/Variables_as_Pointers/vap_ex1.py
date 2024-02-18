# explain the difference between these two expressions.
my_object1 == my_object2
my_object1 is my_object2

# my_object1 == my_object2 compares two objects to see whether they are equal. They are considered equal when they have the same value or state. In the case of collections, two collections are equal when they have the same elements.

# my_object1 is my_object2 checks two variables to see whether they reference the same object. An object is the same as another object if both are stored at the same location in memory. In particular, that means we can say that my_object1 and my_object2 share the referenced object or that my_object1 and my_object2 are aliases for the same object.
