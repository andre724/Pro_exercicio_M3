Exercicio do Módulo 3

Ultilizei as libs BS4, requests, html5lib e re, para fazer o scraping na pagina da Nintendo da Wikipédia.
Peguei o título da pagina principal depois, todos os links do conteudo da pagina e seus respectivos títulos.

No .gitignore tem uma file chamada tests.ipynb uso a extenção de jupiter no vscode para fazer o exercicio, pois consigo visualizar o que cada linha do código faz. Mas depois passo 
tudo para uma file.py normal para a entrega.

Fiz um comentario no fim do codigo para tirar uma duvida, porem irei colocá-la aqui também 

Duvida:
se eu faço esse for loop e depois um print
for table in conteudo:
    #links = table.find_all("a", href=re.compile("/wiki/"))
print(links)

só retorna uma tag 'a', mas quando itero links ele retorna todas
Isso é porque o obejeto links é tipo um generator? 