from datetime import datetime


class TaskStatus: # статус выполнения задачи
    Pending = 'pending'
    Processing = 'processing'
    Completed = 'completed'
    Failed = 'failed'


class TransactionType:
    Deposit = "deposit"        
    Charge = "charge"


class User: # Пользователь
    def __init__(self, id: int, login: str, password: str, role: str, balance = 0.0): 
        # id - идентификатор пользователя
        # login, password - данные для авторизации
        # role - роль пользователя 
        # balance - баланс
        self.id = id
        self.login = login
        self.password = password
        self.role = role
        self.balance = balance
        self.transactions = []


class Wallet:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.transactions = []

    def deposit(self, amount: int, user_id: int) -> bool: #метод для добавления монет
        print(f'монет сейчас до прибавления: {self.__balance}')
        self.__balance = self.__balance + amount
        print(f'добавлено {amount} монет')
        print(f'общая сумма {self.__balance}')
        transaction = Transaction(type_of_tran=TransactionType.Deposit, summa=amount, date_time=datetime.now(), user_id=user_id)
        self.transactions.append(transaction)
        return transaction

    def charge(self, amount2: int, user_id: int) -> bool: #метод для использования вычитания монет
        print(f'монет до вычитания: {self.__balance}')
        if self.__balance < amount2:
            print(f'недостаточно баланса :(, сейчас монет:{self.__balance}, нужно не меньше: {amount2}')
            return False
        else:
            self.__balance = self.__balance - amount2
            print(f'все успешно! сейчас ваш баланс: {self.__balance}!')
        transaction = Transaction(type_of_tran=TransactionType.Charge, summa=amount2, date_time=datetime.now(), user_id=user_id)
        self.transactions.append(transaction)
        return transaction


class ML_model: # ML_модель
    def __init__(self, id_model: int, description: str, cost_predict: float):
        # идентификатор модели, описание модели, стоимость одного предсказания
        self.id_model = id_model
        self.description = description
        self.cost_predict = cost_predict
    def predict(self, image_data): # метод выполнения предсказания 
        return {'digit': 0.5, 'confidence': 0.8} # возвращает словарь с предсказанным числом и уверенностью


class ML_task: # МL-задача      
    def __init__(self, data, status: str, user: User, model: ML_model):
        # входные данные, статус выполнения, ссылка на пользователя, ссылка на ML-модель
        self.data = data
        self.status = TaskStatus.Pending
        self.user = user
        self.model = model
        self.result = None

    def run(self):
        if self.user._Wallet__balance < self.model.cost_predict:
            print('недостаточный баланса для выполнения предсказания')
            self.status = TaskStatus.Failed
        elif self.user._Wallet__balance > self.model.cost_predict:
            self.status = TaskStatus.Processing
            self.result = self.model.predict(self.data)
            self.status = TaskStatus.Completed
            self.user._Wallet__balance = self.user._Wallet__balance - self.model.cost_predict
        else:
            self.status = TaskStatus.Failed


class Transaction:
    def __init__(self, type_of_tran: str, summa: int, date_time: datetime, user_id: int):
        self.type_of_tran = type_of_tran
        self.summa = summa
        self.date_time = date_time
        self.user_id = user_id