import webbrowser 
import time
import subprocess

tabs = ['https://learn.uwaterloo.ca/d2l/home', 'https://outlook.office.com/mail/inbox/id/AAQkADkxYjA2ODczLTQzMGQtNDMwNi1iMzMxLTZkMGU1OWVhYTkyMgAQAFGNKiR%2BxU5FrXfmwx2QE%2Fw%3D', ]
apps = ['C:\\Users\\slgur\\AppData\\Local\\Microsoft\\Teams', 'C:\\Program Files (x86)\\Google\\Chrome\\Application']
allow = False


def open_apps(applications):
	for app_list in applications:
		subprocess.call(app_list)

def open_tabs(webpages):
	for pages in webpages:
		webbrowser.open_new_tab(pages)

if allow:
	def main():
		webbrowser.open('a fucking webpage', new=0, autoraise=True)
		open_tabs(tabs)
		time.sleep(0.5)
		open_apps(apps)
	main()
else:
	print ('fuck off')



