class Project:
    def __init__(self, title, manager_name):
        self.title = title
        self.manager_name = manager_name

    def __str__(self):
        return f"Title: {self.title}\nManager: {self.manager_name}"
