from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

data = {"UK": {"Buy": ['ukbuy1', 'ukbuy2', 'ukbuy3', 'ukbuy4', 'ukbuy5'], "Sell": ['uksell1', 'uksell2', 'uksell3', 'uksell4', 'uksell5']}, "Canada": {"Buy": ['canadabuy1', 'canadabuy2', 'canadabuy3', 'canadabuy4', 'canadabuy5'], "Sell": ['canadasell1', 'canadasell2', 'canadasell3', 'canadasell4', 'canadasell5']}, "USA": {"Buy": ['usabuy1', 'usabuy2', 'usabuy3', 'usabuy4', 'usabuy5'], "Sell": ['usasell1', 'usasell2', 'usasell3', 'usasell4', 'usasell5']}}

@app.route("/")
def index():
  return "Click <a href='/data'>here</a> for data"

@app.route("/data")
def dataroute():
  con = sqlite3.connect("sql.db")
  cur = con.cursor()
  times = []
  countries = []
  for row in cur.execute('SELECT * FROM MomentumIndicator;'):
    if row[2] not in countries:
      countries.append(row[2])
    if row[1] not in times:
      times.append(row[1])
  con.close()
  countryorder = ['Australia', 'Japan', 'India', 'Singapore', 'HongKong', 'GermanySwissAustria', 'RestOfEurope', 'UnitedKingdom', 'USA', 'Canada'] 
  return render_template("data.html", countries=countries, times=times, countryorder=countryorder)

@app.route("/data/<country>")
def country(country):
  con = sqlite3.connect("sql.db")
  cur = con.cursor()
  times = []
  countries = []
  for row in cur.execute('SELECT * FROM MomentumIndicator;'):
    if row[2] not in countries:
      countries.append(row[2])
    if row[1] not in times:
      times.append(row[1])
  con.close()
  countryorder = ['Australia', 'Japan', 'India', 'Singapore', 'HongKong', 'GermanySwissAustria', 'RestOfEurope', 'UnitedKingdom', 'USA', 'Canada'] 
  return render_template("country.html", countries=countries, times=times, countryorder=countryorder, countryname=country)

@app.route('/data/<country>/<thetime>')
def countrytime(country, thetime):
  con = sqlite3.connect("sql.db")
  alldata = []
  cur = con.cursor()
  times = []
  countries = []
  for row in cur.execute('SELECT * FROM MomentumIndicator;'):
    if row[2] not in countries:
      countries.append(row[2])
    if row[1] not in times:
      times.append(row[1])
    if row[2] == country and row[1] == thetime:
      alldata.append(row)
  con.close()
  countryorder = ['Australia', 'Japan', 'India', 'Singapore', 'HongKong', 'GermanySwissAustria', 'RestOfEurope', 'UnitedKingdom', 'USA', 'Canada'] 
  return render_template("countrytime.html", countries=countries, times=times, alldata=alldata, countryorder=countryorder, countryname=country, timename=thetime)

# @app.route('/data/sort/<sortkey>/<country>/<thetime>')
# def sortdata(sortkey, country, thetime):
#   sorts = {"MomentumInd3M": 3, "Positive3M": 4, "Negative3M": 5, "ID3M": 6, "Low": 7, "EquityAmount": 8, "CCY": 9, "P_E": 10, "AnnualDiviYield": 11, "EMA52-208Ratio": 12, "Average_P_E": 13}
#   if sortkey not in sorts.keys():
#     return redirect(f"/data/{country}/{thetime}") 
#   con = sqlite3.connect("sql.db")
#   alldata = []
#   cur = con.cursor()
#   times = []
#   countries = []
#   for row in cur.execute('SELECT * FROM MomentumIndicator;'):
#     if row[2] not in countries:
#       countries.append(row[2])
#     if row[1] not in times:
#       times.append(row[1])
#     if row[2] == country and row[1] == thetime:
#       alldata.append(row)
#   con.close()
#   sortindex = sorts[sortkey]
#   sortdict = {}
#   newalldata = []
#   for x in alldata:
#     sortdict[x[0]] = x[sortindex]
#   sortdict = sorted(sortdict.items(), key=lambda x: x[1])
#   # for x in alldata:

#   #   newalldata.insert()
#   return str(sortdict)
#   countryorder = ['Australia', 'Japan', 'India', 'Singapore', 'HongKong', 'GermanySwissAustria', 'RestOfEurope', 'UnitedKingdom', 'USA', 'Canada'] 
#   return render_template("countrytime.html", countries=countries, times=times, alldata=alldata, countryorder=countryorder, countryname=country, timename=thetime)

# @app.route("/data/<dataname>/<thedate>/<country>")
# def datanameroute(dataname, thedate, country):
#   con = sqlite3.connect("sql.db")
#   cur = con.cursor()
#   for row in cur.execute('SELECT * FROM MomentumIndicator;'):
#     if row[0] == dataname and row[1] == thedate and row[2] == country:
#       con.close()
#       return str(row)
#   con.close()