Name:       openocd
Version:    OPENOCD_VERSION
Release:    BUILD_VERSION
Summary:    Debugging, in-system programming and boundary-scan testing for embedded devices

License:    GPLv2
URL:        http://sourceforge.net/projects/openocd
Source0:    %{name}-%{version}.zip

BuildRequires: capstone-devel
BuildRequires: chrpath
BuildRequires: gcc
BuildRequires: hidapi-devel
BuildRequires: jimtcl-devel
BuildRequires: libgpiod-devel
BuildRequires: libjaylink-devel
BuildRequires: libftdi-devel
BuildRequires: libusbx-devel
BuildRequires: make
BuildRequires: sdcc
BuildRequires: texinfo

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming 
and boundary-scan testing for embedded devices. Various different boards, 
targets, and interfaces are supported to ease development time.

Install OpenOCD if you are looking for an open source solution for hardware 
debugging.

%prep
%setup -q

rm -rf jimtcl
rm -f src/jtag/drivers/OpenULINK/ulink_firmware.hex
sed -i 's/MODE=.*/TAG+="uaccess"/' contrib/60-openocd.rules

%build
pushd src/jtag/drivers/OpenULINK
make PREFIX=sdcc hex
popd

%configure \
  --disable-werror \
  --enable-static \
  --disable-shared \
  --enable-dummy \
  --enable-ftdi \
  --enable-stlink \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster-2 \
  --enable-ft232r \
  --enable-vsllink \
  --enable-xds110 \
  --enable-cmsis-dap-v2 \
  --enable-osbdm \
  --enable-opendous \
  --enable-aice \
  --enable-usbprog \
  --enable-rlink \
  --enable-armjtagew \
  --enable-cmsis-dap \
  --enable-nulink \
  --enable-kitprog \
  --enable-usb-blaster \
  --enable-presto \
  --enable-openjtag \
  --enable-jlink \
  --enable-parport \
  --enable-jtag_vpi \
  --enable-jtag_dpi \
  --enable-ioutil \
  --enable-amtjtagaccel \
  --enable-ep39xx \
  --enable-at91rm9200 \
  --enable-gw16012 \
  --enable-oocd_trace \
  --enable-buspirate \
  --enable-sysfsgpio \
  --enable-linuxgpiod \
  --enable-esp-usb-jtag \
  --enable-xlnx-pcie-xvc \
  --enable-remote-bitbang \
  --disable-internal-jimtcl \
  --disable-doxygen-html \
  --with-capstone \
  CROSS=
%make_build

%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/libopenocd.*
rm -rf %{buildroot}/%{_datadir}/%{name}/contrib
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d/
install -p -m 644 contrib/60-openocd.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/60-openocd.rules
chrpath --delete %{buildroot}/%{_bindir}/openocd

%files
%license COPYING
%doc AUTHORS NEWS* NEWTAPS README TODO
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/OpenULINK/ulink_firmware.hex
%{_bindir}/%{name}
%{_prefix}/lib/udev/rules.d/60-openocd.rules
# doc
%{_infodir}/%{name}.info*.gz
%{_mandir}/man1/*

%changelog
* Fri May 08 2020 Raphael Lehmann <raphael+openocdbuild@rleh.de> - master
- Build from OpenOCDs git master. See upstream OpenOCD project for changelog.
