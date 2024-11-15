from CompanyAddr import *
from CustomerAddr import *

class SmartPhone(Addr):
    def __init__(self):
        self.storage = []
        self.companystorage = []
        self.customerstorage = []

    def set_adden(self):
        name = input("이름을 입력하세요 : ")
        tel = input("번호를 입력하세요 : ")
        mail = input("메일을 입력하세요 : ")
        addre = input("주소를 입력하세요 : ")
        group = input("그룹(회사/거래처)를 입력하세요 : ")
        birth = input("생일 입력하세요 : ")
        Position = input("직급을 입력하세요 : ")
        if group == "회사":
            companyname = input("회사이름을 입력하세요 : ")
            dept = input("부서를 입력하세요 : ")
            title = input("회사직급을 입력하세요 : ")
            contact = CompanyAddr(name, tel, mail, addre, group, birth, Position, companyname, dept, title)
            self.companystorage.append(contact)
            self.storage.append(contact)
            print("저장 완료")
        elif group == "거래처":
            customername = input("거래처이름을 입력하세요 : ")
            item = input("품목이름을 입력하세요 : ")
            customertitle = input("거래처직급을 입력하세요 : ")
            contact = CustomerAddr(name, tel, mail, addre, group, birth, Position, customername, item, customertitle)
            self.customerstorage.append(contact)
            self.storage.append(contact)
            print("저장 완료")
        else:
            print("입력오류")
            return None
 
    def modify_contact(self):
        if not self.storage:
            print("저장된 연락처가 없습니다.")
        else:
            name = input("수정할 이름을 입력하세요 : ")
            for contact in self.storage:
             if contact.get_name() == name:      
                name = input("새로운 이름을 입력하세요 : ")
                tel = input("새로운 번호를 입력하세요 : ")
                mail = input("새로운 메일을 입력하세요 : ")
                addre = input("새로운 주소를 입력하세요 : ")
                birth = input("새로운 생일 입력하세요 : ")
                Position = input("새로운 직급을 입력하세요 : ")
                if contact.get_group() == "회사":
                    companyname = input("새로운 회사이름을 입력하세요 : ")
                    dept = input("새로운 부서를 입력하세요 : ")
                    title = input("새로운 회사직급을 입력하세요 : ")
                    contact.set_companyname(companyname)
                    contact.set_dept(dept)
                    contact.set_title(title)
                elif contact.get_group() == "거래처":
                    customername = input("새로운 거래처이름을 입력하세요 : ")
                    item = input("새로운 품목이름을 입력하세요 : ")
                    customertitle = input("새로운 거래처직급을 입력하세요 : ")
                    contact.set_customername(customername)
                    contact.set_item(item)
                    contact.set_customertitle(customertitle)
                else:
                    print("입력오류")
                    return None
                contact.set_name(name)
                contact.set_tel(tel)
                contact.set_mail(mail)
                contact.set_addre(addre)
                contact.set_birth(birth)
                contact.set_Position(Position)
                print("연락처가 수정되었습니다.")
                return 
             else:
                print("해당 연락처가 없습니다")

    def delete_addr(self):
        name = input("삭제할 이름을 입력하세요 : ")
        for contact in self.storage:
            if contact.get_name() == name:
                self.storage.remove(contact)
                if contact in self.companystorage:
                    self.companystorage.remove(contact)
                if contact in self.customerstorage:
                    self.customerstorage.remove(contact)
                print("연락처가 삭제되었습니다.")
                return
        print("연락처를 찾을 수 없습니다.")

    def see_addr(self):
        if not self.storage:
            print("저장된 연락처가 없습니다.")
        else:
            for contact in self.storage:
                print("-" * 30)
                contact.print_info()
                print("-" * 30)

    def company_addr(self):
        if not self.companystorage:
            print("그룹:회사에 저장된 연락처가 없습니다.")
        else:
            for contact in self.companystorage:
                print("-" * 30)
                contact.print_info()
                print("-" * 30)

    def customer_addr(self):
        if not self.customerstorage:
            print("그룹:거래처에 저장된 연락처가 없습니다.")
        else:
            for contact in self.customerstorage:
                print("-" * 30)
                contact.print_info()
                print("-" * 30)    

    def search_addr(self):
        name = input("검색할 이름을 입력하세요 : ")
        for contact in self.storage:
            if contact.get_name() == name:
                print("-" * 30)
                contact.print_info()
                print("-" * 30)
                return
        print("연락처를 찾을 수 없습니다.")
    
    def print_contacts(self):
        if not self.storage:
            print("-" * 30)    
            print("저장된 연락처가 없습니다.")
            print("-" * 30)    
        else:
            for contact in self.storage:
                print("-" * 30)    
                contact.showData()
                print("-" * 30)

