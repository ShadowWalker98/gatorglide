

def print_order(order_id: int):
    # print information about the order with orderId = order_id
    # output format: [orderId, currentSystemTime, orderValue, deliveryTime, ETA]
    print("order Id: " + str(order_id))


def print_range(time1: int, time2: int):
    # prints information of all the orders that will be delivered within the given times (including both times)
    # these orders include only UNDELIVERED orders. The format is as follows:
    # if orders exist [orderId1, orderId2, .........], There are no orders in that time period if none
    print("time1: " + str(time1))
    print("time2: " + str(time2))


def get_rank_of(order_id: int):
    # prints how many orders will be delivered before it in the following format:
    # Order {orderId} will be delivered after {numberOfOrders} orders
    print(get_rank_of.__qualname__)


def create_order(order_id: int, current_sys_time: int, order_value: int, delivery_time: int):
    # creates the order, prints the ETA, and also prints which previously unfulfilled orders have been delivered
    # along with their delivery times. Output format is as follows:
    # Order {orderId} has been created - ETA: {ETA}
    # Updated ETAs: [orderId1: ETA, orderId2: ETA,.........] if any ETAs have been updated
    # Order {orderId} has been delivered at time {ETA} for all such orders if they exist, each in a new line
    print(create_order.__qualname__)


def cancel_order(order_id: int, current_sys_time: int):
    # cancels the order and updates the ETA of all the orders with lower priority
    # output format:
    # Order {orderId} has been canceled
    # Updated ETAs: [orderId1: ETA, orderId2: ETA, .........] if any ETAs have been updated
    # or
    # Cannot cancel. Order {orderId} has already been delivered
    # if the order is out for delivery or is already delivered
    print(cancel_order.__qualname__)


def update_time(order_id: int, current_sys_time: int, new_delivery_time: int):
    # takes the current system time, order_id and the new delivery time. It updates the ETAs of all the orders with
    # lower priority
    # Output format: Updated ETAs: [orderId1: ETA, orderId2: ETA, .........] if any ETAs have been updated
    # or
    # Cannot update. Order {orderId} has already been delivered if the order is out for delivery or is already
    # delivered
    print(update_time.__qualname__)


def quit_program():
    # close the file writer and quit the program
    exit(0)
