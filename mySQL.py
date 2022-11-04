import mysql.connector
mydb = mysql.connector.connect(host="localhost",
user="root",
password="",
auth_plugin='mysql_native_password',
database = "RideShare")
#databse = "RideShare")
print(mydb)

# #create cursor obj to interact with mySQL
mycursor = mydb.cursor(buffered=True)
running = True
# #create the DB 
# mycursor.execute("CREATE SCHEMA RideShare;")
# #show the databases that exist in my local mySQL 

# mycursor.execute("Show databases;")
# for x in mycursor:
#     print(x)

today = '2022-11-02'

def driverOptions(id):
    choice = int(input("What would you like to do?\n1) Turn on Drive Mode\n2) Turn off Drive mode\n3) Return to Login\n"))
    if(choice == 1):
        print("Drive Mode is ON\n")
        turnOnDriveMode(id)
    elif(choice == 2):
        print("Drive Mode is OFF\n")
        turnOffDriveMode(id)
    elif(choice == 3):
        print("Returning to Login...")
    else:
        print("Invalid opttion")
def riderOptions(id):
    choice = int(input("What would you like to do?\n1) Find Driver\n2) Rate my Driver\n3) Return to Login\n"))
    if(choice == 1):
        print("Finding Driver...")
        findDriver(id)
    elif(choice == 2):
        print("Rating Driver...")
        rateDriver(id)
    elif(choice == 3):
        print("Returning to Login")
    else:
        print("Invalid option")

def showDriverTable():
    mycursor.execute("SELECT * FROM driver")
    myresult = mycursor.fetchall()
    for x in myresult: 
        print(x)

def showRiderTable():
    mycursor.execute("SELECT * FROM rider")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x) 
def showRideTable():
    mycursor.execute("SELECT * FROM rides")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def initializeDrivers():
    mycursor.execute("CREATE TABLE driver(DriverID INT NOT NULL PRIMARY KEY, Name VARCHAR(20), MemberSince DATE, Rating FLOAT, Vehicle VARCHAR(40), DriveMode INT);")

def initializeRiders():
    mycursor.execute("CREATE TABLE rider(RiderID INT NOT NULL PRIMARY KEY, Name VARCHAR(20), RidesTaken INT, Age INT);")

def initializeRides():
    mycursor.execute("CREATE TABLE rides(RideID INT NOT NULL PRIMARY KEY, Date DATE, PickupLocation VARCHAR(20), DropOffLocation VARCHAR(20), DriverRating FLOAT, DriverID INT, RiderID INT);")

def addDrivers(): #not on menu, just to fill data
    query = '''INSERT INTO driver(DriverID, Name, MemberSince, Rating, Vehicle, DriveMode) 
    VALUES(1, 'Rakesh', '2016-10-20', 4.5, 'Toyota Prius', 1);'''
    mycursor.execute(query)
    mydb.commit()
    query = '''INSERT INTO driver(DriverID, Name, MemberSince, Rating, Vehicle, DriveMode) 
    VALUES(2, 'Bob', '2022-09-20', 2.2, 'Tesla Model 3', 1);'''
    mycursor.execute(query)
    mydb.commit()
    query = '''INSERT INTO driver(DriverID, Name, MemberSince, Rating, Vehicle, DriveMode) 
    VALUES(3, 'Sammy', '2018-03-01', 3.9, 'Honda Civic', 0);'''
    mycursor.execute(query)
    mydb.commit()
    query = '''INSERT INTO driver(DriverID, Name, MemberSince, Rating, Vehicle, DriveMode) 
    VALUES(4, 'Chris', '2020-01-04', 5.0, 'Honda Accord', 1);'''
    mycursor.execute(query)
    mydb.commit()
    query = '''INSERT INTO driver(DriverID, Name, MemberSince, Rating, Vehicle, DriveMode) 
    VALUES(5, 'Alan', '2014-02-14', 2.5, 'Honda Oddysey', 0);'''
    mycursor.execute(query)
    mydb.commit()
def addRiders(): #not on menu, just to fill data
    mycursor.execute('''INSERT INTO rider(RiderID, Name, RidesTaken, Age) VALUES(99, 'Christopher', 0, 20);''')
    mydb.commit()
    mycursor.execute('''INSERT INTO rider(RiderID, Name, RidesTaken, Age) VALUES(98, 'Alan', 15, 19);''')
    mydb.commit()
    mycursor.execute('''INSERT INTO rider(RiderID, Name, RidesTaken, Age) VALUES(97, 'Jessica', 0, 22);''')
    mydb.commit()
    mycursor.execute('''INSERT INTO rider(RiderID, Name, RidesTaken, Age) VALUES(96, 'Samantha', 9, 25);''')
    mydb.commit()
    mycursor.execute('''INSERT INTO rider(RiderID, Name, RidesTaken, Age) VALUES(95, 'Justin', 4, 20);''')
    mydb.commit()
