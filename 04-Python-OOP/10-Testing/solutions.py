# # # Lab


# # 01. Test Worker
#
# from unittest import TestCase, main
#
#
# class WorkerTests(TestCase):
#
#     def test_worker_is_initialized_correctly(self):
#         worker = Worker('Test', 1000, 60)
#         self.assertEqual('Test', worker.name)
#         self.assertEqual(1000, worker.salary)
#         self.assertEqual(60, worker.energy)
#         self.assertEqual(0, worker.money)
#
#     def test_worker_works(self):
#         worker = Worker('Test', 1000, 60)
#         self.assertEqual(0, worker.money)
#         self.assertEqual(60, worker.energy)
#         worker.work()
#         current_expected_money = 1000
#         expected_energy = 60 - 1
#         self.assertEqual(current_expected_money, worker.money)
#         self.assertEqual(expected_energy, worker.energy)
#         worker.work()
#         current_expected_money = 1000 + 1000
#         self.assertEqual(current_expected_money, worker.money)
#         expected_energy = 60 - 1 - 1
#         self.assertEqual(expected_energy, worker.energy)
#
#     def test_worker_has_no_energy_can_not_work(self):
#         worker = Worker('Test', 1000, 0)
#         with self.assertRaises(Exception) as ex:
#             worker.work()
#         self.assertEqual('Not enough energy.', ex.exception.args[0])
#
#     def test_worker_can_not_work_with_negative_energy(self):
#         worker = Worker('Test', 1000, -1)
#         with self.assertRaises(Exception) as ex:
#             worker.work()
#         self.assertEqual('Not enough energy.', ex.exception.args[0])
#
#     def test_worker_energy_is_increased_when_worker_rests(self):
#         worker = Worker('Test', 1000, 60)
#         self.assertEqual(60, worker.energy)
#         worker.rest()
#         self.assertEqual(61, worker.energy)
#         worker.rest()
#         self.assertEqual(62, worker.energy)
#
#     def test_get_info(self):
#         worker = Worker('Test', 1000, 60)
#         result = worker.get_info()
#         expected_result = 'Test has saved 0 money.'
#         self.assertEqual(expected_result, result)
#         worker.work()
#         result = worker.get_info()
#         expected_result = 'Test has saved 1000 money.'
#         self.assertEqual(expected_result, result)
#
#
# if __name__ == '__main__':
#     main()


# # 02. Test Cat
# from unittest import TestCase, main
#
#
# class CatTests(TestCase):
#
#     def setUp(self) -> None:
#         self.cat = Cat('Test')
#
#     def test_initialize_cat(self):
#         self.assertEqual('Test', self.cat.name)
#         self.assertFalse(self.cat.fed)
#         self.assertFalse(self.cat.sleepy)
#         self.assertEqual(0, self.cat.size)
#
#     def test_cat_eats(self):
#         self.assertFalse(self.cat.fed)
#         self.assertFalse(self.cat.sleepy)
#         self.assertFalse(0, self.cat.size)
#         self.cat.eat()
#         self.assertTrue(self.cat.fed)
#         self.assertTrue(self.cat.sleepy)
#         self.assertEqual(1, self.cat.size)
#
#     def test_cat_has_eaten_raises(self):
#         self.assertFalse(self.cat.fed)
#         self.assertFalse(self.cat.sleepy)
#         self.assertFalse(0, self.cat.size)
#         self.cat.eat()
#         with self.assertRaises(Exception) as ex:
#             self.cat.eat()
#         self.assertEqual('Already fed.', str(ex.exception))
#         self.assertEqual('Already fed.', str(ex.exception))
#         self.assertTrue(self.cat.fed)
#         self.assertTrue(self.cat.sleepy)
#         self.assertEqual(1, self.cat.size)
#
#     def test_cat_tries_to_sleep_cat_is_not_fed_raises(self):
#         self.assertFalse(self.cat.fed)
#         self.assertFalse(self.cat.sleepy)
#         with self.assertRaises(Exception) as ex:
#             self.cat.sleep()
#         self.assertEqual('Cannot sleep while hungry', str(ex.exception))
#         self.assertFalse(self.cat.fed)
#         self.assertFalse(self.cat.sleepy)
#
#     def test_cat_is_not_hungry_can_go_to_sleep(self):
#         self.cat.eat()
#         self.assertTrue(self.cat.fed)
#         self.assertTrue(self.cat.sleepy)
#         self.cat.sleep()
#         self.assertFalse(self.cat.sleepy)
#
#
# if __name__ == '__main__':
#     main()


