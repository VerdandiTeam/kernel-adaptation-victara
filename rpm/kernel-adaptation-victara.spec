# Device details
%define device victara

# Kernel target architecture
%define kernel_arch arm

%define device_target_cpu armv7hl

# Defconfig to pick-up
%define extra_config sfos-victara_defconfig
%define defconfig %{extra_config}

# Linux kernel source directory
%define source_directory linux

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

%define kernel_image zImage

%define ramdisk_directory ramdisk

%define bootimg_name hybris-boot.img

#Device Info

%define deviceinfo_dtb qcom/qcom-msm8974pro-motorola-victara.dtb
%define deviceinfo_append_dtb true
%define deviceinfo_flash_pagesize 2048
%define deviceinfo_flash_offset_base 0x00000000
%define deviceinfo_flash_offset_kernel 0x00008000
%define deviceinfo_flash_offset_ramdisk 0x02000000
%define deviceinfo_flash_offset_second 0x00f00000
%define deviceinfo_flash_offset_tags 0x00000100
%define deviceinfo_kernel_cmdline console=tty0 clk_ignore_unused pd_ignore_unused lk2nd.pass-simplefb=autorefresh
%define deviceinfo_bootimg_os_version 0
%define deviceinfo_bootimg_os_patch_level 0
%define deviceinfo_bootimg_header_version 0

Version:        6.16.12
Release:        1

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
