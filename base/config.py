import os

# 代理服务器
proxy = os.environ.get('OOI_PROXY', None)

# Cookie的secret key
secret_key = os.environ.get('OOI_SECRET_KEY', 'You Must Set A Secret Key!').encode()

#HTTP or HTTPS
scheme = os.environ.get('OOI_SCHEME', 'http')

# 备案号
beian = {
	'number': os.environ.get('OOI_BEIAN', None),
	'province': os.environ.get('OOI_GONGAN_BEIAN_PROVINCE', None)
	'gongan': os.environ.get('OOI_GONGAN_BEIAN', None)
}

# 项目目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')
kcs_dir = os.path.join(base_dir, '_kcs')
kcs2_dir = os.path.join(base_dir, '_kcs2')
