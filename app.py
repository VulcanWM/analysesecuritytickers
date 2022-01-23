from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  return redirect('/data')

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