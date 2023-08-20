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


# 03. List
