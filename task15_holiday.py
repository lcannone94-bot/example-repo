# ======== TASK 15 HOLIDAY USER-DEFINED FUNCTION ========

# Define functions for calculating the plane cost, hotel cost, rental cost and holiday cost.
def plane_cost(city_flight) :
    ''' 
    Calculate the cost of the hotel

    Parameters :
    city of destination of the trip from the plane price dictionary (str)

    Returns
    float : price of the flight
    '''
    plane_price[city_flight]
    return(plane_price[city_flight])

def hotel_cost(num_nights) :
    ''' 
    Calculate the cost of the hotel

    Parameters :
    number of nights (float).

    Returns
    float : the total cost of the hotel
    '''
    total = hotel_price[city_flight] * num_nights
    return(total)

def rental_cost(rental_days) :
    ''' 
    Calculate the cost of renting a car

    Parameters :
    number of rental day (float).

    Returns
    float : the total cost of the hotel
    '''

    total = rental_price[city_flight] * rental_days
    return(total)

def total_holiday_cost(num_nights, city_flight, rental_days) :
    ''' 
    Calculate the total holiday cost

    Parameters :
    number of nights (float)
    city flight (str)
    rental days (float)

    Returns
    float : the total cost of the holiday
    '''

    total = plane_cost(city_flight) + hotel_cost(num_nights) + rental_cost(rental_days)
    return(total)

# Define list of prices for each destination. Flight cost per destination
plane_price = {"Rome" : 200.0,
               "Zurich" : 350.0,
               "London" : 250.0,
               "New York" : 1200.0,
               "Tokyo" : 1500.0
}


# Hotel price per night per destination
hotel_price = {"Rome" : 40.0,
               "Zurich" : 80.0,
               "London" : 65.5,
               "New York" : 120.4,
               "Tokyo" : 90.0
}

# rental price per night per destination
rental_price = {"Rome" : 10.5,
               "Zurich" : 20.4,
               "London" : 32.3,
               "New York" : 45.8,
               "Tokyo" : 120.5

}

# define destination variable. This variable is used to shown the list of destinations to the user.
destinations = ""

# I use the keys of plane_price dictionary as reference list of the destinations.

for i in plane_price.keys() :
    destinations += i + "\n"

print(f"Please pick one of the available destinations : {"\n" + destinations}")


# Ask user to enter the destination, number of nights and rental days
enter_city = input("Please enter the city where you want to go :")
if enter_city in plane_price.keys() : 
    city_flight = enter_city

    num_nights = float(input("Please enter the number of nights you will be staying at the hotel : "))

    # set a limit for the numbers of day entered. A user cannot enter a negative number, 0 or a number higher than 50.
    if num_nights < 50 and num_nights > 1 :

        rental_days = float(input("Please enter number of days for which you will be hiring a car : "))
        if rental_days < 50 and rental_days > 1 :
            
            total_plane_cost = round(plane_cost(city_flight),2)
            total_hotel_cost = round(hotel_cost(num_nights),2)
            total_rental_cost = round(rental_cost(rental_days),2)
            total_holiday_cost = round((total_holiday_cost(num_nights,city_flight, rental_days)),2)

            # print total cost of holiday with relative breakdown
            print(f"The cost of the flight to go to {city_flight} is {total_plane_cost}")
            print(f"The cost of the hotel in {city_flight} is {total_hotel_cost} - the hotel price per night is {hotel_price[city_flight]}")
            print(f"The cost of the renting a car in {city_flight} is {total_rental_cost} - the rental price per day is {rental_price[city_flight]}")
            print(f"The total cost of the holiday is {total_holiday_cost}")

        else :
             print ("Invalid number of days")
    else :
        print("Invalid number of days. There is no availability for the days entered")       
else :
    print("We are sorry! This city is not an available option")


# ======= END OF THE CODE ========