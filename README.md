# OOI v3
Online Objects Integration (OOI) system based on aiohttp.

本系统要求Python版本大于等于3.4，利用最新的aiohttp库来实现OOI系统，以期望获得更高的效率。

另外请注意本项目采用了AGPLv3开源协议，和之前的ooi2项目的GPLv2不同。

# Docker Image

https://hub.docker.com/r/nanahira/ooi3

Nothing to volume and just expose port to 80.

## Environment Variables

* `OOI_SECRET_KEY`: Any 32 characters.
* `OOI_SCHEME`: Set to `https` for behind proxy.
* `OOI_BEIAN_NUMBER`: The ICP documenting code of your domain. eg. `粤ICP备19057366号-1`. Needed when setting up OOI in China. You may not set this variable when setting up OOI outside China mainland.
* `OOI_BEIAN_NUMBER`: Needed when setting up OOI in China. The ICP police documenting code of your domain. eg. `44030502004135` for `粤公网安备44030502004135号`. The provice would be auto detected.
