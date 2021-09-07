def convert_celsius(celsius):

    c = float(celsius)
    f = c * 9 / 5 + 32
    k = c + 273.5
    print ('{0} Celsius, converted to Fahrenheit, is: {1} Fahrenheit.' .format (c, f))
    print ('{0} Celsius, converted to Kelvin, is: {1} Kelvin.' .format (c, k))



def convert_farenheit(fahrenheit):

    f = float(fahrenheit)
    c = (f - 32) * 5 / 9
    k = 273.5 + ((f - 32.0) * (5.0/9.0))
    print ('{0} Farenheit, converted to Celsius, is: {1} Fahrenheit.' .format (f, c))
    print ('{0} Farenheit, converted to Kelvin, is: {1} Fahrenheit.' .format (f, k))


def convert():
    
    print("Please select operation -\n" \
        "celsius\n" \
        "farenheit\n" )
    user_input = input('From what do you want to convert?: ')
    
    if user_input == 'celsius':
        print ('To convert a temperature from Celsius ')
        cels = input('CELSIUS: ')
        convert_celsius(cels)

    elif user_input == 'farenheit':
        print ('To convert a temperature from Fahrenheit ')
        fahr = input('FAHRENHEIT: ')
        convert_farenheit(fahr)


convert()
  
