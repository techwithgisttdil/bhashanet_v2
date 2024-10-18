import re

def regex_check(input_field, regex_pattern):
  print("REGEX PATTERN : ",regex_pattern)
  pattern = re.compile(regex_pattern)
  
  # VALIDATING STRING WITH PATTERN
  valid_input = re.fullmatch(pattern, input_field)
  print("CHECKING VALIDATION RESULT : " , valid_input)
    
  if not valid_input:
    return False
  else:
    return True 