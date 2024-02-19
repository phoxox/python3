#!C:\Python312\python.exe
#!python3
""" upgrade all installed packages """
from sys import version
from subprocess import call
from threading import Thread
import importlib.metadata

# print('\n'.join([d.metadata['Name']
#                  for d in importlib.metadata.distributions()]))
installed_packages = [d.metadata['Name']
                      for d in importlib.metadata.distributions()]
COUNT_PACK = str(len(installed_packages))


def create_list():
    """ create a text (log) file """
    print(version)
    print("Checking " + COUNT_PACK + " installed packages .....")
    # print("Upgrading the site packages: " + " ".join(installed_packages))
    print("Please wait ........")
    with open('c:\\cache\\tools\\requirements.txt', 'w',
              encoding='utf-8') as file:
        file.write('\n'.join(installed_packages))


def upgrade_list():
    """ upgrade all installed packages """
    call("py.exe -m pip install --upgrade " + " ".join(installed_packages),
         shell=False)


def main():
    """ main program """
    # installed_packages.remove('pikepdf')
    # keep pikepdf==5.6.1  # pikepdf==6.1.0 ok now
    # creating threads
    th1 = Thread(target=create_list)
    th2 = Thread(target=upgrade_list)
    # start all threads activity
    th1.start()
    th2.start()
    # wait until all threads terminate
    th1.join()
    th2.join()
    print("Upgrade finished!")  # show the message


if __name__ == "__main__":
    main()
