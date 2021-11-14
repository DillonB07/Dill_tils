dill\_tils.text package
=======================

Submodules
----------

dill\_tils.text.clear module
----------------------------

.. automodule:: dill_tils.text.clear
   :members:
   :undoc-members:
   :show-inheritance:
   

The :code:`clear()` function clears the terminal.

This uses the :code:`os` module to detect the current operating system and runs the correct command in Terminal accordingly.
This means that your programs will work both on Posix systems(macOS/Linux) as well as Windows.


**Usage:**

.. code-block:: python

   from dill_tils.text import clear

   clear()

dill\_tils.text.write module
----------------------------

.. automodule:: dill_tils.text.write
   :members:
   :undoc-members:
   :show-inheritance:


The :code:`write()` function writes a string to the terminal as if it was being typed.


**Usage:**

.. code-block:: python

   from dill_tils.text import write

   write("Hello World!", 0.2)


---------------

.. .. automodule:: dill_tils.text
   :members:
   :undoc-members:
   :show-inheritance:

