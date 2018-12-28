from __future__ import unicode_literals
import itchat
import time
import requests


def get_news():
    #��ɽ�ʰԿ���api:json����
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    #��ȡÿ��һ��
    contents = r.json()['content']
    #��ȡÿ��һ��ķ���
    translation = r.json()['translation']

    return contents, translation


def send_news():
    try:
        #�Զ����㵯����ά���¼
        itchat.auto_login()
        #������ĺ��ѣ�name=u'���ѱ�ע'�� u����ʾunicode�ַ���
        my_friend = itchat.search_friends(name=u'LLY')
        ifriend = my_friend[0]['UserName']


        #��ȡҪ���͵���Ϣ
        message1 = str(get_news()[0])
        content = str(get_news()[1][5:])
        message2 = str(content)
        message3 = '�����������'

        itchat.send(message1, toUserName=ifriend)
        itchat.send(message2, toUserName=ifriend)
        itchat.send(message3, toUserName=ifriend)
    except:
        message4 = u'�������'
        itchat.send(message4, toUserName=ifriend)


def main():
    send_news()


if __name__ == '__main__':
    main()
