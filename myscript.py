import os


def main():

    firstHash = "c1a4be04b972b6c17db242fc37752ad517c29402"
    secondHash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

    os.system(
        'git bisect start ' + firstHash + ' ' + secondHash)
    os.system('git bisect run python manage.py test')


if __name__ == '__main__':
    main()
