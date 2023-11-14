import reflex as rx
from Innoquine.state import AppState
from Innoquine.style import chat_style, image_upload_style
from typing import Dict

def chat_input_box():
    input_field = rx.text_area(
        value=AppState.input_txt, 
        style={
            **chat_style,
            "border":"1px solid black",
            "background-color":"white",
            "color":"black",
        }, 
        on_change=AppState.set_input_txt,
        is_required=True,
        placeholder="Type your message here."
    )

    send_button = rx.button(
        "Send", 
        on_click=AppState.send_message(AppState.input_txt),
        style={
            "border":"1px solid black",
            "background-color":"white",
            "color":"black",
        },
    )

    return rx.hstack(
        input_field, 
        send_button, 
        spacing="1em", 
        style=chat_style
    )

def format_message(msg: Dict[str, str]) -> str:
    return rx.text(f"{msg['user']}: {msg['text']}")

def chat_messages_display():
    return rx.cond(
        AppState.messages,
        chat_messages_display_helper(),
        rx.text("No messages yet.", style=chat_style)
    )

def chat_messages_display_helper():
    return rx.vstack(
        rx.foreach(AppState.messages, format_message),
        spacing="0.5em", style=chat_style
    )

color = "rgb(107,99,246)"

def image_upload_box():
    return rx.hstack(
        rx. vstack(
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Select File",
                        color=color,
                        bg="white",
                        border=f"1px solid {color}",
                    ),
                    rx.text(
                        "Drag and drop files here or click to select files"
                    ),
                ),
                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"]
                },
                border=f"1px dotted {color}",
                padding="5em",
                
            ),
            rx.hstack(rx.foreach(rx.selected_files, rx.text)),
            rx.button(
                "Upload",
                on_click=lambda: AppState.handle_upload_and_message(
                    rx.upload_files()
                ),
            ),
            
            padding="5em",
        ),
        rx.foreach(
            AppState.img, lambda img: rx.image(src=img)
        ),
    )

def uploaded_image_display():
    return rx.cond(
        AppState.img,
        rx.foreach(
            AppState.img, lambda img: rx.image(src=img)
        ),
        rx.text("No image uploaded.", style=image_upload_style)
    )

def index()-> rx.Component:
    return rx.vstack(
        image_upload_box(),
        chat_messages_display(),
        chat_input_box(),
        spacing="2em"
    )


app = rx.App()
app.add_page(index)
app.compile()