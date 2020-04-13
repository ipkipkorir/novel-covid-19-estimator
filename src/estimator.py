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
	impactHospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - impactSevereCasesByRequestedTime)

	#Compute estimates:
	##Severe Impact computation
	severeImpactCurrentlyInfected = data['reportedCases'] * 50
	severeImpactInfectionsByRequestedTime = (data['reportedCases'] * 50) * (2 ** (timeInDays // 3))
	severeImpactSevereCasesByRequestedTime =  math.trunc(0.15 * (data['reportedCases'] * 50) * (2 ** (timeInDays // 3)))
	severeImpactHospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - severeImpactSevereCasesByRequestedTime)

	#Estimates
	estimate = {
		'impact' : {
			'currentlyInfected' : impactCurrentlyInfected,
			'infectionsByRequestedTime' : impactInfectionsByRequestedTime
		},

		'severeImpact' : {
				'currentlyInfected' : severeImpactCurrentlyInfected,
				'infectionsByRequestedTime' :  severeImpactInfectionsByRequestedTime
				
		}

	}
	return estimate
