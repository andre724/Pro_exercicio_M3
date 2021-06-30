from bs4 import BeautifulSoup
from requests import get
import re   
import html5lib


count=1

response = get("https://en.wikipedia.org/wiki/Nintendo")

tags = BeautifulSoup(response.text, "html5lib")

main_title= tags.find("title")
print(f'Página principal: {main_title.text}')


conteudo = tags.find_all("p")


for table in conteudo:
    links = table.find_all("a", href=re.compile("/wiki/"))
    for link in links:
        branch_title = link.get('title')
        print(f'Página secundaria {count} : {branch_title}')
        count+=1



# Duvida:
# se eu faço esse for loop e depois um print
#for table in conteudo:
    #links = table.find_all("a", href=re.compile("/wiki/"))
#print(links)
# ele só me retorna uma tag 'a', mas quando itero links ele retorna todos
# Isso é porque o obejeto links é tipo um generator? 