def addRide(id, driverID, pickup, dropoff): #adds ride to rides table 
    mycursor.execute("SELECT COUNT(*) FROM rides;")
    fetch = mycursor.fetchone()
    rideID = 100 + fetch[0]
    
    query = "INSERT INTO rides(RideID, Date, PickupLocation, DropOffLocation, DriverID, RiderID) VALUES(%d, '2022-11-02', '%s', '%s', %d, %d);" % (rideID, pickup, dropoff, driverID[0], int(id))
    #print(query)
    mycursor.execute(query)
    mydb.commit()
    #fetchone() returns one tuple, then take first index of tuple
    #tuple = fetchone(query) 
    #value = tuple[0]
    

def updateDriverRating(userRating):
    query = "UPDATE driver SET Rating = {rating} WHERE DriverID = 1;".format(rating = userRating) #upate driver rating based on ID 
    mycursor.execute(query)
    mydb.commit()

def turnOnDriveMode(id):
    query = "UPDATE driver SET DriveMode = 1 WHERE DriverID = "+id+";"
    mycursor.execute(query)
    mydb.commit()
def turnOffDriveMode(id):
    query = "UPDATE driver SET DriveMode = 0 WHERE DriverID = "+id+";"
    mycursor.execute(query)
    mydb.commit()
    print(id)

def rideOrDrive(id):
    #returns int for rider or driver 
    mycursor.execute("SELECT * FROM driver WHERE DriverID ="+id+";")
    driverProfile = mycursor.fetchall()
    role = ""
    try:
        print(driverProfile[0])
        role = "driver"
        driverOptions(id)
    except:
        pass
    if(role != "driver"):
        mycursor.execute("SELECT * FROM rider WHERE RiderID ="+id+";")
        driverProfile = mycursor.fetchall()
        
        try:
            print(driverProfile[0])
            role = "rider"
            riderOptions(id)
        except:
            print("User Not Found")
        
        

def findDriver(id):
    mycursor.execute("SELECT * FROM driver WHERE DriveMode = 1")
    myresult = mycursor.fetchall()
    count = 1
    for x in myresult:
        print(count,") ",end = '')
        print(x) 
        count += 1
    driverChosen = int(input("Which driver would you like? "))
    print(myresult[driverChosen-1],"is on the way!")
    mycursor.execute("SELECT DriverID FROM driver WHERE DriveMode = 1")
    driverID = mycursor.fetchall()
    idDriver = driverID[driverChosen-1]
    pickup = input("Where would you like to be picked up? ")
    drop = input("Where would you like to be dropped off? ")
    #print(idDriver[0])
    addRide(id, idDriver, pickup, drop)
    #send driver id

def rateDriver(id):
    rating = float(input("How would you rate your driver out of 5? "))
    query = "SELECT DriverID FROM rides WHERE RiderID = %s;" % id
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    #print(myresult[0])
    driverIden = myresult[0]
    query = "SELECT Rating FROM driver WHERE DriverID = 3;"
    mycursor.execute('''SELECT Rating FROM driver WHERE DriverID = 3;''')
    myresult = mycursor.fetchone()
    curRating = myresult[0]
    #print(curRating)
    newRating = (curRating + float(rating) ) / 2
    print("New Rating:",newRating)
    mycursor.execute('''UPDATE driver SET Rating = %.1f WHERE DRIVERID = %d;''' % (newRating, driverIden))
    mydb.commit()
    
    #RATING + RATING INPUT / 2 
    #UPDATE DRIVER SET DRIVER RATING = RATING + RATING /2 
#NOW = TODAYS DATE? 
    # if rider, give them options;
        # find driver, matches them with driver that has drive mode on 
        # rider can provide PICKUP INFO, DROP OFF LOCATION 
        # provide rider with RIDE ID 
        # go back to main menu

        # rate my driver
            # rider provides own ID and desired rating /5 
            # look up the rider's last ride and get driver ID 
            # calculate new driver's rating and take current rating + new rating and divide by 2 


# mycursor.execute('''INSERT INTO driver(DriverID, Rating) 
#                     VALUES(1, 3.9);''')


#IDEA make ten of each for driver and rider. do ID's based from 1-10, then 99-90 for other
#initialize all of these in the database and then make functions to make rides 
#
#mycursor.execute('''INSERT INTO rider(RiderID, Name, RidesTaken, Age) VALUES(99, 'Christopher', 0, 20);''')

#addRide()

while(running):
    uberID = input("Please enter your Uber ID: \nOr Type 'q' to quit\n")
    if(uberID == 'q'):
        break
    rideOrDrive(uberID) #check for rider or driver
mydb.close()

#README WHEN YOU GET BACK:
#when making the entry for the ride, make sure you just take parameters of everything you need
#so keep track of things like ID's, location names, etc 
#then just do the same query and use all parameters as inputs 