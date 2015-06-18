IsCool Entertainment Pynba
==========================

.. warning::

    This package is deprecated ! use pynba_ instead.

Pynba is a WSGI Middleware for Pinba_. It allows realtime monitoring/statistics
server using MySQL as a read-only interface. It works on Python 2.7, 3.3 and more.

It accumulates and processes data sent over UDP by multiple Python processes
and displays statistics in a nice human-readable form of simple "reports", also
providing read-only interface to the raw data in order to make possible
generation of more sophisticated reports and stats.

Users also can measure particular parts of the code using timers with arbitrary
tags.


Why another statistics manager ?
--------------------------------

Because Pinba rocks!

At `IsCool Entertainment`_, we already use Pinba for monitoring our PHP based
applications.


Requirements
------------

This library relies only on Pinba_.
You will need to install theses packages before using Pynba.

The installation process requires setuptools to be installed.
If it is not, please refer to the installation of this package.


Setup
-----

If you want to install the official release, do::

    $ pip install iscool_e.pynba

But i you prefer to use the current developement version, do::

    $ git clone https://github.com/IsCoolEntertainment/pynba.git
    $ python setup.py install


Usage
-----

Says that your main WSGI application is::

    def app(environ, start_response):
        ...

Import the pynba decorator, and decorate your main app with it::

    from iscool_e.pynba import monitor

    @monitor(('127.0.0.1', 30002))
    def app(environ, start_response):
        ...

Each time the app will be processed, a new UPD stream will be sent.

You can also tag the process, for example::

    @monitor(('127.0.0.1', 30002), tags={'foo': 'bar'})
    def app(environ, start_response):
        ...

Eventualy, you can use timers to measure particular parts of your code.
For it, just import the pynba proxy, and use it to create new timers::

    from iscool_e.pynba import pynba

    timer = pynba.timer(foo="bar")
    timer.start()
    ...
    timer.stop()

But you may want to supervise simple scripts. For this usage, use ``ScriptMonitor``::

    from iscool_e.pynba.util import ScriptMonitor

    monitor = ScriptMonitor(('127.0.0.1', 30002), tags={'foo': 'bar'})
    timer = monitor.timer(foo='bar')
    timer.start()
    ...
    timer.stop()
    monitor.send()


Some use cases are available on src/examples/


Logging and debugging
---------------------

Pynba log to the 'pynba' logger. You should plug an handler in it. For example,
let's say you want to log everything to syslog, here is the modop::

    import logging
    import logging.handlers
    logger = logging.getLogger('pynba')
    logger.setLevel(logging.DEBUG)
    logger.setHandler(logging.handlers.SysLogHandler)


Another aspect is that reporting will be as discreet as possible, by not
raising exceptions on errors. This feature can be disabled directly into the
reporter instance.

For the WSGI usage::

    from iscool_e.pynba import PynbaMiddleware

    monitored_app = PynbaMiddleware(app, ('127.0.0.1', 30002))
    monitored_app.reporter.raise_on_fail = True

The decorated version::

    from iscool_e.pynba import monitor

    @monitor(('127.0.0.1', 30002))
    def app(environ, start_response):
        ...
    app.reporter.raise_on_fail = True

Or the script usage::

    from iscool_e.pynba.util import ScriptMonitor

    monitor = ScriptMonitor(('127.0.0.1', 30002))
    monitor.reporter.raise_on_fail = True


Contribute
----------

While debugging, you can rebuild c package with this command::

    $ python setup.py cythonize develop


Differences with PHP extension
------------------------------

About the data sent:

*   ``ru_utime`` and ``ru_stime`` represent the resource usage for the current
    process, not the shared resources.
*   ``document_size`` cannot be automaticaly processed with the current WSGI
    specification. You are able to set manually this value like this::

        pynba.document_size = [YOUR VALUE]

*   ``memory_peak`` also is currently not implemented. Like the previous data,
    you can set manually this value like this::

        pynba.memory_peak = [YOUR VALUE]

*   ``memory_footprint`` also is currently not implemented. Like the previous data,
    you can set manually this value like this::

        pynba.memory_footprint = [YOUR VALUE]

About timers:

*   The Python version permites multiple values for each timer tags.
    Just declare any sequences, mapping or callable. This example::

        pynba.timer(foo='bar', baz=['seq1', 'seq2'], qux={'map1': 'val1'})

    Will populates 4 values for 3 tags in the Pinba database::

        ('foo', 'bar'),
        ('baz, 'seq1'),
        ('baz, 'seq2'),
        ('qux.map1', 'val1')

Other additions:

*   ``ScriptMonitor`` allows to monitor single scripts. At IsCool Entertainment, we use it for monitoring our AMQ based workers.


License
-------

This package is release under the MIT Licence.
Please see LICENSE document for a full description.


Credits
-------

- Pinba_
- Pynba_
- `IsCool Entertainment`_

.. _Pinba: http://pinba.org
.. _`IsCool Entertainment`: http://www.iscoolentertainment.com/en/
.. _pynba: http://github.com/johnnoone/pynba
