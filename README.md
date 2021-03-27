# Latest OpenOCD Builds

Automated builds of the latest OpenOCD from http://openocd.zylin.com/openocd.git.

## Installation

### Debian/Ubuntu

Download latest `*.deb` Package from [Releases](https://github.com/rleh/openocd-build/releases) (usually `*.amd64.deb` on x86 computers; `*.arm64.deb` is e.g. for Raspberry Pi).

```bash
# Install Package (replace the file name with the one you downloaded)
sudo dpkg -i openocd-master-20210327.0054.amd64.deb

# Install missing dependencies:
sudo apt install -f
```

### Fedora/CentOS/...

Download latest `*.rpm` Package from [Releases](https://github.com/rleh/openocd-build/releases).

```bash
# Install Package (replace the file name with the one you downloaded)
sudo dnf install openocd-master-20210327.0054.x86_64.rpm
```


## Usage

You can test the installation by letting OpenOCD display its version:

```bash
openocd --version
```
