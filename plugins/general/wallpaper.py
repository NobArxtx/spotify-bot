from bs4 import BeautifulSoup
import aiohttp

import os
import asyncio
from PIL import Image
from pySmartDL import SmartDL


from __main__ import client
from telethon import events
from constants import CMD_PREFIX
from telethon.tl.functions.photos import UploadProfilePhotoRequest


if_run = True
down_p =  './Downloads/'
async def soup(SELECTED_DL):
    async with aiohttp.ClientSession() as session:
        async with session.get(SELECTED_DL) as respe:
            text = await respe.read()
            D = str(respe._real_url)
    return [BeautifulSoup(text.decode('utf-8'), 'html5lib'),D]

async def dlimg(link):
    paea = 'donno.{}'.format(link.split('.')[-1])
    path_i = os.path.join(down_p, paea)
    dlb = SmartDL(dest=path_i,urls=link,progress_bar=False)
    dlb.start()
    if link.endswith('png'):
        im = Image.open(path_i)
        os.remove(path_i)
        path_i = path_i.replace('png', 'jpeg')
        im = im.convert('RGB')
        im.save(path_i, 'jpeg')
    return path_i
async def walld(strin):
    if len(strin.split()) > 1:
        strin = '+'.join(strin.split())
    url = 'https://wall.alphacoders.com/search.php?search='
    none_got = ['https://wall.alphacoders.com/finding_wallpapers.php']
    none_got.append('https://wall.alphacoders.com/search-no-results.php')
    page_link = 'https://wall.alphacoders.com/search.php?search={}&page={}'
    resp = await soup(f'{url}{strin}')
    if resp[1] in none_got:
        return False
    if 'by_category.php' in resp[1]:
        page_link = str(resp[1]).replace('&amp;', '') + '&page={}'
        check_link = True
    else:
        check_link = False
    resp = resp[0]
    try:
        wall_num = list(resp.find('h1',{'class':'center title'}).text.split(' '))
        
        for i in wall_num:
            try:
                wall_num = int(i)
            except ValueError:
                pass
        
        page_num = resp.find('div', {'class': 'visible-xs'})
        page_num = page_num.find('input', {'class': 'form-control'})
        page_num = int(page_num['placeholder'].split(' ')[-1])
    except Exception:
        page_num = 1
    n = randint(1, page_num)
    if page_num != 1:
        if check_link:
            resp = await soup(page_link.format(n))
        else:
            resp = await soup(page_link.format(strin, n))
        resp = resp[0]
    a_s = resp.find_all('a')
    list_a_s = []
    tit_links = []
    r = ['thumb', '350', 'img', 'big.php?i', 'data-src', 'title']
    for a_tag in a_s:
        if all(d in str(a_tag) for d in r):
            list_a_s.append(a_tag)
    try:
        for df in list_a_s:
            imgi = df.find('img')
            li = str(imgi['data-src']).replace('thumb-350-', '')
            titl = str(df['title']).replace('|', '')
            titl = titl.replace('Image', '')
            titl = titl.replace('HD', '')
            titl = titl.replace('Wallpaper', '')
            titl = titl.replace('Background', '')
            p = (li, titl.strip())
            tit_links.append(p)
    except Exception:
        pass
    if len(tit_links) ==  0:
        return False
    else:
        return tit_links
  
@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "autopp (.*)"))
async def autopep(event):
    global if_run
    if_run = True
    a  =  0
    dd =  True
    strin = str(event.pattern_match.group(1))
    while True:
        if if_run == False:
            break
        if dd == True:
            await event.edit('**Auto Profile Pic Started!**')
        dd =  False
        try:
            mas = await walld(strin)
            a = 0
        except:
            a += 1
            if a == 4:
                break
        try:
            if mas:
                for lik in mas:
                    path_i = await dlimg(lik[0])
                    await client(UploadProfilePhotoRequest(
                    await client.upload_file(path_i)
                 ))
                    if if_run ==  False:
                        break
                    await asyncio.sleep(60)
            else:
                await event.edit('**Result Not Found**')
        except:
            await event.edit('**Error Occured!**')
@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "offpp (.*)"))
async def offppg(event):
    global if_run
    if_run =  False
    await event.edit('**Auto Profile Pic Stopped!**')
