import streamlit as st
import functions

todos = functions.get_todo()

# session_state is similar to a dict
# key in text_input becomes the key of the dict
# user input becomes the value of the dict
def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todo(todos)

# st.checkbox()

st.title('My To-Do App')
st.write('Create and organise your to-do items')

# Add a new key which can identify each to-do item
# in the session_state dict
# Add index to identify items to be deleted from the list
for index, todo in enumerate(todos):
    # checkbox contains True/False value
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        # Also delete the item from the FE
        del st.session_state[todo]
        st.rerun()

st.text_input(label='label', placeholder='Add new to-do'
            , on_change=add_todo, key='new_todo')

# st.session_state