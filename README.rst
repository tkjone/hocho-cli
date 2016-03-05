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

    pip install git+https://github.com/tkjone/hocho-cli.git

Usage
=====

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
    When you run ``hocho stir`` you will be prompted with one question at this moment.  Press enter and you are asked to create a file name.  The result is that hocho will create a ``[name].styl`` file.  This file is created in whichever directory you are currently in.

More to come.

Thanks
======

I want to give a special thank you to Anya Craig who helped me with the ideation for this project!  hocho would not exist without you!

