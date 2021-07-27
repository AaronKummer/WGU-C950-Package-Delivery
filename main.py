# Aaron Kummer   Student ID: 000819874
from delivery_package import DeliveryPackage
from package_delivery_service import PackageDeliveryService

class Main:
    print("WGUPS Delivery service")
    package_delivery_service = PackageDeliveryService()
    main_selection = input("1 to see all statuses of packages for a given time \n2 to see the status of a particular package for a given time \n")
    if (main_selection == '1'):
        time_input = input("Please enter a time as hours:minutes am/pm, example '8:30 am' \n")
    if (main_selection == '2'):
        package_id_input = input("Please enter a package id: 1-40")
        if (int(package_id_input) in range (1,40)):
        # time_input = input("Please enter a time as hours:minutes am/pm, example '8:30 am' \n")
            package = package_delivery_service.get_package_status_at_time(int(package_id_input), "test")
            # print(package.transits)
        else:
            print("that is not a valid package id")

    

    

