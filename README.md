# ASSIGNMENT - 3b
## Question 1 -
- Assumptions:
    - `org.json` file to be in the same directory as in `q1.py`.
    - Employee Id to be string, strating from 001.
    - Level 0 employee has no leader.
    - Levels are given as L0 , L1 ...
- Changes from Part A:
    - In Part a, there were 2 sets of variable to store parents level and name , and employee's name and level. Here elements and their levels are stored in lists.
    - Min level is calculated, if min level is 0 then `No leader`, else parent of each element at min level is derived from `org.json` and checked if parent same or not.
    - If parents are still different then one level above parent of each elements is matched until a common leader is found.

## Question 2 -
- Assumptions:
    - Input file will be `date_calculator.txt` file, having 2 Input lines.
    - If input date format is anything other than the format `1st October,1999` or `1st Oct, 1999` then command line argument will be given specifying the date format. And in this case the format for both the dates will be same.
    - Example format of Input is 
        * Date1: 01/08/2012 
        * Date2: 30th September, 2020
    - Output will be in a `output.txt` file.
    - Both Input and Output file will be in the same directory as `q2.py`.
    - Output will be in the form of :
        * Date Difference:425 Days
    - Following Date formats are allowed :
        * 1st October, 1999
        * 1st Oct, 1999
        * dd/mm/yyyy
        * mm/dd/yyyy
        * dd-mm-yyyy
        * mm-dd-yyyy
        * dd.mm.yyyy
        * mm.dd.yyyy
- Changes from Part A:
    - Line 1 `import sys` to fetch command line arguments.
    - If `len(sys.argv) == 2` then date format is specified, else not.
    - In the `DateFormat` function, an extra parameter is added to mention format of the date.
    - Added lines to handle formats :
        * mm/dd/yyyy
        * mm-dd-yyyy
        * mm.dd.yyyy

## Question 3-
- Assumptions-
    - Input busy slots are sorted and contains time between `9:00AM to 5:00PM`.
    -All input files `Employee*.txt` will be inside the same directory as of `q3.py`.
    - `Slot Duration` will be available through user input.
    - Output will in `output.txt` file.
    - Output will contain available slots for each employee, slot duration and common available slot.
    - If there is no common available slot then output will be `No common slot available`.
- Changes from Part A-
    - Imported `glob` to get a list of all files as `Employee*.txt`.
    - Made `open_files` function which stores file descriptors in a list and also loads and returns json of input files in a list `data`.
    - Added `availableSlot` function which returns available slot for each employee.
    - Added `slotAvail` function which returns a list of available slot having hours more than or equal to `slot_duration`.
    

## GitHub Repository - 
https://github.com/ayushipandey5/SSD_Assignment3a
