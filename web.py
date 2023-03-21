import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is subheader for the app")
st.write(
    "This app is to increase our <b>productivity</b> and python knowledge",
    unsafe_allow_html=True)

st.text_input(label="Enter a task here", placeholder="Enter a task here",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

