#AutoIt3Wrapper_Run_AU3Check=n
#include 'Include/OOPE.au3'
#include <Array.au3>

;Populate


#Region Class Codon
	Local $dMutationRate, $iValue, $pCrossRate

	;Mutation Rate
	Func SetMutationRate($dNewMR)
		$This.dMutationRate = $dNewMR
	EndFunc

	Func GetMutationRate()
		Return $This.dMutationRate
	EndFunc

	;Codon's Value
	Func SetValue($iNewValue)
		$This.iValue = $iNewValue
	EndFunc

	Func GetValue()
		Return $This.iValue
	EndFunc

	;CrossOver Rate
	Func SetCrossRate($pNewCR)
		$This.pCrossRate = $pNewCR
	EndFunc

	Func GetCrossRate()
		Return $This.pCrossrate
	EndFunc
#EndRegion

#Region Class Gene
	Local $aCodons[1] = [0]

	Func GetLength()
		Return $aCodons[0]
	EndFunc

	Func Initialize()

	EndFunc
#EndRegion

#Region Class Chromosome
	Local $iSetofValues, $pCrossRate, $pFitness, $aGenes[1] = [0]

	Func Initialize()

	EndFunc
#EndRegion

#Region Class Population


	Func Intialize()

	EndFunc

	Func Decode($iChromosome, $iAnswer)

	EndFunc

	Func Genetics()

	EndFunc
#EndRegion