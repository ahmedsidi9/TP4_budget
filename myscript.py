import os
import sys
import subprocess
import git

# SCript for detecting bugs with git bisect run


def main():
    path = "https://github.com/ahmedsidi9/TP4_budget.git"
    firstHash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
    secondHash = "c1a4be04b972b6c17db242fc37752ad517c29402"
    repository = git.cmd.Git(path)
    repository.bisect("start")
    repository.bisect("good", firstHash)
    message = repository.bisect("bad", secondHash)
    while (message.startswith("Bisecting:")):
        message = repository.bisect("bad", secondHash)
        print(message)
    print("Bisecting finished")
    print("The bad commit is: " + message)

    print(repository.bisect("reset"))
    # repository.cmd("git", "bisect", "start")

    # repository.cmd("git", "bisect", "good", "HEAD~10")
    # repository.cmd("git", "bisect", "bad", "HEAD")


if __name__ == '__main__':
    main()
