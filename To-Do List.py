#Функция создания задачи
def create_task(title, description):
    f = open(f'{title}.txt', 'w', encoding='utf-8')
    f.write(f'{description}')
    f.close()
#Вызов функции
create_task(title="Задача", description="Утренняя пробежка")

# def load_task(title):
