#AutoIt3Wrapper_Change2CUI=y
OnAutoItExitRegister("__cleanup")
#include 'Include/OOPE.au3'
#include <Array.au3>
$oMyError = ObjEvent("Autoit.Error","MyErrFunc")



Dim $aInstructionSet[2] = ["StringIsInt($sGVal)","_isOperator($sGVal)"]
Dim $aKey[14] = ["0", "1", "2", "3", "4", "5","6","7","8","9","+","-","*","/"]
Dim $aLengthRange[5] = [0,1,2,3,4]
Dim $aRangeSet[2] = [0,1]
#forcedef $oPopulation
If UBound(Execute("$oPopulation")) Then
	For $n = 0 To UBound(Execute("$oPopulation"))-1
		$oPopulation[$n] = __OOPE_InstantiateClass("int64 iPopulation;int64 aInstructionSet;int64 aKey;int64 aChromosomes;int64 aAnswers;int64 aChromosomes", "PopulationInitialize int64(int64,int64,int64,int64,int64,int64);PDecode int64(int64,int64);Genetics int64()", Default, Default)
	Next
Else
	$oPopulation = __OOPE_InstantiateClass("int64 iPopulation;int64 aInstructionSet;int64 aKey;int64 aChromosomes;int64 aAnswers;int64 aChromosomes", "PopulationInitialize int64(int64,int64,int64,int64,int64,int64);PDecode int64(int64,int64);Genetics int64()", Default, Default)
EndIf

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
Func PopulationInitialize($___selfObjRef,$iPopulation,$aInstructionSet,$aKey,$aLengthRange,$aRangeSet,$iGLength)
$This = DllStructCreate(__PointerToString(DllStructCreate($__OOPE_ObjectInstanceVariables, $___selfObjRef).psVarsString), $___selfObjRef + $__OOPE_ObjectVariableOffset)

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
Func PDecode($___selfObjRef,$iChromosome,$iAnswer)
$This = DllStructCreate(__PointerToString(DllStructCreate($__OOPE_ObjectInstanceVariables, $___selfObjRef).psVarsString), $___selfObjRef + $__OOPE_ObjectVariableOffset)

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
Func Genetics($___selfObjRef)
$This = DllStructCreate(__PointerToString(DllStructCreate($__OOPE_ObjectInstanceVariables, $___selfObjRef).psVarsString), $___selfObjRef + $__OOPE_ObjectVariableOffset)

		Return 0
	
EndFunc


Func __cleanup()

#forcedef $oPopulation

If UBound(Execute("$oPopulation")) Then
	For $n = 0 To UBound(Execute("$oPopulation"))-1
	$oPopulation[$n] = 0
	Next
Else
	$oPopulation = 0
EndIf
EndFunc
