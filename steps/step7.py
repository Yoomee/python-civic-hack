from xml.dom import minidom
from flask import Flask, request, render_template
import pygal

app = Flask(__name__)
@app.route('/')
def home():
    xmldoc = minidom.parse("FHRS706en-GB.xml")
    list = xmldoc.getElementsByTagName("EstablishmentDetail")
    rating_0 = 0
    rating_1 = 0
    rating_2 = 0
    rating_3 = 0
    rating_4 = 0
    rating_5 = 0

    for n in list:
        type = n.getElementsByTagName("BusinessType")[0].firstChild.data
        if type == "Restaurant/Cafe/Canteen" and n.getElementsByTagName("RatingDate")[0].firstChild:
            rating = n.getElementsByTagName("RatingValue")[0].firstChild.data

            if rating == "0":
                 rating_0 += 1
            if rating == "1":
                rating_1 += 1
            if rating == "2":
                rating_2 += 1
            if rating == "3":
                rating_3 += 1
            if rating == "4":
                rating_4 += 1
            if rating == "5":
                rating_5 += 1

    pie_chart = pygal.Pie()
    pie_chart.title = 'Restaurants and cafes in Durham'
    pie_chart.add('Rating 0', rating_0)
    pie_chart.add('Rating 1', rating_1)
    pie_chart.add('Rating 2', rating_2)
    pie_chart.add('Rating 3', rating_3)
    pie_chart.add('Rating 4', rating_4)
    pie_chart.add('Rating 5', rating_5)

    chart = pie_chart.render_data_uri()
    return render_template( 'home.html', rating_chart = chart)
