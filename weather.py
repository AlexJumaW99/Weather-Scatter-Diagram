#necessary imports 
from bokeh.plotting import figure 
from bokeh.io import output_file,show 
import pandas 

#we read the excel file using pandas
df = pandas.read_excel('verlegenhuken.xlsx')

#we create the figure object
f = figure()

#we style the figure object (and therefore the scatter plot/diagram)
f.title.text="WEATHER DATA: Temp against Pressure"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPA)"

#we divide by 10 bc they both have a scale factor of 10
#this thus ensures accurate visualization and plotting 
x = df['Temperature']/10
y = df['Pressure']/10

output_file('Weather.html')

#we create a scatter plot, with small circles
f.circle(x,y, size = 0.5)

show(f)