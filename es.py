import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context


def main():
    # no cafile!
    ssl_context = create_ssl_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    es = Elasticsearch(hosts=[{'host': 'elasticsearch-crawlab.apps.ocp4.liandisys.com.cn', 'port': 443}],
                       scheme="https",
                       # to ensure that it does not use the default value `True`
                       verify_certs=False,
                       ssl_context=ssl_context,
                       http_auth=("elastic", "ewTt7caGzFsz9903w4436H2U"))
    es.info()


if __name__ == '__main__':
    main()