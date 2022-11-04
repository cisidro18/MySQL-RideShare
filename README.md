# Assignment1-OS
* CPSC 408 MySQL & Python Ride Share App

# Identifying Information
* Name: Christopher Isidro
* Student ID: 2370110
* Email: cisidro@chapman.edu
* Course: CPSC_408 Database Management
* Assignment: MySQL & Python Ride Share App
* Collaborators: Christopher Isidro

# Source Files
* Cisidro_RideShare.zip
    * README.md
    * mySQL.py
    * RideShare.sql

# References
* w3schools.com for reference  
* stackoverflow for buffering set to true on cursor

# Known Errors
* Was having issues with rate driver function, something went wrong with executing 
  queries, but I think it was due to too many executed queries very close together.
  I added a buffer argument for the cursor, which was mentioned in references.
* There is no error handling, only for ID's that don't exist.
* I have driver rating in the "rides" table but didn't have time to implement it. It would be different
  from the overall rating.

# Build Instructions
* python3 mySQL.py
