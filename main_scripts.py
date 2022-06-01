from scripts import count_header_and_main, get_link_list
import json

#list_links('https://docs.blockbit.com/display/RC/Blockbit+GSM+-+Guia+do+Administrador')
link1 = ('https://docs.blockbit.com/display/RC/Blockbit+UTM+-+Guia+do+Administrador','./Blockbit_UTM.html')
link2 = ('https://docs.blockbit.com/display/RC/Blockbit+GSM+-+Guia+do+Administrador','./Blockbit_GSM.html')

l1 = get_link_list(link1[0],link1[1])
l2 = get_link_list(link2[0],link2[1])

total_count = 0

for item in l1:
    print(item['url'])
    url,counter,header,contents = count_header_and_main(item['url'])
    item['count'] = counter
    total_count += counter
    try:
        title = item["title"].replace('/','_')
        with open(f'utm/{title}.txt', 'w+',encoding='utf8') as f:
            f.write(f'{url}\n')
            f.write(f'{counter}\n')
            f.write(f'{header}\n')
            f.write(f'{contents}\n')
    except:
        print(url)
with open('utm.json','w+',encoding='utf8') as fp:
    json.dump(l1, fp)

for item in l2:
    print(item['url'])
    url,counter,header,contents = count_header_and_main(item['url'])
    item['count'] = counter
    total_count += counter
    title = item["title"].replace('/','_')
    try:
        with open(f'gsm/{title}.txt', 'w+',encoding='utf8') as f:
            f.write(f'{url}\n')
            f.write(f'{counter}\n')
            f.write(f'{header}\n')
            f.write(f'{contents}\n')
    except:
        print(url)
with open('gsm.json','w+',encoding='utf8') as fp:
    json.dump(l2, fp)

print(total_count)
