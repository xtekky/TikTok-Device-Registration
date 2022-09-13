"""
@demo file
@author: t.me/xtekky
@price: 500€ - 1.5k€ (algorithm etc...)
"""



class Device:
    @staticmethod
    def __openudid() -> str:
        return binascii.hexlify(random.randbytes(8)).decode()
    
    @staticmethod
    def __uuid() -> str:
        return str(uuid.uuid4())
    
    @staticmethod
    def __install_time() -> int:
        return int(round(time.time() * 1000)) - random.randint(13999, 15555)
    
    @staticmethod
    def __ut() -> str:

        return random.randint(100, 500)
    
    @staticmethod
    def __uid() -> int:
        return random.randrange(10000, 10550, 50)

    @staticmethod
    def __ts() -> int:
        return round(random.uniform(1.2, 1.6) * 100000000) * -1

    @staticmethod
    def __cba() -> str:
        return f"0x{random.randbytes(4).hex()}"
    
    @staticmethod
    def __hc() -> str:
        return f"0016777{random.randint(260, 500)}"
    
    @staticmethod
    def __dp() -> str:
        return f"{random.randint(700000000, 900000000)},0,0"
    
    @staticmethod
    def __rom() -> int:
        return str(random.randint(700000000, 799999999))
    
    @staticmethod
    def gen_device() -> dict:
        return {
            "device_model"  : "SM-G9550",
            "device_serial" : "G9550",
            "resolution"    : "1600x900",
            "resolution2"   : "900*1600",
            "device_brand"  : "samsung",
            "openudid"      : Device.__openudid(),
            "google_aid"    : Device.__uuid(),
            "clientudid"    : Device.__uuid(),
            "cdid"          : Device.__uuid(),
            "req_id"        : Device.__uuid(),
            "install_time"  : Device.__install_time(),
            "ut"            : Device.__ut(),
            "ts"            : Device.__ts(),
            "cba"           : Device.__cba(),
            "hc"            : Device.__hc(),
            "dp"            : Device.__dp(),
            "rom"           : Device.__rom(),
            "uid"           : Device.__uid(),
            "tz_name"       : "Africa\/Harare",
            "tz_offset"     : 7200,
            "device_id"     : 0000000000000000000,
            "install_id"    : 0000000000000000000,
            "install_time"  : int(round(time.time() * 1000)) - random.randint(13999, 15555)
        }

