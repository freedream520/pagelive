#!/usr/bin/env python
#coding: utf-8

import os
import sys
from pyinotify import WatchManager, ThreadedNotifier, ProcessEvent
from pyinotify import IN_MODIFY
from selenium import webdriver


def refresh(fn):
    def wrap(self, *args):
        fn(self, browser, *args)
    return wrap


class ProcessDir(ProcessEvent):
    '''performs actions based on mask values'''
    ignore_file_ext = ['.swp','.un~']

    def __init__(self, browsers):
        self.browsers = browsers

    def process_IN_MODIFY(self, event):
        if any(event.name.endswith(ext) for ext in self.ignore_file_ext):
            pass
        else:
            print('refresh page -- Modify: %s'%event.name)
            # broadcast
            for browser in self.browsers:
                browser.refresh()


def live(path, tv):
    chromedriver = os.path.join(os.path.split(os.path.realpath(__file__))[0],\
                                'chromedriver')
    os.environ['webdriver.chrome.driver'] = chromedriver
    browsers = [ getattr(webdriver, browser.title())() \
            for browser in [s.lower() for s in tv]]

    wm = WatchManager()
    notifier = ThreadedNotifier(wm, ProcessDir(browsers))
    notifier.start()

    print('watching %s' % os.path.abspath(path))
    mask = IN_MODIFY
    wdd = wm.add_watch(path, mask, rec=True)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        path = sys.argv[1]
        browsers = ['chrome'] if len(sys.argv)==2 else sys.argv[2].strip().split(',')
        live(path, browsers)
    else:
        print('<usage %s dir browsers[separate by ,]>\n' +\
              'browsers support chrome, firefox' % __file__)
