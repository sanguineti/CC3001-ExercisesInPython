import numpy as np


class Course:
    def __init__(self, name, code, ud, semester, req):
        self.name = name
        self.code = code
        self.ud = ud
        self.semester = semester
        self.req = req

    def print_info(self):
        print("Course Name: ", self.name)
        print("Course Code: ", self.code)
        print("UDs: ", self.ud)
        print("Semester: ", self.semester)
        print("\n")

    def print_req(self):
        self.print_info()
        print("\n")
        if self.req.size != 0:
            for course in self.req:
                course.print_req()


if __name__ == "__main__":
    # First Semester
    no_req = np.empty(0)
    cc1000 = Course("Herramientas Computacionales", "CC1000", 5, 1, no_req)
    ma1001 = Course("Introducción al Cálculo", "MA1001", 10, 1, no_req)
    ma1101 = Course("Introducción al Álgebra", "MA1101", 10, 1, no_req)
    fi1001 = Course("Introducción a la Física", "FI1001", 10, 1, no_req)

    # Second Semester
    mat_req = np.array([ma1001, ma1101], dtype=Course)
    ma1002 = Course("Cálculo Diferencial e Integral", "MA1002", 10, 2, mat_req)
    ma1102 = Course("álgebra Lineal", "MA1102", 10, 2, mat_req)
    fi1002 = Course("Sistemas Newtonianos", "FI1002", 10, 2, np.array([fi1001, cc1000], dtype=Course))

    fi2001 = Course("Mecánica", "FI2001", 10, 3, np.array([ma1002, ma1102, fi1002], dtype=Course))
    fi2001.print_req()
