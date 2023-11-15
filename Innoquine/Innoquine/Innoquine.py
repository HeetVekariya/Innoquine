import reflex as rx
from Innoquine.state import AppState
import Innoquine.style as style
from typing import Dict

# Image section
def image_upload_box() -> rx.Component:
    return rx.container(
        rx.container(
            rx.cond(
                AppState.img,
                rx.container(
                    rx.foreach(
                        AppState.img, lambda img: rx.image(src=img)
                    ),
                    style=style.image
                ),
                rx.text("No image uploaded."),
                
            ),
            style={
                "border":f"1px dashed {style.color}",
                "padding":"10px",
            }
        ),
        rx.container(
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Select File",
                        color=style.color,
                        bg="white",
                        border=f"1px solid {style.color}",
                    ),
                    rx.text(
                        "Drag and drop files here or click to select files"
                    ),
                ),
                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"]
                },
                border=f"1px dotted {style.color}",
                padding="2em",
                style=style.upload_section,
            ),
            rx.hstack(
                rx.container(
                    rx.foreach(
                        rx.selected_files, 
                        rx.text,
                    ),
                    style={
                        "text-align": "center",
                    }
                ),
                
            ),
            rx.button(
                "Upload",
                on_click=lambda: AppState.handle_upload_and_message(
                    rx.upload_files()
                ),
                style={
                    "border":"1px solid white",
                }
            ),  
            style=style.upload_container
        ),
        style={
            "text-align": "center",
        }
    )

def image_section() -> rx.Component:
    return rx.vstack(
        image_upload_box(),
        style=style.image_section
    )


# Chat section
def format_message(msg: Dict[str, str]) -> str:
    return rx.text(
        f"{msg['user']}: {msg['text']}"
    )

def chat_messages_display_helper():
    return rx.vstack(
        rx.foreach(AppState.messages, format_message),
        spacing="0.5em",
    )

def chat_messages_display():
    return rx.container(
        chat_messages_display_helper(),
        style=style.chat_message_display
    )

def chat_input_box():
    input_field = rx.text_area(
        value=AppState.input_txt, 
        style=style.chat_input_field, 
        on_change=AppState.set_input_txt,
        is_required=True,
        placeholder="Type your message here."
    )

    send_button = rx.button(
        "Send", 
        on_click=AppState.send_message(AppState.input_txt),
        style=style.send_button,
    )

    return rx.hstack(
        input_field, 
        send_button, 
        spacing="1em",
        style=style.chat_input_box
    )


def chat_section() -> rx.Component:
    return rx.vstack(
        chat_messages_display(),
        chat_input_box(),
        spacing="2em",
        style={
            "width": "65%",
            "height": "100%",
        }
    )


# Index page
@rx.page(route="/", on_load=AppState.on_load)
def index()-> rx.Component:
    return rx.container( 
        rx.text(
            "InnoQuine", 
            style=style.index_text
        ),
        rx.hstack(  
            image_section(),
            chat_section(),
        ),
        style=style.index
    )


app = rx.App()
app.add_page(index)
app.compile()