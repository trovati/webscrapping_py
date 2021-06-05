import requests
import pandas as pd 
from lxml import html

class Crawler:

    df = pd.DataFrame(columns=['Memory','vCPUs', 'SSD Disk','Transfer', '$/MO', '$/hour'])
    response = requests.get('https://www.digitalocean.com/pricing/')
    conteudo_site = html.fromstring(response.content)

    if response.status_code == 200:
        try:
            selecionar_table = '//ul[@class = "priceBox"]'
            table = conteudo_site.xpath(selecionar_table)[0]
            rows_table = table.xpath('.//li[@class = "priceBoxItem"]')

            for link in range(0,len(rows_table)):
                data = []
                conteudo_table = rows_table[link].xpath('.//a/div/ul/li')
                money_table = rows_table[link].xpath('.//a/div/div')
                time_table = rows_table[link].xpath('.//a/div/span')

                data.append(conteudo_table[0].text_content().split("/")[0])
                data.append(conteudo_table[0].text_content().split("/")[1])
                data.append(conteudo_table[1].text_content().split("SSD")[0])
                data.append(conteudo_table[2].text_content().split("transfer")[0])
                data.append(money_table[0].text_content().split("/")[0])
                data.append(time_table[0].text_content().split("/")[0])
                df.loc[link] = data


                

        except:
            pass

        print(df)




if __name__ == "__main__":
    teste = Crawler()
