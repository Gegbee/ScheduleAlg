import random

class Course:

    ONE_CHOICE, TWO_CHOICE, THREE_CHOICE = 0, 1, 2

    DEFAULT = 0
    CLASSES = ["default"]

    c1 = CLASSES[DEFAULT]
    c2 = None
    c3 = None

    def __init__(self, first_choice : str = "default", second_choice : str = None, third_choice : str = None):
        classes_dup = self.CLASSES.copy()

        if first_choice == "default":
            first_choice = classes_dup[random.randint(0, len(classes_dup) -1)]
        classes_dup.remove(first_choice)

        if second_choice == None:
            pass
        else:
            if second_choice == "default":
                second_choice = classes_dup[random.randint(0, len(classes_dup) -1)]
            classes_dup.remove(second_choice)

        if third_choice == None:
            pass
        else:
            if third_choice == "default":
                third_choice = classes_dup[random.randint(0, len(classes_dup) -1)]
            classes_dup.remove(third_choice)

        self.c1 = first_choice
        self.c2 = second_choice
        self.c3 = third_choice
        
        print("First:", self.c1, ", Second:", self.c2, ", Third:", self.c3)


    def get_class_val(course, class_name : str = "default"):
        return course.CLASSES.index(class_name)