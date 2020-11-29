def TworzenieGlownegoPlikuCSV():
    import requests
    from bs4 import BeautifulSoup
    import csv
    import json

    with open('UZUPELNIJ.json')as f:
        data = json.load(f)
    for state in data["DANE"]:
        break

    f = open("bf3_strona.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(f, delimiter=' ', quoting=csv.QUOTE_MINIMAL)

    url = state['yupoo_link']
    text = url

    head, sep, tail = text.partition('x.yupoo.com')
    print(head + "x.yupoo.com")

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    writer.writerow(["LINKS", "NAME", "PHOTOS", "LINK ALIEXPRESS", "dsds"])

    row1 = []
    row2 = []
    row3 = []

    for link in soup.findAll('a', class_='album__main'):
        q = (link.get('href'))
        row1.append(q)

    for link in soup.findAll('a', class_='album__main'):
        q = (link.get('href'))
        new_url = head + "x.yupoo.com" + q
        response = requests.get(new_url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        rows1 = (soup.find('span', class_="showalbumheader__gallerytitle"))
        rows = (soup.find('a', rel="nofollow noopener"))
        v = rows.text
        x = rows1.text
        row2.append(v)
        row3.append(x)

    for c in range(len(row3)):
        writer.writerow([row1[c], row2[c], row3[c]])


    f.close()
    print("PLIK Z LINKAMI ZOSTAWL UTOWRZONY...")
    import subprocess

    print("Uruchamiam PobieranieZdjec.py\n [...]")
    subprocess.Popen("python PobieranieZdjec.py", shell=True)


TworzenieGlownegoPlikuCSV()