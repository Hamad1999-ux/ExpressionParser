from Cobra import parseVariableDeclaration,parseForLoop

######################################################

#                 Parsing Variables

######################################################

inputSTR = """string String = "-1.23e4";"""

varDataType, varName, varValue = parseVariableDeclaration(inputSTR)

print(f"Variable type  : {varDataType}")
print(f"Variable name  : {varName}")
print(f"Variable value : {varValue}")


######################################################

#                 Parsing For Loop

######################################################



inputSTR = """
for ( i = 0; i <= 10; i++) {
    
    int j = __HHH+1;
    print(j);
    
    }
"""

initializerDataType, initializerVariable, initializerValue, conditionVariable, conditionOperators, conditionValue, INCDECVariable,INCDECOperators, loopBody = parseForLoop(inputSTR)

print(f"Initializer DataType : {initializerDataType}")
print(f"Initializer Variable : {initializerVariable}")
print(f"Initializer Value    : {initializerValue}")

print(f"Condition Variable   : {conditionVariable}")
print(f"Condition Operators  : {conditionOperators}")
print(f"Condition Value      : {conditionValue}")


print(f"INC/DEC Variable     : {INCDECVariable}")
print(f"INC/DEC Operators    : {INCDECOperators}")

print(f"Loop Body: {loopBody}")
