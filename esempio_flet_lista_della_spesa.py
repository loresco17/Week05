import flet as ft

def main(page:ft.Page):

    my_text_field=ft.TextField(label="Aggiungi un elemento: ")

    def aggiungi_handler():
        page.controls.append(ft.Checkbox(str(my_text_field.value)))
        page.update()

    my_button_add=ft.CupertinoButton(content='Aggiungi', on_click=aggiungi_handler)

    row1=ft.Row([my_text_field, my_button_add], alignment=ft.MainAxisAlignment.CENTER)

    page.controls.append(row1)
    page.update()

ft.run(main)