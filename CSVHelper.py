import Flight
import csv
import datetime

def writeToCSV(allFlights):
	now = datetime.datetime.now()
	fileName = now.strftime("%Y-%m-%d_%H:%M")
	with open('flightDetails'+fileName+'.csv', 'wb') as csvfile:
	    fieldnames = ['fromDate', 'toDate','fromTime','toTime','fromAirport','toAirport','flightNumber','points','lowestPrice','extraCharges']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()
	    for flight in allFlights:        
	        writer.writerow({'fromDate' : flight.departDate, 'toDate':flight.arriveDate,'fromTime':flight.departTime,'toTime':flight.arriveTime,'fromAirport':flight.fromAirport,'toAirport':flight.to,'flightNumber':flight.flightNumber,'points':flight.points,'lowestPrice':flight.lowestPrice,'extraCharges':flight.extraCharges})
