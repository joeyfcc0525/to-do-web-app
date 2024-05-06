# To assign a default argument / paramter into here
# In this case 'todo.txt' we can avoid repeating this when calling this function
# first line is the doc-strings of this function; can be called by print(help(get_todo))
FILEPATH = 'todo.txt'


def get_todo(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file:
        todo = file.readlines()
    return todo

# This function doesn't need to return a value
# because it serves like a proc to update a file
# default argument needs to be put at the end 
def write_todo(todo_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
