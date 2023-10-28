def convert_units(input_unit, output_unit, value):  
  """Converts a value from one unit to another.  
    Args:    
      input_unit: The input unit.    
        output_unit: The output unit.    
        value: The value to be converted.  
          Returns:     The converted value.
              """  
  if input_unit == 'C' and output_unit == 'F':    
     return value * 9 / 5 + 32  
  elif input_unit == 'F' and output_unit == 'C':  
      return (value - 32) * 5 / 9  
  elif input_unit == 'm' and output_unit == 'ft':    
    return value * 3.28084  
  elif input_unit == 'ft' and output_unit == 'm':    
    return value / 3.28084
  elif input_unit == 'kg' and output_unit == 'lb':    
    return value * 2.20462
  elif input_unit == 'lb' and output_unit == 'kg':    
     return value / 2.20462
     
  else:    
     raise ValueError('Invalid unit conversion')
  def main():  
    """Prompts the user to enter the input unit, the output unit, and the value   to be converted, and then performs the conversion and displays the result."""
    input_unit = input('Enter the input unit: ')  
    output_unit = input('Enter the output unit: ')  
    value = float(input('Enter the value to be converted: '))  
    result = convert_units(input_unit, output_unit, value)  
    print(f'{value} {input_unit} = {result} {output_unit}')
    if __name__ == '__main__':   main()