"""This program loops over array and prints it"""
from __future__ import print_function

class QuickFindUF(object):
    """Implementation Classs for Union Find"""

    def __init__(self, uf_id):
        self.uf_id = uf_id
        self.__preload_ids()

    def __preload_ids(self):
        if not self.uf_id:
            raise Exception('Array cannot be empty')

        for index, _ in enumerate(self.uf_id):
            self.uf_id[index] = index

    def is_connected(self, p_pos, q_pos):
        """Check if the given two object is connected

            Args:
                p_pos = Position of Object to be checked
                q_pos = Position of Object to be checked with
            Returns:
                two objects are connected or not
            Raises:
                none
        """
        return self.uf_id[p_pos] == self.uf_id[q_pos]

    def union(self, p_pos, q_pos):
        """Add a path between two objects

            Args:
                p_pos = Position of Object to be checked
                q_pos = Position of Object to be checked with
            Returns:
                prints message if objects are connected or not
            Raises:
                none
        """

        if self.is_connected(p_pos, q_pos):
            print("{0} and {1} are already connected".format(p_pos, q_pos))
            return

        p_id = self.uf_id[p_pos]
        q_id = self.uf_id[q_pos]

        for index, object_id in enumerate(self.uf_id):
            if object_id == p_id:
                self.uf_id[index] = q_id

    def result(self):
        """Shows all objects with connection group
        """
        for index, _ in enumerate(self.uf_id):
            print(index, end='  ')
        print()

        for group_id in self.uf_id:
            print(group_id, end='  ')
        print()

#your_list = [None]*size_required

def main():
    """Run Quck find"""
    size_of_object = int(input("Enter number of objects : "))
    qf_object = QuickFindUF([-1]*size_of_object)

    while True:
        number_list = input("Enter two numbers separated by space to add union: ").split(" ")
        if number_list and len(number_list) == 2:
            p_pos = int(number_list[0])
            q_pos = int(number_list[1])
            if p_pos < size_of_object and q_pos < size_of_object:
                #join objects
                qf_object.union(p_pos, q_pos)
            else:
                print("Number cannot be grater than size of the object")
        else:
            qf_object.result()
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
