# Products

* ProductID (Autonumber)
* Brand (Short Text)
* Name (Short Text)
* Description (Long Text)
* Quantity (Number)
* Retail Price (Currency)

# Workers

* WorkerID (Autonumber)
* Phone (Number)
* First Name (Short Text)
* Second Name (Short Text)
* Third Name (Short Text)
* Hourly Rate (Currency)
* Start Date (Date/Time)
* Job Description (Long Text)
* Shift (Lookup)


# OrderProduct

* OrderProductID (AutoNumber)
* OrderID [Lookup]
* ProductID [Lookup]


# Orders

* OrderID (Autonumber)
* Date (DateTime)
* Worker (Lookup)

# Shifts

* ShiftID (Autonumber)
* ShiftName (Short Text)
