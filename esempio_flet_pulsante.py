import flet as ft

def main(page:ft.Page):
    my_text = ft.Text("Ciao", size=24, color="red")

    def button_handler():
        my_text.color="blue"
        my_text.update()

    my_button=ft.Button(content='Cambia colore', on_click=button_handler)

    page.controls.append(my_text)
    page.controls.append(my_button)

    page.update()

ft.run(main)