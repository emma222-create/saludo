import flet as ft

def calcular_imc(txtPeso,txtAltura, lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value) 
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es de: {imc:.2f}"
        page.update()
        
    #Funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
        
    #Validacion del IMC
        
        if imc<18.5:    
            dialog=ft.AlertDialog(
            title="Bajo de peso",
            content="Tu IMC indica que tienes bajo peso",
            actions=[
                ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
            ]
        )
            
        elif imc>=18.5 and imc<24.9:
                dialog=ft.AlertDialog( 
                    title="Peso normal",
                    content="Tu IMC indica que tienes un peso normal",
                    actions=[
                        ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
        elif imc>=25 and imc<30:
            dialog=ft.AlertDialog(
            title="Sobrepeso",
            content="Tu IMC indica que tienes SOBREPESO",
            actions=[
                ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
            ]
        )
        else:
            dialog=ft.AlertDialog(
                title="OBESIDAD",
                content="Tu IMC indica que tienes OBESIDAD, ACUDE A TU MEDICO LO MAS RAPIDO POSIBLE",
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
        def main(page: ft.Page):
            page.title = "Calculadora de IMC"
            page.bgcolor="purple"
    
        txtAltura=ft.TextField(label="Ingresa tu altura")
        lblIMCV=ft.Text("Tu IMC es de: ")
    
        img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
        def on_Calcular(e):
            calcular_imc(txtPeso,txtAltura,lblIMC,page)
            
        def limpiar():
            txtPeso.value=""    
            txtAltura.value=""
            lblIMC.value="Tu IMC es de:"
        btnCalcular=ft.ElevatedButton(text="Calcular",)
        btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
        page.add(
            ft.Column(
            controls=[
                txtPeso,txtAltura,lblIMCV
            ],alignment="CENTER"),
            ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
            ft.Row(
            controls=[
                btnCalcular,btnLimpiar
            ],alignment="CENTER")
    )
    
    ft.app(main)