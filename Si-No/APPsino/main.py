import flet as ft


def main(page: ft.Page):
    page.title = "¿Me perdonas?"
    page.bgcolor="green"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="bold"))
    img1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="purple",
                            width=100,
                            height=50
                            ) 
    
    btnNo=ft.ElevatedButton("No",
                            color="blue",
                            width=100,
                            height=50
                            )
    page.add(
        ft.column(
            [
                lbl1,
                img1,
                ft.Row(
                    [btnSi,btnNo]
                ) 
            ]
        )
    )
ft.app(main)
