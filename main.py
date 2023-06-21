from fastapi import FastAPI
from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure

@component
def Item(text, done=False):
  attrs = {"style": {"color": "green"}} if done else {}
  # return html.li({
  #   "class": 'item', # esta sería la forma de incrustar clases
  #   "style": {
  #     "color": "blue", #Estilos inline
  #   }
  # }, text)
  return html.li(attrs, text)


#Component with hooks
@component
def Item2(text, initial_done=False): #tal como react necesita que la función comience por mayuscula
  done, set_done = hooks.use_state(initial_done)
  print(f"done: {done}")

  attrs = {"style": {"color": "green"}} if done else {}

  def handle_click(event):
    set_done(not done)

  if done:
    return html.li(attrs, text)
  else:
    return html.li(
      html.span(attrs, text),
      html.button({"on_click": handle_click}, "Done!"),
    )

@component
def HelloWorld():
  return html._( # el undercore significa que es un fragment
    html.h1("Todo list"),
    html.ul(
      Item2("Learning reactpy"),
      Item2("Learning something new every day", initial_done=False),
      Item2("Final task with reactpy", initial_done=True),
    )
  )

app = FastAPI()
configure(app, HelloWorld)
