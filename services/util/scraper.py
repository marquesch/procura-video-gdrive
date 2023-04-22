import requests as rq
from bs4 import BeautifulSoup
import entities.Folder as Folder
from services.util.cookies_info import cookies, headers


def get_soup_object(link):
    html_text = rq.get(link,
                       cookies=cookies,
                       headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    return soup


def count_files():
    return


def count_videos(link, folder: Folder):
    sp = get_soup_object(link)
    item_list = sp.find_all('c-wiz', class_='pmHCK')

    for item in item_list:
        item_type_and_name = item.find('div', class_='KL4NAf')['data-tooltip'].split(':')
        item_type = item_type_and_name[0]
        item_name = item_type_and_name[1].strip()

        if item_type == 'Google Drive Folder':
            new_folder = Folder.Folder(item_name)
            folder_link_base = 'https://drive.google.com/drive/folders/'
            item_tag = item.find('div', {'data-target': 'doc'})['data-id']
            folder_link = folder_link_base + item_tag
            count_videos(folder_link, new_folder)
            folder.add_folder(new_folder)

        elif item_type == 'Video':
            folder.add_video(item_name)

        else:
            folder.add_garbage(item_name)
