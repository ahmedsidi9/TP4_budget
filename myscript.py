import os
import sys
import subprocess
import git

# SCript for detecting bugs with git bisect run


def get_git_revision_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()


def main():
    repo = git.Git()

    firstHash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
    secondHash = "c1a4be04b972b6c17db242fc37752ad517c29402"

    print("Executing : git bisect start")
    subprocess.run("git bisect start",
                   stdout=subprocess.PIPE, shell=True)

    print("Executing : git bisect good " + firstHash)
    subprocess.run("git bisect good " + firstHash,
                   stdout=subprocess.PIPE, shell=True)

    print("Executing : git bisect bad " + secondHash)
    subprocess.run("git bisect bad " + secondHash,
                   stdout=subprocess.PIPE, shell=True)

    # Execute tests
    process = subprocess.run("python3 manage.py test",
                             stdout=subprocess.PIPE, shell=True)

    test_result = process.__getattribute__("returncode")
    head = get_git_revision_hash()

    if (test_result > 0):
        print("Executing : git bisect bad " + head)
        print(head)
        bisect = subprocess.run("git bisect bad " + head,
                                stdout=subprocess.PIPE, shell=True)
        print("output" + bisect.__getattribute__("stdout").decode("utf-8"))
        repo.bisect("bad", head)
        print("apres le bisect", get_git_revision_hash())
        # if (hash_commit == head):
        # return
    else:
        print("Executing : git bisect good " + head)
        repo.bisect("good", head)

    print("Executing : git bisect reset")
    repo.bisect("reset")

    # repository.bisect("start")
    # message = repository.bisect("bad", secondHash)
    # message = repository.bisect("bad", secondHash)

    # print("Bisecting finished")
    # print("The first bad commit is: " +
    #       message.substring(message.indexOf("["), message.indexOf("]")))

    # print(repository.bisect("reset"))
    # repository.cmd("git", "bisect", "start")

    # repository.cmd("git", "bisect", "good", "HEAD~10")
    # repository.cmd("git", "bisect", "bad", "HEAD")
    # if test_output after repo.bisect === FAILED ---> CALL repo.bisect(bad, hash current commit)
    # else: call repo.bisect(good, hash current commit)


if __name__ == '__main__':
    main()
