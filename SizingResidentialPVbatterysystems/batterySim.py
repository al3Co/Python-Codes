### This code simulates the battery size

import time
import matplotlib.pyplot as plt
from xlrd import open_workbook

file = time.strftime("%Y%m%d-%H%M%S")

# function to read excel data
def readExcelData():
    a, b = False, False
    wb = open_workbook('Simulation_Example.xlsx')
    for s in wb.sheets():
        consumption, PVgeneration = [], []
        for col in range(s.ncols):
            col_value = []
            for row in range(s.nrows):
                value  = (s.cell(row,col).value)
                if a == True:
                    try : value = (int(value))
                    except : pass
                    col_value.append(value)
                    consumption.append(value)
                if value == "Consumption (W)":
                    a = True
                if b == True:
                    try : value = (int(value))
                    except : pass
                    col_value.append(value)
                    PVgeneration.append(value)
                if value == "PV generation":
                    b = True
            a, b = False, False
    return consumption, PVgeneration

# main function
def mainCode(consumption, PVgeneration):
	# declared battery as 0% of charge and 10000 (kW) of storage
	batteryCurrentStorage, batterySize, previousCharge, number = [], 10000, 0, 0
	# declare vectors
	Consumption, PVGeneration, Edu, Ebc, Ebd, GridConsumption, selfConsRate = [], [], [], [], [], [], []
	# Prepare file to save data
	f = open(file,'a')
	f.write(("Number")+'\t'+("Consumption (W)")+'\t'+("PV generation")+'\t'+ ("Edu")+'\t'+("Ebc")+'\t'+("batteryCurrentStorage")+'\t'+("GridConsumption")+'\t'+("Ebd")+'\t'+("self-Consumption Rate")+'\n')
	f.close()
	# verify length of data vector
	if len(consumption) == len(PVgeneration):
		# for each data
		for a in range(0, len(consumption)):
			# function to calculate the Energy Directly Used from PVgeneration (Edu)
			Edu = energyDirCons(consumption[a], PVgeneration[a], Edu)
			# function to calculate the Energy Used for charging the battery (Ebc)
			Ebc = energyChargingBattery(consumption[a], PVgeneration[a], Ebc)
			# function to calculate the Energy Discharge from the Battery (Ebd)
			previousCharge = energyBatteryDischarge(consumption[a], PVgeneration[a], Ebd, GridConsumption, batteryCurrentStorage, batterySize, previousCharge)
			# function to calculate the self-Consumption Rate
			selfConsumptionRate(Edu[a], Ebc[a], PVgeneration[a], selfConsRate)
			# save in vetor to plot
			Consumption.append(consumption[a])
			PVGeneration.append(PVgeneration[a])
			# save data on file
			f = open(file,'a')
			f.write(str(a + 1)+'\t'+str(consumption[a])+'\t'+str(PVgeneration[a])+'\t'+ str(Edu[a])+'\t'+str(Ebc[a])+'\t'+str(batteryCurrentStorage[a])+'\t'+str(GridConsumption[a])+'\t'+str(Ebd[a])+'\t'+str(selfConsRate[a])+'\n')
			f.close()
		# plot data
		plotData(Consumption, PVGeneration, Edu, Ebc, batteryCurrentStorage, GridConsumption, Ebd)

def selfConsumptionRate(Edu, Ebc, PVgeneration, selfConsRate):
	try:
		s = (Edu + Ebc)/ PVgeneration
	except:
		s = 0
	selfConsRate.append(s)

def energyBatteryDischarge(consumption, PVgeneration, Ebd, GridConsumption, batteryCurrentStorage, batterySize, previousCharge):
	EbdTemp = 0
	# battery Current Storage
	batteryCurrentStorageTemp = (PVgeneration + previousCharge) - consumption
	if batteryCurrentStorageTemp < 0:
		batteryCurrentStorageTemp = 0
	if batteryCurrentStorageTemp > batterySize:
		batteryCurrentStorageTemp = batterySize
	batteryCurrentStorage.append(batteryCurrentStorageTemp)
	
	# Grid Consumption
	GridConsumptionTemp = consumption - (PVgeneration + batteryCurrentStorageTemp + previousCharge)
	if (PVgeneration + batteryCurrentStorageTemp + previousCharge) > consumption:
		GridConsumptionTemp = 0
	GridConsumption.append(GridConsumptionTemp)

	#Energy Battery Discharge
	if (previousCharge > 0 ):
		EbdTemp = (consumption - (PVgeneration + previousCharge))
	elif (previousCharge < 0 ):
		EbdTemp = 0
	if EbdTemp < 0:
		EbdTemp = 0
	Ebd.append(EbdTemp)
	
	# previous charge
	previousCharge = batteryCurrentStorageTemp
	return previousCharge
	
def energyChargingBattery(consumption, PVgeneration, Ebc):
	if PVgeneration == 0 or PVgeneration < consumption:
		Ebc.append(0)
	elif PVgeneration > consumption:
		Ebc.append(PVgeneration - consumption)
	return Ebc

def energyDirCons(consumption, PVgeneration, Edu):
	if PVgeneration < consumption:
		Edu.append(PVgeneration)
	elif PVgeneration >= consumption:
		Edu.append(consumption)
	return Edu

# function to plot data
def plotData(Consumption, PVGeneration, Edu, Ebc, batteryCurrentStorage, GridConsumption, Ebd):
	plt.plot(Consumption,'b', label="Consumption", linewidth=2)
	plt.plot(PVGeneration,'g', label="PVgeneration", linewidth=2)
	plt.plot(Edu,'r', label="Energy directly used", linewidth=2)
	plt.plot(Ebc,'c', label="Energy Used for charging Battery", linewidth=2)
	plt.plot(batteryCurrentStorage,'m', label="battery Current Storage", linewidth=2)
	plt.plot(GridConsumption,'y', label="Grid Consumption", linewidth=2)
	plt.plot(Ebd,'k', label="Energy Battery Discharge", linewidth=2)
	plt.legend(loc=0, fontsize="x-small", ncol=3)
	plt.xlabel("Time")
	plt.ylabel("KWh")
	plt.title("Grid/Battery Consumption")
	#plt.axis([0, len(cons), 0, max(PVgeneration)])
	plt.grid(True)
	plt.savefig(file + ".png")
	plt.show()

# main
if __name__ == "__main__":
	try :
		# function to read excel data
		consumption, PVgeneration = readExcelData()
		# main function
		mainCode(consumption, PVgeneration)
	except Exception, e:
		print "Oops!  Something is wrong, check the name of the files or input file"
	
	