class Applog:
    def __init__(self, proxy: str or None = None) -> tuple:
        self.__device = Device.gen_device()
        self.__host   = "log-va.tiktokv.com"
        self.proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'} if proxy else None

    def __get_headers(self, params: str, payload: bytes):
        sig = Utils._sig(
            params = params, 
            body   = payload
        )
        
        return {
            "x-ss-stub"             : str(hashlib.md5(payload).hexdigest()).upper(),
            "accept-encoding"       : "gzip",
            "passport-sdk-version"  : "17",
            "sdk-version"           : "2",
            "x-ss-req-ticket"       : str(int(time.time()) * 1000),
            "x-gorgon"              : sig["X-Gorgon"],
            "x-khronos"             : sig["X-Khronos"],
            "content-type"          : "application/octet-stream;tt-data=a",
            "host"                  : "log-va.tiktokv.com",
            "connection"            : "Keep-Alive",
            "user-agent"            : "okhttp/3.10.0.1"
        }

    def __get_params(self):
        
        return urlencode(
            {
                "ac"                    : "wifi",
                "channel"               : "googleplay",
                "aid"                   : APP["aid"],
                "app_name"              : "musically_go",
                "version_code"          : APP["version_code"],
                "version_name"          : APP["version"],
                "device_platform"       : "android",
                "ab_version"            : APP["version"],
                "ssmix"                 : "a",
                "device_type"           : self.__device["device_model"],
                "device_brand"          : self.__device["device_brand"],
                "language"              : "en",
                "os_api"                : 25,
                "os_version"            : "7.1.2",
                "openudid"              : self.__device["openudid"],
                "manifest_version_code" : APP["version_code"],
                "resolution"            : self.__device["resolution"],
                "dpi"                   : 320,
                "update_version_code"   : APP["version_code"],
                "_rticket"              : [int(time.time() * 1000), int(time.time() * 1000) + 111],
                "storage_type"          : 0,
                "app_type"              : "normal",
                "sys_region"            : "US",
                "pass-route"            : 1,
                "pass-region"           : 1,
                "timezone_name"         : self.__device["tz_name"],
                "timezone_offset"       : self.__device["tz_offset"],
                "carrier_region_v2"     : 310,
                "cpu_support64"         : "false",
                "host_abi"              : "armeabi-v7a",
                "ts"                    : [int(time.time()), time.time() + 2],
                "build_number"          : APP["version"],
                "region"                : "US",
                "uoo"                   : 0,
                "app_language"          : "en",
                "carrier_region"        : "IE",
                "locale"                : "en",
                "op_region"             : "IE",
                "ac2"                   : "wifi",
                "cdid"                  : self.__device["cdid"],
                "tt_data"               : "a"
            }
        )
    
    def __get_payload(self):
        
        return {
            "magic_tag":"ss_app_log",
            "header": {
                "display_name"          : "TikTok Lite",
                "update_version_code"   : APP["version_code"],
                "manifest_version_code" : APP["version_code"],
                "app_version_minor"     : "",
                "aid"                   : 1340,
                "channel"               : "googleplay",
                "package"               : "com.zhiliaoapp.musically.go",
                "app_version"           : "16.9.4",
                "version_code"          : APP["version_code"],
                "sdk_version"           : "2.12.1-rc.6-lite",
                "sdk_target_version"    : 29,
                "git_hash"              : APP["git_hash"],
                "os"                    : "Android",
                "os_version"            : "7.1.2",
                "os_api"                : 25,
                "device_model"          : self.__device["device_model"],
                "device_brand"          : self.__device["device_brand"],
                "device_manufacturer"   : self.__device["device_brand"],
                "cpu_abi"               : "armeabi-v7a",
                "release_build"         : APP["release_build"],
                "density_dpi"           : 320,
                "display_density"       : "xhdpi",
                "resolution"            : self.__device["resolution"],
                "language"              : "en",
                "timezone"              : 2,
                "access"                : "wifi",
                "not_request_sender"    : 0,
                "carrier"               : "Android",
                "mcc_mnc"               : "31002",
                "rom"                   : self.__device["rom"],
                "rom_version"           : f"beyond1qlteue-user 7.1.2 PPR1.190810.011 {self.__device['rom']} release-keys",
                "cdid"                  : self.__device["cdid"],
                "sig_hash"              : APP["sig_hash"],
                "gaid_limited"          : 0,
                "google_aid"            : self.__device["google_aid"],
                "openudid"              : self.__device["openudid"],
                "clientudid"            : self.__device["clientudid"],
                "region"                : "US",
                "tz_name"               : self.__device["tz_name"],
                "tz_offset"             : self.__device["tz_offset"],
                "sim_region"            : "IE",
                "oaid_may_support"      : False,
                "req_id"                : self.__device["req_id"],
                "apk_first_install_time": self.__device["install_time"],
                "is_system_app"         : 0,
                "sdk_flavor"            : "global"
            },
            "_gen_time": int(round(time.time() * 1000))
        }
        
    def register_device(self):
        for x in range(5):
            try:
                params  = self.__get_params()
                payload = bytes.fromhex(Utils._ttencrypt(self.__get_payload()))

                r = requests.post(
                    url = (
                        "http://" + 
                            self.__host
                            + "/service/2/device_register/?" 
                            + params
                    ),
                    headers = self.__get_headers(params, payload),
                    data    = payload,
                    proxies = self.proxies
                )
                
                print(r.text)

                if len(str(r.json()["device_id"])) > 6:

                    self.__device["device_id"]  = r.json()["device_id"]
                    self.__device["install_id"] = r.json()["install_id"]
                    
                    return self.__device
            except Exception as e:
                print(e)
                continue
