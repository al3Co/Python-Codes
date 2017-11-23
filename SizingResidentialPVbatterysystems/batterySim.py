# This code simulates the energy behavior depending on the size of the storage battery
# Autor: Raquel Alejandra Vasquez Torres

import time
from fractions import Fraction
import matplotlib.pyplot as plt
from xlrd import open_workbook
import matplotlib.ticker as plticker

date = time.strftime("%Y%m%d-%H%M%S")

# declare time interval conversion factor from kW to kWh of 0.0833 (5 min interval) 
timeInterval = Fraction(5, 60)
electCost = 0.2670
electPrice = 0.1114

# function to read excel data
def readExcelData():
    a, b = False, False
    wb = open_workbook('sample.xlsx')
    for s in wb.sheets():
        consumption, PVgeneration = [], []
        for col in range(s.ncols):
            col_value = []
            for row in range(s.nrows):
                value  = (s.cell(row,col).value)
                if a == True:
                    try : value = (float(value))
                    except : pass
                    consumption.append((value * timeInterval))
                if value == "Consumption (W)":
                    a = True
                if b == True:
                    try : value = (float(value))
                    except : pass
                    PVgeneration.append((value * timeInterval))
                if value == "PV generation":
                    b = True
            a, b = False, False
    return consumption, PVgeneration

# main function
def mainCode(consumption, PVgeneration, BatterySizeMain):
	# declare battery as 0% of charge and 1.2 (W) of storage
	batteryCurrentStorage, batterySize, previousCharge, number = [], BatterySizeMain, 0.0, 0
	# declare vectors
	Consumption, PVGeneration, Edu, Ebc, Ebd, GridConsumption, selfConsRate = [], [], [], [], [], [], 0.0
	degreeSs, gridFeed_In, electCostBuy, electPriceSell = 0.0, [], [], []
	global date
	# Prepare file to save data
	# verify length of data vector
	if len(consumption) == len(PVgeneration):
		# for each data in the row
		for a in range(0, len(consumption)):
			# Functions to calculate the energy behavior depending on the size of the storage battery
			energyDirCons(consumption[a], PVgeneration[a], Edu, timeInterval)
			energyChargingBattery(consumption[a], PVgeneration[a], Ebc, timeInterval)
			batteryCurrentS(consumption[a], PVgeneration[a], previousCharge, batterySize, batteryCurrentStorage)
			gridCons(consumption[a], PVgeneration[a], batteryCurrentStorage[a], previousCharge, GridConsumption)
			gridFeedIn(batteryCurrentStorage[a], batterySize, PVgeneration[a], consumption[a], gridFeed_In)
			previousCharge = energyBatteryDischarge(consumption[a], PVgeneration[a], Ebd, GridConsumption[a], previousCharge, timeInterval, gridFeed_In[a], Edu[a])
			
			electricityCost(GridConsumption[a], electCost, electCostBuy)
			electricityPrice(gridFeed_In[a], electPrice, electPriceSell)
		
		selfConsRate = selfConsumptionRate(Edu, Ebc, PVgeneration, selfConsRate)
		degreeSs = degreeSelfSuff(Edu, Ebd, consumption, degreeSs)

		# function to plot data
		#plotData(consumption, PVgeneration, Edu, Ebc, batteryCurrentStorage, GridConsumption, Ebd, gridFeed_In, batterySize)

		# save data on file
		# writte titles
		file = (str(BatterySizeMain)+'.txt')
		f = open(file,'a')
		f.write(("Number")+'\t'+("Consumption (W)")+'\t'+("PV generation")+'\t'+ ("Edu")+'\t'+("Ebc")+'\t'+("BatteryCurrentStorage")+'\t'+("Grid Consumption")+'\t'+("Ebd")+'\t'+("Grid Feed-In")+'\t'+("Electricity Cost/Buy[Euro]")+'\t'+("Electricity Profit/Sell[Euro]")+'\t'+("Self-Consumption Rate [s]")+'\t'+("Degree of Self-Sufficiency [d]")+'\n')
		f.close()
		# write summations
		f = open(file,'a')
		f.write(str(len(consumption))+'\t'+str(sum(consumption))+'\t'+str(sum(PVgeneration))+'\t'+ str(sum(Edu))+'\t'+str(sum(Ebc))+'\t'+str(sum(batteryCurrentStorage))+'\t'+str(sum(GridConsumption))+'\t'+str(sum(Ebd))+'\t'+str(sum(gridFeed_In))+'\t'+str(sum(electCostBuy))+'\t'+str(sum(electPriceSell))+'\t'+str(selfConsRate)+'\t'+str(degreeSs)+'\n')
		f.close()
		# write all data content
		for a in range(0, len(consumption)):
			f = open(file,'a')
			f.write(str(a + 1)+'\t'+str(consumption[a])+'\t'+str(PVgeneration[a])+'\t'+ str(Edu[a])+'\t'+str(Ebc[a])+'\t'+str(batteryCurrentStorage[a])+'\t'+str(GridConsumption[a])+'\t'+str(Ebd[a])+'\t'+str(gridFeed_In[a])+'\t'+str(electCostBuy[a])+'\t'+str(electPriceSell[a])+'\n')
			f.close()
	else:
		print "The length of the data lists is not the same"
	return degreeSs, selfConsRate

