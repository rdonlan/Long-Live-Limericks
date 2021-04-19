from random import randint


class Limerick:
    line_1 = "empty"
    line_2 = "empty"
    line_3 = "empty"
    line_4 = "empty"
    line_5 = "empty"

    def __init__(self, subject_name):
        self.title = "An old limerick about " + subject_name + " #" + str(randint(0, 1000)) + ":"

    # this method adds lines to limerick object
    def add_line(self, line_num, line):
        if line_num == 1:
            self.line_1 = line
        if line_num == 2:
            self.line_2 = line
        if line_num == 3:
            self.line_3 = line
        if line_num == 4:
            self.line_4 = line
        if line_num == 5:
            self.line_5 = line


    def __str__(self):
        # allows you to use print(Recipe)
        final_string = self.title + "\n"
        final_string += self.line_1 + "\n"
        final_string += self.line_2 + "\n"
        final_string += self.line_3 + "\n"
        final_string += self.line_4 + "\n"
        final_string += self.line_5
        return final_string    



