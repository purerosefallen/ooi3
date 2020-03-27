import os

# 代理服务器
proxy = os.environ.get('OOI_PROXY', None)

# Cookie的secret key
secret_key = os.environ.get('OOI_SECRET_KEY', 'You Must Set A Secret Key!').encode()

#HTTP or HTTPS
scheme = os.environ.get('OOI_SCHEME', 'http')

province_dict = {
        11 : "京",
        12 : "津",
        13 : "冀",
        14 : "晋",
        15 : "冀",
        21 : "辽",
        22 : "吉",
        23 : "黑",
        31 : "沪",
        32 : "苏",
        33 : "浙",
        34 : "皖",
        35 : "闽",
        36 : "赣",
        37 : "鲁",
        41 : "豫",
        42 : "鄂",
        43 : "湘",
        44 : "粤",
        45 : "桂",
        46 : "琼",
        50 : "渝",
        51 : "川",
        52 : "贵",
        53 : "云",
        54 : "藏",
        61 : "陕",
        62 : "甘",
        63 : "青",
        64 : "宁",
        65 : "新"
    }
# 备案号
beian = {
    'number': os.environ.get('OOI_BEIAN', None),
    'province': os.environ.get('OOI_GONGAN_BEIAN_PROVINCE', None),
    'gongan': os.environ.get('OOI_GONGAN_BEIAN', None)
}

if not beian['province'] and beian['gongan']:
    province_code = int(beian['gongan'][0:2])
    beian['province'] = province_dict[province_code]

# 项目目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')
kcs_dir = os.path.join(base_dir, '_kcs')
kcs2_dir = os.path.join(base_dir, '_kcs2')
