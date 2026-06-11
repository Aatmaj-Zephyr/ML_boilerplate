#!/bin/bash
echo "Hi Aatmaj. Welcome to the setup script for your ML boilerplate project! This script will help you set up your development environment and get everything ready for your machine learning project. Let's get started!"

echo ""
read -p "Press Enter to continue..."


echo "Before starting any project, remember that the journey of research is a marathon, not a sprint. Take time to relax. Hurdles are everywhere. Don't get demotivated."
echo "Jai Shree Mataji 🙏"
echo ""

echo ""
read -p "Press Enter to continue..."

echo ""
echo " We will now begin setup. For any doubts regarding the setup, refer to setup/README.md"
echo ""


echo "Getting sudo permissions"
chmod +x setup/create_venv.sh
chmod +x run_scripts/debug.sh
chmod +x run_scripts/build.sh
chmod +x run_scripts/server.sh


echo "Creating virtual env"


echo "First, we'll set up a Conda virtual environment to keep your project dependencies organized and isolated. This will ensure that your project runs smoothly without conflicts with other Python packages on your system."
setup/create_venv.sh
echo "Virtual environment setup complete! All the required packages are installed. You can activate it later with:"
echo "  conda activate ./venv"


echo ""
echo -e "\033[1;36m╔══════════════════════════════════════════════════════════╗"
echo -e "║                  🚀 SETUP COMPLETE 🚀                    ║"
echo -e "╠══════════════════════════════════════════════════════════╣"
echo -e "║  Your ML development environment is ready to go!         ║"
echo -e "║                                                          ║"
echo -e "║  💡 Keep experimenting                                   ║"
echo -e "║  📊 Build amazing models                                 ║"
echo -e "║  🔬 Stay curious                                         ║"
echo -e "║                                                          ║"
echo -e "║  ✨ All the best, Aatmaj! Happy coding! ✨✨             ║"
echo -e "╚══════════════════════════════════════════════════════════╝\033[0m"
echo ""

echo -e "\033[1;32m"
cat << "EOF"

 █████╗ ██╗     ██╗         ████████╗██╗  ██╗███████╗    ██████╗ ███████╗███████╗████████╗
██╔══██╗██║     ██║         ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝╚══██╔══╝
███████║██║     ██║            ██║   ███████║█████╗      ██████╔╝█████╗  ███████╗   ██║
██╔══██║██║     ██║            ██║   ██╔══██║██╔══╝      ██╔══██╗██╔══╝  ╚════██║   ██║
██║  ██║███████╗███████╗       ██║   ██║  ██║███████╗    ██████╔╝███████╗███████║   ██║
╚═╝  ╚═╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝╚══════╝   ╚═╝

              

EOF
echo -e "\033[0m"