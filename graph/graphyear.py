# -*- coding: utf-8 -*-
import pygal
import csv

def main():
    years = range(2014, 2017+1)
    year2557 = []
    year2558 = []
    year2559 = []
    year2560 = []
    for year in years:
        totalvalue =  0
        totalquantity = 0
        path = '../data/%d.csv' % year
        file = open(path, 'r', encoding='utf-8')
        data = csv.reader(file)
        table = [row for row in data]
        for i in table:
            totalvalue += float(i[5])
            totalquantity += float(i[4])
        if int(table[1][0]) == 2014:
            year2557.append(totalvalue)
            year2557.append(totalquantity)
        elif int(table[1][0]) == 2015:
            year2558.append(totalvalue)
            year2558.append(totalquantity)
        elif int(table[1][0]) == 2016:
            year2559.append(totalvalue)
            year2559.append(totalquantity)
        elif int(table[1][0]) == 2017:
            year2560.append(totalvalue)
            year2560.append(totalquantity)
    line_chart = pygal.Line()
    line_chart.title = 'ยอดขายในแต่ละปี (หนึ่งต่อพันล้านบาท)'
    line_chart.x_labels = map(str, range(2557, 2561))
    line_chart.add('ยอดขาย(พันล้าน)', [ year2557[0]/1000000000, year2558[0]/1000000000, year2559[0]/1000000000, year2560[0]/1000000000] )
    line_chart.render_to_file('graph-allyear-circulation.svg' )

    line_chart = pygal.Line()
    line_chart.title = 'ปริมาตรส่งออกในแต่ละปี (หนึ่งต่อร้อยล้านกิโลกรัม)'
    line_chart.x_labels = map(str, range(2557, 2561))
    line_chart.add('ปริมาตร', [ year2557[1]/100000000, year2558[1]/100000000, year2559[1]/100000000, year2560[1]/100000000] )
    line_chart.render_to_file('graph-allyear-quantity.svg' )

main()
