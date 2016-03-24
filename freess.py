#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: edward
# @Date:   2015-12-06 09:42:12
# @Last Modified by:   edward
# @Last Modified time: 2016-02-01 23:03:56
import urllib
import os
import sys
import re
import socket
import socks

class ShadowsocksServer:

    timeout = 600
    local_port = 1987
    urls = [
        # 'http://www.feixunvpn.com/page/testss.html',
        'https://www.freevpnss.org/'
    ]
    def __init__(self):
        self._launched = False
        self._act = self._handle_act()
        for url in self.urls:
            resp = urllib.urlopen(url)
            if resp.code == 200:
                self.html = resp.read()
                break

    def get_params(self):
        _params = list(self._ext_params())
        if all(_params):
            return _params
        else:
            raise Exception('exists invalid parameter!')

    def _ext_params(self):
        pat_ip = re.compile(r'服务器地址：([\w\.]+)')
        pat_port = re.compile(r'端口：(\d+)')
        pat_passwd = re.compile(r'密.*码：(\d+)')
        pat_encrypt = re.compile(r'加密方式：([\w-]+)')
        patterns = [pat_ip, pat_port, pat_passwd, pat_encrypt]
        params_groups = map(lambda p:p.findall(self.html), patterns)
        for i in zip(*params_groups):
            yield i

    def _check_sock5_proxy(self, addr, port):

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, addr=addr, port=port)
        socket.socket = socks.socksocket
        resp = urllib.urlopen(url="http://www.google.com")
        if resp.code == 200:
            return 0
        return 1

    def _handle_act(self):

        if self._launched is False:
            try:
                act = sys.argv[1]
                assert act in ('start', 'restart')
            except IndexError:
                raise IndexError('missing "act" param (start/restart)!')
            except AssertionError:
                raise IndexError('invalid "act" param (start/restart)!')
        else:
            act = 'restart'
        return act

    def execute(self, params):

        _params = list(params)
        to_extend_params = [self.local_port, self.timeout]
        if sys.platform.startswith('win'):
            launch_cmd = 'sslocal -s %s -p %s -k %s -m %s -l %s -t %s'
        else:
            launch_cmd = 'sslocal -s %s -p %s -k %s -m %s -l %s -t %s -d %s'
            to_extend_params.append(self._act)

        _params.extend(to_extend_params)
        os.system(launch_cmd % tuple(_params))
        self._launched = True

    def serve(self):
        servername = self.__class__.__name__
        for params in self.get_params():
            self.execute(params=params)
            signal = self._check_sock5_proxy('localhost', self.local_port)
            if signal == 1:
                continue
            elif signal == 0:
                return
        else:
            print '{} launched failed!'.format(servername)
            exit(1)


if __name__ == '__main__':
    server = ShadowsocksServer()
    server.serve()
