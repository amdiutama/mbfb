#!usr/bin/python2.7
# coding=utf-8
import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    post = raw_input('\n\x1b[1;97m [?] Url Post :\x1b[1;93m ')
    try:
        domain = post.split('//')[1].split('/')[0]
        post = post.replace(domain, 'mbasic.facebook.com')
    except IndexError:
        exit('\n \x1b[1;91m[!] Url Salah')

    url_likes = None
    response = config.httpRequest(post, cookie).encode('utf-8')
    html = parser(response, 'html.parser')
    for x in html.find_all('a'):
        if '/ufi/reaction/profile/browser/?' in x['href']:
            url_likes = url + x['href']
            break

    if url_likes == None:
        exit('\n \x1b[1;91mTidak ada hasil.')
    try:
        max = int(raw_input('\x1b[1;97m [?] Limit : \x1b[1;93m'))
    except ValueError:
        exit('\n \x1b[1;91m[!] Isi yg benar')

    if max == 0:
        exit('\n\x1b[1;91m [!] Isi yg benar')
    statusStop = False
    output = 'dump/likes.json'
    id = []
    print ''
    while True:
        try:
            response = config.httpRequest(url_likes, cookie).encode('utf-8')
            html = parser(response, 'html.parser')
            find = html.find_all('h3')
            for i in find:
                full_name = i.text.encode('utf-8')
                href = i.find('a')
                if '+' in str(href) or href == None:
                    continue
                else:
                    if 'profile.php?id=' in str(i):
                        uid = re.findall('\\/profile.php\\?id=(.*?)$', href['href'])
                    else:
                        uid = re.findall('\\/(.*?)$', href['href'])
                    if len(uid) == 1:
                        id.append({'uid': uid[0].replace('/', ''), 'name': full_name})
                    sys.stdout.write('\r\x1b[1;95m•  \r\x1b[1;95m• \x1b[1;97m%s\x1b[1;95m • \x1b[1;97m%s\x1b[1;95m • \x1b[1;97mSedang Dump ' % (
                     datetime.now().strftime('%H:%M:%S'), len(id)))
                    sys.stdout.flush()
                    if len(id) == max or len(id) > max:
                        statusStop = True
                        break

            if statusStop == False:
                if 'Lihat Selengkapnya' in str(html):
                    url_likes = url + html.find('a', string='Lihat Selengkapnya')['href']
                else:
                    break
            else:
                break
        except KeyboardInterrupt:
            print '\n\n \x1b[1;97m[!] Error, Berhenti'
            break

    try:
        for filename in os.listdir('dump'):
            os.remove('dump/' + filename)

    except:
        pass

    print '\n\n\x1b[1;97m [*] Output :\x1b[1;93m ' + output
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()
    return
# Awokawokawok Ngerekod:v