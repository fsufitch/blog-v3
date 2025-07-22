from datetime import datetime
from typing import Literal
from unittest import result
from docutils.nodes import Node
from sphinx.directives.other import TocTree
from sphinx.transforms.post_transforms import SphinxPostTransform
from docutils.parsers.rst import directives as D


import sphinx.addnodes

import sphinx.util.logging

from blogv3.utils import get_latest_commit, get_title

LOG = sphinx.util.logging.getLogger(__name__)

DEFAULT_DATE_FORMAT = "%Y-%m-%d"


def _parse_date_sort(value: str) -> Literal["asc", "desc", None]:
    """
    Parse the date-sort option value.
    """
    if value not in ("asc", "desc"):
        raise ValueError(f"Invalid date-sort value: {value}. Expected 'asc' or 'desc'.")
    return value


class DatedTocTree(TocTree):
    """
    Custom Sphinx directive for a dated table of contents.
    """

    option_spec = {
        **(TocTree.option_spec or {}),
        "use-dates": D.flag,
        "date-format": str,
        "date-sort": _parse_date_sort,
    }

    def run(self) -> list[Node]:
        """
        Pass through the use-dates and date-format options to the toctree.
        """
        nodes = super().run()

        for node in nodes:
            for toctree in node.findall(
                lambda n: isinstance(n, sphinx.addnodes.toctree)
            ):
                # Assert to double-check, but mainly to appease type checking
                assert isinstance(
                    toctree, sphinx.addnodes.toctree
                ), "Expected a sphinx.addnodes.toctree node"

                if "use-dates" in self.options:
                    toctree.attributes["use-dates"] = None
                if "date-format" in self.options:
                    toctree.attributes["date-format"] = self.options["date-format"]
                if "date-sort" in self.options:
                    toctree.attributes["date-sort"] = self.options["date-sort"]

        return nodes


class DatedTocPostTransform(SphinxPostTransform):
    """
    Transform to process dated table of contents.
    """

    default_priority = 100

    def run(self) -> None:
        """
        Apply the transformation to the document.
        """
        # Here you can implement any logic needed to transform the document
        # based on the dated table of contents.
        toctrees = self.document.findall(
            lambda node: isinstance(node, sphinx.addnodes.toctree)
        )

        for toctree in toctrees:
            self.apply_toctree_dates(toctree)

    def apply_toctree_dates(self, toctree: sphinx.addnodes.toctree) -> None:
        """
        Apply date formatting to the toctree entries.
        """
        if "use-dates" not in toctree.attributes:
            return

        date_format = toctree.attributes.get("date-format", DEFAULT_DATE_FORMAT)

        ignored_entries = []

        new_entries = list[tuple[datetime | None, str, str]]()
        for entry in toctree["entries"]:
            try:
                old_title, ref = entry
            except ValueError:
                LOG.warning(
                    "Invalid entry in toctree: %s. Expected a tuple of (title, ref). "
                    "Passing it through unchanged.",
                    entry,
                )
                ignored_entries.append(entry)
                continue

            if old_title:
                title = old_title
            else:
                doc = self.env.get_doctree(ref)
                title = get_title(doc)

            commit = get_latest_commit(self.app, ref)

            if commit.hexsha == "0000000000000000000000000000000000000000":
                changed_dt = None
            else:
                changed_dt = max(commit.committed_datetime, commit.authored_datetime)

            new_entries.append((changed_dt, ref, title))

        if toctree.attributes.get("date-sort") == "asc":
            new_entries.sort(key=lambda x: x[1] or datetime.min)
        elif toctree.attributes.get("date-sort") == "desc":
            new_entries.sort(key=lambda x: x[1] or datetime.min, reverse=True)

        print(new_entries)

        result_entries: list[tuple[str, str]] = []
        for dt, ref, title in new_entries:
            if dt is None:
                result_entries.append((f"[NO COMMIT] {title}", ref))
            else:
                formatted_date = dt.strftime(date_format)
                result_entries.append((f"[{formatted_date}] {title}", ref))

        print(result_entries)
        print(ignored_entries)
        result_entries.extend(ignored_entries)
        toctree["entries"] = result_entries
