from collections import namedtuple

"""
Track Nadia drivers car type, driver name and capacity as tuple

"""


def can_take_order(driver, num_package):
    return driver.car_capacity >= num_package


def main():
    # add code here
    # create a driver with a name, car type, and car capacity
    # an example you can use to practice: "Iris", "Toyota Prius", 7
    # check if they can take a certain order, given their car's capacity.
    drivers_info = namedtuple("Driver", ["Name", "car_type", "car_capacity"])
    d001 = drivers_info("Iris", "Toyota Prius", 7)
    print(can_take_order(d001, 10))
    return None


if __name__ == "__main__":
    main()
