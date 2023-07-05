---
hide:
  - navigation
---

# Contributing

To contribute to this project please either open an Issue with the details of the change you would like.
If you have already discussed this with the maintainers or have contributed in the past you can also open a Pull Request.

## Opening an Issue

You can open an Issue from the [GitHub Issue tracker page](https://github.com/iml-wg/HEPML-LivingReview/issues).
Before you open an Issue please search through both the closed and open Issues to make sure that your Issue hasn't already been discussed or addressed in the past.

## Pull Request Process

1. Create a [fork of the project](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).
2. Create your Pull Request (PR) from your fork (see the FAQ below).
3. Verify that you have run `make_md.py` to update the `README`.
4. Ensure that the tests in the CI are passing.
5. Request that a maintainer review your PR.
6. Your PR can be merged in once you have the sign-off of at least one maintainer. If you do not have permission to make the merge, request the approving maintainer to merge it for you.

## Areas of Requested Help

1. Adding content across experiments
2. An additional volunteer maintainer

## FAQ

### There is a subject not listed that I think should be. How do I get it added to the listing?

If there is content missing that you'd like added please create an issue with as much description as possible (and maybe some examples).
A maintainer will add the content once it has been approved.
Alternatively, feel free to fork the repository and add the content you want and then create a pull request.

### Should I add papers that are only about machine learning?

No.
While the ML papers that have inspired the work of the particle physics community are invaluable, trying to keep an updated list of all of them would be both beyond the scope of the project and unmaintainable.
We welcome and encourage contributions of papers that cover modern machine learning applications to particle physics!

### How do I add a paper?

All paper additions should be submitted as a single pull request on a source branch that isn't `master`.

1. Make a new branch on your fork for the pull request
2. Find the paper on [INSPIRE](https://inspirehep.net/?ln=en)
   - **N.B.:** If you have already found the paper on [arXiv](https://arxiv.org/) you should be able to find the INSPIRE listing linked under "References & Citations"
3. Get the BibTeX for the paper citation provided by INSPIRE (under "Export" at the bottom of the page)
4. Add this BibTeX entry to [`HEPML.bib`](https://github.com/iml-wg/HEPML-LivingReview/blob/master/HEPML.bib) in the appropriate chronological position
   - If the entry is from a collaboration like for instance ATLAS, remove the collaboration entry and change the author, for instance, according to
      ```diff
      - author = "Aad, Georges and others",
      - collaboration = "ATLAS",
      + author = "{ATLAS Collaboration}",
      ```
6. Add the citation to [`HEPML.tex`](https://github.com/iml-wg/HEPML-LivingReview/blob/master/HEPML.tex) in the appropriate categories
7. Verify that if you run `make` the LaTeX will compile
8. Run `make_md.py` to update the `README`, `docs/index.md` with the new references
9. Add and commit `HEPML.bib`, `HEPML.tex`, `README.md`, and all new `docs/*.md` to your pull request
10. If you haven't yet, push your branch to GitHub and open a pull request to the main project
