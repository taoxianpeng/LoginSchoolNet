import requests
import time
import os

ab_address=os.getcwd()+'/config'
password = ''
yournumber='18163977148'
def sendMessage():
    postData_sM={"userid": yournumber,"group_id": "0",\
        "class_id": "0","smsContext": "0","smsid": "1",\
        "usertype_value": "","wlanacname": "amnon",\
        "ssid": "","vlan": "0","listgetpass": "1",\
        "getpasstype": "0","act": "get"
        }
    try:
        r = requests.post("http://59.71.0.168/sendsmsAction.do",postData_sM)
        if r.text.find('1')!=-1:
            print("信息发送成功")
        else:
            print("error:信息发送失败")
    except Exception as e:
        print(e)

def login():
    postDate_login ={
        'wlanuserip': '10.18.45.37',
        'wlanacname': 'amnon',
        'chal_id': '',
        'chal_vector': '',
        'auth_type': 'PAP',
        'seq_id': '',
        'req_id': '',
        'wlanacIp': '59.71.0.169',
        'ssid': '',
        'vlan': '0',
        'mac': '44:85:00:e7:4e:29',
        'message': '',
        'bank_acct': '',
        'isCookies': '',
        'version': '0',
        'authkey': 'amnoon',
        'url': 'http://www.msftconnecttest.com/redirect',
        'usertime': '0',
        'listpasscode': '0',
        'listgetpass': '1',
        'getpasstype': '0',
        'randstr': '7455',
        'domain': '',
        'isRadiusProxy': 'false',
        'usertype': '0',
        'isHaveNotice': '0',
        'times': '12',
        'weizhi': '0',
        'smsid':'1',
        'freeuser':'',
        'freepasswd': '',
        'listwxauth': '0',
        'templatetype': '1',
        'tname': '1',
        'logintype': '0',
        'act': '',
        'is189': 'false',
        'terminalType': '',
        'checkterminal': 'true',
        'portalpageid': '1',
        'listfreeauth': '0',
        'viewlogin': '1',
        'userid': yournumber,
        'wisprpasswd': '',
        'twocode': '0',
        'authGroupId':'',
        'alipayappid': '',
        'wlanstalocation':'',
        'wlanstamac': '',
        'wlanstaos': '',
        'wlanstahardtype': '',
        'smsoperatorsflat': '3',
        'reason': '',
        'res': '',
        'userurl': '',
        'challenge': '',
        'uamip': '',
        'uamport': '',
        'useridtemp': yournumber,
        'passwd': password,
        'wxuser': ''
    }
    try:
        r=requests.post("http://59.71.0.168/portalAuthAction.do",postDate_login)
        #print(r.text)
        #print(r.text.find("错误1002：密码错误！请检查大小写是否正确！"))
        if r.text.find("错误1002：密码错误！请检查大小写是否正确！") != -1:
            print('密码错误')
            return False
        else:
            print("登录成功！")
            savePws()
            return True
    except Exception as e:
        print(e)
def readPwd():
    global password
    with open(ab_address,'r') as fp:
        password = fp.read()
        fp.close
    if  password == '':
        print("当前没有密码，请先获取密码！")
        input_pwd()
def savePws():
    if  password != '':
        with open(ab_address,'w') as fp:
            fp.write( password)
            fp.close
            return True
    return False
    

def input_pwd():
    global password
    rep = input('是否需要重新发送密码？(y/n): ')
    if rep == 'y':
        print('正在重新发送密码到手机上.......')
        sendMessage()
    #if rep == 'n':
    password = input("请填写密码: ")
    if not savePws():
        print('保存密码错误')
    else:
        print('密码保存成功！')
def disconnect():
    postDate_disconnect = {
        'portaltype': '',
        'wlanuserip': '10.18.45.37',
        'wlanacname': 'amnon',
        'chal_id': '',
        'chal_vector': '',
        'auth_type': 'PAP',
        'seq_id': '',
        'req_id': '',
        'wlanacIp': '59.71.0.169',
        'ssid': '',
        'vlan': '0',
        'message': '',
        'bank_acct': '',
        'isCookies': '',
        'version': '0',
        'authkey': 'amnoon',
        'url': 'http://www.baidu.com/',
        'usertime': '30169740',
        'listpasscode':' 0',
        'listgetpass': '1',
        'getpasstype': '0',
        'randstr': '9074',
        'domain': '',
        'isRadiusProxy': 'false',
        'usertype': '0',
        'isHaveNotice': '0',
        'times': '12',
        'weizhi': '0',
        'smsid': '1',
        'freeuser': '',
        'freepasswd': '',
        'listwxauth': '0',
        'templatetype': '1',
        'tname': '1',
        'logintype': '0',
        'act': 'DISCONN',
        'is189': 'false',
        'terminalType': '',
        'checkterminal': 'true',
        'portalpageid': '1',
        'listfreeauth': '0',
        'viewlogin': '1',
        'userid': yournumber,
        'wisprpasswd': password,
        'twocode': '0',
        'authGroupId': '',
        'alipayappid': '',
        'wlanstalocation':'' ,
        'wlanstamac': '',
        'wlanstaos': '',
        'wlanstahardtype': '',
        'smsoperatorsflat': '3',
        'reason': '',
        'res': '',
        'userurl': '',
        'challenge': '',
        'uamip': '',
        'uamport': '',
        'time_ellapse': '00:00:00',
        'time_remain': 'unknown'
    }
    try:
        r=requests.post("http://59.71.0.168/portalDisconnAction.do",postDate_disconnect)
        #print(r.text)
        #print(r.text.find("下线成功(Logout successful)"))
        if r.text.find("下线成功(Logout successful)") == -1:
            print('下线失败,帐号不在线')
        else:
            print("下线成功(Logout successful)")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    #sendMessage()
    #time.sleep(3000)
    if not os.path.exists(ab_address):
        with open(ab_address,'w') as f:
            f.close()

    print('1 - 登录\n2 - 断开\n0 - 关闭程序')
    rep = input('输入：')
    if(rep == '1'):
        readPwd()
        sign = login()
        while not sign:
            input_pwd()
            sign = login()
    if(rep == '2'):
        disconnect()

    input()

    

