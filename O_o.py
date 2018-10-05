#! /usr/local/bin/python3

import datetime as datetime
import os
import emoji


terminal_notifier_path = '/path/to/brew/terminal-notifier/install'


def alert(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    o = '-sound default'
    os.system(terminal_notifier_path+'/terminal-notifier.app/Contents/MacOS/terminal-notifier {}'
              .format(' '.join([m, t, s, o])))


def main():
    print("O_o check at " + str(datetime.datetime.now()))
    alert(title='TWENTY-TWENTY-TWENTY',
          subtitle='Protect your ' + emoji.emojize(':eyes:', use_aliases=True),
          message='Time to stare off into the distance...')

if __name__ == '__main__':
    main()
