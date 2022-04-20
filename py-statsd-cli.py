#!/usr/bin/env python3

import statsd
import sys
import time


METRIC_NAME = 'my_gauge_metric_00'
STATSD_HOST = '127.0.0.1'
STATSD_PORT = 8125


def get_metric_value():
    fname = '/tmp/%s' % METRIC_NAME
    v = 0.0
    try:
        with open(fname, 'r') as f_obj:
            lines = f_obj.readlines()
        if len(lines) > 0:
            v = float(lines[0])
    except FileNotFoundError:
        print('\nFile not found:', fname)
    return v


def main():
    print('StatsD: %s:%d' % (STATSD_HOST, STATSD_PORT))
    c = statsd.StatsClient(STATSD_HOST, STATSD_PORT)

    while True:
        v = float(get_metric_value())
        print('%s ' % (v), end='')
        sys.stdout.flush()
        c.gauge(METRIC_NAME, v)
        time.sleep(5)


if __name__ == '__main__':
    main()
