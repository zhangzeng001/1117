import os,sys

BASE_FILE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_FILE)
from src import connect




if __name__ == '__main__':
    P = connect.SSH_client()