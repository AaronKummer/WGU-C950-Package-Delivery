This Readme serves to satisfy the writing section of the assignment.
There are comments throughout the code that help explain logic, and attempt to calculate Big O
Screenshots of the program running are included folder

B1:
The packages are manually loaded into the trucks to simplify the sorting.
Truck three is assigned the 'problematic' or delayed packages, and leaves after truck 1 or 2 finishes.
The packages are then looped through one by one, and related to the addresses and distances data which is then stored in an array
The distance for each location from the current location is calculated, and the shorted location is then selected and traveled to
The package is then marked as delivered and removed from the truck upon reaching the next destination
This process is repeated until there are no more packages on the truck.

B2:
This program was written using visual studio code as a text editor.

B3: 
There comments in the code that attempt to evaluate the time complexity for most of the intensive methods

B4:
This solution is not very scalable or adaptable due to manually loading the trucks, and maybe some other hard coded data such as
the start time of the first two trucks. Other than that most of the code is dynamic and could be adapted to be more scalable with some refactoring

B5:
I do not believe this software is 'very' efficient; though I believe with some refactoring it could be made to be more so.
I tried to make it easy to contain by making the packages and trucks into actual objects rather than trying ot keep track of tuples.
The program also attemps to be modular by separating concerns into small methods.

B6: 
I believe that the algorithm itself is a strenght of the program. It is dynamic and straightforward; east to understand.
One of the downfalls of this program is that the code itself may be dense, particularly the time calculations and comparing 
time inputs that a user can type in to minutes passed in a day, compared to minutes elapsed in terms of an individual truck.

I1: 
One of the major strengths of the algorithm I used to find the nearest location for the next package to be delievered is its simplicity to understand the logic. It calculates the distances of all of the location from the current location, and delivers the package, and then repeats in a recursive fashion. Another strength of this algorithm is that it is easy to code... 
I initially thought to try a more iterative approach without using recursion, but this seemed easier for me to wrap my head around.

I3:
Dijkstra algorithm, A* search algorithm

J:
If I were to write this program again I would start with very abstract methods and think more 'object oriented'.
I got hung up on small details too soon, and that hindered me from thinking about the big picture.

K1a:
    The hash table has an insert and lookup function that work correctly and without
    any errors.

K1b:
    The hash table will continue to grow was the number of packages grow.

K1c: 
    The cities and distances between them are held in a graph. The lookup time there
    will remain O(1) as the number of cities grows. The space grows at O(n^2) as
    each city references the other.

K2a:  Linked list, priority queue

    A linked list's average lookup is O(n)
    its stored elements need to be iterated over in order to find the desired value. 
    If appending to the end of the list, insertion is O(n) 

    A priority queue could help simplify the delivery of packages by assigning a
    priority to the package before putting it in the queue. This could be done two
    ways:

    O(1) retrieval and O(n) insertion if elements are sorted at insertion time
    O(n) retrieval and O(1) insertion if elements are not sorted at insertion time
    













The assignment rubrick:

The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution
for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their
promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to
deliver each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in
the attached “WGUPS Package File,” will be delivered on time with the least number of miles added to the combined
mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map”
and distances to each location are given in the attached “WGUPS Distance Table.”

While you work on this assessment, take into consideration the specific delivery time expected for each package and the
possibility that the delivery requirements—including the expected delivery time—can be changed by management at any
time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be able
to see, at assigned points, the progress of each truck and its packages by any of the variables listed in
the “WGUPS Package File,” including what has been delivered and what time the delivery occurred.

The intent is to use this solution (program) for this specific location and to use the same program in many cities in each
state where WGU has a presence. As such, you will need to include detailed comments, following the industry-standard Python
style guide, to make your code easy to read and to justify the decisions you made while writing your program.


Assumptions:
1. Each truck can carry a maximum of 16 packages.
2. Trucks travel at an average speed of 18 miles per hour.
3. Trucks have a “infinite amount of gas” with no need to stop.
4. Each driver stays with the same truck as long as that truck is in service.
5. Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
   The day ends when all 40 packages have been delivered.
6. Delivery time is instantaneous, i.e., no time passes while at a delivery
   (that time is factored into the average speed of the trucks).
7. There is up to one special note for each package.
8. The wrong delivery address for package #9, Third District Juvenile Court, will be corrected
   at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
9. The package ID is unique; there are no collisions.
10. No further assumptions exist or are allowed.