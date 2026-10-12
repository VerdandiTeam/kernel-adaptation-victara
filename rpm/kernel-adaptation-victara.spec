# Device details
%define device victara

# Kernel target architecture
%define kernel_arch arm

# Defconfig to pick-up
%define defconfig config-motorola-victara.armv7

# Linux kernel source directory
%define source_directory linux/

# Build modules
%define build_modules 1

# Build Image
%define build_Image 0

# Build uImage
##define build_uImage 1

# Build zImage
%define build_zImage 1

# Build and pick-up the following devicetrees
%define devicetrees qcom/qcom-msm8974pro-motorola-victara.dtb 

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
