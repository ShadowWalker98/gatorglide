from gatorglidedriver.driver import Driver
import sys
from internal.constants import *


def print_order(driver: Driver, order_id: int):
    driver.print_order(order_id)


def print_range(driver: Driver, time1: int, time2: int):
    driver.print_range(time1, time2)


def get_rank_of(driver: Driver, order_id: int):
    driver.get_rank_of(order_id)


def create_order(driver: Driver, order_id: int, current_sys_time: int, order_value: int, delivery_time: int):
    driver.create_order(order_id, current_sys_time, order_value, delivery_time)


def cancel_order(driver: Driver, order_id: int, current_sys_time: int):
    driver.cancel_order(order_id, current_sys_time)


def update_time(driver: Driver, order_id: int, current_sys_time: int, new_delivery_time: int):
    driver.update_time(order_id, current_sys_time, new_delivery_time)


def quit_gator_glide(driver: Driver):
    driver.quit_gator_glide()


def run_test_case_one():
    driver = Driver()
    driver.create_order(1001, 1, 200, 3)
    driver.create_order(1002, 3, 250, 6)
    driver.create_order(1003, 8, 100, 3)
    driver.create_order(1004, 13, 100, 5)
    driver.print_range(2, 15)
    driver.update_time(1003, 15, 1)
    driver.create_order(1005, 30, 300, 3)
    driver.quit_gator_glide()


def run_test_case_two():
    driver = Driver()
    driver.create_order(101, 2, 300, 4)
    driver.create_order(102, 3, 600, 3)
    driver.print_order(101)
    driver.create_order(103, 7, 200, 2)
    driver.create_order(104, 8, 500, 3)
    driver.cancel_order(102, 9)
    driver.create_order(105, 10, 300, 4)
    driver.get_rank_of(105)
    driver.quit_gator_glide()


def run_test_case_three():
    driver = Driver()
    driver.create_order(1001, 1, 100, 4)
    driver.create_order(1002, 2, 150, 7)
    driver.create_order(1003, 8, 50, 2)
    driver.print_range(2, 15)
    driver.create_order(1004, 9, 300, 12)
    driver.get_rank_of(1004)
    driver.print_range(45, 55)
    driver.create_order(1005, 15, 400, 8)
    driver.create_order(1006, 17, 100, 3)
    driver.cancel_order(1005, 18)
    driver.get_rank_of(1004)
    driver.create_order(1007, 19, 600, 7)
    driver.create_order(1008, 25, 200, 8)
    driver.update_time(1007, 27, 12)
    driver.get_rank_of(1006)
    driver.print_range(55, 85)
    driver.create_order(1009, 36, 500, 15)
    driver.create_order(1010, 40, 250, 10)
    driver.quit_gator_glide()


def run_test_case_four():
    driver = Driver()
    driver.create_order(3001, 1, 200, 7)
    driver.create_order(3002, 3, 250, 6)
    driver.create_order(3003, 8, 1000, 3)
    driver.create_order(3004, 13, 100, 5)
    driver.create_order(3005, 15, 300, 4)
    driver.create_order(3006, 17, 800, 2)
    driver.print_range(2, 20)
    driver.update_time(3004, 20, 2)
    driver.print_range(5, 25)
    driver.cancel_order(3005, 25)
    driver.print_range(10, 30)
    driver.create_order(3007, 30, 200, 3)
    driver.get_rank_of(3005)
    driver.create_order(3008, 33, 250, 6)
    driver.create_order(3009, 38, 100, 3)
    driver.create_order(3010, 40, 4000, 5)
    driver.get_rank_of(3008)
    driver.create_order(3011, 45, 300, 4)
    driver.create_order(3012, 47, 150, 2)
    driver.print_range(35, 50)
    driver.get_rank_of(3006)
    driver.quit_gator_glide()


def run_test_case_five():
    driver = Driver()
    driver.create_order(4001, 1, 200, 3)
    driver.create_order(4002, 3, 250, 6)
    driver.create_order(4003, 8, 100, 3)
    driver.create_order(4004, 13, 100, 5)
    driver.print_range(2, 15)
    driver.get_rank_of(4003)
    driver.update_time(4003, 15, 2)
    driver.create_order(4005, 17, 150, 4)
    driver.cancel_order(4002, 20)
    driver.create_order(4006, 22, 300, 3)
    driver.print_range(10, 25)
    driver.create_order(4007, 25, 200, 2)
    driver.create_order(4008, 28, 350, 5)
    driver.print_range(20, 30)
    driver.get_rank_of(4006)
    driver.create_order(4009, 32, 250, 3)
    driver.cancel_order(4004, 34)
    driver.update_time(4005, 37, 5)
    driver.create_order(4010, 40, 400, 6)
    driver.print_range(35, 45)
    driver.get_rank_of(4007)
    driver.create_order(4011, 40, 200, 4)
    driver.create_order(4012, 42, 300, 3)
    driver.print_range(50, 55)
    driver.update_time(4010, 55, 7)
    driver.cancel_order(4009, 56)
    driver.print_range(60, 90)
    driver.quit_gator_glide()


def init_command_map():
    command_dic = {CREATE_ORDER: create_order, UPDATE_TIME: update_time, GET_RANK: get_rank_of,
                   CANCEL_ORDER: cancel_order, QUIT: quit_gator_glide}
    return command_dic


if __name__ == "__main__":

    command_map = init_command_map()

    if len(sys.argv) != 2:
        print("Usage: python script.py input_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    arr = input_filename.split('.')
    w = open(arr[0] + "_output.txt", "w")

    driver = Driver(w)

    with open(input_filename, "r") as f:
        for line in f:
            stripped_line = line.strip()
            left_idx = stripped_line.find('(')
            right_idx = stripped_line.find(')')
            args_string = stripped_line[left_idx + 1:right_idx]
            args_list = args_string.split(',')
            args_int_list = [0 for i in args_list]

            for i in range(len(args_list)):
                stripped_arg = args_list[i].strip()
                args_int_list[i] = int(stripped_arg) if stripped_arg != '' else None

            command = stripped_line[: left_idx]
            # print(command)
            # print(args_int_list)

            if command == PRINT_ORDER:
                if len(args_int_list) == 2:
                    print_range(driver, *args_int_list)
                elif len(args_int_list) == 1:
                    print_order(driver, *args_int_list)
            elif command in command_map.keys():
                if command == QUIT:
                    quit_gator_glide(driver)
                else:
                    command_map[command](driver, *args_int_list)

    # run test cases by calling the corresponding function above
    # test 1 - o - passes
    # test 2 - o - passes
    # test 3 - o - passes
    # test 4 - o - passes
    # test 5 - o - passes
