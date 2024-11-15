from Addr import *  

class CompanyAddr(Addr):
    def __init__(self, name, tel, mail, addre, group, birth, Position, companyname, dept, title):
        super().__init__(name, tel, mail, addre, group, birth, Position)
        self.__companyname = companyname
        self.__dept = dept
        self.__title = title

    def get_companyname(self):
        return self.__companyname
    def set_companyname(self, value):
        self.__companyname = value

    def get_dept(self):
        return self.__dept
    def set_dept(self, value):
        self.__dept = value

    def get_title(self):

        return self.__title
    def set_title(self, value):
            self.__title = value
                
    def print_info(self):
        super().print_info()
        print(f"회사이름 : {self.get_companyname()}")
        print(f"부서이름 : {self.get_dept()}")
        print(f"직급 : {self.get_title()}")
