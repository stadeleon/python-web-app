FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Reading the file and
    Returning the list of todos
    """
    with open(filepath) as file:
        return file.readlines()


def write_todos(todos_list, filepath=FILEPATH):
    """Write todos list to assigned file
    :type todos_list: list
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)

print(__name__)
if __name__ == "__main__":
    print(get_todos())
