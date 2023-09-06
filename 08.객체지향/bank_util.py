import datetime as dt
from account import Account

# 입력: 이름, 금액, 통장번호: 현재 시분초 6자리
# Account를 생성하여 acc_list에 append
def create_account(acc_list):
    while True:
        try:
            cmd = input('이름 금액> ').split()
            name, amount = cmd[0], int(cmd[1])
        except:
            print('입력이 잘못되었습니다.\n')
            continue
        if amount < 0 or amount > 10000000:
            print('금액이 잘못되었습니다.\n')
            continue
        break
    now = dt.datetime.now()
    ano = now.strftime('%H%M%S')
    account = Account(ano, name, amount)
    acc_list.append(account)

# 입력: 계좌번호, 금액
# 계좌에 금액을 추가, 단 한도를 초과할 수 없음
def deposit(acc_list):
    while True:
        try:
            cmd = input('계좌번호 금액> ').split()
            ano, amount = cmd[0], int(cmd[1])
        except:
            print('입력이 잘못되었습니다.\n')
            continue
        if amount < 0:
            print('금액이 잘못되었습니다.\n')
            continue
        break
    for acc in acc_list:
        if acc.ano == ano:
            acc.deposit(amount)
            return

# 입력: 계좌번호, 금액
# 계좌에서 금액을 차감, 단 마이너스가 될 수 없음
def withdraw(acc_list):
    while True:
        try:
            cmd = input('계좌번호 금액> ').split()
            ano, amount = cmd[0], int(cmd[1])
        except:
            print('입력이 잘못되었습니다.\n')
            continue
        if amount < 0:
            print('금액이 잘못되었습니다.\n')
            continue
        break
    for acc in acc_list:
        if acc.ano == ano:
            acc.withdraw(amount)
            return
