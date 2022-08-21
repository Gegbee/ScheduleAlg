import random

from courses import English, SocialStudies

class StudentForm:

    YEAR_ONE = FRESHMAN = 0
    YEAR_TWO = SOPHOMORE = 1
    YEAR_THREE = JUNIOR = 2
    YEAR_FOUR = SENIOR = 3

    english_choice = None
    social_studies_choice = None
    year = YEAR_ONE
    student_id = 000000

    def __init__(self, _id : int, _year : int, _english_choice : str, _social_studies_choice : str):
        self.english_choice = English(_english_choice, "default")
        self.social_studies_choice = SocialStudies(_social_studies_choice, "default")
        self.year = _year
        self.student_id = _id
        