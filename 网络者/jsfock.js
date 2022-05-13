var CryptoJS = require('crypto-js');
var gg;
var window = global;
(function () {
    let time_tmp = Date.now();
    let date = Date.parse(new Date());
    window = {};
    let click = true;
    let key_tmp;
    let iv_tmp;
    if (!click) {
        key_tmp = date * 1234;
    } else {
        key_tmp = date * 1244;
    }
    if (time_tmp - window.time < 1000) {
        iv_tmp = date * 4321;
    } else {
        iv_tmp = date * 4311;
    }
    const key = CryptoJS.enc.Utf8.parse(key_tmp);
    var iv = CryptoJS.enc.Utf8.parse(iv_tmp);
    (function tmp(date, key, iv) {
        function Encrypt(word) {
            let srcs = CryptoJS.enc.Utf8.parse(word);
            let encrypted = CryptoJS.AES.encrypt(srcs, key, {
                iv: iv,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            });
            return encrypted.ciphertext.toString().toUpperCase();
        }

        window.sign = Encrypt(date);
        gg = window.sign
    })(date, key, iv);
})();

function get() {
    return gg
}