Second Post: RST Features Showcase
==================================

Welcome to the second placeholder post! This entry demonstrates additional reStructuredText features, including math, diagrams, and figures.

Math Example
------------

You can include inline math, such as :math:`E = mc^2`, or display equations:

.. math::

   \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}

.. admonition:: Did you know?

   The above is the Gaussian integral, a fundamental result in probability and statistics.

Diagram Example
---------------

Below is a simple graph using the ``graphviz`` directive:

.. graphviz::

   digraph G {
       A -> B;
       B -> C;
       C -> A;
   }

Figure Example
--------------

.. figure:: https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png
   :alt: PNG Transparency Demonstration
   :width: 300px
   :align: center

   This is a sample figure with a caption. Figures can be local files or remote URLs.

Definition List
---------------

RST supports definition lists:

Term 1
   Definition of the first term.

Term 2
   Definition of the second term, which can span multiple lines and include *emphasis*.

Conclusion
----------

RST is a powerful markup language for technical writing, supporting math, diagrams, images, and more!
