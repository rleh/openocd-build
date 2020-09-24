Name:       openocd
Version:    master
Release:    VERSION
Summary:    Debugging, in-system programming and boundary-scan testing for embedded devices

License:    GPLv2
URL:        http://sourceforge.net/projects/openocd
Source0:    %{name}-%{version}.zip

BuildRequires:  gcc
BuildRequires:  chrpath, libftdi-devel, libusbx-devel, jimtcl-devel, hidapi-devel, sdcc, libusb-devel, texinfo, libjaylink-devel

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming 
and boundary-scan testing for embedded devices. Various different boards, 
targets, and interfaces are supported to ease development time.

Install OpenOCD if you are looking for an open source solution for hardware 
debugging.

%prep
%setup -q

#pushd doc
#iconv -f iso8859-1 -t utf-8 openocd.info > openocd.info.conv
#mv -f openocd.info.conv openocd.info
#popd

sed -i 's/MODE=.*/TAG+="uaccess"/' contrib/60-openocd.rules

#%build
#pushd src/jtag/drivers/OpenULINK
#make PREFIX=sdcc hex
#popd

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
  --enable-jlink \
  --enable-osbdm \
  --enable-opendous \
  --enable-aice \
  --enable-vsllink \
  --enable-usbprog \
  --enable-rlink \
  --enable-armjtagew \
  --enable-cmsis-dap \
  --enable-parport \
  --enable-parport_ppdev \
  --enable-jtag_vpi \
  --enable-usb_blaster_libftdi \
  --enable-amtjtagaccel \
  --enable-ioutil \
  --enable-ep39xx \
  --enable-at91rm9200 \
  --enable-gw16012 \
  --enable-presto_libftdi \
  --enable-openjtag_ftdi \
  --enable-oocd_trace \
  --enable-buspirate \
  --enable-sysfsgpio \
  --enable-remote-bitbang \
  --disable-internal-jimtcl \
  --disable-doxygen-html \
  CROSS=
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/libopenocd.*
rm -rf %{buildroot}/%{_datadir}/%{name}/contrib
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d/
install -p -m 644 contrib/60-openocd.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/60-openocd.rules
chrpath --delete %{buildroot}/%{_bindir}/openocd

%files
%doc README COPYING AUTHORS ChangeLog NEWS TODO
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
