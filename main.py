from nicegui import ui

everything_to_draw = []

# This creates the interactive image where my picture will be drawn.
drawing_area = ui.interactive_image(size=(1000, 1000), cross=False, sanitize=True)

# This gives the background a color.
drawing_area.classes("w-lg bg-green-300")

#This is my backboard for the hoop.
backboard = '''<rect x="400" y="120" width="200" height="170"
fill="white" stroke="black" stroke-width="5" />'''
everything_to_draw.append(backboard)


# This rectangle is the pole holding up the backboard.
pole = '''<rect x="490" y="290" width="20" height="400"
fill="gray" stroke="black" stroke-width="5" />'''
everything_to_draw.append(pole)


# This is the rim of the basketball hoop.
rim = '''<ellipse cx="500" cy="290" rx="70" ry="18"
fill="orange" stroke="black" stroke-width="6" />'''
everything_to_draw.append(rim)


# These lines are making the net for the rim.
net1 = '''<line x1="435" y1="290" x2="450" y2="375"
stroke="red" stroke-width="5" />'''

net2 = '''<line x1="465" y1="290" x2="470" y2="375"
stroke="red" stroke-width="5" />'''

net3 = '''<line x1="500" y1="290" x2="500" y2="375"
stroke="red" stroke-width="5" />'''

net4 = '''<line x1="535" y1="290" x2="530" y2="375"
stroke="red" stroke-width="5" />'''

net5 = '''<line x1="565" y1="290" x2="550" y2="375"
stroke="red" stroke-width="5" />'''

everything_to_draw.append(net1)
everything_to_draw.append(net2)
everything_to_draw.append(net3)
everything_to_draw.append(net4)
everything_to_draw.append(net5)


# These horizontal lines connect the net together.
net_horizontal1 = '''<line x1="445" y1="315" x2="555" y2="315"
stroke="red" stroke-width="3" />'''

net_horizontal2 = '''<line x1="450" y1="340" x2="550" y2="340"
stroke="red" stroke-width="3" />'''

net_horizontal3 = '''<line x1="455" y1="365" x2="545" y2="365"
stroke="red" stroke-width="3" />'''

everything_to_draw.append(net_horizontal1)
everything_to_draw.append(net_horizontal2)
everything_to_draw.append(net_horizontal3)

# This is drawing a basketball using a circle.
basketball = '''<circle cx="350" cy="650" r="55"
fill="orange" stroke="black" stroke-width="6" />'''
everything_to_draw.append(basketball)


# This is putting a cross on the basketball.
basketball_line1 = '''<line x1="295" y1="650" x2="405" y2="650"
stroke="black" stroke-width="5" />'''

basketball_line2 = '''<line x1="350" y1="595" x2="350" y2="705"
stroke="black" stroke-width="5" />'''

everything_to_draw.append(basketball_line1)
everything_to_draw.append(basketball_line2)

# This is adding my name to the picture.
name = '''<text x="375" y="850"
font-size="40" fill="red">Shaquane Green</text>'''
everything_to_draw.append(name)


# This is joining all the shapes and lines together.
shapes_to_draw = "\n".join(everything_to_draw)


# This puts all the shapes on the interactive image.
drawing_area.set_content(shapes_to_draw)


ui.run()