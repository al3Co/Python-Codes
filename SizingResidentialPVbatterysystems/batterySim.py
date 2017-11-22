# This code simulates the energy behavior depending on the size of the storage battery
# Autor: Raquel Alejandra Vasquez Torres

import time
from fractions import Fraction
import matplotlib.pyplot as plt
from xlrd import open_workbook

file = time.strftime("%Y%m%d-%H%M%S")

# declare time interval conversion factor from kW to kWh of 0.0833 (5 min interval) 
timeInterval = Fraction(5, 60)

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
def mainCode(consumption, PVgeneration):
	# declare battery as 0% of charge and 1.2 (kW) of storage
	batteryCurrentStorage, batterySize, previousCharge, number = [], 1.2, 0.0, 0
	# declare vectors
	Consumption, PVGeneration, Edu, Ebc, Ebd, GridConsumption, selfConsRate = [], [], [], [], [], [], []
	degreeSs, gridFeed_In = [], []
	# Prepare file to save data
	f = open(file,'a')
	f.write(("Number")+'\t'+("Consumption (W)")+'\t'+("PV generation")+'\t'+ ("Edu")+'\t'+("Ebc")+'\t'+("BatteryCurrentStorage")+'\t'+("Grid Consumption")+'\t'+("Ebd")+'\t'+("Self-Consumption Rate")+'\t'+("Degree of Self-Sufficiency")+'\t'+("Grid Feed-In")+'\n')
	f.close()
	# verify length of data vector
	if len(consumption) == len(PVgeneration):
		# for each data
		for a in range(0, len(consumption)):
			# function to calculate the Energy Directly Used from PVgeneration (Edu)
			Edu = energyDirCons(consumption[a], PVgeneration[a], Edu, timeInterval)
			# function to calculate the Energy Used for charging the battery (Ebc)
			Ebc = energyChargingBattery(consumption[a], PVgeneration[a], Ebc, timeInterval)
			# function to calculate the Battery Current Storage
			batteryCurrentS(consumption[a], PVgeneration[a], previousCharge, batterySize, batteryCurrentStorage)
			# function to calculate the Grid Consumption
			gridCons(consumption[a], PVgeneration[a], batteryCurrentStorage[a], previousCharge, GridConsumption)
			# function to calculate the grid feed In
			gridFeedIn(batteryCurrentStorage[a], batterySize, PVgeneration[a], consumption[a], gridFeed_In)
			# function to calculate the Energy Discharge from the Battery (Ebd)
			previousCharge = energyBatteryDischarge(consumption[a], PVgeneration[a], Ebd, GridConsumption[a], previousCharge, timeInterval, gridFeed_In[a])
			# function to calculate the self-Consumption Rate
			selfConsumptionRate(Edu[a], Ebc[a], PVgeneration[a], selfConsRate)
			# function to calculate degree of self-sufficiency (d)
			degreeSelfSuff(Edu[a], Ebd[a], consumption[a], degreeSs)
			# save in vetor to plot
			Consumption.append(consumption[a])
			PVGeneration.append(PVgeneration[a])
			# save data on file
			f = open(file,'a')
			f.write(str(a + 1)+'\t'+str(consumption[a])+'\t'+str(PVgeneration[a])+'\t'+ str(Edu[a])+'\t'+str(Ebc[a])+'\t'+str(batteryCurrentStorage[a])+'\t'+str(GridConsumption[a])+'\t'+str(Ebd[a])+'\t'+str(selfConsRate[a])+'\t'+str(degreeSs[a])+'\t'+str(gridFeed_In[a])+'\n')
			f.close()
		# function to plot data
		plotData(Consumption, PVGeneration, Edu, Ebc, batteryCurrentStorage, GridConsumption, Ebd, selfConsRate, degreeSs, gridFeed_In, batterySize)

def energyDirCons(consumption, PVgeneration, Edu, timeInterval):
	if PVgeneration < consumption:
		Edu.append(PVgeneration)
	elif PVgeneration >= consumption:
		Edu.append(consumption)
	return Edu

