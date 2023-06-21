from fastapi import FastAPI
from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure

@component
def Counter():
  counter, set_counter = hooks.use_state(10)

  def handle_click_plus(event):
    set_counter(counter + 1)

  def handle_click_minus(event):
    set_counter(counter - 1)

  return html._(
    html.h2(f"Counter: {counter}"),
    html.div(
      html.button({"on_click": handle_click_plus, "class_name": "btn btn-primary mx-3"}, "Added +"),
      html.button({"on_click": handle_click_minus, "class_name": "btn btn-success"}, "Sustracted -"),
    )
  )


@component
def AppMain():
  return html._(
    html.link(
      {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        "rel": "stylesheet",
        "crossorigin": "anonymous",
        "integrity": "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
      }
    ),
    html.h1('Hello Victor to Reactpy'),
    html.div(
      Counter()
    )
  )

app = FastAPI()
configure(app, AppMain)
