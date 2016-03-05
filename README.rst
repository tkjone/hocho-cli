*********
hocho cli
*********

hocho = hot chocolate, but for people who have better things to do with their time than stumble over four syllables when two will do nicely.  Me?  I’m going to do something awesome with all the time I save by cutting out those two extraneous syllables.  Like maybe snow tubing or eating ice cream.  Or both at once.

Purpose
=======

Hocho is going to save you some time.  Don't worry about creating files and directories for your projects anymore.  Let hocho do it for you!

Installation
============

.. code-block::

    pip install

Usage
=====

Just by typing in ``hocho`` you will get a warm and friendly message.

.. code-block::

    welcome to hocho

How do I learn about hocho?  Try typing in ``hocho --help``

.. code-block::

    Options:
       --help  Show this message and exit.

    Commands:
        stir

Deep Dive
=========

``hocho`` is the main command.  It has several subcommands that allows us to do some magical things.

stir : subcommand
    takes one argument:
        filename: the name of the file you are going to create
    flags:
        -s, --styles: tells hocho to create a style file.
    example:
        hocho stir material.styl -s



