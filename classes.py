from datetime import datetime


class TaskStatus: # статус выполнения задачи
    Pending = 'pending'
    Processing = 'processing'
    Completed = 'completed'
    Failed = 'failed'
class TransactionType:
    Deposit = "deposit"        
    Charge = "charge"  
class User:
    # Пользователь
    def __init__(self, id, login, password, role, balance = 0.0):
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
    def deposit(self, amount): #метод для добавления монет
        print(f'монет сейчас до прибавления: {self.balance}')
        self.balance = self.balance + amount
        print(f'добавлено {amount} монет')
        print(f'общая сумма {self.balance}')
        transaction = Transaction(type_of_tran=TransactionType.Deposit, summa=amount, date_time=datetime.now(), user_id=self)
        self.transactions.append(transaction)
        return transaction

    def charge(self, amount2): #метод для использования вычитания монет
        print(f'монет до вычитания: {self.balance}')
        if self.balance < amount2:
            print(f'недостаточно баланса :(, сейчас монет:{self.balance}, нужно не меньше: {amount2}')
        else:
            self.balance = self.balance - amount2
            print(f'все успешно! сейчас ваш баланс: {self.balance}!')
        transaction = Transaction(type_of_tran=TransactionType.Charge, summa=amount2, date_time=datetime.now(), user_id=self)
        self.transactions.append(transaction)
        return transaction

class ML_model: # ML_модель
    def __init__(self, id_model, description, cost_predict):
        # идентификатор модели, описание модели, стоимость одного предсказания
        self.id_model = id_model
        self.description = description
        self.cost_predict = cost_predict
    def predict(self, image_data): # метод выполнения предсказания 
        return {'digit': digit, 'confidence': confidence}

class ML_task: # МL-задача
    def __init__(self, data, status, ref_us, ref_ml):
        # входные данные, статус выполнения, ссылка на пользователя, ссылка на ML-модель
        self.data = data
        self.status = TaskStatus.Pending
        self.ref_us = ref_us
        self.ref_ml = ref_ml
        self.result = None
    def run(self, model):
        if self.ref_us.balance < self.ref_ml.cost_predict:
            print('недостаточный баланса для выполнения предсказания')
            self.status = TaskStatus.Failed
        elif self.balance > self.cost_predict:
            self.status = TaskStatus.Processing
            self.result = model.predict(self.data)
            self.status = TaskStatus.Completed
            self.balance = self.balance - self.cost_predict
        else:
            self.status = TaskStatus.Failed

class Transaction:
    def __init__(self, type_of_tran, summa, date_time, user_id):
        self.type_of_tran = type_of_tran
        self.summa = summa
        self.date_time = date_time
        self.user_id = user_id
        


