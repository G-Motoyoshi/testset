class Withoutanimal(Exception):
    """animal is not in ['dog', 'cat', 'bird']"""
    pass

class animal:
    """animal information"""
    def __init__(self, animal = 'dog'):
        """information saved

        Arguments:
            animal {str} -- select ['dog', 'cat', 'bird']
        """
        if animal in ['dog', 'cat', 'bird']:
            self.animal = animal
        else :
            raise Withoutanimal("{0} is not in ['dog', 'cat', 'bird']".format(animal))

    def judge(self):
        """animal judge sound"""
        if self.animal == 'dog':
            print('bow-wow')
        elif self.animal == 'cat':
            print('meow')
        elif self.animal == 'bird':
            print('chirp')
