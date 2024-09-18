class User:
    def __init__(self, user_id, name, permission='user'):
        self._user_id = user_id
        self._name = name
        self._permission = permission

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_permission(self):
        return self._permission

    def set_permission(self, new_permission):
        if new_permission in ['user', 'admin']:
            self._permission = new_permission
        else:
            raise ValueError("Неверный уровень доступа")

    def __str__(self):
        return f"User(id={self._user_id}, имя={self._name}, доступ={self._permission})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, permission='admin')
        self._users = []

    def add_user(self, user_id, name, permission='user'):
        new_user = User(user_id, name, permission)
        self._users.append(new_user)
        print(f"Пользователь {new_user} добавлен.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь {user} удалён.")
                break
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self):
        for user in self._users:
            print(user)


admin1 = Admin(1, "Буцефал")
admin1.add_user(1, "Буцефал", "admin")
admin1.add_user(2, "Кеша", "user")
admin1.add_user(3, "Василь", "user")
admin1.remove_user(3)
admin1.list_users()

