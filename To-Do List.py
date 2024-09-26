#Функция создания задачи
def create_task(title, description):
    f = open(f'{title}.txt', 'w')
    f.write(f'{description}')
    f.close()
#Вызов функции
create_task(title="Задача", description="Утренняя пробежка")

def