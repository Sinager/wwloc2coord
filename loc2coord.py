''
MAIDENHEAD LOCATOR TO DECIMAL LAT/LON CONVERTER
based on the excellent explaination by M0NWK
https://www.m0nwk.co.uk/how-to-convert-maidenhead-locator-to-latitude-and-longitude/
2023 Stefano Sinagra IZ0MJE
released under GNU/GPL conditions
''

locator = "jn61fu"

# LATITUDE 
lata =(ord(locator[1].upper())-65)*10
latb =int(locator[3])
latc =(ord(locator[5].lower())-97)/24+(1/48)-90
latitude = lata + latb + latc

#LONGITUDE
lona =(ord(locator[0].upper())-65)*20
lonb =int(locator[2])*2
lonc =(ord(locator[4].lower())-97)/12+(1/24)
longitude = (lona + lonb + lonc) -180


print("Latitude: ", end="")
print(latitude)
print("Longitude: ", end="")
print(longitude) 
