from pathlib import Path

import docutils.nodes as N
import git
import sphinx.util.logging
from sphinx.application import Sphinx

LOG = sphinx.util.logging.getLogger(__name__)


def get_title(doctree: N.document) -> str:
    """
    Extract the title from a Sphinx document.

    Args:
        doctree (docutils.nodes.document): The Sphinx document node.

    Returns:
        str: The title of the document.
    """
    nodes = doctree.findall(lambda node: isinstance(node, N.title))
    try:
        title_node = next(nodes)
    except StopIteration:
        LOG.warning("No title found in the document.")
        return ""

    return title_node.astext()


def get_latest_commit(sphinx: Sphinx, doc_name: str) -> git.Commit:
    path = Path(sphinx.env.srcdir) / sphinx.env.doc2path(doc_name, base=True)

    for git_root in path.parents:
        if (git_root / ".git").exists():
            break
    else:
        LOG.error("No .git directory found in the path hierarchy.")
        raise FileNotFoundError("No .git directory found.")

    repo = git.Repo(git_root)

    if not repo.head.is_valid():
        LOG.error("No valid HEAD in the repository.")
        raise ValueError("No valid HEAD in the repository.")

    blame = next(repo.blame_incremental(None, str(path)))
    commit = blame.commit
    assert isinstance(commit, git.Commit), "Expected a git.Commit object"

    return commit
