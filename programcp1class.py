import json
import csv
import xml.etree.cElementTree as e
class Program():
    
    def __init__(self):
        self.data = None
        
    def json_read(self):
        with open("dane.json") as file:
            self.data = json.load(file)
            
    def json_dis(self):
        if self.data != None:
            data_toprint = json.dumps(self.data, indent=2)
            print(data_toprint)
        else:
            print("Frist read json file")
    
    
    def csv_save(self):
        x = self.data[0].keys()
        with open("JSON_to_CSV.csv", "w", newline='') as file:
            writer=csv.writer(file)
            writer.writerow(x)
            for i in range(len(self.data)):
                y= self.data[i].values()
                writer.writerow(y)
    
    def xml_save(self):
        r = e.Element("Root")
        for z in range(len(self.data)):
            s = e.SubElement(r,"App")
            for i in self.data[z].keys():              
                e.SubElement(s,i).text = str(self.data[z][i])
            a = e.ElementTree(r)
            a.write('JSON_to_XML.xml')  
    def create_table(self):
        f = open("JSON_to_CSV.csv", "r")
        dt = f.readlines()
        self.table = "<table>\n"
        header = dt[0].split(',')
        self.table += "  <tr>\n"
        for column in header:
            self.table += "    <th>{0}</th>\n".format(column.strip())
        self.table += "  </tr>\n"
        for line in dt[1:]:
            row = line.split(",")
            self.table += "  <tr>\n"
            for column in row:
                self.table += "    <td>{0}</td>\n".format(column.strip())
            self.table += "  </tr>\n"
        f.close()
        
        self.table += "</table>"
    
    
    def create_html(self):
        with open('Final Project.html', 'w') as file:
            file.write(f'<html>\n<head>\n<title>Final Project</title>\n<link rel="stylesheet" href="stylish.css">\n<link href="https://fonts.googleapis.com/css2?family=Barlow&display=swap" rel="stylesheet">\n</head>\n<body>\n<div id="container">\n<div id="header">\n<h1 style="text-align: center;">Final Project</h1>\n</div>\n<div id="autor">\n<h2>Autorzy</h2>\n<li>XXX</li>\n<li>YYY</li>\n<li>ZZZ</li>\n</div>\n<hr />\n<div id="opis">\n<p1>Projekt zawiera program do odczytywania plików JSON, a także zapisywania ich w formacie CSV lub XML. Oprócz tego tworzy także stroną html na której teraz sie znajdujesz:). Program został zrealizowany w oparciu o Programowanie Obiektowe (ang. Object Oriented Programming - OOP).</p1>\n</div>\n<hr />\n<div id="dane">\n<p2>Dane zawierają informacje na temat różnych Aplikacji. Z danych możemy dowiedzieć się m.in. kto jest producentem, kto właścicielem, kiedy miała miejsce premiera. Zawiera m.in. rodzaje struktur: tekstowe, liczbowe, daty, logiczne, kwoty.</p2>\n{self.table}</div>\n</body>\n</html>')
    def create_css(self):
        with open ('stylish.css', 'w') as file:
            file.write('* {margin: 0;padding: 0;box-sizing: border-box;font-family: "Barlow", sans-serif;text-align: center;}\nbody {background: linear-gradient(to bottom, #33ccff 0%, #ccffff 100%);}\n#container {max-width: 1200px;margin: 0 auto;background-color: white;}\ntable, th, td {border: 1px solid black;border-collapse: collapse;text-align: center;padding: 3px;}\ntable {width: 80%;margin-left: 120px;margin-top: 10px;}\nh2 {padding: 5px;}\ntr:nth-child(even) {background-color: darkturquoise;}\ntr:nth-child(odd) {background-color: aqua;}\ntr {color:black;}\nth {background-color: dodgerblue;color: white;}\n#autor {padding-bottom: 10px;}\n#opis {padding: 10px;}\n#dane {padding: 5px;}\np2 {text-align: center;}\nh1 {padding: 15px;}\nli {list-style-type: none;}')
            
            


