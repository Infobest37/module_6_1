import threading


class BankAccount:
    # Метот конструкор котррый вызывается при создании объекта класса
    # устанавливает имя вдадельца счета (account_holder) и начальный баланс balance который с начало равен 0
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder # Имя владельца счета
        self._balance = balance # Приватный атребут для хранения баланса (не доступны на прямую)
        # self.balance_lock = threading.Lock()
        # self.balance_lock.acquire()
        # self.balance_lock.release()
        # self.balance_lock = threading.Lock()

    def deposit(self, amount):
        # self.balance_lock.acquire()
        self._balance += amount # Увеличели баланс на переданную сумму
        print(f" Остаток на счете {self._balance}")


    def withdraw(self, amount):
        if amount <= self._balance: # Проверяем хватает ли средст на счете
            self._balance -= amount # Если средств не хватает уменьшаем баланс
            print(f'Остаток на счете: {self._balance}')
        else:
            print("Недостатчно средст на счете")

    def display_balance(self):
        print(f" Баланс: {self._balance} руб")

# Пример использования:
# Создаем банковский счет для "Ивана Иванова" с балансом по умолчанию (0)
account = BankAccount("Иван Иванов")
# Пополняем счет на 1000 рублей
account.deposit(1000)
# Снимаем 500 рублей со счета
account.withdraw(500)
# Отображаем текущий баланс на экране
account.display_balance()
account.withdraw(400)
account.deposit(10000)
account.withdraw(400)
account.display_balance()
