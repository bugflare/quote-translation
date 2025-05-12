import flet as ft

def main(page):
    # Basic page setup
    page.title = "Quote Translator"
    page.bgcolor = "#f0f0f0"
    page.padding = 20
    
    # Our quotes in different languages
    english_quote = "Just do it. - Nike"
    spanish_quote = "Simplemente hazlo. - Nike"
    french_quote = "Fais-le simplement. - Nike"
    
    # The text that will show the quote
    quote_display = ft.Text(english_quote, size=20, color="black")
    
    # The picture (same for all languages)
    quote_pic = ft.Image(
        "https://1000logos.net/wp-content/uploads/2021/11/Nike-Logo.png",
        width=200,
        height=100
    )
    
    # What happens when you pick a language
    def change_language(e):
        if e.control.value == "english":
            quote_display.value = english_quote
        elif e.control.value == "spanish":
            quote_display.value = spanish_quote
        elif e.control.value == "french":
            quote_display.value = french_quote
        page.update()
    
    # The language selector buttons
    language_buttons = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="english", label="English"),
            ft.Radio(value="spanish", label="Spanish"),
            ft.Radio(value="french", label="French")
        ]),
        on_change=change_language,
        value="english"
    )
    
    # Put everything on the page
    page.add(
        ft.Column([
            quote_pic,
            ft.Divider(height=20, color="transparent"),
            quote_display,
            ft.Divider(height=20, color="transparent"),
            ft.Text("Select language:"),
            language_buttons
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)