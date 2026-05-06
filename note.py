import streamlit as st

def onClickButton():
  addToTodo()

def onClickUpdate(index):
  updateTODO(index)

def onClickDelete(index):
  del st.session_state["database"][index]

@st.dialog(
    title="Update TODO",
    icon=":material/edit:"
)
def updateTODO(index):
  name = st.text_input(
    label="Update TODO",
    placeholder="Enter updated name",
    value=st.session_state["database"][index]["name"]
  )
  goal = st.text_area(
    label="Enter your updated goal",
    placeholder="Enter your updated text",
    max_chars=200,
    value=st.session_state["database"][index]["goal"]
  )
  if st.button(label="Submit", type="primary"):
    st.session_state["database"][index] = {
      "name": name,
      "goal": goal
    }
    st.rerun()

@st.dialog(
  title="Add new TODO",
  icon=":material/thumb_up:"
)
def addToTodo():
  name = st.text_input(
    label="Enter TODO name",
    placeholder="Enter name"
  )
  goal = st.text_area(
    label="Enter your goal",
    placeholder="Enter your text",
    max_chars=200
  )
  if st.button(label="Submit", type="primary"):
    st.session_state["todo_name"] += 1
    st.session_state["database"][f"name{st.session_state["todo_name"]}"] = {
      "name": name,
      "number": st.session_state["todo_name"],
      "goal": goal
    }
    st.rerun()

st.write(f"##### Add new todo")

if "database" not in st.session_state: 
  st.session_state["database"]=dict()
  st.session_state["todo_name"] = 0


button_pressed = st.button(
  label="Add",
  key="add",
  type="primary",
  on_click=onClickButton
)

# latest_key = f"name{st.session_state["todo_name"]}"
# st.write(latest_key)

if len(st.session_state["database"])>0:
  for key, value in st.session_state["database"].items():
    with st.container(border=True, key=f"{key}"):
      st.write(f"TODO name: {value['name']}")
      st.write(f"TODO goal: {value['goal']}")
      index = key
      button_edit = st.button(
        label="Edit",
        key=f"edit{key}",
        on_click=onClickUpdate,
        args=[index]
      )
      button_delete = st.button(
        label="Delete",
        key=f"delete{key}",
        on_click=onClickDelete,
        args=[index]
      )
else:
  st.write("TODO is not written yet")