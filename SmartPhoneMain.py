from SmartPhone import *

class SmartPhoneMain(SmartPhone):
    def __init__(self):
        self.smartphone = SmartPhone()

    def start(self):
        while True:
            self.smartphone.print_contacts()
            print(
            """
            1. 연락처 추가
            2. 연락처 목록(회사)
            3. 연락처 목록(거래처)
            4. 모든 연락처 출력
            5. 연락처 검색
            6. 연락처 삭제
            7. 연락처 수정
            8. 프로그램 종료
            """)

            choice = input("원하는 작업을 선택하세요 (1~8): ")

            if choice == "1":
                self.smartphone.set_adden() 
            elif choice == "2":
                self.smartphone.company_addr()                
            elif choice == "3":
                self.smartphone.customer_addr()
            elif choice == "4":
                self.smartphone.see_addr()
            elif choice == "5":
                self.smartphone.search_addr()
            elif choice == "6":
                self.smartphone.delete_addr()
            elif choice == "7":
                self.smartphone.modify_contact()
            elif choice == "8":
                print("작업을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    SmartPhoneMain().start()
#     smartphone_Main = SmartPhoneMain()
#     smartphone_Main.start()


