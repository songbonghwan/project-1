from Addr import *

class CustomerAddr(Addr):
    def __init__(self, name, tel, mail, addre, group, birth, Position, customername, item, customertitle):
        super().__init__(name, tel, mail, addre, group, birth, Position)
        self.__customername = customername
        self.__item = item
        self.__customertitle = customertitle

    def get_customername(self):
        return self.__customername
    def set_customername(self, value):
        self.__customername = value

    def get_item(self):
        return self.__item
    def set_item(self, value):
        self.__item = value

    def get_customertitle(self):
        return self.__customertitle
    def set_customertitle(self, value):
        self.__customertitle = value
                
    def print_info(self):
        super().print_info()
        print(f"회사이름 : {self.get_customername()}")
        print(f"부서이름 : {self.get_item()}")
        print(f"직급 : {self.get_customertitle()}")
