# -*- coding: utf-8 -*-
import pygal
import csv
from itertools import groupby


def main():
    file = open('../data/2557.csv', 'r', encoding='utf-8')
    data = csv.reader(file)
    table = [row for row in data]
    year = 2557
    # whiterice = [year, 0, 0, 0]
    whiterice1 = [year, 0, 0, 0]
    whiterice2 = [year, 0, 0, 0]
    whiterice3 = [year, 0, 0, 0]
    whiterice5per = [year, 0, 0, 0]
    extrabrokenrice = [year, 0, 0, 0]
    brokenrice = [year, 0, 0, 0]
    for key, group in groupby(table, lambda x: x[2]):
        for item in group:
            if key == "ข้าวขาว100%ชั้น1":
                whiterice1[1] = key
                whiterice1[3] += float(item[5])
                whiterice1[2] += float(item[4])
            elif key == "ข้าวขาว100%ชั้น2":
                whiterice2[1] = key
                whiterice2[3] += float(item[5])
                whiterice2[2] += float(item[4])
            # elif key == "ข้าวขาว100%":
            #     whiterice[1] = key
            #     whiterice[3] += float(item[5])
            #     whiterice[2] += float(item[4])
            elif key == "ข้าวขาว100%ชั้น3":
                whiterice3[1] = key
                whiterice3[3] += float(item[5])
                whiterice3[2] += float(item[4])
            elif key == "ข้าวขาว5%":
                whiterice5per[1] = key
                whiterice5per[3] += float(item[5])
                whiterice5per[2] += float(item[4])
            elif key == "ข้าวขาวหักเอวันเลิศพิเศษ":
                extrabrokenrice[1] = key
                extrabrokenrice[3] += float(item[5])
                extrabrokenrice[2] += float(item[4])
            elif key == "ข้าวขาวหักเอวันเลิศ":
                brokenrice[1] = key
                brokenrice[3] += float(item[5])
                brokenrice[2] += float(item[4])
    bar_chart = pygal.Bar(legend_at_bottom=True)
    bar_chart.title = ('ยอดปริมาตรส่งออกข้าวปี%i (หนึ่งต่อสิบล้านกิโลกรัม)' %year)
    bar_chart.add(whiterice1[1], whiterice1[2]/10000000)
    bar_chart.add(whiterice2[1], whiterice2[2]/10000000)
    bar_chart.add(whiterice3[1], whiterice3[2]/10000000)
    # bar_chart.add(whiterice[1], whiterice[2]/10000000)
    bar_chart.add(whiterice5per[1], whiterice5per[2]/10000000)
    bar_chart.add(extrabrokenrice[1], extrabrokenrice[2]/10000000)
    bar_chart.add(brokenrice[1], brokenrice[2]/10000000)
    bar_chart.render_to_file('graph-amount%i.svg' %year)

    bar_chart = pygal.Bar(legend_at_bottom=True)
    bar_chart.title = ('ยอดขายข้าวปี%i (หนึ่งต่อพันล้านบาท)' %year)
    bar_chart.add(whiterice1[1], whiterice1[3]/1000000000)
    bar_chart.add(whiterice2[1], whiterice2[3]/1000000000)
    bar_chart.add(whiterice3[1], whiterice3[3]/1000000000)
    # bar_chart.add(whiterice[1], whiterice[3]/1000000000)
    bar_chart.add(whiterice5per[1], whiterice5per[3]/1000000000)
    bar_chart.add(extrabrokenrice[1], extrabrokenrice[3]/1000000000)
    bar_chart.add(brokenrice[1], brokenrice[3]/1000000000)
    bar_chart.render_to_file('graphs-circulation%i.svg' %year)
main()
