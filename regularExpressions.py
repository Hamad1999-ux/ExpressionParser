
patternValidVariable = r'^(int|float|string|bool)\s+([a-zA-Z_]\w*)\s*=\s*(.+)\s*;$'
patternDataType      = r"int|float|string|bool"
patternVariableName  = r"^[a-zA-Z_]\w*$"
patternBool          = r"true|false"
patternInt           = r'^[+-]?\d+$'
patternFloat         = r'^[+-]?\d*\.?\d+(?:[eE][+-]?\d+)?$'
patternString        = r'^\".*\"$'
reservedWords        = set(['int', 'float', 'string', 'bool','for','if','while'])
forLoopRE            = r"for\s*\(\s*(.+)\s+(.+)\s*=\s*(\d+)\s*;\s*(.+)\s+([<>=!]+)\s+(\w+)\s*;\s*(.+)\s*([+-]{2})\s*\)\s*{(.*)}"
