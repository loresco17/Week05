import asyncio
import flet as ft

async def main(page:ft.Page):
    my_text=ft.Text("Il mio testo", size=24, color='Purple', bgcolor='Green')
    page.controls.append(my_text)
    for i in range(1,100):
        my_text.value= str(i)
        await asyncio.sleep(1)
        my_text.update()
    page.update()

ft.run(main)