# function to calculate the Energy Directly Used from PVgeneration (Edu)
def energyDirCons(consumption, PVgeneration, Edu, timeInterval):
	EduTemp = 0.0
	if PVgeneration < consumption:
		EduTemp = PVgeneration
	elif PVgeneration >= consumption:
		EduTemp = consumption
	Edu.append(EduTemp)

# function to calculate the Energy Used for charging the battery (Ebc)
def energyChargingBattery(consumption, PVgeneration, Ebc, timeInterval):
	EbcTemp = 0.0
	if PVgeneration == 0.0 or PVgeneration < consumption:
		EbcTemp = 0.0
	elif PVgeneration > consumption:
		EbcTemp = (PVgeneration - consumption)
	else:
		EbcTemp = 0.0
	Ebc.append(EbcTemp)

# function to calculate the Battery Current Storage
def batteryCurrentS(consumption, PVgeneration, previousCharge, batterySize, batteryCurrentStorage):
	batteryCurrentStorageTemp = ((PVgeneration - consumption) + previousCharge)
	if batteryCurrentStorageTemp < 0.0:
		batteryCurrentStorageTemp = 0.0
	if batteryCurrentStorageTemp > batterySize:
		batteryCurrentStorageTemp = batterySize
	batteryCurrentStorage.append(batteryCurrentStorageTemp)

# function to calculate the Grid Consumption
def gridCons(consumption, PVgeneration, batteryCurrentStorage, previousCharge, GridConsumption):
	GridConsumptionTemp = 0.0
	GridConsumptionTemp = (consumption - (PVgeneration + batteryCurrentStorage + previousCharge))
	if (PVgeneration + batteryCurrentStorage + previousCharge) > consumption:
		GridConsumptionTemp = 0.0
	GridConsumption.append(GridConsumptionTemp)

# function to calculate the grid feed In
def gridFeedIn(batteryCurrentStorage, batterySize, PVgeneration, consumption, gridFeed_In):
	gridFeedIn = 0.0
	#if ((batteryCurrentStorage >= batterySize) & (PVgeneration > consumption)):
	if ((PVgeneration - consumption) > 0):
		gridFeedIn = (PVgeneration - consumption)
	else:
		gridFeedIn = 0.0
	gridFeed_In.append(gridFeedIn)

# function to calculate the Energy Discharge from the Battery (Ebd)
def energyBatteryDischarge(consumption, PVgeneration, Ebd, GridConsumption, previousCharge, timeInterval, gridFeed_In, Edu):
	EbdTemp = 0.0
	# Energy Battery Discharge (revisar)
	if ((consumption > PVgeneration) & (PVgeneration > 0)):
		EbdTemp = (consumption - PVgeneration)
		if EbdTemp < 0.0:
			EbdTemp = 0.0
	else:
		EbdTemp = 0.0
	Ebd.append(EbdTemp)
	# Previous charge (keep at the end of this function) (Ok)
	previousCharge = PVgeneration - consumption
	if previousCharge < 0.0:
		previousCharge = 0.0
	return previousCharge

# function to calculate the self-Consumption Rate
def selfConsumptionRate(Edu, Ebc, PVgeneration, selfConsRate):
	try:
		s = (sum(Edu) + sum(Ebc))/ sum(PVgeneration)
	except:
		s = 0.0
	selfConsRate = s
	return selfConsRate