# # 03. List
# from unittest import TestCase, main
#
#
# class IntegerListTests(TestCase):
#
#     def setUp(self) -> None:
#         self.int_list = IntegerList(1, 2, 3)
#
#     def test_init_list_all_ints(self):
#         integer = IntegerList(4, 5, 6)
#         self.assertEqual(3, len(integer._IntegerList__data))
#
#     def test_init_list_not_integers_are_not_added(self):
#         integer = IntegerList(4, 5, 6.5)
#         self.assertEqual(2, len(integer.get_data()))
#         self.assertEqual([4, 5], integer.get_data())
#
#     def test_get_data_returns_list_of_the_elements(self):
#         integer = IntegerList(4, 5, 6)
#         self.assertEqual([4, 5, 6], integer.get_data())
#
#     def test_add_method_not_int_raises(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         test_data_values = [4.6, 'asd', {}, [], False]
#         for value in test_data_values:
#             with self.assertRaises(ValueError) as ve:
#                 self.int_list.add(value)
#         self.assertEqual('Element is not Integer', str(ve.exception))
#         self.assertEqual(3, len(self.int_list.get_data()))
#
#     def test_add_method_add_int_adds_the_element(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         result = self.int_list.add(5)
#         self.assertEqual(4, len(self.int_list.get_data()))
#         self.assertIn(5, self.int_list.get_data())
#         self.assertEqual([1, 2, 3, 5], result)
#
#     def test_remove_index_invalid_index_raises(self):
#         with self.assertRaises(IndexError) as ie:
#             self.int_list.remove_index(5)
#         self.assertEqual('Index is out of range', str(ie.exception))
#         self.assertEqual(3, len(self.int_list.get_data()))
#
#     def test_remove_index_removes_element(self):
#         self.assertEqual(1, self.int_list.get_data()[0])
#         result = self.int_list.remove_index(0)
#         self.assertEqual(1, result)
#         self.assertEqual(2, len(self.int_list.get_data()))
#         self.assertEqual(2, self.int_list.get_data()[0])
#
#     def test_get_invalid_index_raises(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         with self.assertRaises(IndexError) as ie:
#             self.int_list.get(4)
#         self.assertEqual('Index is out of range', str(ie.exception))
#
#     def test_get_by_index(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         element = self.int_list.get(1)
#         self.assertEqual(2, element)
#
#     def test_insert_invalid_index_raises(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         with self.assertRaises(IndexError) as ie:
#             self.int_list.insert(4, 5)
#         self.assertEqual('Index is out of range', str(ie.exception))
#
#     def test_insert_element_not_integer(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         with self.assertRaises(ValueError) as ve:
#             self.int_list.insert(0, 5.6)
#         self.assertEqual('Element is not Integer', str(ve.exception))
#         self.assertEqual(3, len(self.int_list.get_data()))
#
#     def test_insert(self):
#         self.assertEqual(3, len(self.int_list.get_data()))
#         self.assertEqual([1, 2, 3], self.int_list.get_data())
#         self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)
#         self.int_list.insert(0, 100)
#         self.assertEqual(4, len(self.int_list.get_data()))
#         self.assertEqual([100, 1, 2, 3], self.int_list.get_data())
#         self.assertEqual([100, 1, 2, 3], self.int_list._IntegerList__data)
#
#     def test_get_biggest(self):
#         my_list = IntegerList(0, 12, -3)
#         result = my_list.get_biggest()
#         self.assertEqual(12, result)
#
#     def test_get_index(self):
#         self.assertEqual(self.int_list.get_data()[0], 1)
#         result = self.int_list.get_index(1)
#         self.assertEqual(0, result)
#
#
# if __name__ == '__main__':
#     main()


# 04. Car Manager
# from unittest import TestCase, main
#
#
# class TestCar(TestCase):
#
#     def setUp(self):
#         self.car = Car('Nissan', 'GT-R', 15, 75)
#
#     def test_correct_initialization(self):
#         self.assertEqual('Nissan', self.car.make)
#         self.assertEqual('GT-R', self.car.model)
#         self.assertEqual(15, self.car.fuel_consumption)
#         self.assertEqual(75, self.car.fuel_capacity)
#         self.assertEqual(0, self.car.fuel_amount)
#
#     def test_no_make_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.make = ''
#
#         self.assertEqual('Make cannot be null or empty!', str(ex.exception))
#
#     def test_no_model_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.model = ''
#
#         self.assertEqual('Model cannot be null or empty!', str(ex.exception))
#
#     def test_fuel_consumption_with_zero_value_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.fuel_consumption = 0
#
#         self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))
#
#     def test_fuel_consumption_with_negative_value_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.fuel_consumption = -1
#
#         self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
#
#     def test_fuel_capacity_with_zero_value_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.fuel_capacity = 0
#
#         self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))
#
#     def test_fuel_capacity_with_negative_value_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.fuel_capacity = -1
#
#         self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))
#
#     def test_fuel_amount_with_negative_value_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.fuel_amount = -1
#
#         self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))
#
#     def test_refuel_withe_zero_raises_exception(self):
#         with self.assertRaises(Exception) as ex:
#             self.car.refuel(0)
#
#         self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))
#
#     def test_refuel_not_full_tank(self):
#         self.car.refuel(10)
#         self.assertEqual(10, self.car.fuel_amount)
#
#     def test_refuel_car_more_than_capacity_expect_fill_to_capacity(self):
#         self.car.refuel(100)
#         self.assertEqual(75, self.car.fuel_amount)
#
#     def test_drive_more_than_possible_raises_exception(self):
#         self.car.fuel_amount = 20
#
#         with self.assertRaises(Exception) as ex:
#             self.car.drive(1000)
#
#         self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
#
#     def test_drive_valid_distance_expect_fuel_amount_decrease(self):
#         self.car.fuel_amount = 75
#         self.car.drive(100)
#
#         self.assertEqual(60, self.car.fuel_amount)
#
#
# if __name__ == '__main__':
#     main()
