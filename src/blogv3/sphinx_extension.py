from sphinx.application import Sphinx

from blogv3.dated_toc import DatedTocTree, DatedTocPostTransform


def setup(sphinx: Sphinx) -> None:
    """
    Setup function for the Sphinx extension.
    """

    sphinx.add_directive("toctree", DatedTocTree, override=True)
    sphinx.add_post_transform(DatedTocPostTransform)
