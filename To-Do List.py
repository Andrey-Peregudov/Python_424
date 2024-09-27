#Функция создания задачи

class ToDo:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def create_task(self):
        f = open(f'{self.title}.txt', 'w', encoding='utf-8')
        f.write(f'{self.title} {self.description}')
        f.close()
    def load_task(self):
        d = {}
        with open(f'{self.title}.txt', 'r', encoding='utf-8') as file:
            fr = file.read().split("\n")
            for i in fr:
                key = i.split(" ")[0]
                value = i.split()[1:]
                d[key] = value
            return d

            # for line in file:
            #     key, *value = line.split()
            #     d[key] = value
#Вызов функции
create_task = ToDo(title="Задача", description="Утренняя пробежка")
create_task.create_task()
print(create_task.load_task())



