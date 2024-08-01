SUMMARY = "Tool for analyzing memory usage of a process"
HOMEPAGE = "https://docs.zarhus.com"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=5a6917ac6c34ca9b935f702e32987df1"

SRC_URI = " \
    file://mem_test \
    file://plot_measurements.py \
    file://LICENSE \
    "

S = "${WORKDIR}"

RDEPENDS:${PN} += "zarhus-memory-usage bash python3"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${S}/mem_test ${D}${bindir}
    install -m 0755 ${S}/plot_measurements.py ${D}${bindir}

}

FILES:${PN} += " \
    ${bindir}/mem_test \
    ${bindir}/plot_measurements.py \
    "
