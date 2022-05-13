import json

import requests
import execjs



headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://spider.wangluozhe.com",
    "Pragma": "no-cache",
    "Referer": "http://spider.wangluozhe.com/challenge/2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "session": "fa60fe13-1209-4592-8255-0faca8f29e32.nSUuFr03-MfaY5HxSbR7my-i1BU"
}


def get_signature():
    data = """
    var window=global;
    var hexcase = 0;
    var chrsz = 8;
    function hex_sha1(s) {
        return binb2hex(core_sha1(AlignSHA1(s)));
    }
    function sha1_vm_test() {
        return hex_sha1("abc") == "a9993e364706816aba3e25717850c26c9cd0d89d";
    }
    function core_sha1(blockArray) {
        var x = blockArray;
        var w = Array(80);
        var a = 1732584173;
        var b = -271733877;
        var c = -1752584194;
        var d = 271733878;
        var e = -1009589776;
        for (var i = 0; i < x.length; i += 16) {
            var olda = a;
            var oldb = b;
            var oldc = c;
            var oldd = d;
            var olde = e;
            for (var j = 0; j < 80; j++) {
                if (j < 16)
                    w[j] = x[i + j];
                else
                    w[j] = rol(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1);
                var t = safe_add(safe_add(rol(a, 5), sha1_ft(j, b, c, d)), safe_add(safe_add(e, w[j]), sha1_kt(j)));
                e = d;
                d = c;
                c = rol(b, 30);
                b = a;
                a = t;
            }
            a = safe_add(a, olda);
            b = safe_add(b, oldb);
            c = safe_add(c, oldc);
            d = safe_add(d, oldd);
            e = safe_add(e, olde);
        }
        return new Array(a, b, c, d, e);
    }
    function sha1_ft(t, b, c, d) {
        if (t < 20) {
            return (b & c) | ((~b) & d);
        }
        if (t < 40) {
            return b ^ c ^ d;
        }
        if (t < 60) {
            return (b & c) | (b & d) | (c & d);
        }
        return b ^ c ^ d;
    }
    function sha1_kt(t) {
        return (t < 20) ? 1518500249 : (t < 40) ? 1859775393 : (t < 60) ? -1894007588 : -899497514;
    }
    function safe_add(x, y) {
        var lsw = (x & 0xFFFF) + (y & 0xFFFF);
        var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
        return (msw << 16) | (lsw & 0xFFFF);
    }
    function rol(num, cnt) {
        return (num << cnt) | (num >>> (32 - cnt));
    }
    function AlignSHA1(str) {
        var nblk = ((str.length + 8) >> 6) + 1;
        var blks = new Array(nblk * 16);
        for (var i = 0; i < nblk * 16; i++) {
            blks[i] = 0;
        }
        for (i = 0; i < str.length; i++) {
            blks[i >> 2] |= str.charCodeAt(i) << (24 - (i & 3) * 8);
        }
        blks[i >> 2] |= 0x80 << (24 - (i & 3) * 8);
        blks[nblk * 16 - 1] = str.length * 8;
        return blks;
    }
    function binb2hex(binarray) {
        var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
        var str = "";
        for (var i = 0; i < binarray.length * 4; i++) {
            str += hex_tab.charAt((binarray[i >> 2] >> ((3 - i % 4) * 8 + 4)) & 0xF) + hex_tab.charAt((binarray[i >> 2] >> ((3 - i % 4) * 8)) & 0xF);
        }
        return str;
    }
    function get_data(){
    
        window.sign = hex_sha1(Date.parse(new Date).toString())
        return window.sign
    }
    
    """
    ctx = execjs.compile(data)
    _signature = ctx.call("get_data")
    return _signature


def get_num(num):
    data_num = 0
    _signature = get_signature()
    url = "http://spider.wangluozhe.com/challenge/api/2"
    data = {
        "page": num,
        "count": "10",
        "_signature": _signature
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)
    res = response.content.decode()
    data = json.loads(res)
    for val in data['data']:
        data_num += val['value']
    return data_num


def get_all():
    data = 0
    for i in range(1, 101):
        data += get_num(i)
        print(data)
    print(data)


if __name__ == '__main__':
    get_all()
