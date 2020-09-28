windspeed=float(input("Wind speed in miles per hour please:"))

if windspeed<1.0:
    print("Calm")
elif windspeed>=1 and windspeed<12:
    print("Gentle breeze")
elif windspeed>=12 and windspeed<30:
    print("Strong breeze")
elif windspeed>=30 and windspeed<46:
    print("Gale")
elif windspeed>=46 and windspeed<63:
    print("Storm")
elif windspeed>=63 and windspeed<74:
    print("Violent storm")
elif windspeed>=74:
    print("Hurricane force")
