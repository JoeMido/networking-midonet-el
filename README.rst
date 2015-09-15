networking-midonet-el
=====================

This is the rpm package project for RHEL.


How to Generate the Package
---------------------------


Run the following command to generate the package:

::

    $ ./package.sh

The package is generated in same directory as the script.


How to Update the Package
-------------------------

Grab the appropriate pristine tarball from:

::

    http://tarballs.openstack.org/networking-midonet/


Update `networking-midonet.spec` with the updated upstream and downstream versions.
