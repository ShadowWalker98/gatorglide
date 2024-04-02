from internal.helpers import *


class Order:

    def __init__(self, order_id, current_sys_time, order_value, delivery_time, est_toa):
        self.order_id = order_id
        self.current_sys_time = current_sys_time
        self.order_value = order_value
        self.delivery_time = delivery_time
        self.est_toa = est_toa
        self.priority = self.__calculate_order_priority()

    def __calculate_order_priority(self):
        return get_priority(self.order_value, self.current_sys_time)

