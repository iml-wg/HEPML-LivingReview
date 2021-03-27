import os
import subprocess
from shutil import copyfile


def make_patch():
    """
    While being run in CI by GitHub Actions, collect repo, commit, and CI run
    information to patch jheppub.sty.
    """
    commit_SHA = (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
        .strip()
        .decode("utf-8")
    )
    # GITHUB_REPOSITORY is set by GitHub Actions
    try:
        github_repository = os.environ["GITHUB_REPOSITORY"]
    except KeyError:
        github_repository = (
            subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
            .strip()
            .decode("utf-8")
            .replace("git@github.com:", "")
            .replace(".git", "")
        )
    github_repository_url = "https://github.com/" + github_repository
    # GITHUB_RUN_ID is set by GitHub Actions
    try:
        github_run_id = os.environ["GITHUB_RUN_ID"]
    except KeyError:
        github_run_id = ""

    github_actions_url = github_repository_url + "/actions/runs/" + github_run_id
    github_commit_url = github_repository_url + "/tree/" + commit_SHA

    footnote = (
        r"\footnotesize Built \href{"
        + github_actions_url
        + r"}{\today}\ from \href{"
        + github_commit_url
        + "}{"
        + commit_SHA
        + "}"
    )

    patch = (
        r"\usepackage{fancyhdr}"
        + "\n"
        + r"\newcommand\ps@titlepage{\renewcommand\@oddfoot{}\renewcommand\@oddhead{}"
        + "\n"
        + r"\pagestyle{fancy}"
        + "\n"
        + r"\renewcommand{\headrulewidth}{0pt}"
        + "\n"
        + r"\fancyfoot{}"
        + "\n"
        + r"\rfoot{"
        + footnote
        + "}"
        + "\n}"
    )
    return patch


def main():
    """
    Patch jheppub.sty to record build information as a footnote on the title page.
    """
    patch = make_patch()

    copyfile("jheppub.sty", "jheppub.sty.bak")
    with open("jheppub.sty.bak") as read_file, open(
        "jheppub.sty", "w+"
    ) as write_file:
        for line in read_file:
            write_file.write(
                line.replace(
                    r"\newcommand\ps@titlepage{\renewcommand\@oddfoot{}\renewcommand\@oddhead{}}",
                    patch,
                )
            )


if __name__ == "__main__":
    main()
