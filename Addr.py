from ShowData import *

class Addr(ShowData):
        def __init__(self, name, tel, mail, addre, group, birth, Position):
                self.__name = name
                self.__tel = tel
                self.__mail = mail
                self.__addre = addre
                self.__group = group
                self.__birth = birth
                self.__Position = Position
        
        def get_name(self):
                return self.__name
        def set_name(self, value):
                self.__name = value

        def get_tel(self):
                return self.__tel
        def set_tel(self, value):
                self.__tel = value

        def get_mail(self):
                return self.__mail
        def set_mail(self, value):
                self.__mail = value

        def get_addre(self):
                return self.__addre
        def set_addre(self, value):
                self.__addre = value

        def get_group(self):
                return self.__group
        def set_group(self, value):
                self.__group = value

        def get_birth(self):
                return self.__birth
        def set_birth(self, value):
                self.__birth = value

        def get_Position(self):
                return self.__Position
        def set_Position(self, value):
                self.__Position = value

        def print_info(self):
                print(f"이름 : {self.get_name()}")
                print(f"번호 : {self.get_tel()}")                
                print(f"메일 : {self.get_mail()}")
                print(f"주소 : {self.get_addre()}")
                print(f"그룹(회사/거래처) : {self.get_group()}")
                print(f"생일 : {self.get_birth()}")
                print(f"직급 : {self.get_Position()}")
        
        def showData(self):
                print(f"이름 : {self.get_name()}")
                print(f"번호 : {self.get_tel()}")  
                return

