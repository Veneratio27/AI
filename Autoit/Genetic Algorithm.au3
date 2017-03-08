#AutoIt3Wrapper_Run_AU3Check=n
#include 'Include/OOPE.au3'
#include <Array.au3>
$oMyError = ObjEvent("Autoit.Error","MyErrFunc")

;Populate
Dim $aInstructionSet[2] = ["StringIsInt($sGVal)","_isOperator($sGVal)"]
Dim $aKey[14] = ["0", "1", "2", "3", "4", "5","6","7","8","9","+","-","*","/"]
Dim $aLengthRange[5] = [0,1,2,3,4]
Dim $aRangeSet[2] = [0,1]
#classdef <Population> $oPopulation
$oPopulation.PopulationInitialize(1000,$aInstructionSet,$aKey,$aLengthRange,$aRangeSet,4)
$sOutput = ""
ConsoleWrite("Test")
For $i = 0 To UBound($oPopulation.aChromosomes)-1
	ConsoleWrite("Chromosome " & String($i))
	$sOutput = ""
	For $j = 0 To UBound($oPopulation.aChromosome.aGenes)-1
		For $k In $oPopulation.aChromosome[$i].aGenes[$j].aCodons
			$sOutput &= String($k.GetValue)
		Next
		$sOutput &= " "
	Next
	ConsoleWrite($sOutput)
	ConsoleWrite($oPopulation.Decode($i, 24))
Next

#Region Class Codon
	Local $dMutationRate = 0.001, $iValue, $pCrossRate

	;Mutation Rate
	Func SetMutationRate($dNewMR)
		$This.dMutationRate = $dNewMR
	EndFunc

	Func GetMutationRate()
		Return $This.dMutationRate
	EndFunc

	;Codon's Value
	Func SetCodonValue($iNewValue)
		$This.iValue = $iNewValue
	EndFunc

	Func GetCodonValue()
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
	Local $aCodons[1]
	#classdef <Codon> $aCodons

	Func GetGeneLength()
		Return UBound($aCodons)
	EndFunc

	Func GeneInitialize($aRangeSet, $iLength, $pCrossrate)
		Dim $aTemp[1]
		For $i = 1 to $iLength
			If $i > UBound($This.aCodons)-1 Then
				$aTemp = $This.aCodons
				ReDim $aTemp[UBound($This.aCodons)+1]
			EndIf
			$aTemp[$i].iValue = $aRangeSet[Random(1,$aRangeSet[0])]
			$aTemp[$i].pCrossRate = $pCrossrate
			$This.aCodons = $aTemp
		Next
	EndFunc

	Func GeneDecode($aKey, $aRangeSet)
		$iIndex = 0
		For $i = 0 to UBound($aCodons)-1
			$iIndex += $This.aCodons[$i].iValue*$aRangeSet[0]^($This.aCodons[0]-$i-2)
		Next
		If $iIndex >= UBound($aKey) Then
			Return ""
		Else
			Return $aKey[$iIndex]
		EndIf
	EndFunc
#EndRegion

#Region Class Chromosome
	Local $iSetofValues, $pCrossRate, $pFitness, $aRangeSet, $aGenes[1]
	#classdef <Gene> $aGenes

	Func ChromosomeInitialize($iLength, $aRangeSet, $iGLength, $pFitness)
		$This.pCrossRate = 0.1
		$This.aRangeSet = $aRangeSet
		$This.pFitness = $pFitness
		ConsoleWrite("ChromosomeInitialize Pre For Loop")
		Dim $aTemp[1]
		For $i = 1 To $iLength
			If $i > UBound($This.aGenes)-1 Then
				$aTemp = $This.aGenes
				ReDim $aTemp[UBound($This.aGenes)+1]
			EndIf
			$aTemp[$i].GeneInitialize($aRangeSet, $iGLength, $This.pCrossRate/($iLength*$iGLength))
			$This.aGenes = $aTemp
		Next
	EndFunc

	Func ChromosomeDecode($aInstructionSet, $aKey)
		$aVal[1]
		$j = 0
		For $i = 0 To UBound($This.aGenes)-1
			$sGVal = $This.aGenes[$i].GeneDecode($aKey, $This.aRangeSet)
			$bCheck = Execute($aInstructionSet[Mod($j, $aInstructionSet)])
			If $bCheck Then
				If $j > $aVal Then
					ReDim $aVal[UBound($aVal)+1]
				EndIf
				$aVal[$j] = $sGVal
			EndIf
		Next
		If UBound($aVal) <> 0 Then
			$sVal = _ArrayToString($aVal,"",1)
			If $sVal <> "" Then
				Return Execute($sVal)
			Else
				Return $sVal
			EndIf
		Else
			Return ""
		EndIf
	EndFunc

	Func TotalLen()
		Return 0
	EndFunc

	Func Split()
		Return 0
	EndFunc
