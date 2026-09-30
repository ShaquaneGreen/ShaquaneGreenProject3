from nicegui import ui

everything_to_draw = [

#This is putting a label above my drawing.
first_label = ui.Label("Shaquane's King Of The Court")
first_label.classes("text-pink-400")
first_label.style("font-size: 200%")

#This creates the interactive image where my picture will be drawn.
drawing_area = ui.interactive_image(size=(1000, 1000), cross=False, sanitize=True)

#This gives the background a color.
drawing_area.classes("w-lg bg-green-300")

backboard = '''<rect x="750" y="150" width="180" height="20" fill="white" stroke="black" stroke-width="5" />'''


