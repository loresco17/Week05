import flet as ft

def main(page:ft.Page):
    page.window.width=420
    page.window.height=300
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    def handler_minus(e):
        v=int(my_text.value)
        v=v-1
        my_text.value=str(v)
        my_text.update()

    def handler_plus():
        v=int(my_text.value)
        v=v+1
        my_text.value=str(v)
        my_text.update()

    my_btn_minus=ft.IconButton(icon=ft.Icons.REMOVE, icon_size=50, on_click=handler_minus)
    my_btn_plus=ft.IconButton(icon=ft.Icons.ADD, icon_size=50, on_click=handler_plus)
    my_text=ft.TextField(value='0',
                         width=100,
                         disabled=True,
                         text_size=50,
                         text_align=ft.TextAlign.CENTER)

    my_row=ft.Row([my_btn_minus, my_text, my_btn_plus], alignment=ft.MainAxisAlignment.CENTER)

    page.controls.append(my_row)
    page.update()

ft.run(main)