# function to calculate degree of self-sufficiency (d)
def degreeSelfSuff(Edu, Ebd, consumption, degreeSs):
	try:
		d = (sum(Edu) + sum(Ebd)) / sum(consumption)
	except:
		d = 0.0
	degreeSs = d
	return degreeSs

# function to calculate the daily electricity cost (buy from grid)
def electricityCost(GridConsumption, electCost, electCostBuy):
	electCostBuyTemp = GridConsumption * electCost
	electCostBuy.append(electCostBuyTemp)

# function to calculate the daily electricity price (sell to grid)
def electricityPrice(gridFeed_In, electPrice, electPriceSell):
	electPriceSellTemp = gridFeed_In * electPrice
	electPriceSell.append(electPriceSellTemp)


# function to plot data
def plotData(consumption, PVgeneration, Edu, Ebc, batteryCurrentStorage, GridConsumption, Ebd, gridFeed_In, batterySize):
	labels = list(range(-1,25))
	fig, ax = plt.subplots()
	fig.canvas.draw()

	plt.plot(consumption,'b', label="Consumption", linewidth=2)
	plt.plot(PVgeneration,'g', label="PV Generation", linewidth=2)
	plt.plot(Edu,'r', label="Energy directly used", linewidth=2)
	#plt.plot(Ebc,'c', label="Energy Used for charging Battery", linewidth=2)
	plt.plot(batteryCurrentStorage,'m', label="battery Current Storage", linewidth=2)
	plt.plot(GridConsumption,'y', label="Grid Supply", linewidth=2)
	plt.plot(Ebd,'k', label="Energy Battery Discharge", linewidth=2)
	plt.plot(gridFeed_In, 'c', label="Grid Feed-In", linewidth=2)
	plt.legend(loc=9, fontsize="x-small", ncol=3)
	plt.xlabel("Time")
	plt.ylabel("KWh")
	title = "Energy Flows of PV System (Battery Size: {}kW) ".format(batterySize)
	plt.title(title)
	
	loc = plticker.MultipleLocator(base=(12))
	ax.xaxis.set_major_locator(loc)
	ax.set_xticklabels(labels)
	plt.margins(0.01)
	plt.grid(True)
	plt.savefig(file + ".png")
	plt.show()

def plotBatteryCapacity(DegreeOfSelfSuf, SelfConsumptionRate, BatterySizeMain):
	print DegreeOfSelfSuf, SelfConsumptionRate

	labels = list(range(0, 10))
	fig, ax = plt.subplots()
	fig.canvas.draw()

	plt.plot(DegreeOfSelfSuf,'b', label="Degree of self-sufficiency (d)", linewidth=2)
	plt.plot(SelfConsumptionRate,'k', label="Degree of self-consumption (s)", linewidth=2)
	plt.legend(loc=9, fontsize="x-small", ncol=3)
	plt.xlabel("Battery Size Capacity [kWh]")
	plt.ylabel("")
	title = "Energy Flows of PV System"
	plt.title(title)

	loc = plticker.MultipleLocator(base=10)
	ax.xaxis.set_major_locator(loc)
	ax.set_xticklabels(labels)
	plt.axis([0, 10, 0, 1.2])
	plt.margins(0.01)
	plt.grid(True)
	plt.savefig("Energy Flows of PV System.png")
	plt.show()


# main
if __name__ == "__main__":
	#try :
		# function to read excel data
	consumption, PVgeneration = readExcelData()
	# main function
	BatteryCapacityMain	= [0, 5, 10, 25, 50, 75, 100, 150, 300] # este no lo estoy usando
	BatterySizeMain 	= [0.0, 0.07, 0.14, 0.35, 0.71, 1.07, 1.42, 2.14, 4.28]
	DegreeOfSelfSuf, SelfConsumptionRate = [], []

	for a in BatterySizeMain:
		degreeSs, selfConsRate = mainCode(consumption, PVgeneration, a)
		DegreeOfSelfSuf.append(degreeSs)
		SelfConsumptionRate.append(selfConsRate)
		print "Output files: Data:", str(str(a) + ".txt"), " Image: ", str(str(a) + ".png")

	plotBatteryCapacity(DegreeOfSelfSuf, SelfConsumptionRate, BatterySizeMain)
	#except Exception, e:
		#print "Oops!  Something is wrong: ", e
	
	



