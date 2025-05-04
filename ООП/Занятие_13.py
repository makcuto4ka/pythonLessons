# 1
import json
class UserProfile:
    def __init__(self, name , age, interest):
        self.name = name
        self.age = age
        self.interest = interest
        
    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'interest': self.interest}
    
    def from_dict(d):
        return UserProfile(d['name'], d['age'], d['interest'])
    
    @staticmethod
    def save_UserProfiles(UserProfiles, filename="profile.json"):
        with open(filename, "w") as f:
            json.dump([Us.to_dict() for Us in UserProfiles], f)
    @staticmethod
    def load_UserProfiles(filename="profile.json"):
        with open(filename) as f:
            return [UserProfile.from_dict(d) for d in json.load(f)]
    
    def __str__(self):
        return f"{self.name}: {self.age}"
UserProfiles = [UserProfile("Ann",35, [4, 5])]
UserProfile.save_UserProfiles(UserProfiles)
Us = UserProfile.load_UserProfiles()

print(Us[0])

# 2

import pickle

class Task:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed



def load_tasks():
    try:
        with open('tasks.pickle', 'rb') as f:
            try:
                return pickle.load(f)
            except EOFError:
                return []
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.pickle', 'wb') as f:
        pickle.dump(tasks, f)

def add_task(tasks, name, priority):
    tasks.append(Task(name, priority))
    save_tasks(tasks)

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)

def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        save_tasks(tasks)

def print_tasks(tasks):

    for i, task in enumerate(tasks):
        status = "+" if task.completed else "-"
        print(f"{i}. [{status}] {task.name} (Приоритет: {task.priority})")


tasks = load_tasks()

add_task(tasks, "Помыть посуду", 1)
add_task(tasks, "Сделать уроки", 3)
add_task(tasks, "Купить продукты", 2)

mark_completed(tasks, 0)

remove_task(tasks, 1)


print_tasks(tasks)


# 4
import json
import os

def load_users():

    loaded = 0
    skipped = 0
    valid_users = []


    if not os.path.exists('users.json'):
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2)

    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            content = f.read()

            users_data = json.loads(content) if content.strip() else []
            
    except json.JSONDecodeError as e:
        print(f"Ошибка формата JSON: {e}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


    for user in users_data:
        errors = []
        

        required_fields = ['id', 'name', 'email']
        for field in required_fields:
            if field not in user:
                errors.append(f'отсутствует поле "{field}"')
        

        if not errors:
            if not isinstance(user['id'], int):
                errors.append('поле "id" должно быть целым числом')
            if not isinstance(user['name'], str):
                errors.append('поле "name" должно быть строкой')
            if not isinstance(user['email'], str):
                errors.append('поле "email" должно быть строкой')
            elif '@' not in user['email']:
                errors.append('email должен содержать @')
        
        if errors:
            print(f'Пропущен пользователь {user}:')
            print(''.join(errors))
            skipped += 1
            continue
        
        valid_users.append(user)
        loaded += 1

    print(f"\nРезультат загрузки:")
    print(f"Успешно загружено: {loaded}")
    print(f"Пропущено: {skipped}")
    return valid_users

if __name__ == "__main__":
    # Первый запуск создаст файл users.json
    users = load_users()
    
    print("\nЗагруженные пользователи:")
    if not users:
        print("Нет данных для отображения")
    for user in users:
        print(f"- {user['name']} (ID: {user['id']}, Email: {user['email']})")