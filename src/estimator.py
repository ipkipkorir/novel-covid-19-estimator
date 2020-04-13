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


	#Compute estimates:
	##Severe Impact computation
	severeImpactCurrentlyInfected = data['reportedCases'] * 50
	severeImpactInfectionsByRequestedTime = (data['reportedCases'] * 50) * (2 ** (timeInDays // 3))

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
