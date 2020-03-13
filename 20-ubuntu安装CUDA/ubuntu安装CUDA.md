# 0 写在前面
安装环境：ubuntu18.04以及GTX1050Ti笔记本

为什么要安装CUDA？  
参考百科，CUDA是英伟达推出的集成技术，通过该技术可利用GeForce 8 以后的GPU或者较新的Quadro GPU进行计算。例如典型的tensorflow-GPU和pyCUDA安装之前都要先安装CUDA。

# 1 安装N卡驱动
安装ubuntu系统之后自带开源NVIDIA Nouveau驱动，但是很容易出现[ubuntu18双系统安装后登陆重启卡死问题](https://blog.csdn.net/JohnJim0/article/details/100187156)。安装N卡驱动（即CUDA的硬件支持）之前必须先[禁用这个驱动](https://blog.csdn.net/weixin_38635229/article/details/85253443)。
终端输入以下命令没有返回结果说明禁用成功。
```bash
lsmod | grep nouveau
```
然后终端输入如下可以查看推荐的驱动版本：
```bash
ubuntu-drivers devices
```
笔者显示结果如下，说明nvidia-driver-435是推荐的
```bash
jj@jj-u:~/Downloads$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v000010DEd00001C8Csv0000103Csd0000838Fbc03sc00i00
vendor   : NVIDIA Corporation
model    : GP107M [GeForce GTX 1050 Ti Mobile]
driver   : nvidia-driver-435 - distro non-free recommended
driver   : nvidia-driver-430 - distro non-free
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-410 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin
```
此时终端输入```sudo ubuntu-drivers autoinstall```即可自动安装，或者输入```sudo apt install nvidia-driver-435```安装，然后重启系统即可。
> 安装过程中可能会跳出让你进入什么Key界面，这是因为安全模式安装第三方驱动需要写入key，具体遇到可百度，最简单粗暴的方法就是进入BIOS关闭安全模式启动，然后再安装n卡驱动。

重启后终端输入```nvidia-smi```，结果如下：
```bash
jj@jj-u:~/Downloads$ nvidia-smi
Tue Jan  7 12:31:39 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 435.21       Driver Version: 435.21       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 105...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   42C    P0    N/A /  N/A |    523MiB /  4040MiB |     18%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1491      G   /usr/lib/xorg/Xorg                           210MiB |
|    0      1658      G   /usr/bin/gnome-shell                         146MiB |
|    0      2808      G   /proc/self/exe                                12MiB |
|    0      7951      G   ...quest-channel-token=9976497191416364032   142MiB |
|    0      8743      G   /opt/teamviewer/tv_bin/TeamViewer              9MiB |
+-----------------------------------------------------------------------------+
```
可以看到该驱动支持的最高CUDA版本是10.1，刻意提及最高版本是因为某些比如tensorflow-gpu 1.x版本或最高支持CUDA9.1，但是驱动支持向下兼容所以可以安装CUDA9.1，但最好版本别太老。  
然后终端输入```nvidia-settings```出现图形设置界面说明到此N卡驱动安装成功。
# 2 安装CUDA
## 2.1 下载安装CUDA
点击[CUDA各版本链接](https://developer.nvidia.com/cuda-toolkit-archive)，由于tensorflow 1.x版本可能不兼容CUDA10.1，所以选择CUDA10，按提示下载了2G左右的runfile，然后按提示终端输入```sudo sh cuda_10.1.105_418.39_linux.run```，然后一直按F键读条到100%，然后根据终端提示输入即可，NVIDIA Accelerated Graphics Driver由于上一步安装过驱动就否了，
```bash
Do you accept the previously read EULA?
accept/decline/quit: accept          

Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 410.48?
(y)es/(n)o/(q)uit: n

Install the CUDA 10.0 Toolkit?
(y)es/(n)o/(q)uit: y

Enter Toolkit Location
 [ default is /usr/local/cuda-10.0 ]: 

Do you want to install a symbolic link at /usr/local/cuda?
(y)es/(n)o/(q)uit: y

Install the CUDA 10.0 Samples?
(y)es/(n)o/(q)uit: y

Enter CUDA Samples Location
 [ default is /home/jj ]: 

Installing the CUDA Toolkit in /usr/local/cuda-10.0 ...
```
## 2.2 配置环境变量
终端输入：
```bash
cd ~
sudo gedit .bashrc
```
打开文档后末尾加入以下信息：
```
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CPUTI/lib64
export CUDA_HOME=/usr/local/cuda/bin
export PATH=$PATH:$LD_LIBRARY_PATH:$CUDA_HOME
```
然后```source .bashrc```或者重启XD即可，终端输入```nvcc -V```可检查是否安装成功，结果如下：
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:01_CDT_2018
Cuda compilation tools, release 10.0, V10.0.130
```
或者终端输入：
```bash
cd ~/NVIDIA_CUDA-10.0_Samples/1_Utilities/bandwidthTest
make
./bandwidthTest
```
返回```Result = PASS```代表cuda安装成功。
# 3 安装cuDNN
cuDNN是用于深度神经网络的GPU加速库，如果CUDA是工作台，那么cuDNN就是上面的螺丝刀等工具。  
下载安装参考[CSDN](https://blog.csdn.net/jsjason1/article/details/88087414)。
