#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
        TestRectangle_width - line 114
    TestRectangle_height - line 190
        TestRectangle_x - line 262
     TestRectangle_y - line 334
         TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
        TestRectangle_update_args - line 538
     TestRectangle_update_kwargs - line 676
         TestRectangle_to_dictionary - line 788
         """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiation(unittest.TestCase):
     """Unittests for testing instantiation of the Rectangle class."""
     def test_rectangle_base(self):
         self.assertIsInstance(rectangle(10,2), Base)
     
     def test_no_args(self):
         with self.assertRaise(TypeError):
             rectangle()
     
     def test_one_args(self):
         with self.assertRaise(TypeError):
             rectangle(1)
     
     def test_three_args(self):
         r1 =  Rectangle(2, 2, 4)
         r2 = Rectangle(4, 4, 2)
         self.assertEqual(r1.id, r2.id - 1)

     def test_two_args(self):
         r1 = Rectangle(10, 2)
         r2 = Rectangle(2, 10)
         self.assertEqual(r1.id, r2.id - 1)
     def  test_four_args(self):
         r1 = Rectangle(1, 2, 3, 4)
         r2 = Rectangle(4, 3, 2, 1)
         self.assertEqual(r1.id, r2.id - 1)

     def test_five_args(self):
         self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)
     def test_more_than_five_args(self):
         with self.assertRaises(TypeError):
             Rectangle(1, 2, 3, 4, 5, 6)
     
     def test_width_private(self):
         with self.assertRaises(AttributeError):
             print(Rectangle(5, 5, 0, 0, 1).__width)
     
     def test_height_private(self):
         with self.assertRaises(AttributeError):
             print(Rectangle(5, 5, 0, 0, 1).__height)

     def test_x_private(self):
         with self.assertRaises(AttributeError):
             print(Rectangle(5, 5, 0, 0, 1).__x)
     
     def test_y_private(self):
         with self.assertRaises(AttributeError):
             print(Rectangle(5, 5, 0, 0, 1).__y)
     
     def test_width_getter(self):
         r1 = Rectangle(5,6,7,5,1)
         self.assertEqual(5, r1.width)

     def test_height_getter(self):
         r = Rectangle(5, 7, 7, 5, 1)
         self.assertEqual(7, r.height)
     
     def test_height_setter(self):
         r = Rectangle(5, 7, 7, 5, 1)
         r.height = 10
         self.assertEqual(10, r.height)
     
     def test_x_getter(self):
         r = Rectangle(5, 7, 7, 5, 1)
         self.assertEqual(7, r.x)

      def test_x_setter(self):
          r = Rectangle(5, 7, 7, 5, 1)
          r.x = 10
          self.assertEqual(10, r.x)
      
      def test_y_getter(self):
          r = Rectangle(5, 7, 7, 5, 1)
          self.assertEqual(5, r.y)
      
      def test_y_setter(self):
          r = Rectangle(5, 7, 7, 5, 1)
          r.y = 10
          self.assertEqual(10, r.y)

class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

     def test_None_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(None, 2)
     def test_str_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle("invalid", 2)
     
     def test_float_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(5.5, 1)
     
     def test_complex_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(complex(5), 2)
     
     def test_dict_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle({"a": 1, "b": 2}, 2)
     
     def test_bool_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(True, 2)

     def test_list_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle([1, 2, 3], 2)

     def test_set_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
              Rectangle({1, 2, 3}, 2)
     def test_tuple_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
              Rectangle((1, 2, 3), 2)
     
     def test_frozenset_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
              Rectangle(frozenset({1, 2, 3, 1}), 2)

     def test_range_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(range(5), 2)

     def test_bytes_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(b'Python', 2)

     def test_bytearray_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(bytearray(b'abcdefg'), 2)

     def test_memoryview_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(memoryview(b'abcedfg'), 2)

     def test_inf_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(float('inf'), 2)

     def test_nan_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(float('nan'), 2)

     def test_negative_width(self):
         with self.assertRaisesRegex(ValueError, "width must be > 0"):
             Rectangle(-1, 2)

     def test_zero_width(self):
          with self.assertRaisesRegex(ValueError, "width must be > 0"):
              Rectangle(0, 2)

class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""
     def test_None_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, None)

     def test_str_height(self):
         with self.assertRaisesRegex(TypeError, "number must be enteger"):
             rectangle(2,'hello')

     def test_float_rectangle(self):
         with self.assertRaisesRegex(TypeError, "height must be enteger"):
             rectangle(2, 3.3)

     def test_complex_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, {"a": 1, "b": 2})

     def test_set_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, {1, 2, 3})

     def test_tuple_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
              Rectangle(1, (1, 2, 3))

     def test_list_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, [1, 2, 3])

     def test_frozenset_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, frozenset({1, 2, 3, 1}))

     def test_range_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, range(5))
     
     def test_bytes_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, b'Python')

     def test_bytearray_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, bytearray(b'abcdefg'))

     def test_memoryview_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, memoryview(b'abcedfg'))

     def test_inf_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, float('inf'))

     def test_nan_height(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(1, float('nan'))

     def test_negative_height(self):
          with self.assertRaisesRegex(ValueError, "height must be > 0"):
              Rectangle(1, -1)

     def test_zero_height(self):
         with self.assertRaisesError(ValueError, "height must > 0"):
             Rectangle(1, 0)




