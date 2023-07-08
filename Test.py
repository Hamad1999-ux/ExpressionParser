import re

patternValidVariable = r'^(int|float|string|bool)\s+([a-zA-Z_]\w*)\s*=\s*(.+)\s*;$'
patternDataType      = r"int|float|string|bool"
patternVariableName  = r"^[a-zA-Z_]\w*$"
patternBool          = r"true|false"
patternInt           = r'^[+-]?\d+$'
patternFloat         = r'^[+-]?\d*\.?\d+(?:[eE][+-]?\d+)?$'
patternString        = r'^\".*\"$'
reservedWords        = set(['int', 'float', 'string', 'bool','for','if','while'])
forLoopRE            = r"for\s*\(\s*(.+)\s+(.+)\s*=\s*(\d+)\s*;\s*(.+)\s+([<>=!]+)\s+(\w+)\s*;\s*(.+)\s*([+-]{2}|[+-]\=\d+)\s*\)\s*{(.*)}"




def parseForLoop(code):

    match = re.search(forLoopRE, code,flags=re.DOTALL)

    if not match:
        print("Error : Syntax Error :(")
        return "", "", "", "","","","","",""

    initializerDataType,initializerVariable, initializerValue, conditionVariable, conditionOperators,conditionValue, INCDECVariable, INCDECOperators, loopBody = match.groups()

    match = re.search(r"int", initializerDataType)
    if not match:
        print("Error : Invalid initializer data type :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternVariableName, initializerVariable.strip())
    if not match or initializerVariable.strip()  in reservedWords:
        print("Error : Invalid initializer variable name :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternVariableName, conditionVariable.strip())
    if not match or conditionVariable.strip()  in reservedWords:
        print("Error : Invalid condition variable name :(")
        return "", "", "", "","","","","",""

    match = re.search(patternVariableName, INCDECVariable.strip())
    if not match or INCDECVariable.strip()  in reservedWords:
        print("Error : Invalid inc/dec variable name :(")
        return "", "", "", "","","","","",""
    
    if initializerVariable.strip() != conditionVariable.strip() or initializerVariable.strip() != INCDECVariable.strip():
        print("Error : initializer variable name,condition variable name and inc/dec variable name dont match  :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternInt, initializerValue)
    if not match:
        print("Error : Initializer Value is an invalid integer literal :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternInt, conditionValue)
    if not match:
        print("Error : Condition Value is an invalid integer literal :(")
        return "", "", "", "","","","","",""

    if conditionOperators not in ['!=', '<', '<=', '>', '>='] :
        print("Error : Invalid Condition Operator :(")
        return "", "", "", "","","","","",""


    return initializerDataType,initializerVariable,initializerValue, conditionVariable ,conditionOperators, conditionValue, INCDECVariable,INCDECOperators, loopBody



inputSTR = """
for (int i = 0; i <= 10; i=-1000) {
    
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
