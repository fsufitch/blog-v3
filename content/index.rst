Filip Sufitchi's Blog
===================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :glob:

   posts/*/index

Test Area
-----


Stuff and things :doc:`hello </posts/2025-06-21/index>`.

Another reference: :ref:`hello world <my-label>`.


.. _my-label:

   >>> print("Hello, World!")



.. code-block:: c
   
   #include <stdio.h>

   int main() {
       printf("Hello, World!\n");
       return 0;
   }

blah blah. |:smile:| |:snake:|

Reference to the definition of :ref:`abc <my-section-reference>`.
