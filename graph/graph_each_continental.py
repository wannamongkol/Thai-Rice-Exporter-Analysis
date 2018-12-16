# -*- coding: utf-8 -*-
import pygal
import csv
from itertools import groupby


def main():
    file = open('../data/2560.csv', 'r', encoding='utf-8')
    data = csv.reader(file)
    table = [row for row in data]
    year = 2560
    asia = [year, 0, 0, 0]
    europe = [year, 0, 0, 0]
    africa = [year, 0, 0, 0]
    northamerica = [year, 0, 0, 0]    
    centeralamerica = [year, 0, 0, 0]
    southamerica = [year, 0, 0, 0]
    australiaandoceania = [year, 0, 0, 0]
    for key, group in groupby(table, lambda x: x[3]):
        for item in group:
            if key == "Asia":
                asia[1] = key
                asia[3] += float(item[5])
                asia[2] += float(item[4])
            elif key == "Europe":
                europe[1] = key
                europe[3] += float(item[5])
                europe[2] += float(item[4])
            elif key == "Africa":
                africa[1] = key
                africa[3] += float(item[5])
                africa[2] += float(item[4])
            elif key == "NorthAmerica":
                northamerica[1] = key
                northamerica[3] += float(item[5])
                northamerica[2] += float(item[4])            
            elif key == "CenteralAmerica":
                centeralamerica[1] = key
                centeralamerica[3] += float(item[5])
                centeralamerica[2] += float(item[4])
            elif key == "SouthAmerica":
                southamerica[1] = key
                southamerica[3] += float(item[5])
                southamerica[2] += float(item[4])
            elif key == "AustraliaandOceania":
                australiaandoceania[1] = key
                australiaandoceania[3] += float(item[5])
                australiaandoceania[2] += float(item[4])
    bar_chart = pygal.Bar(legend_at_bottom=True)
    bar_chart.title = ('ยอดปริมาตรส่งออกข้าวแต่ละทวีปปี%i (หนึ่งต่อสิบล้านกิโลกรัม)' %year)
    bar_chart.add(asia[1], asia[2]/10000000)
    bar_chart.add(europe[1], europe[2]/10000000)
    bar_chart.add(africa[1], africa[2]/10000000)
    bar_chart.add(northamerica[1], northamerica[2]/10000000)
    bar_chart.add(centeralamerica[1], centeralamerica[2]/10000000)
    bar_chart.add(southamerica[1], southamerica[2]/10000000)
    bar_chart.add(australiaandoceania[1], australiaandoceania[2]/10000000)
    bar_chart.render_to_file('graph-continental-amount%i.svg' %year)

    bar_chart = pygal.Bar(legend_at_bottom=True)
    bar_chart.title = ('ยอดขายข้าวปี%iในแต่ละทวีป (หนึ่งต่อพันล้านบาท)' %year)
    bar_chart.add(asia[1], asia[3]/1000000000)
    bar_chart.add(europe[1], europe[3]/1000000000)
    bar_chart.add(africa[1], africa[3]/1000000000)
    bar_chart.add(northamerica[1], northamerica[3]/1000000000)
    bar_chart.add(centeralamerica[1], centeralamerica[3]/1000000000)
    bar_chart.add(southamerica[1], southamerica[3]/1000000000)
    bar_chart.add(australiaandoceania[1], australiaandoceania[3]/1000000000)
    bar_chart.render_to_file('graph-continental-circulation%i.svg' %year)
main()