#EndRegion

#Region Class Population
	Local $iPopulation, $aInstructionSet, $aKey, $aChromosomes[1], $aAnswers[1]
	#classdef <Chromosome> $aChromosomes

	Func PopulationInitialize($iPopulation, $aInstructionSet, $aKey, $aLengthRange, $aRangeSet, $iGLength)
		$This.iPopulation = $iPopulation
		$This.aInstructionSet = $aInstructionSet
		$This.aKey = $aKey
		ConsoleWrite("PopulationInitialize Pre For Loop" & @CRLF)
		Dim $aTemp[1]
		For $i = 0 To $iPopulation-1
			ConsoleWrite("PopulationInitialize Start For Loop on " & String($i) & " Pre If Statement" & @CRLF)
			ConsoleWrite("PopulationInitialize Start For Loop on " & String($i) & " Pre If Statement " & "UBound($This.aChromosomes)-1 = " & String(UBound($This.aChromosomes)-1) & @CRLF)
			ConsoleWrite("PopulationInitialize Start For Loop on " & String($i) & " Pre If Statement " & $This.aChromosomes & @CRLF)
			If $i > UBound($This.aChromosomes)-1 Then
				$aTemp = $This.aChromosomes
				ReDim $aTemp[UBound($This.aChromosomes)+1]
			EndIf
			ConsoleWrite("PopulationInitialize Start For Loop on " & String($i) & " Post If Statement" & @CRLF)
			$aTemp[$i].ChromosomeInitialize(Random(1, $aLengthRange[0]), $aRangeSet, $iGLength, 1/$iPopulation)
			$This.aChromosomes = $aTemp
		Next
	EndFunc

	Func PDecode($iChromosome, $iAnswer)
		$iValue = $This.aChromosomes[$iChromosome].ChromosomeDecode($This.aInstructionSet,$This.aKey)
		Dim $aTemp[1]
		If $iValue = $iAnswer Then
			If $This.aAnswers[UBound($This.aAnswers)-1] <> 0 Then
				$aTemp = $This.aAnswers
				ReDim $aTemp[UBound($This.aAnswers)+1]
			EndIf
			$aTemp[UBound($This.aAnswers)-1] = $This.aChromosomes[$iChromosome]
			$This.aAnswers = $aTemp
			$aTemp = $This.aChromosomes
			_ArrayDelete($aTemp,$iChromosome)
			$This.aChromosomes = $aTemp
			$This.iPopulation -= 1
		Else
			$aTemp = $This.aChromosomes
			$aTemp.pFitness = ($This.iPopulation*$This.aChromosomes[$iChromosome].pFitness)+$This.iPopulation/Abs($iAnswer-$iValue)
			$This.aChromosomes = $aTemp
		EndIf
		Return $iValue
	EndFunc

	Func Genetics()
		Return 0
	EndFunc
#EndRegion

Func MyErrFunc()
  Msgbox(0,"AutoItCOM Test","We intercepted a COM Error !"    & @CRLF  & @CRLF & _
             "err.description is: " & @TAB & $oMyError.description  & @CRLF & _
             "err.windescription:"   & @TAB & $oMyError.windescription & @CRLF & _
             "err.number is: "       & @TAB & hex($oMyError.number,8)  & @CRLF & _
             "err.lastdllerror is: "   & @TAB & $oMyError.lastdllerror   & @CRLF & _
             "err.scriptline is: "   & @TAB & $oMyError.scriptline   & @CRLF & _
             "err.source is: "       & @TAB & $oMyError.source       & @CRLF & _
             "err.helpfile is: "       & @TAB & $oMyError.helpfile     & @CRLF & _
             "err.helpcontext is: " & @TAB & $oMyError.helpcontext _
            )
Endfunc