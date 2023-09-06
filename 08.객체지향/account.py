"""
class Account (계좌)를 만드세요.

1. 속성값: 
	- 계좌번호(ano), 소유주(owner), 잔액(balance)
	- 단, 잔액은 0원 이상이고 10,000,000원 이하이어야 한다.

2. deposit method
	- amount를 매개변수로 받아 balance에 더해준다.
	- 잔액은 10000000원을 초과할 수 없다.

3. withdraw method
	- amount 만큼의 금액을 balance에서 차감한다.
	- 잔액은 마이너스 금액이 될 수 없다.

4. __str__ method
	- 계좌번호: OOO, 소유주: OOO, 잔액: 10자리의 천단위 구분기호가 있는 정수
"""
class Account:
    def __init__(self, ano, owner, balance):
        self.ano = ano
        self.owner = owner
        self.__balance = 0
        if 0 <= balance <= 10000000:
        	self.__balance = balance
              
    def deposit(self, amount):
        if self.__balance + amount > 10000000:
            print('일천만원이 초과할 수 없습니다.')
            return
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance < amount:
            print('잔액이 부족합니다.')
            return
        self.__balance -= amount

    def __str__(self):
        return f'계좌번호: {self.ano}, 소유주: {self.owner}, 잔액: {self.__balance:10,d}'
    
if __name__ == '__main__':
    acc = Account('230906', '제임스', 100000)
    print(acc)
    acc.deposit(200000)
    print(acc)
    acc.withdraw(400000)
    acc.withdraw(250000)
    print(acc)
    