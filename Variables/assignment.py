"""
Create your own Python Variables
Instructions
Create a new variable named 'welcome', that has a value of 'Welcome to Python!'

Test(s)
Test 1
import exercise  # Import student's code
from unittest import TestCase

class Evaluate(TestCase):
    def test_name(self):
        self.assertTrue(hasattr(exercise, "welcome"), "You must declare 'welcome'")
        self.assertEqual(exercise.welcome, "Welcome to Python!", "'welcome' value seems wrong")
"""

welcome = "Welcome to Python!"
print(welcome)
