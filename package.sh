#!/bin/bash
# Copyright (C) 2015 Midokura SARL.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

set -o errexit
set -o xtrace

# Create the structure of directories to build the rpm
# a new hierarchy will be created in $HOME/rpmbuild
SRC_NAME=networking-midonet
BUILD_DIR=$HOME/rpmbuild
rm -rf $BUILD_DIR
rpmdev-setuptree

# Copy the tarball to the SOURCES directory
cp ./${SRC_NAME}-*.tar.gz $BUILD_DIR/SOURCES

# Copy the patches to the SOURCES directory
cp ./patches/* $BUILD_DIR/SOURCES || true

# Copy the spec file to the SPECS directory
cp ./${SRC_NAME}.spec ${BUILD_DIR}/SPECS

rpmbuild -ba ${BUILD_DIR}/SPECS/${SRC_NAME}.spec

# Copy the rpm to the current directory
cp -r $BUILD_DIR/RPMS/noarch/*.rpm .
