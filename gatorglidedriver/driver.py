from collections import deque

from internal.avlimpl.avltree import AvlTree
from internal.constants import BRANCH_PRIORITY, BRANCH_EST_TOA
from internal.order.order import Order
from queue import Queue


class Driver:
    def __init__(self):
        self.eta_avl_tree = AvlTree(BRANCH_EST_TOA)
        self.priority_avl_tree = AvlTree(BRANCH_PRIORITY)
        self.order_eta_node = {}
        self.order_priority_node = {}
        self.updated_order_info = {}

    def print_order(self, order_id: int):
        # print information about the order with orderId = order_id
        # output format: [orderId, currentSystemTime, orderValue, deliveryTime, ETA]
        # TODO: update this to pull from updated_order_info dictionary instead
        # TODO: update to also use the mapped order_eta_node so that we can directly fetch instead of searching
        order_info = self.eta_avl_tree.get_order_info(order_id)
        self.print_order_info_helper(order_info)

    def print_range(self, time1: int, time2: int):
        # prints order_ids of all the orders that will be delivered within the given times (including both times)
        # these orders include only UNDELIVERED orders. The format is as follows:
        # if orders exist [orderId1, orderId2, .........], There are no orders in that time period if none

        # search in the eta tree and get the order ids which lie within this time frame
        order_list = self.eta_searcher(time1, time2)
        if len(order_list) == 0:
            print("There are no orders in that time period")
        else:
            ans_str = "["
            for i, val in enumerate(order_list):
                if i == len(order_list) - 1:
                    ans_str += str(order_list[i])
                else:
                    ans_str += str(order_list[i]) + ","
            ans_str += "]"
            print(ans_str)

    def get_rank_of(self, order_id: int):
        # prints how many orders will be delivered before it in the following format:
        # Order {orderId} will be delivered after {numberOfOrders} orders
        node, eta = self.eta_avl_tree.get_order_info(order_id)
        if node is None:
            return 0
        order_list = self.get_rank_order_helper(eta)
        print("Order {} will be delivered after {} orders".format(order_id, len(order_list)))

    def create_order(self, order_id: int, current_sys_time: int, order_value: int, delivery_time: int):
        # creates the order, prints the ETA, and also prints which previously unfulfilled orders  been delivered
        # along with their delivery times. Output format is as follows:
        # Order {orderId} has been created - ETA: {ETA}
        # Updated ETAs: [orderId1: ETA, orderId2: ETA,.........] if any ETAs have been updated
        # Order {orderId} has been delivered at time {ETA} for all such orders if they exist, each in a new line

        # we first get the current system time which is used to determine which orders have been finished
        delivered_orders = self.get_delivered_orders(current_sys_time)
        for (order_eta, delivered_order) in delivered_orders:
            self.eta_avl_tree.delete_node(delivered_order, False)
        # we do this by checking the eta tree for nodes which have val < current system time and delete these nodes
        # from the eta tree.
        # we also remove these order ids from the priority tree as well
        # we then find the order which is supposed to be delivered before the one which was created now
        # we do this by first checking the priority tree and seeing which order has the least priority which is
        # greater than the created order's priority
        # if there is more than one order then we would have to search in the eta tree to find the order which has
        # the highest eta out of all of them
        # we then use the eta we found to calculate the eta of the created order
        # we then find the orders which have lower priority and then update their etas
        # after this we add the created order to the priority tree and the eta tree

        print(self.create_order.__qualname__)

    def cancel_order(self, order_id: int, current_sys_time: int):
        # cancels the order and updates the ETA of all the orders with lower priority
        # output format:
        # Order {orderId} has been canceled
        # Updated ETAs: [orderId1: ETA, orderId2: ETA, .........] if any ETAs have been updated
        # or
        # Cannot cancel. Order {orderId} has already been delivered
        # if the order is out for delivery or is already delivered
        print(self.cancel_order.__qualname__)

    def update_time(self, order_id: int, current_sys_time: int, new_delivery_time: int):
        # takes the current system time, order_id and the new delivery time. It updates the ETAs of all the orders with
        # lower priority
        # Output format: Updated ETAs: [orderId1: ETA, orderId2: ETA, .........] if any ETAs have been updated
        # or
        # Cannot update. Order {orderId} has already been delivered if the order is out for delivery or is already
        # delivered
        print(self.update_time.__qualname__)

    @staticmethod
    def quit_program():
        # close the file writer and quit the program
        exit(0)

    def print_order_info_helper(self, order_details: Order) -> str:
        return ("[" + str(order_details.order_id)
                + ", " + str(order_details.current_sys_time)
                + ", " + str(order_details.order_value)
                + ", " + str(order_details.delivery_time) + ", "
                + str(order_details.est_toa)
                + "]")

    def eta_searcher(self, time1: int, time2: int) -> list[int] | None:
        node = self.eta_avl_tree.root
        order_list = []

        if node is None:
            return None

        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()
            if time1 <= node.val <= time2:
                keys = node.order_info.keys()
                for key in keys:
                    order_list.append(node.order_info[key])
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return order_list

    def get_rank_order_helper(self, eta: int) -> list[int]:
        node = self.eta_avl_tree.root
        if node is None:
            return 0

        order_list = []
        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()
            if node.val < eta:
                for key in node.order_info.keys():
                    order_list.append(key)
            if node.left is not None and node.left.val < eta:
                queue.append(node.left)
            if node.right is not None and node.right.val < eta:
                queue.append(node.right)
        return order_list

    def get_delivered_orders(self, current_sys_time: int) -> list[(int, Order)]:
        node = self.eta_avl_tree.root
        if node is None:
            return 0

        delivered_orders = []
        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()
            if node.val <= current_sys_time:
                for key in node.order_info.keys():
                    delivered_orders.append((key, node.order_info[key]))
            if node.left is not None and node.left.val < current_sys_time:
                queue.append(node.left)
            if node.right is not None and node.right.val < current_sys_time:
                queue.append(node.right)
        return delivered_orders



