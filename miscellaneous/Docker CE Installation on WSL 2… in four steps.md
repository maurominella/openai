# Docker CE Installation on WSL 2… in four steps

Yes, you can run Docker containers directly within your WSL 2 (Windows Subsystem for Linux version 2) environment on Windows 11, treating it much like an independent Linux machine. This setup allows you to use Docker natively within Linux without needing Docker Desktop for Windows. Here's how you can set it up:



**Step 1: Ensure WSL 2 is Enabled and Installed**

First, make sure you have WSL 2 installed and enabled. You can check your WSL version by opening a PowerShell window as administrator and running:

wsl --list --verbose

If you haven't installed WSL or need to upgrade to WSL 2, you can follow the official Microsoft documentation to do so.





**Step 2: Install Your Preferred Linux Distribution**

If you haven't already, install a Linux distribution from the Microsoft Store (e.g., Ubuntu, Debian, Fedora, etc.). Once installed, launch it to complete its setup.





**Step 3: Install Docker within Your WSL 2 Linux Distribution** 

1. Update and Upgrade Your Linux Distribution

Open your WSL 2 terminal and run the following commands to update and upgrade your distribution's packages:
**sudo apt update && sudo apt upgrade -y**  





1. Install Docker's Dependencies

Next, install the necessary packages to allow your system to use repositories over HTTPS:

sudo apt install apt-transport-https ca-certificates curl software-properties-common -y



1. Add Docker's Official GPG Key and Set up the Stable Repository

curl -fsSL <https://download.docker.com/linux/ubuntu/gpg> | sudo apt-key add -  
sudo add-apt-repository "deb [arch=amd64] <https://download.docker.com/linux/ubuntu> $(lsb\_release -cs) stable"



1. Install Docker CE (Community Edition)

Update your package index and install Docker CE:

sudo apt update
sudo apt install docker-ce -y



1. Manage Docker as a Non-root User

To run Docker commands without sudo, add your user to the Docker group:

sudo usermod -aG docker $USER

You'll need to exit your WSL session and start it again or log out and log back in for this to take effect.



1. Start Docker on WSL 2

You might need to start the Docker service manually:

sudo service docker start

To have Docker start automatically with your WSL 2 distribution, you can add the above command to your shell's profile script (e.g., .bashrc or .zshrc).


**


**Step 4: Verify Docker Installation**

Run a test Docker container to verify your installation:

docker run hello-world

This should download a test image and run a container, outputting the "Hello from Docker!" message if everything is set up correctly.





**Conclusion**

Following these steps, you've installed Docker directly within your WSL 2 environment, enabling you to run Docker containers as if in an independent Linux machine. This setup is particularly useful for development and testing purposes, providing a more Linux-native experience on Windows 11.

