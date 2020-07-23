import sys

sys.path.insert(0, 'c:\Temp/python/planet_teams/uijuwebsite')

from main import app as application

if __name__ == '__main__':
	application.run(host='0.0.0.0', port=8000)

