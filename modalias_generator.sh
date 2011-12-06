#!/bin/sh
#
# Create modaliases for kmod packages
# Copyright (c) 2011, Hedayat Vatankhah <hedayat.fwd@gmail.com>
# Distributed under GPL version 3 or any later version
#

LATEST_KERNEL_VER="3.1.2-1"
OUTPUT_BASENAME=rpmfusion-modules
OUTPUT=${OUTPUT_BASENAME}.aliases

echo "Downloading kmod packages..."
echo "================================================================="
yumdownloader "kmod*${LATEST_KERNEL_VER}*"

[ -e $OUTPUT ] && echo "Output file already exists: $OUTPUT" && exit 1

echo "Generating modalias files..."
echo "================================================================="

for kmodpkg in *.rpm; do
	rpmdev-extract "$kmodpkg" > /dev/null
	PKGNAME="${kmodpkg%%-${LATEST_KERNEL_VER}*}"
	PKGDIR="${kmodpkg%.rpm}"
	KMODS="$(find "$PKGDIR" -name "*ko")"
        for kmod in $KMODS; do
		MODULE_NAME=$(basename $kmod)
		MODULE_NAME=${MODULE_NAME%.ko}
		modinfo $kmod | grep "alias:.*:" | sed "s|alias: *\(.*\)|alias \1 ${MODULE_NAME} ${PKGNAME}|" >> $OUTPUT
		modinfo $kmod | grep "alias:.*:" | sed "s|alias: *\(.*\)|alias \1 ${MODULE_NAME} ${PKGNAME}-PAE|" >> $OUTPUT_BASENAME-PAE.aliases
		modinfo $kmod | grep "alias:.*:" | sed "s|alias: *\(.*\)|alias \1 ${MODULE_NAME} a${PKGNAME}|" >> $OUTPUT_BASENAME-akmods.aliases
	done
	echo "Package: $PKGNAME"
	rm -rf "${PKGDIR}"
done

