from nicegui import ui

first_label = ui.label("Hello Comp151")
first_label.classes("text-pink-400")
first_label.style("font-size: 200%")
drawing_area = ui.interactive_image(size=(1000, 1000), cross = False, sanitize= True)
drawing_area.classes("w-lg bg-green-300")
drawing_area.set_content('''<circle cx="500" cy= "500" r= "75" fill="orange" /> ''')



ui.run()