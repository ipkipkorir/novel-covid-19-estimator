import math
def estimator(data):
		
	#Convert or check that 'timeToElapse' is in days
	if data['periodType'] == 'days':
		timeInDays = data['timeToElapse']
	elif data['periodType'] == 'weeks':
		timeInDays = data['timeToElapse'] * 7
	elif data['periodType'] == 'months':
		timeInDays = data['timeToElapse'] * 30

	#Compute estimates:
	##Impact computation
	impactCurrentlyInfected = data['reportedCases'] * 10
	impactInfectionsByRequestedTime = (data['reportedCases'] * 10) * (2 ** (timeInDays // 3))
	impactSevereCasesByRequestedTime = math.trunc(0.15 * (data['reportedCases'] * 10) * (2 ** (timeInDays // 3)))
	impactHospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - (0.15 * (data['reportedCases'] * 10) * (2 ** (timeInDays // 3))))
	impactCasesForICUByRequestedTime = math.trunc(0.05 * (data['reportedCases'] * 10) * (2 ** (timeInDays // 3)))
	impactCasesForVentilatorsByRequestedTime = math.trunc(0.02 * impactInfectionsByRequestedTime)
	impactDollarsInFlight = ((impactInfectionsByRequestedTime * data["region"]['avgDailyIncomePopulation']) * data["region"]['avgDailyIncomeInUSD']) // timeInDays

	#Compute estimates:
	##Severe Impact computation
	severeImpactCurrentlyInfected = data['reportedCases'] * 50
	severeImpactInfectionsByRequestedTime = (data['reportedCases'] * 50) * (2 ** (timeInDays // 3))
	severeImpactSevereCasesByRequestedTime =  math.trunc(0.15 * (data['reportedCases'] * 50) * (2 ** (timeInDays // 3)))
	severeImpactHospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - (0.15 * (data['reportedCases'] * 50) * (2 ** (timeInDays // 3))))
	severeImpactCasesForICUByRequestedTime = math.trunc(0.05 * (data['reportedCases'] * 50) * (2 ** (timeInDays // 3)))
	severeImpactCasesForVentilatorsByRequestedTime = math.trunc(0.02 * severeImpactInfectionsByRequestedTime)
	severeImpactDollarsInFlight = ((severeImpactInfectionsByRequestedTime * data["region"]['avgDailyIncomePopulation']) * data["region"]['avgDailyIncomeInUSD']) // timeInDays

	#Estimates
	estimate = {
		'impact' : {
			'currentlyInfected' : impactCurrentlyInfected,
			'infectionsByRequestedTime' : impactInfectionsByRequestedTime,
			'severeCasesByRequestedTime' : impactSevereCasesByRequestedTime,
			'HospitalBedsByRequestedTime' : impactHospitalBedsByRequestedTime,
			'casesForICUByRequestedTime' : impactCasesForICUByRequestedTime,
			'casesForVentilatorsByRequestedTime' : impactCasesForVentilatorsByRequestedTime,
			'dollarsInFlight' : impactDollarsInFlight
		},

		'severeImpact' : {
				'currentlyInfected' : severeImpactCurrentlyInfected,
				'infectionsByRequestedTime' :  severeImpactInfectionsByRequestedTime,
				'severeCasesByRequestedTime' : severeImpactSevereCasesByRequestedTime,
				'HospitalBedsByRequestedTime' : severeImpactHospitalBedsByRequestedTime,
				'casesForICUByRequestedTime' : severeImpactCasesForICUByRequestedTime,
				'casesForVentilatorsByRequestedTime' : severeImpactCasesForVentilatorsByRequestedTime,
				'dollarsInFlight' : severeImpactDollarsInFlight	
		}

	}
	return estimate
