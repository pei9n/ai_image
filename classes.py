class TaskStatus: # статус выполнения задачи
    Pending = 'pending'
    Processing = 'processing'
    Completed = 'completed'
    Failed = 'failed'
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
    def added(self, amount): #метод для добавления монет
        print(f'монет сейчас до прибавления: {self.balance}')
        self.balance = self.balance + amount
        print(f'добавлено {amount} монет')
        print(f'общая сумма {self.balance}')
    def use(self, amount2): #метод для использования вычитания монет
        print(f'монет до вычитания: {self.balance}')
        if self.balance < amount2:
            print(f'недостаточно баланса :(, сейчас монет:{self.balance}, нужно не меньше: {amount2}')
        else:
            self.balance = self.balance - amount2
            print(f'все успешно! сейчас ваш баланс: {self.balance}!')

class ML_model: # ML_модель
    def __init__(self, id_model, description, cost_predict):
        # идентификатор модели, описание модели, стоимость одного предсказания
        self.id_model = id_model
        self.description = description
        self.cost_predict = cost_predict
    def predict(self, image_data): # метод выполнения предсказания 
        return {'digit': digit, 'confidence': confidence}

class ML_task: # МL-задача
    def __init__(self, data, ref_us, ref_ml):
        # входные данные, статус выполнения, ссылка на пользователя, ссылка на ML-модель
        self.data = data
        self.ref_us = ref_us
        self.ref_ml = ref_ml
    def run(self, ):
        if self.balance < self.cost_predict:
            print('недостаточный баланса для выполнения предсказания').Failed
        


chel = User(123, "qwe123!", "qwerty123", "defolt", 10)
chel = ML_task(1, 2, 3)

chel.run()