def energyChargingBattery(consumption, PVgeneration, Ebc, timeInterval):
	if PVgeneration == 0.0 or PVgeneration < consumption:
		Ebc.append(0.0)
	elif PVgeneration > consumption:
		Ebc.append(PVgeneration - consumption)
	else:
		Ebc.append(0.0)
	return Ebc

def batteryCurrentS(consumption, PVgeneration, previousCharge, batterySize, batteryCurrentStorage):
	batteryCurrentStorageTemp = ((PVgeneration - consumption) + previousCharge)
	if batteryCurrentStorageTemp < 0.0:
		batteryCurrentStorageTemp = 0.0
	if batteryCurrentStorageTemp > batterySize:
		batteryCurrentStorageTemp = batterySize
	batteryCurrentStorage.append(batteryCurrentStorageTemp)

def gridCons(consumption, PVgeneration, batteryCurrentStorage, previousCharge, GridConsumption):
	GridConsumptionTemp = 0.0
	GridConsumptionTemp = (consumption - (PVgeneration + batteryCurrentStorage + previousCharge))
	if (PVgeneration + batteryCurrentStorage + previousCharge) > consumption:
		GridConsumptionTemp = 0.0
	GridConsumption.append(GridConsumptionTemp)

def gridFeedIn(batteryCurrentStorage, batterySize, PVgeneration, consumption, gridFeed_In):
	gridFeedIn = 0.0
	if ((batteryCurrentStorage >= batterySize) & (PVgeneration > consumption)):
		gridFeedIn = (PVgeneration - consumption)
	else:
		gridFeedIn = 0.0
	gridFeed_In.append(gridFeedIn)

def energyBatteryDischarge(consumption, PVgeneration, Ebd, GridConsumption, previousCharge, timeInterval, gridFeed_In):
	EbdTemp = 0.0
	# Energy Battery Discharge
	if ((PVgeneration > 0) & (gridFeed_In == 0.0)):
		EbdTemp = PVgeneration - (consumption - GridConsumption)
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

def selfConsumptionRate(Edu, Ebc, PVgeneration, selfConsRate):
	try:
		s = (Edu + Ebc)/ PVgeneration
	except:
		s = 0.0
	selfConsRate.append(s)

def degreeSelfSuff(Edu, Ebd, consumption, degreeSs):
	try:
		d = (Edu + Ebd) / Consumption
	except:
		d = 0.0
	degreeSs.append(d)

def plotData(Consumption, PVGeneration, Edu, Ebc, batteryCurrentStorage, GridConsumption, Ebd, selfConsRate, degreeSs, gridFeed_In, batterySize):
	plt.plot(Consumption,'b', label="Consumption", linewidth=2)
	plt.plot(PVGeneration,'g', label="PV Generation", linewidth=2)
	plt.plot(Edu,'r', label="Energy directly used", linewidth=2)
	#plt.plot(Ebc,'c', label="Energy Used for charging Battery", linewidth=2)
	plt.plot(batteryCurrentStorage,'m', label="battery Current Storage", linewidth=2)
	plt.plot(GridConsumption,'y', label="Grid Supply", linewidth=2)
	plt.plot(Ebd,'k', label="Energy Battery Discharge", linewidth=2)
	#plt.plot(selfConsRate, 'g', label="Self-Consumption Rate", linewidth=2)
	#plt.plot(degreeSs, 'b', label="Degree of Self-Sufficiency", linewidth=2)
	plt.plot(gridFeed_In, 'c', label="Grid Feed-In", linewidth=2)
	plt.legend(loc=9, fontsize="x-small", ncol=3)
	plt.xlabel("Time")
	plt.ylabel("KWh")
	title = "Grid/Battery Consumption (Battery Size: {}kW) ".format(batterySize)
	plt.title(title)
	#plt.axis([0, len(cons), 0, max(PVgeneration)])
	plt.grid(True)
	plt.savefig(file + ".png")
	plt.show()

# main
if __name__ == "__main__":
	#try :
		# function to read excel data
	consumption, PVgeneration = readExcelData()
	# main function
	mainCode(consumption, PVgeneration)
	print "Output files: Data:", file, " Image: ", str(file + ".png")
	#except Exception, e:
		#print "Oops!  Something is wrong: ", e
	
	



